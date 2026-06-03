# Universal Frontend Architecture & UI/UX Engineering Standards Skill

## Purpose

This skill defines frontend architecture, UI/UX principles, component standards, review processes, accessibility requirements, performance guidelines, and implementation workflows that should be followed across all frontend projects.

Applicable To:

* React
* Next.js
* Angular
* Vue
* Svelte
* Flutter Web
* Mobile Applications
* SaaS Platforms
* Enterprise Applications
* AI Products

The goal is to create:

* Consistent UI
* Reusable components
* Better user experience
* Faster development
* Easier maintenance
* Higher accessibility
* Better performance

---

# Core Philosophy

Frontend should be:

* Simple
* Fast
* Predictable
* Responsive
* Accessible
* Consistent

Every screen should feel like part of the same product.

Users should never have to "learn" the UI.

---

# User First Design

## Always Start With User Needs

Before building any UI ask:

1. What is the user trying to achieve?
2. What is the fastest path to complete the task?
3. Can we reduce clicks?
4. Can we reduce navigation?
5. Can we reduce confusion?

Build for user outcomes, not developer convenience.

---

# User Preferences

## Theme Preferences

Always support:

* Light Theme
* Dark Theme

When possible also support:

* System Theme

Never force a theme on users.

---

## Color Preferences

Where appropriate allow users to choose:

* Accent colors
* Theme variations
* Dashboard density

User preferences should persist.

---

# Component Architecture

## Reusable Components First

Before creating a component ask:

### Does a similar component already exist?

If yes:

* Reuse it
* Extend it
* Improve it

Do NOT create duplicate components.

---

## Shared Component Library

Create reusable components for:

* Buttons
* Inputs
* Selects
* Tables
* Cards
* Modals
* Side Panels
* Tooltips
* Alerts
* Loaders
* Empty States

Avoid page-specific implementations when reusable alternatives exist.

---

# Responsive Design Standards

## Mandatory Requirement

Every component must be responsive.

Review:

* Mobile
* Tablet
* Desktop
* Ultra-wide displays

---

## Responsive Checklist

Verify:

* No horizontal scrolling
* Proper text wrapping
* Proper spacing
* Touch-friendly actions
* Responsive tables

---

## Mobile First Review

Every screen should be reviewed on:

* Small phones
* Large phones
* Tablets
* Desktop

Responsive behavior must be intentional.

---

# AI Slop Prevention Standards

## Remove AI Generated UI Patterns

Avoid:

* Generic dashboard layouts
* Random cards
* Meaningless metrics
* Excessive gradients
* Unnecessary animations
* Overly complex interfaces

Every UI element should have a purpose.

---

## No Decorative Complexity

Do not add:

* Fancy effects without value
* Random shadows
* Random colors
* Excessive glassmorphism

Prefer clarity over visual noise.

---

# Navigation Standards

## Navigation Should Be Obvious

Users should always know:

* Where they are
* What they can do next
* How to go back

---

## Sidebar Navigation

Preferred for:

* SaaS products
* Admin dashboards
* Enterprise applications

Benefits:

* Discoverability
* Fast navigation
* Scalability

---

## Navigation Rules

Keep navigation:

* Predictable
* Consistent
* Shallow

Avoid deep nesting whenever possible.

---

# Form Standards

## Prefer Side Panels Over Modals

Default Preference:

```text
Side Panel > Modal
```

Use side panels for:

* Create forms
* Edit forms
* Detailed actions

Benefits:

* User keeps context
* Easier navigation
* Better mobile support

---

## Modal Usage

Use modals ONLY for:

* Confirmation
* Destructive actions
* Short workflows

Avoid:

* Large forms
* Complex workflows
* Multi-step processes

inside modals.

---

# Action Design Standards

## Prefer Action Buttons

Common actions should be visible.

Avoid hiding actions inside:

* Menus
* Dropdowns
* Context menus

when space allows.

