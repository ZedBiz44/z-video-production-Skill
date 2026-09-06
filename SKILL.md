---
name: z-video-production
description: "Plan, create, edit, review, or deliver videos using the lightest reliable workflow and available media tools."
---

# Z Video Production

Make the requested video without adding process the job does not need. Treat this skill as a decision framework, not a fixed production sequence.

Use this skill for video planning, generation, editing, assembly, revision, review, or delivery. Do not use it for standalone audio, still images, logos, or publishing unless that work is part of the video assignment.

## Choose The Lightest Reliable Route

- Start from the user's actual outcome, source material, constraints, and definition of done. Clarify only missing information that would materially change the result.
- Choose the simplest suitable combination of generation, recording, stock or owned media, editing, assembly, and inspection.
- Use the user's requested product or provider when feasible. Otherwise choose from tools that are genuinely available in the current runtime.
- Before paid generation, verify the callable route, required inputs, current limits, and material estimated cost. Inspect the live model schema when the provider exposes or requires one. Do not confuse documented capability with a working connection.
- A quick clip may need only generation, a sensible review, and delivery. Add planning, records, proofs, or editable sources only when their value justifies the effort.

## Deliver The Requested Media Type

- If the user requests a video or video clip, completion requires a playable video file. An image, audio file, production plan, provider link, or promise to check later is not a substitute.
- Save completed provider media into the project before reporting success. Return the actual playable file through the channel's supported media attachment route; treat a URL as backup access only.
- If the requested media cannot be produced, report the real job status and failure. Do not disguise a fallback asset as the requested deliverable.
- For delayed jobs, keep the real job reference, use the runtime's supported background or status-check route, and check provider history before retrying. Do not abandon the job or submit a duplicate merely because generation is slow.

## Use Audio First When Timing Or Voice Matters

- Lock the spoken script before producing narration, lip-sync, captions, or final scene timing.
- Use `z-audio-production` to create the full approved dry narration when voice identity, exact wording, performance, or repeatability matters.
- Treat that full narration master as the final timing and performance source. Cut exact scene extracts from it; do not generate unrelated scene narrations that can drift or overlap.
- Give a talking-avatar or lip-sync route the exact scene extract when it requires audio. B-roll does not need to speak.
- Do not get stuck trying to force a video provider to return a silent clip. Generate the usable visual clip, then remove or mute its returned audio during assembly. Use the approved narration master in the final mix.

## Use Remotion And FFmpeg Deliberately

- Use Remotion for multi-scene editable assembly, captions, titles, lower thirds, logos, offers, URLs, calls to action, layout, timing, transitions, and repeatable revisions.
- Before changing a Remotion project, read `remotion-best-practices`, then load only the relevant official Remotion skill such as `remotion-markup`, `remotion-captions`, or `remotion-render`.
- Use FFmpeg for practical media preparation and inspection such as extracting or muting audio, trimming, conversion, concatenation when simple, frame capture, and final stream validation.
- Treat generated video as source material rather than a finished branded edit when exact text, consistent captions, multiple scenes, or future revisions matter.
- Read [Remotion production guidance](references/remotion-production.md) for an audio-led multi-scene edit or material Remotion revision.

## Preserve What Should Not Change

- Keep approved audio or visual assets stable when changing an unrelated layer. Do not silently change an approved script, timing, voice, identity, offer, call to action, brand treatment, provider, duration, aspect ratio, or delivery format. Revise the smallest part that solves the problem.
- Treat a supplied or approved script as the spoken words unless the user authorizes an adaptation.
- Never overwrite the only original or approved master. Save a new version when rollback may matter.
- Use an available audio-production skill—prefer `z-audio-production` when it is installed and authoritative—if consistent, approved, reusable, cloned, or lip-sync-critical audio matters. Do not force a full audio workflow onto casual audio that does not need it.
- When approved narration exists, use it as the timing source and final narration track. Derive scene audio from that master, mute conflicting audio embedded in generated avatar clips, and do not regenerate the same line merely to change a visual.
- When exact captions, logos, prices, calls to action, URLs, or other critical text matter, add them with an editable composition or editing tool rather than trusting generated pixels.
- Use character references or saved identities when the same identifiable person must remain consistent. Do not require a character package for disposable or unrelated people.
- Save editable sources and useful job details when revisions, reuse, handoff, rights, or accountability are reasonably expected.

## Scale Up Only When The Job Earns It

- Use more structure when the production is expensive, complex, repeatable, identity-sensitive, rights-sensitive, client-facing, revision-prone, or split across people or agents.
- Possible controls include a brief, shot list, approved audio, identity references, provider or rights records, proof render, editable project, or completion evidence. Use only the controls that reduce a real risk or future cost.
- Read [Advanced production guidance](references/advanced-production.md) when meaningful spend, recurring identity or voice, uncertain rights, client or public delivery, multi-worker handoff, or likely revisions create material risk.

## Respect Authorization Boundaries

- Obtain approval before meaningful paid generation when the user has not already authorized the spend.
- Do not publish, launch an ad, or deliver client-facing media unless that external action is authorized.
- Confirm permission and suitable usage rights before cloning or imitating a real person or using third-party media. Possessing a local file does not prove commercial usage rights.
- Check provider job history and real status before retrying or abandoning a slow or timed-out paid request. Do not repeatedly spend against the same failure; after two failed paid attempts for the same asset, stop and report unless further spend is authorized.
- Never invent provider output, job IDs, a completed render, or an inspection result. Do not silently substitute a materially different provider, model, voice, identity, or format to bypass a failure.

## Finish Against The Request

- Inspect the actual completed render across its full timeline using playback, video analysis, or an equivalent visual-and-audio review. Metadata-only inspection does not prove the video is good.
- Confirm it opens, plays, satisfies the requested content and format, and has no obvious visual, audio, timing, freeze, corruption, or truncation failure. Check delivery-specific details such as duration, aspect ratio, caption accuracy and synchronization, identity, brand treatment, text readability, safe areas, or platform compatibility when they matter.
- Report and attach the actual output file when the channel supports attachments, whether it is a working draft, review draft, or approved final, meaningful cost, and any unresolved limitation. Include the saved project location, provider, model, and job ID when they materially help recovery or accountability. A delivery attempt without a playable file or confirmed attachment is not complete.
- Do not create a manifest or formal completion report unless it helps this particular job or the user requests it.

