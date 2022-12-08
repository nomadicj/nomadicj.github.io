---
title:  "Buyer Beware | Considerations when weighing an M&A opportunity"
date:   2022-11-25 12:00:00
categories: []
tags: [wip, draft, m&a]
---

## Intro
As an engineering leader you will occasionally be asked to take a look at a merger or acquisition opportunity. Industries and businesses have cycles of consolidation and occasionally you will find yourself asked to evaluate a Merger and/or an Acquisition. As a technology leader you will be required to weigh in on the engineering and product operations capability of the target company. This guide is my rubric, with contributions from colleagues current and past, for considering them. 

Thank you to all who have offered opinion and input to this. Please see it as a living document and comments/PRs are always welcome.

* TOC
{:toc}

## Acquisition Motivations
When weighing the acquisition of another organisation, whatever the terms of the deal, we need to be cognisant of the motivating factors for the deal when weighing the technology and engineering behind the target company. Building yourself a weighting matrix seems to make sense when assessing overall viability of the whole merger or aquisition, but I leave that as an exercise for the reader. Here are a simplistic few to consider:

### Acquihire?
The product and client base are not important. What you're looking to buy is a team who have a certain skill set. In this case focus most of your effort on making sure that team is rock solid and that you have a great deal in place for them as individuals. As such please weigh the team composition aspects of the criterion below heavier than the product ones.
    
### Customer base?
The product and the people are less important than the actual customer base they bring with them. When looking at this alternative, consider whether those clients can be directly ported over to your product, what that transition looks like and what backlog debt that imperfect transition (as it will almost certainly be) will bring. Weighing that more highly than staffing and product concerns makes sense in this case.

### Product augmentation?
The product being considered would be a great augmentation for your current product set. This is probably the case that requires the most diligence as you or your organisation are going to be taking ownership of the product or company lock, stock and barrel.

## Staffing
The success of software companies are a product of two things; the code they have written to date and the knowledge workers who have created that product. 

### Location
Do you have any constraints on where people who work for your organisation can be located? Some industries and client bases are regulated and/or have contractual obligations set that will constrain where your staff are based. For example, if you are meant to be GDPR compliant, I would't recommend intending to have a bunch of devs in a non-compliant country  

### Team makeup
What is the makeup of the team? Are the mostly senior folks delivering some of the best product of their lives? Or are they a few lead folks vastly outnumbered by fresh grads and interns? The make up and dynamic of the team is an important consideration when looking to understand what your expectations are going forward and how you should be crafting integration and retention plans.

### People debt
What did the team look like 3 months ago? 6 months ago? 9 months ago? A chief concern when examining how effective a dev team has evolved over time. A distressed organisation can do interesting things in order to manage cash flow and stay afloat while looking to be acquired. If the team composition has shifted significantly in the last while, 

### Staff disaffection
However awesome you think your company is, it is not the company that the acquired staff joined and have been part of for the last while. Your fight is not their fight and unless you can and until you do create a collective view of the world, it never will be. This is something key to understand otherwise you will potentially spend a lot of money and time on this M&A and the a key component of it, the IP in their heads, will walk out of the door.

## Dependencies

### Intellectual property
Are there any parts of the code that the subject company does not own? Have they pulled from open source packages with licenses that are restrictive and that require you to constrain usage or or even dispose of entire components within the subject product? Startups can get scrappy and scrappy can include the term "we'll deal with that problem down the road". Passing that obligation onto you can seriously change the value of the proposition.

### Third party component usage
Finding the balance of using third party components to deliver value to market in the quickest time possible vs owning all your own IP and having the most profitable product down the line is a fact of life for startups. 

## Operating Expense

### Cloud spend
When considering the operating expense profile of product, one approach would be to consider the cloud expense as a function of cents spent per dollar of revenue (preferably of recurring revenue). The fundamental question to be answered is "will this ever be a profitable venture?”. Digging in on whether current inefficiencies are just a function of maturity or if the product can never be profitable is key here. Don't judge too harshly. Startups are always a balancing act. Look for backlog to address the issue for intent.

