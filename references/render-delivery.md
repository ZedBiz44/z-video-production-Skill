# Rendering And Delivery Recovery

## Use The Installed Tools

- Identify project-local Remotion versions, package manager/lockfile and the actual FFmpeg/FFprobe paths. Remotion may use its own binary; changing the system binary does not update every renderer.
- Check requested filters/codecs in the installed build. GPU acceleration requires compatible hardware and drivers; a published feature is not proof it runs here.
- Keep Remotion packages on one compatible version. When upgrades are authorized, preserve the existing assembly, follow the installed official upgrade guidance, pin the tested versions and compare a real export before wider use.

## Keep Rendering Proportionate

- Use FFmpeg for a simple trim, join, static end card, audio adjustment or delivery conversion; use Remotion when an editable composition adds value.
- On constrained/shared hosts, start with one render worker and bounded decoding/cache settings supported by the installed version. Avoid concurrent heavy renders by default. Test a short representative interval before a costly full assembly.
- After an out-of-memory or browser failure, inspect the actual error and reduce workload/concurrency or use a simpler equivalent route. Do not rerun the same failing settings indefinitely or regenerate paid source footage to solve a local rendering problem.
- Preserve the original and approved master. Render recoveries and compression into new files; verify the final file after the last transformation.

## Keep Speech And Sound Intact

- Preserve approved native dialogue. When independent narration replaces source speech, mute only the unwanted audio and keep the approved master as the timing source.
- Balance speaker loudness, keep music below speech and avoid clipping. Use loudness measurement/normalization, fades and noise reduction only where they improve the actual recording.
- Smooth ambience across cuts on a separate layer when available. Avoid fading across spoken words; listen for missing syllables, doubled speech and unnatural pauses.
- Keep subtitles tied to the final spoken audio, not just the intended script. Check names, speaker changes, timing and platform-safe placement. Automated transcription needs review.

## Validate And Attach

- Check metadata with FFprobe and perform a complete decode with FFmpeg. Check actual duration, video dimensions and expected audio streams; metadata and a successful decode do not establish creative quality.
- Review the complete timeline with visual-and-audio coverage. Report the method and any sampling limitations; automated black/silence/freeze detection flags candidates, not automatic failures.
- Check the channel's current file-size limit before upload. If needed, calculate a suitable delivery bitrate, retain a margin, export a smaller copy and verify actual size and playback. Keep the full-quality master in Drive.
- Retry delivery with the exact verified file path using the channel's supported attachment method. Confirm the attachment receipt; do not submit another generation because an upload failed.
