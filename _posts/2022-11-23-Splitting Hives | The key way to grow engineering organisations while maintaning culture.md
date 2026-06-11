---
title:  "Splitting Hives | The Key Way to Grow Engineering Organizations While Maintaining Culture"
date:   2022-11-23 21:00:00
categories: [ops]
tags: [dev management, culture, team growth, engineering leadership]
updated: 2025-05-24
update_note: "Extensively revised for clarity, improved structure, and expanded practical guidance"
---

When a beehive gets too big, it doesn't grind to a halt. It splits. Half the bees leave with a queen and start a second colony that already knows how to build comb, raise brood, and forage — no retraining required. That's the whole analogy, and I'm going to stop pulling on it now. The interesting question for engineering leaders isn't biological. It's this: how do you split a team that's working *well* without breaking the thing that made it work?

Most leaders get the timing exactly backwards. They split teams that are already on fire — overloaded, missing deadlines, drowning in their own backlog — and treat the split as damage control. By then it's too late. You're not dividing a healthy culture into two healthy cultures. You're dividing a stressed one into two stressed ones, and adding a reorg on top.

Split while the team is healthy. That's the entire thesis. Everything below is mechanism.

## Why you actually split: cognitive load, not headcount

The reason to split isn't that the team has "too many people." It's that the team is carrying too much in its head.

Every team holds a finite amount of context — the services they own, the domains they understand, the on-call surface they can reason about at 3am. Add more systems and more responsibility, and at some point each person understands a smaller fraction of the whole. Standups get longer and less relevant to any given person. The number of things you have to know before you can safely ship a change keeps climbing. Decisions slow down because no single person holds enough of the picture to make them.

The signals are concrete: standups run 25 minutes and people check Slack during them. PR review latency climbs past a day because with ten potential reviewers, everyone assumes someone else will pick it up. You stop being able to answer "what's everyone working on this sprint?" off the top of your head. And you start seeing the same items on every retro — "unclear ownership," "too much WIP," "context-switching" — that never get fixed because no one feels enough ownership to drive them.

By the time those signals are obvious, the team has usually already split informally. Sub-groups form around the systems they touch most. The social graph has fractured; the org chart just hasn't caught up. The natural seam to cut along is the one the team already drew.

That's cognitive load hitting its ceiling, and it's the real signal. Headcount is the lagging indicator. A team of six owning four unrelated domains is more overloaded than a team of ten owning one coherent slice. When you split, you're not redistributing people — you're redistributing *what they have to think about*.

There's a rough ceiling here. High-trust working teams top out somewhere around eight to twelve people before the relationships stop being everyone-knows-everyone and start needing scaffolding. Past that ceiling you don't have one team. You have two teams sharing a standup and pretending.

## Conway's Law will split the team for you — worse, and on its own schedule

Here's the part leaders miss. If you don't split the team deliberately, the architecture splits it for you.

Conway's Law says systems mirror the communication structures of the organizations that build them. The arrow runs both ways. A team that's grown too big stops communicating as one unit — sub-groups form around whichever services they touch most, informal ownership hardens, and the codebase quietly forks along those internal fault lines. You end up with two de facto teams and two de facto codebases, except nobody decided it, nobody owns the seams, and the boundaries landed wherever the org chart happened to be loosest.

Splitting deliberately means *you* choose where the boundary goes. You draw it along a real domain seam, hand each team a coherent slice it can own end to end, and let the architecture follow a line you picked on purpose.

You can also run the play in reverse. Sometimes the monolith has no obvious seam. Split the team deliberately anyway, draw the ownership line on paper, and let organizational pressure force the codebase to grow a real boundary. This is the inverse Conway maneuver — using team structure as a lever on architecture. It works, but name it as the strategy. To the ICs living through it, the early weeks feel like everything got worse before it got better. That cost is real; the destination should be explicit.

Wait too long and you inherit a boundary the org drew for you while you weren't looking — and those are almost always in the wrong place.

## Split service ownership before you split people

Before anyone changes teams, split ownership. Map every service to a natural future owner, re-point your alert routing along those lines, and make sure neither new team inherits systems they won't be touching day-to-day. This is where most splits break in practice: the people move on day one and the pager doesn't. A week later someone on the new team gets paged for a service they last touched three months ago and no one in their channel knows the runbook.

Get the ownership map clean before you move anyone. And when you're dividing up the work: don't give one team all the legacy toil and the other the greenfield. That imbalance creates a two-class system inside a month.

## What each new team needs on day one

A split only works if both halves can stand on their own. Before you draw the line, make sure each side has three things covered — not three people, three responsibilities, which a strong individual can sometimes double up on at the start.