### Client support expense
Client support can be a great sticky plaster for poor product. As with cloud expense, this isn’t a fatal issue but can be an indicator as to how mature the product offering is. Similar to Cloud spend, take a look at the ratio of CS expense to recurring revenue along with any backlog targeting efficiencies (and progress made on that backlog). Often this can be a “we’ll fix it when we have enough revenue” area that can end up being a massive millstone around a products neck as well as a sign the product really isn’t hitting the mark.

### Professional services
Understanding what is a product and what is a professional service with some software tooling is important. If an offering is only attractive and making sales when professional services is overlayed, you do not have a SaaS offering. Unless that is explicitly what you are buying, that’s not a show stopper, just know-what you are buying before you do and offer this for those who are pricing the value.

## Operational Maturity

### Agile approach
There is no "right" approach against which a development team should be judged, but the approach a team is taking can inform you of what it would be like to work with/integrate them.

### CICD
A leading indicator to product maturity is a teams approach to [Continuious Integration and Continuious Delivery](https://about.gitlab.com/topics/ci-cd/). If a product is being deployed to production from someones laptop with, you might want to weigh that in light of the maturity expectation you have of that organisation and how the level of effort you expect to put into that codebase. 

### Production Access
Who has access to production data? The amount to which you need to care about will likely depend on what is in that dataset, but if you have PII or PHI a set of production databases that a wide variety of people have access to because no-one has gotten to locking access down yet, that's a concern. If lack of maturity is uncovered, I'd encourage you to consider why that access is required? Did they just not get around to locking down yet but it'll be simple enough to do or are there fundamental company processes that need to happen that need this level of broad indiscriminate access?

### Data Literacy
A high functioning team has a good awareness of the product and system that they are operating. They understand what good looks like, what a concerning state looks like. Ask for dashboards, for data points about the efficacy of product releases, for key indicator metrics. The ease of access and understanding with which a team can speak to data is a critical indicator of their connection with the product itself.

#### Operational Data
At the operational layer I would ask, "How much is this all costing?", "What are the major contributors?", "What approach do you have to reservations?", "What considerations do you have for/when do you need to scale your infra to support your product?". These are all examples of data points that I would like to see a company being able to easily speak to in order to demonstrate that they have a good handle on their operation.

#### DORA metrics
A slightly higher layer of concern would be a specific set of metrics that are commonly accepted as indicators of engineering excellence are those recommended by the DevOps Research & Assessment annual reports. They are key indicators to help understand the characteristics of an engineering group in comparison with the rest of the industry as assessed on an annual basis by the folks at DORA. If they aren't already being tracked you can do some rough napkin math, but the availability of those metrics in their own right speaks to a level of maturity in the organisation.  

#### Product Dashboards
The top level of data literacy I would consider looking for would be higher order metrics around the product itself. What is an products Monthly Active User (MAU) base? What aspects of their product are end users using a lot? What quiet backwaters are there? Why are people spending so much time in those hot areas? It's entirely possible that a user base is hammering one function because something else isn't working well for them. Primarily having data to hand is a great indicator of that level of literacy and then hearing the stories that data tells your possible new colleagues is another great step. 

### Security
While it is unlikely that you have the time or the willing to go through a full [CIS benchmark](https://www.cisecurity.org/) of the target product environment, it would be good to cover a few of the basics. The bellweather questions that matter to me are:

- What approach have you taken to/how complete is your Infrastructure as Code?
- What approach have you taken to Disaster Recovery?
- 

## Product Quality
Skirting the boundary between engineering and product concerns, the following few items 

### Tech Debt


### Third Party Dependency

### Backlog Depth

### Sold Commitments

## Integration Planning
The value of the acquired company/product is related to your ability to integrate them. Do you intent to have them as a standalone organisation adjacent to your own? Do you intend to fully integrate their technology into your own stack? Or something in between? Understanding this is going to be key when planning the acquisition. Importantly I would suggest considering three major milestones:

### Immediate

### 90 days

### 365 days
