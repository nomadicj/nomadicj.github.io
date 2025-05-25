---
title:  "Team composition - What team compositions should I be using to achieve my goals?"
date:   2023-08-09 21:00:00
categories: [organisation structure]
tags: []
---
When leading and adapting an organisation to the changing challenges backlogs present it is important to consider team composition and what impact that has on its overall approach. These are the key types you need to consider and use as tools in your leadership toolkit.

## Strike Teams - The “get it done” team
Occasionally you need a team to go and take on a defined task. Get a project done. Meet a deadline. On this team you need people who know what they are doing and, given direction, can make it happen. As such you should deploy a small team of highly skilled engineers who can hit the ground running with a minimum of fuss (trying to beat [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe's_law) with both low node count and high prior experience)

#### Composition (Total 4 - 6 members)
- Architect level tech lead capable of setting direction for the rest of the team
- 3-5 Senior to Staff level engineers
- An assigned individual who leads the Product and Kanban practice
#### Work Style
- [Milestone based Kanban](https://www.agilealliance.org/milestone-kanban-a-hybrid-project-scheduling-technique/)
#### Pros
- This team can get things done. Given a mandate and the space to deliver, amazing things can be delivered in very short periods of time.
#### Cons
- As individuals who are knowledgable and capable, they will likely be comfortable challenging norms and breaking rules that others can’t. They will likely be seen as being separate from the rest of your engineering team. Therefore their deployment on any given project should be reasonably short to avoid building a toxic “us and them” mentality in the overall engineering group.

## Holistic Service Teams - The “own that service” team
More typically you will want a team that owns between one and three services, depending on the size, complexity and age of those services. This team will own a service performing all new feature development, maintenance and operational overhead of the services they have in their purview. 
#### Composition (Total 6 - 10 members)
- Senior to Staff level tech lead to support others in their break down of work and to pre-digest the challenges around the challenge
- 2-3 Senior engineers who can mentor others and handle complex technical decisions
- 2-4 Mid-level engineers who can work independently on most tasks
- 1-2 Junior engineers who bring fresh perspectives while learning from the team
- 1 Product Manager or Product Owner to define priorities and requirements
- Optional: 1 Designer (shared across multiple teams) for user-facing features
#### Work Style
- Scrum
#### Pros
- Mixed experience allows junior members to grow in a safe and well mentored environment while seniors get the experience of mentoring and starting to lead.
#### Cons
- This structure is the workhorse of a SaaS engineering department. Using OKRs to keep things focussed, fresh and goal oriented is critical otherwise stagnation can occur.

## Shared Services Teams - The “specialists” team
A team of service area experts that it doesn’t make sense to have one on each of your other teams. Aggregate them into a single team and allow them to act as a supporting function on all teams while managing and maintaining a common approach and architecture for delivery of their speciality. Examples are Security, QA, DevOps/DevExp, ML, etc.
#### Composition (Total 3 - 8 members)
- Architect to set the overall vision and direction for the service area. 
- Good overall mix of contributors for the area
- Management taking an evangelic leadership role to ensure everyone sees the value in a common approach
#### Work Style
- Kanban style to react to requests for support from teams while 
#### Pros
- Bringing the common approach together in one team facilitates others and simplifies delivery for all.
- The one team creates a growth path for specialists. Without this there is little room for career growth, leading to undesirable departures.
#### Cons
- This model works by mutual consent. If teams find interactions with this team negative, they will step away from this shared services model and will try to solve their own issues.
#### Variation
- Consider having an association between certain members of the team and regular client teams. Allow the team to build trust in the shared service capability and the individual to build understanding of the teams domain.

## Maintenance Teams - The “keep it alive” team
Sometimes a product or group of components needs to be put into “maintenance only” mode. Essentially there is nothing new to be done in that code base and you need a group of people to run maintenance only tasks. This team is intended for that.
#### Composition (Total 4 - 6 members)
- Senior to Staff level tech lead to support others in their break down of work and to pre-digest the challenges around the challenge
- Often the rest of the group is largely junior members who are happy to learn their tradecraft in this kind of environment. 
#### Work Style
- [Scrumban](https://www.agilealliance.org/scrumban/) as the issue list dictates
#### Pros
- Finding the right people to take on the maintenance role can be hard but if you have knowledgeable capable people who find this kind of work rewarding, embrace them and provide them with this opportunity.
#### Cons
- Attrition on this kind of team can be high. Your main challenge is creating a real sense of worth and value delivery for this group of people while presenting enough challenges to ensure they are feel personal career growth. 
#### Variation
- If you can fold one long term support code base/product into a Holistic teams backlog instead, try and do that. It’s sometimes easier to allocate 25% of an existing teams capacity rather than build this specialised kind of group.

## Anti-Patterns
### The group of individuals
To have an individual who is the sole knowledgable person around a subsystem/codebase/technology is a pretty common thing around some lesser known technologies. Email Spam, IdPs and OAuth stuff, JVM optimisation, Database storage partitioning. All of these things needs to be taken care of once in a while and it’s just easier to go back to the person who did it last time, time and time again. 

If we extrapolate that effect over a whole team, the unfortunate impact is that you end up with a group of individuals who cannot substitute for one another. The impact of any one individual taking well deserved vacation or personal leave is high and the pain of any one individuals departure from the company is far too great. A collection of individuals in this state is not healthy and unsustainable in the long term.

The system needs to be seen to reward this move away from individual ownership. Cross-training, breaking down barriers to collaboration and encouragement to diversity skillsets should be both mandated and rewarded. Time needs to be made available to doing all those things and glorification of individual success related to the single owner areas should be appropriately withheld.

## Summary
Creating a team that is well suited for the work you present them with is key for their overall long term success. While the consequence of a poorly thought out team composition is negatively impactful, get this right and you’ll be able to deliver amazing things.