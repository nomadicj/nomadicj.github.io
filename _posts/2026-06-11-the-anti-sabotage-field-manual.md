---
layout: post
title: "The Anti-Sabotage Field Manual"
date: 2026-06-11
---

The OSS published their *Simple Sabotage Field Manual* in 1944 to help occupied citizens quietly destroy their enemies from the inside. The terrifying part isn't that it worked during wartime — it's that most engineering organizations reproduce every tactic on the list, accidentally, every single quarter.

The manual had three audiences: people running meetings, people managing others, and individual contributors. The inverse follows the same structure. Each principle below is the direct counter to a specific sabotage tactic — reframed for the engineering organizations that actually need it.

---

## Part I: Decisions and the Meetings That Stop Them

The original manual's first target was collective decision-making. Its saboteur was told to invoke channels, form committees, reopen settled questions, and wrap every decision in procedural fog. The goal: make shipping feel dangerous and delay feel safe.

The modern version doesn't look like sabotage. It looks like rigor. It looks like a steering committee, an RFC that's been "in review" for three weeks, and a decision that gets relitigated in every retro. The counter isn't recklessness — it's the same discipline that keeps your change failure rate low and your deploys boring.

**1. Push decisions to where the context lives.**
Escalation is a routing decision, not a safety ritual — and every hop up the org chart adds latency to a system that already has too much. The engineer debugging the incident has more context at 2am than the VP will have at the 10am sync. Let them make the call. Reserve escalation for decisions with a genuinely large blast radius: irreversible data changes, security posture, anything that touches money or trust. Everything else, push down. If you find yourself in the approval path for a config change, you're the bottleneck, not the safeguard.

**2. Optimize for change lead time, not airtime.**
Long speeches are someone spending the room's time to feel heard. The number that matters is how fast an idea travels from "we should" to "it's in prod" — and a forty-minute monologue is pure lead time with no throughput. Make your point, show your evidence, stop. If your argument only holds together with a war story and three caveats, it isn't ready to ship.

**3. Small group, hard deadline, written output.**
The saboteur wanted committees of five-plus with no end date, because a group that large can't decide anything and a group with no deadline never has to. Invert both: two or three people who own the outcome, a fixed date, and a written artifact at the end — a decision record, an RFC, an ADR. A "working group" that meets indefinitely isn't deliberating. It's generating the appearance of progress while the real decisions get made in DMs by the people who got tired of waiting.

**4. Name the drift and cut it.**
A meeting that wanders is an incident with no incident commander. When the conversation slides off the thing you're there to decide, say so out loud and pull it back. Park the tangent in a follow-up ticket or ADR and move on. Time spent on the wrong topic doesn't come back, and unlike a rolled-back deploy, there's no revert.

**5. Decide it, record it, and hold it.**
Write the decision where the team can find it — including the context and the alternatives you rejected, so nobody reconstructs your reasoning six months later. Then hold it. Reopen it for exactly one reason: new data changed the inputs. "I've been thinking about it" is not new data. You can disagree with the outcome and commit to it anyway — that's what makes a decision real, and a team that can do that ships faster than one that needs full consensus before moving.

**6. Write to be understood once, then ship the doc.**
Wordsmithing a decision document into oblivion is procrastination with a spell-checker. Clarity is the bar, not polish. Write so the intent can't be misread, publish it, move to the work it describes. A doc still being edited is a doc that isn't being executed against.

**7. Default to the reversible move.**
"Let's be cautious" wears the costume of good judgment. Reserve your caution budget for the one-way doors: irreversible data migrations, public API contracts, deleted production data. For everything else, the whole reason you invested in feature flags, canary deploys, fast rollback, and observability is so you can ship the small change, watch the graphs, and adjust. Slow is a choice — and on two-way doors, it's almost always the wrong one.

**8. If you have enough context to have an opinion, own the call.**
"Is this really our team's remit?" is occasionally a real question about ownership. Far more often it's a way to hand the pager to someone else. Decision ownership should map to the people closest to the work and its consequences — the same way service ownership does. Make the call, put your name on it, and own what happens next. Diffused ownership is how things rot in the gap between two teams that each assumed the other had it.

---

## Part II: What Engineering Leadership Actually Looks Like

