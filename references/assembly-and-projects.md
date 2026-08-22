# Assembly And Project Structure

## Assembly Ownership

Choose one assembly owner and machine. Provider dashboards are job records, not the only storage copy. Transfer accepted files once when another agent created them on a separate filesystem.

Use an existing authoritative project structure when present. Otherwise use:

```text
projects/<project-id>/
|-- brief/
|-- audio/master/
|-- audio/scenes/
|-- characters/
|-- brand/
|-- scenes/source/
|-- scenes/approved/
|-- captions/
|-- music-and-sfx/
|-- assembly/
|-- proofs/
|-- exports/
`-- records/video-manifest.json
```

Use versioned filenames such as `scene-03-avatar-v2.mp4`, `proof-v3.mp4`, and `final-approved-v1.mp4`. Never overwrite an approved source, proof, or export.

## Remotion Or Editable Composition

Use Remotion or an approved equivalent when the job needs a multi-scene branded timeline, programmatic captions, reusable layouts, overlays, responsive aspect ratios, or layer-specific revision.

- Keep scene order, source paths, timing, captions, logos, colours, music, and output settings in versioned project configuration.
- Use the approved master narration continuously; mute avatar clip audio.
- Crop a stable presenter into a corner circle or frame during B-roll when the brief calls for a hybrid layout.
- Render a proof before final export and retain the exact template and configuration versions.

## FFmpeg

Use FFmpeg for source inspection, trims, proxy creation, lossless or controlled transforms, audio replacement, normalization, container repair, simple assembly, and final technical checks.

- Inspect before converting.
- Avoid unnecessary re-encoding.
- Do not use FFmpeg as a substitute for the editable project when the job requires repeatable layer changes.
- Record every delivery conversion applied after the approved proof.

## Handoff Package

Retain and deliver as required:

- approved final exports and optional caption file;
- proof versions and approval record;
- editable project, configuration, and template version;
- brief, final script, audio package, scene manifest, character and brand references;
- accepted source assets, prompts, provider jobs, file IDs, costs, licences, and attribution;
- technical and visual QC results.

