#!/usr/bin/env python3
"""Validate required fields and cross-field invariants in a video manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_PATHS = (
    "schema_version",
    "project.id",
    "project.name",
    "project.video_version",
    "project.status",
    "brief.script_version",
    "brief.approval_owner",
    "delivery.width",
    "delivery.height",
    "delivery.fps",
    "audio_package.version",
    "audio_package.manifest_path",
    "audio_package.master_path",
    "assembly.owner",
    "assembly.tool",
    "assembly.project_path",
)


def get_path(data: dict, dotted: str) -> object:
    value: object = data
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Z video production manifest.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--require-approved-audio", action="store_true")
    parser.add_argument("--require-final-approval", action="store_true")
    args = parser.parse_args()

    path = args.path.resolve()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc), "path": str(path)}, indent=2))
        return 2

    errors = []
    for dotted in REQUIRED_PATHS:
        value = get_path(data, dotted)
        if value is None or value == "" or value == 0:
            errors.append(f"missing required value: {dotted}")

    if not isinstance(data.get("scenes"), list) or not data.get("scenes"):
        errors.append("scenes must contain at least one scene")
    if args.require_approved_audio and get_path(data, "audio_package.approved") is not True:
        errors.append("audio_package.approved must be true")
    if args.require_final_approval:
        if not get_path(data, "approval.approved_by"):
            errors.append("approval.approved_by is required")
        if not get_path(data, "approval.approved_at"):
            errors.append("approval.approved_at is required")
        exports = data.get("final_exports")
        if not isinstance(exports, list) or not exports:
            errors.append("final_exports must contain at least one export")

    scene_ids = [scene.get("id") for scene in data.get("scenes", []) if isinstance(scene, dict)]
    if any(not scene_id for scene_id in scene_ids):
        errors.append("every scene must have an id")
    if len(scene_ids) != len(set(scene_ids)):
        errors.append("scene ids must be unique")

    print(json.dumps({"ok": not errors, "path": str(path), "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
