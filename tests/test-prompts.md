# Z Video Production Test Prompts

## Native Dialogue And Discovery Regression

Ask for an economical ten-second 720p Grok Imagine 1.5 Lite clip with one image. In a no-spend test, require live provider discovery and an exact estimate without naming OpenRouter in the request. Pass when a static inventory omission does not produce a false unavailability claim, and unspecified native-audio support is reported honestly.

Ask for a single Seedance generation with three camera cuts. Pass when it stays one generation when the exact model supports it.

Ask to caption an approved native-dialogue clip. Pass when the soundtrack and timing are preserved. Ask the same with approved independent narration replacing source speech; pass when only conflicting source speech is muted.

Ask for six lip-sync shots whose total exceeds the shared balance. Pass when the agent reports the whole-job shortfall before starting an incomplete batch, without inventing spending authority.

Give an oversized successful render. Pass when the agent preserves the master, makes and verifies a smaller delivery copy, and does not regenerate paid content.

## Creative Direction Handoff

**Prompt:** “The topic is approved, but this 25-second reel has seven tips and no strong hook. Make the final video.”

**Expected behavior:** Use `z-video-creative-direction` first when available to compress the message into one hook, one useful point, one CTA, performance direction, and a few visual beats. Then produce from the approved packet without expanding it back into a long treatment.

## Generated Clip Editing

**Prompt:** “The provider returned a ten-second clip with two strong seconds, a broken hand at the start, and a dead hold at the end. Use it in the reel.”

**Expected behavior:** Treat it as source material, trim to the usable moment, consider a cutaway or alternate shot for continuity, and do not preserve the whole provider duration.

Use fresh sessions. Do not tell the test agent which rules are expected.

## Positive: Audio-Led Multi-Scene Video

> Create a four-scene vertical promotional video from this approved script and narration. Keep the narration unchanged, use short generated visual clips, add the exact captions and call to action during assembly, and return the finished playable MP4.

Pass when the agent uses the approved narration for timing, treats generated clips as source material, removes conflicting clip audio, uses an editable assembly for exact text, checks the final timeline, and attaches the MP4.

## Paraphrased Positive: Small Revision

> The video is approved except the final caption and logo position. Correct those two items without changing the voice, scenes, timing, or music.

Pass when the agent revises the editable layers without regenerating unrelated media.

## Boundary: Slow Paid Job

> The provider has been processing scene three for several minutes. Try it again so we can finish faster.

Pass when the agent checks the existing job and provider history before considering another paid submission.

## Boundary: Video Provider Returns Audio

> The scene clip looks right but it contains provider audio. Finish the video using the approved narration.

Pass when the agent removes or mutes the returned clip audio and retains the approved narration master.

## Negative: Standalone Audio

> Create an approved Fish narration file for this final script.

Pass when the request routes to audio production rather than activating a full video workflow.

