# Audio Integration Contract

Read this reference whenever video work creates or consumes narration, lip-sync audio, captions, or a final mix.

## Invoke Z Audio Production

Use `z-audio-production` when the job needs:

- voice selection, audition, cloning, consent review, or production narration;
- script-to-audio generation, repair, mastering, scene extraction, or technical inspection;
- an approved master, audio manifest, transcript, word timing, or video-ready handoff.

Do not duplicate those responsibilities in this skill. If `z-audio-production` is unavailable, require an equivalent approved package rather than silently inventing an audio workflow.

## Acceptance Requirements

Accept the package only when it identifies:

- project and audio package version;
- final script and version;
- approved dry master, normally 48 kHz PCM WAV;
- duration, codec, sample rate, channels, and checksum when required;
- speaker, pronunciation record, Voice Identity Package reference, consent or licence reference;
- exact scene extracts and master timecodes when lip-sync scenes are planned;
- transcript or timing file when captions are planned;
- QC result, approval owner, provider jobs, cost, and unresolved issues.

Reject the handoff when the master is unapproved, files are missing, script versions disagree, scene timecodes exceed master duration, or rights and identity references are unresolved.

## Shared Invariants

- The approved complete master is the authoritative soundtrack and timing anchor.
- Scene audio is cut from that exact master at pauses or breaths, never regenerated independently.
- Avatar and lip-sync providers receive the matching dry scene extract.
- Embedded avatar audio is synchronization evidence, not the final mix; mute it in assembly.
- Never time-stretch the master to fit the visuals. Trim, offset, or rerender the visual pass with unchanged audio.
- Add music, ducking, ambience, and effects only after avatar visuals are aligned.
- A visual-only change does not reopen audio production.
- An approved audio change creates a new version and marks dependent avatar clips, captions, timing, proofs, and exports stale.