The manual's sabotage playbook for managers was elegant in its malice: assign important work to the wrong people, demand perfection on trivialities, promote the useless, punish the competent, and bury everything in paperwork. The modern engineering org reproduces every one of these by accident — not through bad managers, but through good managers who confuse activity with progress and control with leadership.

**1. Direct the mission, not the mechanics.**
Tell a team what outcome they're accountable for and why it matters. Resist specifying the implementation. A team that needs your approval on its technical approach isn't a team — it's a queue of your decisions wearing a team's name. Push authority to where the context lives. If the engineers closest to the system don't have enough judgment to make technical calls, that's a hiring or onboarding problem, not a reason to keep the decisions centralized.

**2. Manage cognitive load as a first-class constraint.**
Ambiguous instructions are not a neutral failure — they transfer cognitive load onto the people least able to absorb it, while you keep the context in your head. The same is true of a sprawling service surface, tangled on-call responsibilities, and a backlog spanning four unrelated domains. Before you add anything to a team's plate — a new system to own, a new stakeholder to serve, a new process to follow — ask what it costs them in attention. A team carrying too much never fails loudly. It gets slow, and slowness is the hardest form of sabotage to detect because it looks like work.

**3. Design your team topology on purpose.**
The saboteur scattered responsibility so nobody owned anything end to end. The counter is deliberate team design: most teams should be stream-aligned — owning a slice of the product from idea to production, with everything they need to ship inside their boundary. When a team blocks constantly on another team, that's not a people problem; it's a topology problem. Stand up an enabling team to raise capability, or a platform to remove the toil — but don't let "we'll coordinate" stand in for a boundary you should have drawn. Coordination is the tax you pay for a missing boundary.

**4. Build a platform that removes toil, not a gate that collects it.**
There are two ways to be the team everyone depends on. One is to own the deployment pipeline, the golden paths, the shared infrastructure — and offer them as a product other teams choose because they're genuinely faster. The other is to insert yourself as a mandatory approval in everyone's path and call it governance. The saboteur ran the second playbook and called it standards. A real platform team measures itself by how fast its consumers ship. A gate measures itself by how many requests it processed. Know which one you're building.

**5. Optimize for flow efficiency, not resource utilization.**
A manager who keeps every engineer fully utilized has built a system that cannot move. Work queues everywhere — waiting for review, waiting for a deploy slot, waiting for the one person who understands the auth service. Watch the work, not the workers. How long does a change take from "started" to "in production," and how much of that time was actual work versus waiting? Cap work-in-progress, kill the queues, and accept that slack in the system is what makes it flow.

**6. Ship small, ship continuously, surface problems early.**
Small changes, merged often, deployed through a pipeline that makes shipping boring — this is not a practice for its own sake. It's how you keep your change failure rate low and your mean time to recovery short. The longer a branch lives, the more expensive its surprises. The point of small batches is that you find out you were wrong while the fix is still cheap. Every step you add between writing code and learning whether it works is a gift to entropy.

**7. Hold the line on what ships; release it on what doesn't.**
Decide what quality actually matters: the things that page someone at 3am, the data you can't recover, the trust you can't rebuild. Hold those hard — in automated tests and in the pipeline, not in a reviewer's mood on a given day. Set explicit reliability targets. Spend your error budget on velocity below them. Blocking a deploy over formatting a linter should have caught is sabotage with good intentions.

**8. Make psychological safety the precondition, not the perk.**
The saboteur's deepest move was to teach an organization that telling the truth is dangerous. The counter isn't a values poster. It's what happens in the room when someone says "I broke production" or "I think we're building the wrong thing." Run blameless postmortems because you mean it. Reward the engineer who killed their own bad idea before it shipped. The teams that ship fastest are the ones where the truth travels fastest, and the truth only travels where it's safe to carry.

---

## Part III: Individual Contributors

The manual's advice to the individual saboteur was almost poetic in its contempt for real work: move slowly, manufacture interruptions, feign incomprehension, blame the tools, and hoard what you know. Every one of these has a clean engineering equivalent — and most of them pass code review.

