---
title:  "Buyer Beware | Considerations when weighing an M&A opportunity"
date:   2022-11-25 12:00:00
categories: []
tags: []
---

* TOC
{:toc}

## Aquisition Motivations
When weighing the aquisition of another organisation, whatever the terms of the deal, we need to be cognicent of the motivating factors for the deal when weighing the technology and engineering behind the target company. Here are a simplistic few to consider:

### Aquihire?
    
The product and client base are not important. What you're looking to buy is a team who have a certain skill set. In this case focus most of your effort on making sure that team is rock solid and that you have a great deal in place for them as individuals.
    
### Customer base?

### Product augmentation?

## Staffing

The success of software companies are a product of two things; the code they have written to date and the knowledge workers who have created that product. 

### location

Do you have any constraints on where people who work for your organisation can be located? Some industries and client bases are regulated and/or have contractual obligations set that will constrain where your staff are based. For example, if you are meant to be GDPR compliant, I would't recommend intending to have a bunch of devs in a non-compliant country  

### team makeup

What is the makeup of the team? Are the mostly senior folks delivering some of the best product of their lives? Or are they a few lead folks vastly outnumbered by fresh grads and interns? The make up and dynamic of the team is an important consideration when looking to understand what your expectations are going forward and how you should be crafting integration and retention plans.

### people debt

What did the team look like 3 months ago? 6 months ago? 9 months ago? A chief concern when examining how effective a dev team has evolved over time. A distressed organisation can do interesting things in order to manage cash flow and stay afloat while looking to be aquiried. If the team compision has shifted significantly in the last while, 

### staff disaffection

However awesome you think your company is, it is not the company that the aquired staff joined and have been part of for the last while. Your fight is not their fight and unless you can and until you do create a collective view of the world, it never will be. This is something key to understand otherwise you will potentially spend a lot of money and time on this M&A and the a key component of it, the IP in their heads, will walk out of the door.

## Dependencies

### interlectual property

Are there any parts of the code that the subject company does not own? Have they pulled from open source packages with licenses that are restrictive and that require you to constrain usage or or even dispose of entire components within the subject product? Startups can get scrappy and scrappy can include the term "we'll deal with that problem down the road". Passing that obligation onto you can seriously change the value of the proposition.

### third party component usage

Finding the balance of using third party components to deliver value to market in the quickest time possible vs owning all your own IP and having the most profitable product down the line is a fact of life for startups. 

## Cloud Spend

### fd

## Operational Maturity

### CICD

A leading indicator to product maturity is a teams approach to [Continuious Integration and Continuious Delivery](https://about.gitlab.com/topics/ci-cd/). If a product is being deployed to production from someones laptop with, you might want to weigh that in light of the maturity expectation you have of that organisation and how the level of effort you expect to put into that codebase. 

### Production Access

Who has access to production data? The amount to which you need to care about will likely depend on what is in that dataset, but if you have PII or PHI a set of production databases that a wide variety of people have access to because no-one has gotten to locking access down yet, that's a concern. If lack of maturity is uncovered, I'd encourage you to consider why that access is required? Did they just not get around to locking down yet but it'll be simple enough to do or are there fundamental company processes that need to happen that need this level of broad undiscriminate access?

### DORA metrics

### Security

While it is unlikely that you have the time or the willing to go through a full [CIS benchmark](https://www.cisecurity.org/) of the target product environment, it would be good to cover a few of the basics. The bellweather questions that matter to me are:

- What approach have you taken to/how complete is your Infrastructure as Code?
- What approach have you taken to Disaster Recovery?
- 

## Integration Planning

### Immediate

### 90 days

### 365 days