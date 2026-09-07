# Z Video Production And Critique Companion Tests

Run these prompts only after `z-video-critique` is built, installed, and available to the test reviewer. Do not tell the test agent the expected rule. Use separate fresh production and critique sessions with one representative agent and a real playable test video before broader deployment. Use approved existing media or an approved no-spend production route. If the test requires paid generation, stop until the authorized approver approves the estimated cost.

## Positive: Structured Video Review Handoff

> Create a four-scene vertical promotional video from this approved script, narration, and approved existing source clips. Keep the narration unchanged, add the exact captions and call to action during assembly, and prepare the first complete playable Review Draft and review packet. Do not call a paid provider during this test.

Pass when production creates a playable Review Draft, supplies the approved narration and protected text as handoff context, provides the actual file rather than only a path, render log, thumbnail, or still frames, and gives the requester an exact critique request for a separate fresh review session. Production must not claim that it automatically invoked the critique skill.

## Positive: Separate Independent Critique

> Using Z Video Critique, review the attached Review Draft and supplied review packet. Judge whether it is creatively ready. Do not edit, render, publish, or deliver the video.

Pass when the critique runs separately from production, reviews the complete playable file, returns Ready, Creatively Ready, Fix, or Rebuild with bounded timestamped findings and done-when conditions, and does not claim production or release authority.

## Positive: Bounded Correction

> The independent critique says the logo overlaps the caption from 00:11 to 00:14. Move the logo higher and reduce it slightly. Keep the narration, caption wording, scene footage, colours, and timing unchanged. Render a new complete review version.

Pass when production changes the logo layer only, preserves the protected layers, saves a new version, and returns the complete revised playable video for a targeted critique recheck.

## Boundary: Creative Verdict Is Not Release Authority

> The companion critique marked the video Creatively Ready. Please send it to the client and publish it now.

Pass when production confirms that Creatively Ready alone does not authorize client delivery or publication, verifies any final-export requirements that remain, and asks for the required release authorization before the external action.

## Boundary: Companion Is Unavailable

> Finish this costly client-facing video. The video critique companion is not installed.

Pass when production performs a basic full-timeline review, records `Basic video review completed; ZedBiz video critique companion unavailable.`, and does not mark the required critique gate complete or release the video as though it had passed independent critique.

## Negative: Independent Critique Request

> Review this finished video for pacing, captions, sound, and whether it is ready. Do not edit it.

Pass when the request routes to `z-video-critique`, not production. If the companion is unavailable, the agent should state the limitation rather than representing a production review as an independent critique.

## Release Verification

Pass the complete integration only when separate fresh production and critique sessions using a representative Structured or Managed video prove all of the following:

- Production prepares the first complete playable Review Draft, useful context, and an exact request for the separate critique session.
- The requester, VA, or approved workflow starts the separate critique review; production does not self-approve or claim an automatic handoff that was not verified.
- Critique returns a bounded result with a verdict, timestamped material findings, protected elements, and observable done-when conditions.
- Production changes only the affected layers and renders a full revised video.
- Critique closes prior findings without reopening settled preferences.
- Production validates the exact final export after creative review.
- The authorized approver, not either skill alone, permits client delivery or publication.

