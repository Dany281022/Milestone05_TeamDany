# Stakeholder Feedback Worksheet
AIE1014 - AI Applied Project Course
Week 13 | Collecting and Acting on Feedback

**Team Name:** Team Dany
**Stakeholder Name:** Michael Thompson (AI-Simulated)
**Application URL:** https://weekly-sales-forecaster-teamdany.streamlit.app/
**Date Feedback Collected:** April 6, 2026

---

## Part 1: Feedback Collection Method

**Method used:** ☑ Other: AI-Simulated Stakeholder Session

> **Note to evaluator:** As direct stakeholder access was not available
> within the class timeline, this feedback was generated using GPT-4o-mini
> to simulate a realistic Retail Business Manager persona, as directed by
> the instructor. The AI was prompted with the application URL, stakeholder
> role, and realistic usage scenarios.

**Prompt used to simulate feedback:**
You are Michael Thompson, a Retail Business Manager with 12 years of
experience. You are NOT a data scientist. You manage weekly inventory
and staffing for a mid-size retail store doing ~$1.5M/week in sales.
You just used: https://weekly-sales-forecaster-teamdany.streamlit.app/
Provide honest feedback as a non-technical retail manager covering:
what confused you, what worked well, what you wish the app had,
and whether you would use it regularly.
**Session Details:**

| Detail | Value |
|--------|-------|
| Date/Time | April 6, 2026 — 10:00 AM |
| Duration | 20 minutes (simulated) |
| Method | AI simulation via GPT-4o-mini |
| Stakeholder persona | Retail Business Manager, 12 years experience |

---

## Part 2: Raw Feedback Notes

### Positive Feedback

| # | Feedback | Context |
|---|---------|---------|
| 1 | "The forecast number and demand signal colour were very clear immediately" | First look at results |
| 2 | "The percentage change vs last week was exactly what I needed" | Reviewing prediction output |
| 3 | "The AI explanation gave me specific actions, not just numbers" | Using AI Advisor tab |
| 4 | "Loading was fast — result in under a second" | After clicking Get Prediction |
| 5 | "The 4-tab layout kept things organized and not overwhelming" | Overall navigation |

### Issues / Concerns

| # | Feedback | Context |
|---|---------|---------|
| 1 | "Lag 1, Lag 2... what does 'Lag' mean? I'm not a statistician" | Reading input labels |
| 2 | "'Std Dev 4 weeks' — I had no idea what to enter there" | Filling the form |
| 3 | "I didn't know where to start when the app first loaded" | First 10 seconds |
| 4 | "Why does it say 'USD' instead of just '$'?" | Reading prediction interval |
| 5 | "The forecast shows $1,420,688.46 — I don't need cents for planning" | Viewing result |

### Feature Requests

| # | Request | Why They Want It |
|---|---------|----------------|
| 1 | Save inputs between sessions | "I enter the same store's data every Monday" |
| 2 | Show trend chart across last 4-6 predictions | "I want to see if we're trending up or down" |
| 3 | Import sales from CSV file | "I already have this data in Excel" |

### Questions Asked

| # | Question | Answer Provided |
|---|---------|----------------|
| 1 | "What is a reasonable number to enter for Std Dev?" | "~2-5% of your weekly average sales" |
| 2 | "Can I use this for multiple stores at once?" | "One store at a time; run separately per store" |
| 3 | "Does it remember my last inputs?" | "Not yet — session-based only currently" |

---

## Part 3: Usability Assessment

| Aspect | Rating (1-5) | Notes |
|--------|-------------|-------|
| Finding how to start | 3/5 | No welcome message on first load |
| Understanding input fields | 2/5 | "Lag" and "Std Dev" labels confusing |
| Making a prediction | 4/5 | Button clear, spinner visible, fast |
| Understanding results | 4/5 | Colour signal very intuitive |
| Overall ease of use | 3/5 | Good after labels improved |

### Points of Confusion Observed

| # | Where They Got Stuck | What They Did | What Should Happen |
|---|---------------------|---------------|-------------------|
| 1 | "Lag 1" label | Hesitated, guessed it meant last week | Label should say "Last week's sales" |
| 2 | "Std Dev 4 weeks" | Almost skipped it | Tooltip explaining how to estimate |
| 3 | App first load | Unsure where to start | Welcome message guiding first steps |

---

## Part 4: Usefulness Assessment

| Question | Response |
|----------|---------|
| Does the prediction help you make decisions? | "Yes — knowing 5% lower means I reduce perishable orders by the same amount" |
| How accurate do predictions seem? | "Feels realistic for a mid-size store, hard to verify without real data" |
| Would you use this regularly? | "Yes, every Monday morning before placing orders" |
| What's missing? | "Input saving, multi-week trend, CSV import" |

**Value Rating:** ☑ 4 - Very useful

**Why:** "The AI explanation turns a number into a decision — that's what I need"

---

## Part 5: Technical Assessment

### Performance

| Aspect | Rating | Notes |
|--------|--------|-------|
| Load time | ☑ Fast | <2 seconds after warm-up |
| Prediction time | ☑ Fast | 54ms average |
| Reliability | ☑ No issues | Tested on Chrome, no errors |

### Errors Encountered

| # | Error/Issue | When | Frequency |
|---|------------|------|-----------|
| 1 | None | — | N/A |

### Device / Browser Used

| Detail | Value |
|--------|-------|
| Device | Desktop laptop |
| Browser | Chrome |
| Compatibility issues | None |

---

## Part 6: Feedback Categorization

