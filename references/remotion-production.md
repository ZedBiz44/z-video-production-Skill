# Remotion Production Guidance

Use this reference when Remotion is the editable assembly or revision system. The official Remotion skills contain the current implementation guidance; this file defines how that guidance fits the ZedBiz production workflow.

## Load The Right Official Guidance

- Read `remotion-best-practices` first when routing is uncertain.
- Read `remotion-create` when creating a new project or composition.
- Read `remotion-markup` for composition structure, animation, layout, typography, media, effects, audio, fonts, or timing.
- Read `remotion-captions` for captions and subtitles.
- Read `remotion-studio` for interactive preview work.
- Read `remotion-render` before rendering video or still output.
- Read `remotion-docs` before relying on an uncertain or changing Remotion API.
- Do not load every specialist skill when only one or two are relevant.

## Keep Tool Responsibilities Clear

- Video generators, avatar tools, stock libraries, owned footage, and screen recorders provide source scenes.
- `z-audio-production` provides the approved dry narration master and exact scene extracts.
- Remotion owns the editable multi-scene timeline, captions, titles, lower thirds, logos, calls to action, layout, timing, transitions, music, effects, and final render.
- FFmpeg prepares, trims, converts, mutes, extracts, repairs, and technically checks media.

## Assemble From The Approved Narration

- Set the composition timing from the approved narration rather than guessing scene duration first.
- Keep the full approved narration on the final timeline.
- Use scene extracts only to drive talking-avatar or lip-sync generation.
- Remove or mute audio embedded in returned scene clips before final mixing.
- Keep music and effects on separate layers and below the narration.
- Add exact text and branding as editable Remotion layers, never as instructions for a generative video model.

## Revise The Smallest Layer

- Change Remotion text, timing, layout, captions, music, or transitions without regenerating source video.
- Replace or regenerate only the scene whose visual content failed.
- Regenerate narration only when the approved script or performance changes.
- Preserve the previous approved render and editable project until the replacement is accepted.

## Proof And Delivery

- Render a low-cost proof before committing to a final client-facing export when the edit is complex or expensive.
- Review the beginning, every scene change, captions, audio synchronization, identity, exact text, and ending.
- Validate the final video and audio streams with FFmpeg or FFprobe.
- Save the editable Remotion project in `Assembly/` and the versioned MP4 in `Proofs/` or `Final/` within the project's **Video-Creation** Shared Drive folder: https://drive.google.com/drive/folders/0AAlVr-SRjSeQUk9PVA.
- Render and inspect from local working storage when practical, then upload and verify the retained files in the Shared Drive. Do not use a temporary local path as the final handoff location.
- Attach the playable MP4 through the conversation channel. A path, provider URL, or render log alone is not delivery.


