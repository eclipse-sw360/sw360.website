---
title: "ADR Template (DAR/SWOT)"
linkTitle: "ADR Template (DAR/SWOT)"
weight: 99
---

# ADR Template: Decision Analysis and Resolution (DAR)

> **Template Version:** 1.0  
> **Based on:** ABT UI Technology Stack Decision Framework  
> **Approach:** SWOT Analysis + T-Shirt Sizing for Weighted Criteria Evaluation

---

## ADR-XXX: [Decision Title]

**Created by:** [Author Name]  
**Last updated:** [Date]  
**Estimated read time:** [X] minutes

---

## Table of Contents

1. [Background](#background)
2. [Goal](#goal)
3. [Key Principles](#key-principles)
4. [Key Inputs, Assumptions and Restrictions](#key-inputs-assumptions-and-restrictions)
5. [Options Analysis](#options-analysis)
   - [Option 1](#option-1---name)
   - [Option 2](#option-2---name)
   - [Option 3](#option-3---name)
6. [Criteria for Making a Decision](#criteria-for-making-a-decision)
7. [Final Decision](#final-decision)
8. [Contributors](#contributors)
9. [Discussion & Brainstorming](#discussion--brainstorming)

---

## Background

[Describe the experience and context that led to this decision point. Include:]
- What is the current state?
- What problems or feedback triggered this decision?
- Why is this decision important now?
- What are the business/technical drivers?

---

## Goal

[State the goal of this decision analysis clearly:]
- What problem are we trying to solve?
- What outcomes do we expect?
- How will we measure success?

---

## Key Principles

[List the guiding principles that will inform this decision:]

| # | Principle | Description |
|---|-----------|-------------|
| 1 | [Principle Name] | [Brief description] |
| 2 | [Principle Name] | [Brief description] |
| 3 | [Principle Name] | [Brief description] |

---

## Key Inputs, Assumptions and Restrictions

| Type | Description |
|------|-------------|
| **Input** | [Known fact that informs the decision] |
| **Assumption** | [Something we believe to be true but cannot verify] |
| **Restriction** | [Hard constraint we must work within] |

---

## Options Analysis

### Option 1 - [Name]

#### Summary
[Brief description of this option - 2-3 sentences]

#### Conceptual View
[Architecture diagram or description of how this option works]

```
[ASCII diagram or reference to image]
```

#### Impact / Changes Required
[What changes would be needed to implement this option?]

#### SWOT Analysis

| Category | Analysis |
|----------|----------|
| **Strengths** | 1. [Strength 1]<br/>2. [Strength 2]<br/>3. [Strength 3] |
| **Weaknesses** | 1. [Weakness 1]<br/>2. [Weakness 2] |
| **Opportunities** | 1. [Opportunity 1]<br/>2. [Opportunity 2] |
| **Threats** | 1. [Threat 1]<br/>2. [Threat 2] |

---

### Option 2 - [Name]

#### Summary
[Brief description of this option]

#### Conceptual View
```
[ASCII diagram or reference to image]
```

#### Impact / Changes Required
[What changes would be needed?]

#### SWOT Analysis

| Category | Analysis |
|----------|----------|
| **Strengths** | 1. [Strength 1]<br/>2. [Strength 2] |
| **Weaknesses** | 1. [Weakness 1]<br/>2. [Weakness 2] |
| **Opportunities** | 1. [Opportunity 1] |
| **Threats** | 1. [Threat 1] |

---

### Option 3 - [Name]

#### Summary
[Brief description of this option]

#### Conceptual View
```
[ASCII diagram or reference to image]
```

#### Impact / Changes Required
[What changes would be needed?]

#### SWOT Analysis

| Category | Analysis |
|----------|----------|
| **Strengths** | 1. [Strength 1] |
| **Weaknesses** | 1. [Weakness 1] |
| **Opportunities** | 1. [Opportunity 1] |
| **Threats** | 1. [Threat 1] |

---

## Criteria for Making a Decision

### T-Shirt Sizing Scale

| T-Shirt Size | Numeric Value | Meaning |
|--------------|---------------|---------|
| XS | 1.0 | Worst for this aspect |
| S | 2.5 | Poor |
| S-M | 3.75 | Below Average |
| M | 5.0 | Average |
| M-L | 6.25 | Above Average |
| L | 7.5 | Good |
| L-XL | 8.75 | Very Good |
| XL | 10.0 | Best for this aspect |

### Weighted Evaluation Matrix

| Criteria | Description | Weight (1-10) | Option 1 | | Option 2 | | Option 3 | |
|----------|-------------|---------------|----------|-------|----------|-------|----------|-------|
| | | | Rating | Score | Rating | Score | Rating | Score |
| **[Criterion 1]** | [Description] | [W] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] |
| **[Criterion 2]** | [Description] | [W] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] |
| **[Criterion 3]** | [Description] | [W] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] |
| **[Criterion 4]** | [Description] | [W] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] |
| **[Criterion 5]** | [Description] | [W] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] | [T-Shirt] | [W×V] |
| | | **TOTAL** | | **[Sum]** | | **[Sum]** | | **[Sum]** |

### Common Criteria (customize as needed)

1. **Performance** - Response time, throughput, resource usage
2. **Maintainability** - Ease of updates, debugging, code quality
3. **Developer Experience** - Learning curve, tooling, debugging
4. **Reuse of Existing Assets** - Leverage current code, tests, documentation
5. **Integration & Extensibility** - 3rd party support, future growth
6. **Time to Market** - Development speed, delivery timeline
7. **Team Feasibility** - Skills available, training needed
8. **Support & Community** - Vendor support, community, longevity
9. **Security** - Vulnerabilities, compliance, best practices
10. **Cost & Licensing** - License fees, infrastructure costs

---

## Final Decision

### Selected Option: **[Option Name]**

### Rationale
[Explain why this option was selected based on:]
- Total weighted score
- Key differentiating factors
- Risk considerations
- Strategic alignment

### Implementation Notes
[Any specific guidance for implementing the decision]

### Review Triggers
[Conditions that would cause us to revisit this decision:]
- [ ] [Trigger 1]
- [ ] [Trigger 2]

---

## Contributors

| Name | Role | Contribution |
|------|------|--------------|
| [Name] | [Role] | [What they contributed] |
| [Name] | [Role] | [What they contributed] |

---

## Discussion & Brainstorming

> **Instructions:** Team members add their thoughts, concerns, and suggestions below.

### [Name] - [Date]
[Comment or concern]

### [Name] - [Date]
[Comment or concern]

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial decision |