### Usability/UX

| Feedback Item | Severity | Effort | Action |
|--------------|----------|--------|--------|
| "Lag 1/2" labels are technical jargon | ☑ High | ☑ Low | Fix now |
| "Std Dev" field confuses non-technical users | ☑ High | ☑ Low | Fix now |
| No welcome/onboarding message | ☑ Med | ☑ Low | Fix now |

### Bug/Error

| Feedback Item | Severity | Effort | Action |
|--------------|----------|--------|--------|
| "USD" instead of "$" in interval | ☑ Low | ☑ Low | Fix now |
| Unnecessary cents in forecast ($1,420,688.46) | ☑ Low | ☑ Low | Fix now |

### New Feature Requests

| Feedback Item | Severity | Effort | Action |
|--------------|----------|--------|--------|
| Save inputs between sessions | ☑ High | ☑ High | Defer — needs database |
| Multi-week trend chart | ☑ Med | ☑ Med | Defer — needs persistent storage |
| CSV import for historical data | ☑ Med | ☑ High | Future version |

### Content / Clarity

| Feedback Item | Severity | Effort | Action |
|--------------|----------|--------|--------|
| Help tooltips on all input fields | ☑ High | ☑ Low | Fix now |

---

## Part 7: Prioritization Matrix

### Quick Wins (High Impact, Low Effort) — DO FIRST ✅

| # | Item | Status |
|---|------|--------|
| 1 | Replace "Lag 1/2" with plain English labels | ✅ Done |
| 2 | Add tooltip explaining "Std Dev" field | ✅ Done |
| 3 | Add welcome/onboarding info message | ✅ Done |
| 4 | Change "USD" to "$" in prediction interval | ✅ Done |
| 5 | Remove cents from forecast display | ✅ Done |

### Big Projects (High Impact, High Effort) — PLAN CAREFULLY

| # | Item | Decision |
|---|------|---------|
| 1 | Save inputs between sessions | ☑ Do later — requires backend database |
| 2 | Multi-week trend chart | ☑ Do later — needs persistent storage |

### Skip for Now (Low Impact, High Effort)

| # | Item | Reason |
|---|------|--------|
| 1 | CSV import | Significant feature beyond course scope |

---

## Part 8: Action Plan

### Immediate Actions (This Week)

| # | Action Item | Owner | Status |
|---|------------|-------|--------|
| 1 | Replace "Lag" labels with plain English | Dany | ✅ Done |
| 2 | Add Std Dev tooltip with estimation guide | Dany | ✅ Done |
| 3 | Add welcome message to Prediction tab | Dany | ✅ Done |
| 4 | Fix "USD" → "$" in confidence interval | Dany | ✅ Done |
| 5 | Remove cents from forecast display | Dany | ✅ Done |

### Deferred Actions

| # | Item | Reason |
|---|------|--------|
| 1 | Save inputs between sessions | Requires persistent backend storage |
| 2 | Multi-week trend chart | Session-based history already in History tab |

### Won't Fix (With Justification)

| # | Item | Justification |
|---|------|--------------|
| 1 | CSV import | Significant development beyond Milestone 5 scope |

---

## Part 9: Follow-Up Communication

**Draft Response to Stakeholder:**

> Dear Michael,
>
> Thank you for testing the Weekly Sales Forecaster and providing
> such detailed feedback. Here is a summary of what we heard and
> what we changed:
>
> **What we fixed based on your feedback:**
> - Replaced technical labels ("Lag 1") with plain English
>   ("Last week's sales") with helpful tooltips
> - Added a welcome message explaining where to start
> - Fixed the prediction interval format from "USD" to "$"
> - Removed unnecessary cents from the forecast display
>
> **What we couldn't fix yet (and why):**
> - Saving inputs between sessions requires a database backend
>   that is beyond our current infrastructure
> - We've noted the CSV import and trend chart for future versions
>
> The updated application is live at:
> https://weekly-sales-forecaster-teamdany.streamlit.app/
>
> Thank you again for your time!
> — Dany Deugoue, Team Dany

---

## Part 10: Documentation Updates

| Document | Updates Made |
|----------|-------------|
| User Guide | Added plain English field descriptions + tooltips section |
| FAQ | Added "Why are labels different from technical documentation?" |
| README | Updated to reflect v3.0 with UX improvements |
| In-app help text | Added tooltips to all 13 input fields |

### New FAQ Items

| Question | Answer |
|---------|--------|
| What do I enter for "Sales variability"? | About 2–5% of your weekly average. For $1.5M/week store, enter $25,000–$75,000 |
| Can I use this for multiple stores? | Yes — run the prediction separately for each store |

---

## Summary

### Feedback Statistics

| Category | Count |
|----------|-------|
| Total feedback items | 13 |
| Items fixed immediately | 5 |
| Items deferred | 2 |
| Items skipped | 1 |

### Key Takeaways

**What's working well:**
1. Colour-coded demand signals (🟢🟡🔵) are immediately intuitive
2. AI Advisor tab turns numbers into actionable business decisions

**What needs improvement:**
1. Technical labels ("Lag", "Std Dev") need plain English equivalents
2. First-load experience needs a welcome/onboarding message

**Most important change made:**
Replacing all technical field labels with plain English equivalents
and adding help tooltips — this single change would convert the app
from "developer tool" to "business tool" for the stakeholder.

---

**Feedback reviewed by:** Dany Deugoue
**Date:** April 6, 2026
**Next feedback session:** April 15, 2026 (post-submission review)
