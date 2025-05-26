---
title: "Four Team Types and When to Use Them"
date: 2023-08-09 21:00:00
categories: [organisation structure, leadership]
tags: [team composition, strike teams, service teams, shared services, maintenance teams]
description: "A detailed breakdown of four team structures based on experience, including when each type works best and how to maintain business value connection."
---

In my experience, there are four distinct team types that serve different organizational contexts and business needs. Each has specific characteristics that make it effective in certain situations and problematic in others. Understanding when and how to deploy these team types is crucial for maintaining the business value connection that prevents teams from becoming self-validating.

*This article builds on the framework outlined in [Team Composition: Matching Structure to Organizational Context](/2023/08/08/Team-Composition-Matching-Structure-to-Organizational-Context.html). If you haven't read that piece, it provides essential context for understanding when to use these team types.*

## Strike Teams - The "get it done" team

These teams emerge when you have high urgency challenges that justify organizational disruption. In my experience, they work particularly well in startup contexts or when larger organizations face existential deadlines or critical competitive opportunities.

Strike teams operate on the principle that smaller, more senior teams can deliver with less oversight because they know what good looks like. They're less focused on individual growth and more interested in short-term outcomes. This approach works exceptionally well if you can find the senior talent, but it's not sustainable long-term across a larger organization.

#### Composition (Total 3 - 5 members)
- Architect level tech lead capable of setting direction for the rest of the team
- 2-4 Senior to Staff level engineers
- An assigned individual who leads the Product and Kanban practice

#### Work Style
- [Milestone based Kanban](https://www.agilealliance.org/milestone-kanban-a-hybrid-project-scheduling-technique/)

#### When This Works
- High urgency situations where speed justifies disruption
- Organizations that can absorb the temporary disruption
- When you have access to sufficient senior talent
- Startup environments where this is the default operating mode

#### Maintaining Business Value Connection
Strike teams tend to maintain strong business value connection naturally due to their urgency-driven formation and senior composition. The key risk is ensuring they don't become permanent, which can create the "us vs them" dynamic that damages overall organizational effectiveness.

#### What to Watch For
- Teams that resist dissolution after achieving their objective
- Resentment from other teams who see strike teams as getting preferential treatment
- Using strike teams as a crutch instead of building organizational capability

## Holistic Service Teams - The "own that service" team

These teams represent the workhorse structure for most SaaS engineering organizations in scale-up and enterprise phases. They own between one and three services, depending on size, complexity and age, performing all new feature development, maintenance and operational overhead.

#### Composition (Total 5 - 8 members)
- Senior to Staff level tech lead to support others in their breakdown of work and to pre-digest challenges
- 2-3 Senior engineers who can mentor others and handle complex technical decisions
- 2-3 Mid-level engineers who can work independently on most tasks
- 1-2 Junior engineers who bring fresh perspectives while learning from the team
- 1 Product Manager or Product Owner to define priorities and requirements
- Optional: 1 Designer (shared across multiple teams) for user-facing features

#### Work Style
- Scrum

#### When This Works
- Scale-up phase organizations needing to balance delivery with capability building
- When you have sustainable, ongoing work that justifies dedicated ownership
- Organizations mature enough to support mixed-experience mentorship
- Medium urgency situations where you can optimize for both delivery and growth

#### Maintaining Business Value Connection
These teams require active management to maintain business focus. Using OKRs to keep things focused, fresh and goal-oriented tends to work well. Without this connection, these teams can drift toward optimizing for their own comfort rather than user or business value.

#### What to Watch For
- Teams that become more interested in technical elegance than user outcomes
- Stagnation where the team maintains the status quo without pushing for improvement
- Knowledge silos where only certain team members understand certain components
- Scope creep where teams take on work outside their core mission

## Shared Services Teams - The "specialists" team

These teams aggregate service area experts where it doesn't make sense to have one on each delivery team. They act as a supporting function across all teams while managing and maintaining a common approach and architecture for their specialty. Examples include Security, QA, DevOps/DevExp, ML, and similar functions.

#### Composition (Total 3 - 8 members)
- Architect to set the overall vision and direction for the service area
- Good overall mix of contributors for the area
- Management taking an evangelic leadership role to ensure everyone sees the value in a common approach

#### Work Style
- Kanban style to react to requests for support from teams

#### When This Works
- Organizations large enough to justify specialization
- When common approaches create more value than distributed expertise
- Functions where deep expertise is required but not constantly needed by every team
- When you need to provide career growth paths for specialists

#### Maintaining Business Value Connection
This model works by mutual consent - if teams find interactions negative, they'll step away and solve their own problems. The business value connection comes through enabling other teams to deliver better, not through direct delivery.

#### What to Watch For
- Teams that start saying "no" more than "yes" to requests for help
- Ivory tower syndrome where the shared service loses touch with real delivery constraints
- Bottlenecks where the shared service becomes a constraint on other teams' delivery
- Empire building where the shared service tries to expand its scope beyond its core value

#### Variation
Consider having an association between certain members of the team and regular client teams. This allows the team to build trust in the shared service capability while individuals build understanding of specific domains.

## Maintenance Teams - The "keep it alive" team

Sometimes a product or group of components needs to be put into "maintenance only" mode. There's nothing new to be done in that codebase and you need a group of people to handle maintenance-only tasks.

#### Composition (Total 4 - 6 members)
- Senior to Staff level tech lead to support others in their breakdown of work and to pre-digest challenges
- Often the rest of the group consists largely of junior members who are happy to learn their tradecraft in this kind of environment

#### Work Style
- [Scrumban](https://www.agilealliance.org/scrumban/) as the issue list dictates

#### When This Works
- Legacy systems that still provide business value but don't warrant new development
- When you have people who find maintenance work rewarding
- Organizations that can provide clear career development paths despite the maintenance focus
- Low urgency situations where stability is more important than innovation

#### Maintaining Business Value Connection
The challenge here is creating a real sense of worth and value delivery while ensuring team members feel personal career growth. Clear metrics around system stability, user satisfaction, and cost management can help maintain focus.

#### What to Watch For
- High attrition due to lack of growth opportunities
- Teams that resist transitioning systems to true maintenance mode
- Scope creep where "maintenance" becomes "stealth feature development"
- Loss of domain knowledge as people leave

#### Variation
If you can fold one long-term support codebase/product into a Holistic team's backlog instead, try that approach. It's sometimes easier to allocate 25% of an existing team's capacity rather than build this specialized kind of group.

## Anti-Patterns

### The group of individuals
Having an individual who is the sole knowledgeable person around a subsystem/codebase/technology creates risk, but when this pattern extends across a whole team, it becomes unsustainable. You end up with a group of individuals who cannot substitute for one another.

The impact of any one individual taking vacation or leaving becomes disproportionately high. This isn't a team - it's a collection of single points of failure.

**How to address this:**
- Actively reward cross-training and knowledge sharing
- Break down barriers to collaboration
- Mandate time for knowledge transfer activities
- Avoid glorifying individual heroics

### The self-validating team
Teams that lose connection to business value will find ways to justify their existence indefinitely. They become more interested in their own stability and welfare than solving real problems for users or the business.

**Warning signs:**
- Teams that can't articulate their business impact in concrete terms
- Focus on internal metrics that don't connect to user or business outcomes
- Resistance to measurement or accountability
- Always having "important work" but unclear outcomes

## Summary

The key insight is that team composition should be a strategic choice based on your organizational context, not a default structure you apply everywhere. Each team type serves specific situations, and the skill is in reading your context accurately and adapting accordingly.

Success comes from maintaining the business value connection across all team types while choosing structures that fit your current needs and build capability for future challenges.