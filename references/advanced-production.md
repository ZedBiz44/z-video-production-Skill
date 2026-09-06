# Advanced Production Guidance

Read this only when meaningful spend, recurring identity or voice, uncertain rights, client or public delivery, multi-worker handoff, or likely revisions create material risk.

## Choose The Production Route

Choose the simplest route that fits the intended result:

- speaking-avatar or lip-sync generation when a visible speaker must perform approved narration;
- generated cinematic scenes or B-roll when original motion and atmosphere matter more than exact speech;
- licensed stock, owned media, or supplied footage when speed, realism, or control matters;
- screen recording when the product, website, or process itself is the subject;
- editing and assembly when the job is primarily combining or revising existing layers.

Mix routes only when the result benefits. A preference or configured model is not proof of live availability.

## Keep Voice-First Work Stable

- Produce or approve the narration before lip-sync, caption timing, or scene assembly when recurring voice, exact delivery, or timing matters.
- Treat the approved narration as the timing source and final narration track.
- Cut scene extracts from the master, mute conflicting embedded avatar audio, and do not regenerate approved lines for new poses or scenes.

## Use A Repeatable Multi-Scene Sequence

For an audio-led multi-scene video:

- lock the script and approve one full dry narration master;
- use the narration duration to set scene timing;
- cut exact scene narration extracts from the approved master;
- create or collect each scene's visual source;
- use the exact scene extract for talking-avatar or lip-sync work when required;
- remove or mute audio returned inside source clips;
- assemble the source clips, approved master, captions, graphics, music, and effects in an editable timeline;
- render a proof, review the full timeline, revise only the failed layer, and then render the delivery file.

Do not ask separate scene generators to reinvent the voice or wording. Do not get stuck trying to force provider-generated clips to be silent; strip their audio before final assembly.

## Select A Scene Profile

- **Talking avatar:** use the approved identity reference and exact narration extract; check mouth movement, identity, hands, clothing, and background; keep the approved master as final audio.
- **Generated B-roll or hero shot:** describe one clear action, setting, camera behavior, lighting, and style; avoid generated words, logos, prices, and calls to action.
- **Stock, owned footage, or screen recording:** prefer this route when realism, factual accuracy, product demonstration, speed, or repeatable control matters more than novel generation.

Use a consistent visual reference, aspect ratio, color direction, and camera language across related scenes. A negative phrase such as “do not look AI-generated” is not a useful visual direction by itself.

## Run Paid Providers Deliberately

- Confirm that the provider route is callable in the current runtime.
- Inspect the current model and live input schema when applicable, then estimate the material cost.
- Generate only after required spending, identity, and rights approvals are clear.
- Poll the real job and check provider history before retrying or abandoning a delayed request.
- Save the completed output into the project and retain the job details needed for recovery or accountability.
- Do not silently swap a requested or approved provider, model, voice, identity, or format after failure.

For paid or multi-scene work, keep a light scene-and-job record containing the scene ID, intended duration, source type, prompt or source reference, provider, model, job ID, status, estimated or actual cost, downloaded file, and review result. This may be a project table, Markdown file, or JSON record; do not create unnecessary paperwork for a disposable one-off clip.

## Choose Useful Controls

Add only the controls that reduce a real risk or future cost. Depending on the job, that may include:

- a concise brief or shot list;
- approved narration or a stable audio master;
- character or brand references;
- an editable assembly project and retained sources;
- provider job, cost, licence, or approval records;
- a proof before final-quality generation or external delivery;
- targeted technical, visual, identity, caption, or brand review.

Do not require every control and do not invent a universal manifest. Store project-specific information in the project using the structure that best serves its likely users.

## Preserve Reusable Layers And Handoffs

- When a recurring person matters, preserve the approved identity references and distinguish fixed traits from details that may change.
- Keep exact text, logos, captions, offers, and calls to action in editable layers when accuracy or later revision matters.
- Check material text and captions for readability, synchronization, and platform safe areas.
- Confirm the usage rights for supplied, owned, stock, and generated media; local possession alone does not establish a licence.
- Retain approved media, never overwrite the only original or approved master, and replace only the failed or changed layer.
- State the useful handoff status: **Working Draft**, **Review Draft**, **Approved Master**, or **Published/Delivered**. Do not imply approval or delivery that did not occur.

## Coordinate Larger Jobs

- Use a proof before committing substantial cost or producing a client-facing final.
- Keep enough source and decision evidence for the expected revision, handoff, rights, or approval need—no more.
- If multiple people or agents contribute, agree on ownership and file locations only to the extent needed to avoid lost assets or conflicting edits.
- Use Remotion when editable multi-scene design or repeatable revision matters. Use FFmpeg for preparation and technical verification. Do not force either tool onto a simpler route that already meets the request.