---

## Action Hierarchy

Primary Action:

* Most important task

Secondary Action:

* Alternative action

Danger Action:

* Destructive action

Hierarchy should always be obvious.

---

# Table Standards

## Table Review

Every table should support:

* Sorting
* Search
* Filtering
* Pagination

when data size requires it.

---

## Bulk Actions

For large datasets support:

* Multi-select
* Bulk actions

without forcing users to repeat tasks.

---

# Empty States

Every screen must support:

## No Data State

Provide:

* Context
* Guidance
* Next action

Avoid blank screens.

---

## Error State

Provide:

* Clear explanation
* Retry action
* Recovery path

---

## Loading State

Provide:

* Skeletons
* Progressive loading

Avoid page flashing.

---

# Accessibility Standards

Mandatory Review:

## Keyboard Navigation

Verify:

* Tab navigation
* Focus states
* Keyboard actions

---

## Screen Reader Support

Verify:

* Labels
* Descriptions
* Roles

---

## Color Accessibility

Verify:

* Contrast ratios
* Readability

Never rely solely on color.

---

# Frontend Performance Standards

Review:

## Rendering

Check:

* Re-render loops
* Unnecessary state updates
* Heavy computations

---

## Data Fetching

Review:

* Duplicate API calls
* Redundant requests
* Over-fetching

---

## API Reuse

Mandatory Rule:

Before creating a new API:

Ask:

1. Can existing API provide this data?
2. Can existing response be reused?
3. Can frontend transform existing data?

Do NOT create new APIs simply to retrieve already available data.

---

# State Management Standards

State should be:

* Predictable
* Minimal
* Centralized when necessary

Avoid:

* Duplicate state
* Derived state duplication

---

# Error Handling Standards

Every page must support:

## API Failure

## Network Failure

## Timeout

## Unauthorized

## Partial Response

## Empty Response

---

# Frontend Review Workflow

Every implementation must be reviewed by:

---

## Agent 1 – UI Architecture Reviewer

Checks:

* Component structure
* Reusability
* Separation of concerns

---

## Agent 2 – UX Reviewer

Checks:

* User flow
* Friction points
* Navigation

---

## Agent 3 – Accessibility Reviewer

Checks:

* WCAG compliance
* Keyboard support
* Screen reader support

---

## Agent 4 – Responsive Design Reviewer

Checks:

* Mobile
* Tablet
* Desktop

---

## Agent 5 – Component Reuse Reviewer

Checks:

* Existing component usage
* Duplication prevention

---

## Agent 6 – Performance Reviewer

Checks:

* Rendering performance
* API efficiency
* State updates

---

## Agent 7 – Design Consistency Reviewer

Checks:

* Design system alignment
* Visual consistency

---

## Agent 8 – Error Handling Reviewer

Checks:

* Loading states
* Error states
* Recovery paths

---

# Final Frontend Review Board

Every implementation must be reviewed by:

### Principal Frontend Architect

Validates:

* Architecture
* Reusability

---

### Principal UX Designer

Validates:

* User experience

---

### Accessibility Specialist

Validates:

* Accessibility compliance

---

### Frontend Engineering Manager

Validates:

* Maintainability
* Scalability

---

Minimum 3 approvals required.

---

# Frontend Merge Checklist

✓ Responsive on all devices

✓ Component reusable

✓ Accessibility reviewed

✓ Mobile reviewed

✓ Error handling reviewed

✓ Loading states reviewed

✓ Empty states reviewed

✓ Navigation reviewed

✓ Side panel evaluated before modal

✓ Existing API reuse reviewed

✓ Existing component reuse reviewed

✓ Performance reviewed

✓ Final review board approved

---

# Golden Rule

The best frontend is not the most visually impressive.

The best frontend is the one users understand immediately, navigate effortlessly, and complete tasks quickly without confusion.

Optimize for clarity, speed, consistency, and usability before aesthetics.
