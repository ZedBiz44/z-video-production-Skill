---
name: z-video-production
description: Plan, create, revise, assemble, inspect, and package branded videos from approved scripts, audio, avatars, B-roll, captions, and brand assets.
---

# Z Video Production

Direct a traceable video project from approved brief to retained editable project and approved exports. Orchestrate callable providers and local production tools without implying that a skill itself supplies accounts, credentials, models, or rendering software.

## Establish The Production Contract

Confirm or derive:

- business goal, audience, offer, call to action, channel, runtime, aspect ratio, resolution, frame rate, deadline, and approval owner;
- final script and version, scene plan, visual style, caption treatment, brand assets, music direction, and accessibility requirements;
- recurring people or characters and their approved identity references;
- audio package, provider routes, output folder, naming convention, cost ceiling, and publication destination;
- whether the request is a proof, controlled pilot, revision, final export, or provider comparison.

Use [the video production brief](assets/video-production-brief-template.md) when no controlling brief exists. Do not submit paid generation from an unapproved brief or script.

## Accept Or Create The Audio Package

- Invoke `z-audio-production` when narration must be created, auditioned, repaired, segmented, or approved.
- Accept only an approved dry master, normally 48 kHz PCM WAV, plus its script version, duration, QC status, and manifest.
- Treat the approved full master as the authoritative timing and final narration track.
- Create every lip-sync input from exact scene extracts of that master. Never resynthesize a line for a new pose or visual revision.
- Mute duplicate audio returned inside avatar or lip-sync clips and align their visuals to the authoritative master.
- If audio changes, open a new audio approval cycle and mark affected avatar clips, captions, timing, proofs, and exports stale.

Read [the audio-to-video contract](references/audio-integration.md) before any narration, avatar, lip-sync, caption-timing, or final-mix work.

## Lock Visual Identity And Brand Inputs

- Build or accept a Character Consistency Package for every recurring identifiable person.
- Separate fixed identity traits from changeable wardrobe, pose, framing, location, and lighting.
- Use approved front-facing, three-quarter, side, and full-body references when available; a written description alone is insufficient when exact identity matters.
- Keep original brand files, fonts, colours, logos, usage rights, and reference assets in project storage.
- Do not ask generative video models to render required logos, captions, calls to action, or other exact text inside moving pixels. Add them during assembly.
- Reject a scene when an ordinary viewer would believe a recurring person has changed identity.

Read [character and brand controls](references/character-and-brand.md) when creating or using recurring people, avatars, clients, logos, or licensed media.

## Verify The Real Production Route

- Inventory callable tools, provider connections, local binaries, templates, credentials, account ownership, models, schemas, limits, and current prices in the active runtime.
- Distinguish documented capability, configured access, successful discovery, controlled generation, and an end-to-end production-ready route.
- Inspect the exact provider schema immediately before submission. Do not guess field names or copy stale model parameters.
- Estimate material cost before generation and require the approval defined in the brief.
- Do not assume one agent shares another agent's provider account, subscription, project history, or filesystem.
- Download every accepted provider output into the assembly project with its provider, model, prompt, job ID, source or licence, and cost record.

Read [provider and route selection](references/provider-selection.md). Read only the active platform adapter: [Codex](references/codex.md), [OpenClaw](references/openclaw.md), or [Hermes](references/hermes.md).

## Produce By Layer

Use the approved scene manifest as the work order.

- Generate or acquire only the assigned layer: speaking avatar, generated B-roll, stock or owned footage, screen recording, graphic, music, or sound effect.
- Give each shot one purpose, target duration, aspect ratio, identity package, negative constraints, filename, and acceptance criteria.
- Lock accepted assets. A caption, logo, music, timing, or layout edit must not regenerate approved footage.
- Regenerate only a failed visual asset. Reuse the unchanged audio extract and locked identity inputs for avatar retries.
- Keep provider workers inside their assigned scene and settings; they must not rewrite the approved storyboard or prompts.
- Use parallel production workers only when the runtime supports governed delegation, the user has authorized it, and shared manifests prevent conflicting edits.

For the end-to-end sequence and revision routing, read [production workflow](references/production-workflow.md).

## Assemble An Editable Proof

- Choose one assembly owner. That owner retains the local project, sources, configuration, proofs, and exports.
- Use Remotion or another approved editable composition system for the branded timeline, captions, logos, overlays, transitions, and repeatable revisions.
- Use FFmpeg for inspection, normalization, trimming, proxy creation, audio replacement, repair, simple transforms, and delivery validation.
- Keep narration, avatar video, B-roll, stock, captions, graphics, music, and effects on separable layers.
- Align visuals and captions to the approved master audio; do not time-stretch the master to fit a visual render.
- Create a low-cost or low-resolution proof before final-quality re-generation or export.
- Change the smallest responsible layer after review, then re-render the proof.

Read [assembly and project structure](references/assembly-and-projects.md) for storage, manifest, Remotion, FFmpeg, proof, and handoff rules.

## Apply Approval And Publication Gates

- Require human approval of the proof before labelling an export approved or publishing client-facing media.
- Public posting, ad launch, client delivery, and production deployment are separate actions from rendering; do not infer authorization for them.
- Record approval owner, date, approved proof version, requested changes, and final delivery specifications.
- Preserve the last approved proof and editable project before a revision or rollback.

## Inspect And Package

- Run `scripts/inspect_video.py` on proofs and final exports.
- Complete and validate the manifest using `assets/video-manifest-template.json` and `scripts/validate_video_manifest.py`.
- Apply [video quality and completion gates](references/quality-gates.md).
- Verify playback, expected duration, dimensions, aspect ratio, frame rate, codecs, audio presence, script match, caption safe areas, identity, logo readability, visual relevance, and unintended black or frozen sections.
- Retain source assets, prompts, licences, provider records, editable configuration, proofs, final exports, transcript or captions, QC result, and approval evidence.

## Failure And Stop Conditions

- Stop when the brief, script, audio approval, identity rights, asset licence, provider access, cost ceiling, destination, or approval owner is unresolved.
- Poll the real provider job before retrying. Never duplicate a paid job merely because it is slow.
- Retry one clearly transient failure after checking final status. After two failed paid attempts for the same asset, preserve evidence and stop.
- After three failed validation or repair attempts, preserve the last known-good project and report the decision required.
- Do not silently change provider, model, voice, character, duration, aspect ratio, or brand treatment to bypass a failure.

## Completion Report

Report:

- project, script, audio package, manifest, proof, final export, and editable source versions and paths;
- providers, models, job IDs, prompts, source or licence records, and estimated and actual costs;
- technical inspection, visual QC, script-match, caption, identity, and brand results;
- human approval and publication status;
- regenerated assets and retained approved assets;
- unproven capabilities, unresolved risks, and blocked delivery or deployment actions.