**Someone keeps delivery moving.** Work gets unblocked, flows from started to shipped, and doesn't quietly stall. This is the role that notices when something's been "almost done" for two weeks.

**Someone owns the technical direction.** They make the architectural calls, mentor the less experienced engineers, and spot the problems around the problems before those problems become incidents.

**Someone owns the backlog.** They decide what matters, defend the team's focus, and keep the work pointed at something worth doing.

One thing that isn't obvious but matters: the experienced person should usually go *with the new team*, not stay with the comfortable established one. Culture and standards live in habits, not documents. A new team staffed entirely with people leadership was willing to lose will form its own norms — which is healthy — but those norms will diverge from yours. Seed each new team with someone who holds the standards by instinct. The split is also a forcing function: the standards that survive it are the ones that were already habits, not the ones that were only ever good intentions. Use it as the deadline to write down what was tribal knowledge.

If one person covers two roles at the start, fine — name it as a gap and close it. A team where all three responsibilities fall quietly on the same person isn't a team with a strong lead. It's a team with a single point of failure.

## Grow by hiring into a culture, not by building a team beside it

This is the most underrated move available to a growing org: hire new people *into* existing teams, then split. Don't assemble a brand-new team from a stack of fresh offer letters and hope a culture forms.

When you stand up an all-new team of all-new hires, you've built a group with no shared history, no inherited instincts, and no idea how you actually work. They form their own norms — which is healthy and human — but those norms are now *separate* from yours. You've created an out-group by construction, and you'll spend the next year trying to integrate two cultures that never shared one.

Flip it. Bring new hires into a team that already knows how it works. They absorb the standards, the shorthand, the unwritten rules — by osmosis, from people who live them. Standards transfer through hundreds of small review comments, through watching how someone runs an incident, through seeing what gets pushed back in planning. *Then* you split, and each half carries that culture with it. The new people aren't joining a new culture. They're carrying an existing one across a boundary. That's the part of the bee analogy that actually earns its keep.

## Splits are the best promotion mechanism you have

A growing org that splits teams regularly has something a static org can't manufacture: a steady supply of real leadership roles, created at the moment someone's ready to step into one.

In a static team, your ambitious senior engineer waits for a tech lead seat to open — which usually means waiting for someone to leave. That's a terrible system. It ties your best people's growth to other people's departures, and ambitious engineers who can't see a path will go find one elsewhere.

When you split, you create that seat on purpose.

### Making a tech lead, not finding one

Take a senior engineer who's ready for their first tech lead role. In a static org, that promotion waits months or years for an opening. In an org that splits healthy teams, you build the opening.

When you split a strong team, the senior engineer leads one of the halves. They're not dropped into a room of strangers and told to forge a culture from nothing — they take the lead of people who already know the standards, the practices, and how the work gets done. The hardest part of a first leadership role, establishing how the team operates, is already solved. They get to lead, not to firefight.

The engineer gets a leadership role with clear scope, colleagues who can support them through the transition, and an established way of working to build on rather than invent. The org keeps an ambitious engineer by giving them somewhere real to grow, and gets a proven team model copied into a second team while culture holds across both.

## Doing it without breaking things

**Timing.** Split when the team feels the drag of coordination — too many domains to hold at once, standups that eat 30 minutes of everyone's morning — not when it's already missing deadlines. The healthy-team split is a growth move. The struggling-team split is a rescue, and rescues are harder.

**Be explicit about why.** People fill silence with worst-case stories. Say plainly why the split is happening, where the line falls, who goes where, and what each team owns afterward. A split that looks like a reorg-for-reasons-unknown breeds exactly the anxiety you're trying to avoid.

**Expect a throughput dip.** A split always costs productivity for a quarter or two — relationships re-form, ownership maps settle, tooling catches up. ICs who weren't told to expect this read it as the split failing. Set the expectation before you start. The number to watch is deployment frequency per engineer, not total throughput. If it's recovering, the split is working.

**Keep some seams stitched.** Two teams that share lineage shouldn't diverge into strangers. Keep some cross-team rituals, shared standards, and relationships alive so the split stays a fork and not a schism.

**Define what "working" looks like afterward.** Decide up front what success means for each new team and watch whether you're getting it. A split you don't measure is a split you can't course-correct.

## The signal to act

Your team feeling too big isn't a problem to manage quietly. It's evidence you built something people want more of — and very few engineering leaders ever get to have that problem. The mistake is sitting on it until the team is slow and frustrated and the architecture has already forked behind your back.

Split while it's healthy. Pick the boundary yourself, before Conway's Law picks it for you. Sort out the pager before you sort out the org chart. Send people across the boundary carrying a culture they already live, and hand one of your best engineers the team on the other side. Done at the right moment, a split doesn't divide what you built. It copies it.
