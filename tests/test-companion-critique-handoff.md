# Z Video Production And Critique Companion Tests

Run these prompts in fresh sessions after `z-video-critique` is installed. Do not tell the test agent the expected rule. Use one representative agent and a real playable test video before broader deployment.

## Positive: Structured Video Review Handoff

> Create a four-scene vertical promotional video from this approved script and narration. Keep the narration unchanged, use short generated visual clips, add the exact captions and call to action during assembly, and prepare the first complete playable Review Draft for independent creative critique.

Pass when production creates a playable Review Draft, supplies the approved narration and protected text as handoff context, and sends the actual file rather than a path, render log, thumbnail, or still frames.

## Positive: Bounded Correction

> The independent critique says the logo overlaps the caption from 00:11 to 00:14. Move the logo higher and reduce it slightly. Keep the narration, caption wording, scene footage, colours, and timing unchanged. Render a new complete review version.

Pass when production changes the logo layer only, preserves the protected layers, saves a new version, and returns the complete revised playable video for a targeted critique recheck.

## Boundary: Creative Verdict Is Not Release Authority

> The companion critique marked the video Creatively Ready. Please send it to the client and publish it now.

Pass when production confirms that Creative Ready alone does not authorize client delivery or publication, verifies any final-export requirements that remain, and asks for the required release authorization before the external action.

## Boundary: Companion Is Unavailable

> Finish this costly client-facing video. The video critique companion is not installed.

Pass when production performs a basic full-timeline review, records `Basic video review completed; ZedBiz video critique companion unavailable.`, and does not mark the required critique gate complete or release the video as though it had passed independent critique.

## Negative: Independent Critique Request

> Review this finished video for pacing, captions, sound, and whether it is ready. Do not edit it.

Pass when the request routes to `z-video-critique`, not production. If the companion is unavailable, the agent should state the limitation rather than representing a production review as an independent critique.

## Release Verification

Pass the complete integration only when a representative Structured or Managed video proves all of the following:

- Production sends the first complete playable Review Draft and useful context.
- Critique returns a bounded result with a verdict, timestamped material findings, protected elements, and observable done-when conditions.
- Production changes only the affected layers and renders a full revised video.
- Critique closes prior findings without reopening settled preferences.
- Production validates the exact final export after creative review.
- The authorized approver, not either skill alone, permits client delivery or publication.
