# Production And Revision Workflow

## Production Order

- Lock the Master Brief, final script, approval owner, cost ceiling, delivery specifications, and scene manifest.
- Obtain the approved `z-audio-production` package and verify the audio-to-video acceptance gate.
- Lock Character Consistency Packages, brand files, rights, licences, and provider assignments.
- Create or acquire scene assets with stable IDs and filenames.
- Download accepted provider outputs into the assembly project and record their provenance.
- Transcribe the final approved master when word or caption timing is required.
- Assemble separate visual, narration, caption, graphic, music, and effects layers.
- Render a low-resolution or low-cost proof.
- Route each requested change to the smallest responsible layer.
- Pass technical, visual, script, caption, identity, brand, and human approval gates.
- Render final delivery formats and retain the editable project and evidence.

## Scene Work Order

Each scene should identify:

- scene ID, purpose, exact script or master timecode, and target duration;
- source type: avatar, generated B-roll, stock, owned, screen recording, still, or graphic;
- provider, model, parameters, identity references, brand constraints, and negative constraints;
- expected aspect ratio, resolution, file name, destination, cost estimate, and approval requirement;
- acceptance criteria and fallback route.

## Revision Routing

- **Words, performance, pronunciation, or voice changes:** reopen `z-audio-production`; create a new master version and invalidate dependent assets.
- **Lip-sync or avatar movement failure:** rerender only that visual pass with the unchanged scene audio and identity package.
- **Bad generated B-roll:** replace only the failed scene.
- **Caption wording or timing:** correct the transcript or timing layer and rerender assembly.
- **Logo, colour, font, CTA, crop, overlay, music, volume, transition, or layout:** edit the composition layer and rerender.
- **Codec, file size, container, or platform compatibility:** repair or convert the approved render without regenerating creative assets.

Keep approved scenes locked unless the brief itself changes. Record why each revision occurred, what became stale, and which approved files remain current.

## Governed Workers

When the active runtime and authorization permit workers or sub-agents:

- keep one director responsible for the brief, prompt lock, cost approval, manifest, proof review, and final approval;
- assign narrow avatar, B-roll, assembly, and QC jobs against the same manifest;
- prohibit workers from changing the storyboard, voice, identity package, provider, or model without director approval;
- return files, job IDs, cost, settings, failures, and QC evidence to the director;
- test the architecture on a small controlled scene set before scaling parallel work.

