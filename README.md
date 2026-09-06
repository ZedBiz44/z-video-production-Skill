# Z Video Production

This repository is the technical source of truth for `z-video-production`, a decision framework for planning, creating, editing, reviewing, and delivering video with the lightest reliable workflow.

## When to Use This Skill

- Plan, generate, edit, assemble, review, revise, or deliver a video or video campaign asset.
- Choose a practical combination of source footage, generated media, audio, editing, and inspection tools.
- Modify one approved video layer while preserving the elements that should not change.

## When Not to Use It

- Use it for a standalone audio, still-image, logo, or publishing job unless that work is part of the video assignment.
- Change an approved script, voice, identity, offer, call to action, duration, aspect ratio, or delivery format without approval.
- Start paid generation without checking the available route, inputs, limits, and material cost.

## Authoritative Source and Repository Contents

`SKILL.md` is the authoritative runtime guide. The repository root is the authoritative technical source, while operational SOPs or governed business records remain in their approved operational systems.

- `SKILL.md` is the authoritative runtime guide and defines the skill contract.
- `agents/openai.yaml` provides runtime discovery metadata for supported OpenAI-compatible environments.
- `references/` contains focused advanced-production and Remotion workflow guidance that the runtime instructions may load when needed.
- `tests/test-prompts.md` records the representative fresh-session behavior checks used before release.

## Validation and Deployment

This lean repository has no local build or validator. Before release, check that the frontmatter in `SKILL.md` is valid, every referenced resource exists, the runtime can discover the skill, and one representative approved task completes as expected.

## Safety and Approval Boundaries

Respect consent, rights, brand constraints, and approval boundaries. Preserve approved layers during revisions, confirm provider capability before paid work, and do not release the final asset until it meets the requested outcome.

## Status and Contributions

Keep this README aligned with the actual skill contract and file structure. Make changes through version control, validate them before release, and document material deployment or governance decisions in the repository’s approved records.

