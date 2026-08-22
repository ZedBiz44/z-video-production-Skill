# ZedBiz Skill Implementation Profile

## Identity And Ownership

- Organization and owner: ZedBiz
- Namespace and canonical skill: `z-video-production`
- Technical repository: `ZedBiz44/z-video-production-Skill`
- Operational record: `Z-Video-Production-Skill-SOP` in the Notion `AI-Agent-Skills-SOPs` database
- Required dependency: `z-audio-production` for approved narration and audio handoffs

## Supported Platforms

- Shared target: Codex, OpenClaw, and Hermes
- The core remains portable; platform adapters own discovery, placement, and tool differences.
- Pilot one authorized agent and a short controlled ZedBiz proof before wider deployment.

## Operating Controls

- Get-er-Done Mode: build the smallest approved proof, test it, and record evidence.
- Diagnose Mode: investigate and propose; make no changes until confirmation.
- Require approval before material paid generation, public publishing, client delivery, or production deployment.
- Stop after two failed paid attempts for one asset or three failed validation or repair attempts.
- Roll back to the last committed and approved project or skill version.

## Sources Of Truth

- GitHub owns skill files, scripts, tests, issues, commits, and technical deployment evidence.
- Notion owns the business-readable SOP, ownership, decisions, approvals, and operating summary.
- The Notion SOP links to GitHub and does not duplicate the complete `SKILL.md`.
- Record work in the repository issue and Cody's Technical Documentation daily journal.

## Security And Restricted Assets

- Secrets remain in 1Password or the approved runtime secret mechanism.
- Never commit provider keys, complete environment files, private voice sources, confidential consent records, client-confidential media, or unreleased campaign assets.
- Store only secure references to restricted assets in manifests and documentation.

