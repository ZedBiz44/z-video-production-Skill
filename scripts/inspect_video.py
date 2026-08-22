#!/usr/bin/env python3
"""Inspect a video file with ffprobe and verify common delivery invariants."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def number(value: object) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def frame_rate(value: str | None) -> float:
    if not value or value == "0/0":
        return 0.0
    try:
        return round(float(Fraction(value)), 6)
    except (ValueError, ZeroDivisionError):
        return 0.0


def inspect(path: Path) -> dict:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe was not found")
    command = [
        executable,
        "-v", "error",
        "-show_entries",
        "format=format_name,duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,avg_frame_rate,r_frame_rate,duration,sample_rate,channels",
        "-of", "json",
        str(path),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    streams = payload.get("streams", [])
    videos = [stream for stream in streams if stream.get("codec_type") == "video"]
    audios = [stream for stream in streams if stream.get("codec_type") == "audio"]
    if not videos:
        raise RuntimeError("no video stream found")
    video = videos[0]
    audio = audios[0] if audios else {}
    container = payload.get("format", {})
    width = int(video.get("width") or 0)
    height = int(video.get("height") or 0)
    fps = frame_rate(video.get("avg_frame_rate") or video.get("r_frame_rate"))
    duration = number(video.get("duration")) or number(container.get("duration"))
    return {
        "format": container.get("format_name", ""),
        "duration_seconds": round(duration, 6),
        "size_bytes": int(container.get("size") or path.stat().st_size),
        "bit_rate": int(container.get("bit_rate") or 0),
        "video": {
            "codec": video.get("codec_name", ""),
            "width": width,
            "height": height,
            "aspect_ratio": f"{width}:{height}" if width and height else "",
            "fps": fps,
        },
        "audio": {
            "present": bool(audio),
            "codec": audio.get("codec_name", ""),
            "sample_rate_hz": int(audio.get("sample_rate") or 0),
            "channels": int(audio.get("channels") or 0),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a video and verify delivery settings.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--expected-width", type=int)
    parser.add_argument("--expected-height", type=int)
    parser.add_argument("--expected-fps", type=float)
    parser.add_argument("--expected-video-codec")
    parser.add_argument("--expected-audio-codec")
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--duration-tolerance", type=float, default=0.25)
    parser.add_argument("--expected-duration", type=float)
    args = parser.parse_args()

    path = args.path.resolve()
    if not path.is_file() or path.stat().st_size == 0:
        print(json.dumps({"ok": False, "error": "file not found or empty", "path": str(path)}, indent=2))
        return 2

    try:
        details = inspect(path)
    except (OSError, RuntimeError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc), "path": str(path)}, indent=2))
        return 2

    checks: list[dict] = []

    def check(name: str, expected: object, actual: object, passed: bool) -> None:
        checks.append({"name": name, "expected": expected, "actual": actual, "passed": passed})

    if args.expected_width is not None:
        check("width", args.expected_width, details["video"]["width"], details["video"]["width"] == args.expected_width)
    if args.expected_height is not None:
        check("height", args.expected_height, details["video"]["height"], details["video"]["height"] == args.expected_height)
    if args.expected_fps is not None:
        check("fps", args.expected_fps, details["video"]["fps"], abs(details["video"]["fps"] - args.expected_fps) <= 0.01)
    if args.expected_duration is not None:
        check("duration_seconds", args.expected_duration, details["duration_seconds"], abs(details["duration_seconds"] - args.expected_duration) <= args.duration_tolerance)
    if args.expected_video_codec:
        check("video_codec", args.expected_video_codec, details["video"]["codec"], details["video"]["codec"].lower() == args.expected_video_codec.lower())
    if args.expected_audio_codec:
        check("audio_codec", args.expected_audio_codec, details["audio"]["codec"], details["audio"]["codec"].lower() == args.expected_audio_codec.lower())
    if args.require_audio:
        check("audio_present", True, details["audio"]["present"], details["audio"]["present"])

    ok = all(item["passed"] for item in checks)
    print(json.dumps({"ok": ok, "path": str(path), "video_file": details, "checks": checks}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