**1. Optimize for throughput, not the appearance of effort.**
Deliberate slowdown is obvious on an assembly line. In engineering it hides behind a full calendar, a busy Slack status, and a PR that's always "almost ready." The tell is the same one you'd use in a postmortem: trace the work back to a shipped change, a closed incident, a removed bottleneck. If the trail ends at a status update, you found the problem. Force multipliers are visible in what *other people* shipped because of them — the unblocked team, the migration that stopped being scary. Measure yourself by second-order effects, not your own commit count.

**2. Protect the maker's schedule — yours and the team's.**
Context-switching is not free. Reloading the mental model of a complex system after an interruption costs real minutes, and the cost compounds across a team. Batch the interruptible work. Defend long blocks for the work that needs a loaded cache. And when you carry the pager, treat on-call as the *containment* of interruption — the deal is that one person absorbs the chaos so the rest of the team doesn't have to. Break that deal and you've manufactured exactly the distraction the manual wanted.

**3. Reduce cognitive load instead of redistributing it.**
Feigning incomprehension was sabotage. So is its quieter cousin: shipping work that forces everyone downstream to reconstruct what you already understood. The clever one-liner that takes the next reader twenty minutes to parse. The PR with no description that makes the reviewer reverse-engineer your intent. The "self-documenting" code that documents nothing about *why*. Ask the real question once, get the real answer, then write the change so the next person doesn't have to ask it again. An ADR that captures why you rejected the obvious approach saves a future engineer from relitigating a decision you already worked through.

**4. Fix the tools — or stop routing around them.**
"The build is flaky." "The pipeline is slow." Sometimes the tools really are broken — and the flaky test you route around today is the incident you get paged for at 2am. So pick one: if the tooling is the problem, file it with a repro, fix it, or make the toil visible enough that someone funds the fix. If it isn't, the work is yours. The unacceptable middle is the shrug — quietly retrying the flaky test, hand-running the broken step, normalizing the deviance until the whole team has memorized a list of things that don't work and calls it "tribal knowledge." That list *is* the sabotage.

**5. Automate yourself out of the toil.**
Toil is the manual work that scales linearly with the system and teaches you nothing new the tenth time you do it. Hunt it. Every manual deploy step, every copy-paste runbook, every "just SSH in and restart it" is a candidate for a script, a pipeline stage, or a deleted requirement. The work isn't done when the ticket closes; it's done when the *next* person doesn't have to do it. This is the most underrated form of leverage available to an IC — and it's invisible on a sprint board, which is exactly why you have to make it explicit.

**6. Make yourself replaceable on purpose.**
Hoarding knowledge is the saboteur's legacy play: become the single point of failure, make the organization fragile, mistake indispensability for value. It feels like security. It's a bus factor of one and a vacation you can never fully take. The inverse is deliberate transfer: write the runbook before the incident, not after. Pair on the scary subsystem until someone else can carry the pager. Turn the answer you just gave in a DM into a doc that lives somewhere findable. A blameless postmortem is knowledge transfer at organizational scale — it converts one person's painful night into something the whole team now knows. The engineers who build systems other people can run without them are the ones who earn the room to do bigger work.

**7. Every artifact you hand off is a message to a stranger.**
The saboteur filed paperwork that was illegible, incomplete, or just plausible enough to waste the next person's day. The engineering surface area for this is enormous: a commit message that says "fix"; a ticket with no repro steps; a PR that bundles a refactor, a bugfix, and a formatting sweep so the reviewer can't actually review it; a runbook that's been wrong since the last migration. Write the commit message for the engineer bisecting a regression six months from now. Keep PRs small and single-purpose so review is a real check and not a rubber stamp. Update the doc in the same change that makes it stale. The person downstream is often you, with the context evaporated.

---

## A Final Note

None of the sabotage in the original manual required malice. Most of it just required inertia — channels that accumulated, committees that grew, approvals that multiplied, knowledge that stayed with the person who couldn't be bothered to write it down.

The counter has three parts. Push decisions to the people with the most context. Treat cognitive load as the scarce resource it is. Make the truth safe to carry. Everything else in this document is downstream of those three things, and they are downstream of each other — an organization that does all three ships, learns, and recovers faster than one running on heroism and tribal knowledge.

None of this requires a methodology. It requires building the conditions where good work can happen, and then getting out of the way.

---

*Based on Sections 11–12 of the OSS Simple Sabotage Field Manual (1944), declassified by the CIA in 2008.*
