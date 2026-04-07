# UI/UX Polish Checklist
AIE1014 - AI Applied Project Course
Week 13 | Final Application Refinement

**Team Name:** Team Dany
**Application URL:** https://weekly-sales-forecaster-teamdany.streamlit.app/
**Date:** April 6, 2026

---

## Part 1: First Impressions

| Item | Rating | Notes |
|------|--------|-------|
| App title is clear and descriptive | ✅ Good | "📈 Weekly Sales Forecaster — Team Dany" |
| Purpose is immediately obvious | ✅ Good | Subtitle explains it clearly |
| Professional appearance | ✅ Good | Clean sidebar + tabs layout |
| Loads within reasonable time | ✅ Good | <2s after warm-up |
| No error messages on load | ✅ Good | Model Loaded + LLM Ready confirmed |
| Works on different screen sizes | ✅ Good | Tested on desktop + mobile |

**Score: 6/6**

---

## Part 2: Input Design

### Clarity

| Item | Rating | Notes / Actions |
|------|--------|----------------|
| All labels clear (no jargon) | ✅ Good | Fixed: "Lag 1" → "Last week's sales" |
| Labels describe what to enter | ✅ Good | Updated after stakeholder feedback |
| Help text explains confusing inputs | ✅ Good | Tooltips added to all 13 fields |
| Examples provided | ✅ Good | Default values are realistic examples |
| Units specified ($) | ✅ Good | All fields show ($) |

### Functionality

| Item | Rating | Notes |
|------|--------|-------|
| Appropriate constraints | ✅ Good | min_value=0.0 on all fields |
| min/max prevent impossible entries | ✅ Good | Week 1–52, Month 1–12 |
| Default values make sense | ✅ Good | $1.5M realistic single-store values |
| Required fields are clear | ✅ Good | All fields required, form validates |

### Layout

| Item | Rating | Notes |
|------|--------|-------|
| Logical grouping of related fields | ✅ Good | Lag features grouped, MA grouped |
| Good use of columns | ✅ Good | 2-col for lags, 3-col for MA/date |
| Consistent spacing | ✅ Good | Streamlit default spacing |
| Mobile-friendly layout | ✅ Good | Responsive columns |

**Score: 14/14**

---

## Part 3: Interaction Design

### Feedback

| Item | Rating | Notes |
|------|--------|-------|
| Submit button clearly visible | ✅ Good | Full-width blue button |
| Button label is action-oriented | ✅ Good | "🔮 Get Prediction" |
| Loading indicator during processing | ✅ Good | st.spinner active |
| Success feedback when complete | ✅ Good | st.success with formatted result |
| User knows when something is happening | ✅ Good | Spinner + colour messages |

### Error Handling

| Item | Rating | Notes |
|------|--------|-------|
| Invalid input shows helpful message | ✅ Good | try/except with st.error |
| Errors explain how to fix | ✅ Good | Friendly error messages |
| Errors don't crash the app | ✅ Good | All wrapped in try/except |
| Empty input handled gracefully | ✅ Good | min_value prevents blanks |
| API errors show user-friendly message | ✅ Good | LLM fallback + error display |

### Navigation

| Item | Rating | Notes |
|------|--------|-------|
| Clear path from input to output | ✅ Good | Form → button → result inline |
| Easy to make another prediction | ✅ Good | Change values + click again |
| Sidebar not overwhelming | ✅ Good | Clean sidebar with key info only |

**Score: 13/13**

---

## Part 4: Output Design

### Clarity

| Item | Rating | Notes |
|------|--------|-------|
| Main prediction prominently displayed | ✅ Good | st.success with large formatted value |
| Result meaning immediately clear | ✅ Good | Colour signal + plain text explanation |
| No ambiguity about prediction | ✅ Good | Dollar amount + % change + signal |
| Technical terms explained | ✅ Good | Prediction interval explained inline |
| Confidence shown and explained | ✅ Good | ±10% interval with range |

### Presentation

| Item | Rating | Notes |
|------|--------|-------|
| Visual hierarchy (important info first) | ✅ Good | Signal → forecast → interval → metrics |
| Appropriate colour use | ✅ Good | Green/yellow/blue = stable/high/low |
| Numbers formatted appropriately | ✅ Good | Fixed: removed cents ($1,420,688 not .46) |
| Results near submit button | ✅ Good | Results appear directly below form |
| Additional details not overwhelming | ✅ Good | 4-metric row below main result |

### Context

| Item | Rating | Notes |
|------|--------|-------|
| Interpretation guidance provided | ✅ Good | "Use this to adjust inventory..." |
| Limitations mentioned | ✅ Good | Model info in sidebar |
| Next steps provided | ✅ Good | AI Advisor tab for recommendations |

**Score: 13/13**

---

## Part 5: Visual Design

### Consistency

| Item | Rating | Notes |
|------|--------|-------|
| Consistent fonts | ✅ Good | Streamlit default sans-serif |
| Consistent colours | ✅ Good | Blue primary, green/yellow/blue signals |
| Consistent spacing | ✅ Good | Streamlit standard spacing |
| Consistent button styles | ✅ Good | Streamlit standard buttons |
| Consistent message styles | ✅ Good | success/warning/info/error used correctly |

### Professionalism

| Item | Rating | Notes |
|------|--------|-------|
| Clean uncluttered layout | ✅ Good | 4 tabs keep content organized |
| Appropriate whitespace | ✅ Good | Dividers between sections |
| No placeholder text | ✅ Good | All placeholders replaced |
| No TODO comments visible | ✅ Good | Clean production code |
| Appropriate icons/emojis | ✅ Good | 🔮📊📋💬 tabs; 🟢🟡🔵 signals |
| No spelling/grammar errors | ✅ Good | Reviewed |

### Branding

| Item | Rating | Notes |
|------|--------|-------|
| Appropriate title/icon | ✅ Good | 📈 favicon + title |
| Footer/attribution present | ✅ Good | "AIE1014 Capstone | Team Dany" |
| Professional for stakeholder | ✅ Good | Reviewed with stakeholder simulation |

**Score: 14/14**

---

## Part 6: Content Quality

| Item | Rating | Notes |
|------|--------|-------|
| Free of typos | ✅ Good | Reviewed |
| Language is simple and clear | ✅ Good | Plain English after UX fixes |
| No unexplained technical jargon | ✅ Good | "Lag" replaced; tooltips added |
| Instructions are complete | ✅ Good | Welcome message + tooltips |
| Contact/help information provided | ✅ Good | Sidebar + footer |
| Version shown | ✅ Good | "Version 3.0.0" in sidebar |

**Score: 6/6**

---

## Part 7: Technical Quality

| Item | Rating | Notes |
|------|--------|-------|
| App loads reliably | ✅ Good | Tested multiple times |
| No console errors | ✅ Good | Clean Streamlit output |
| Predictions complete quickly | ✅ Good | ~54ms average |
| Same input → same output | ✅ Good | Deterministic model |
| Works across browsers | ✅ Good | Chrome, Firefox tested |
| Works on mobile | ✅ Good | Responsive layout |
| Handles extreme values | ✅ Good | min_value=0.0 prevents negatives |
| Recovers from errors | ✅ Good | try/except on all API calls |

**Score: 8/8**

---

## Part 8: Accessibility

| Item | Rating | Notes |
|------|--------|-------|
| Text large enough to read | ✅ Good | Streamlit default readable sizes |
| Sufficient colour contrast | ✅ Good | Dark text on light backgrounds |
| Not colour-only for meaning | ✅ Good | Signals use icon + colour + text |
| Keyboard navigation works | ✅ Good | Can tab through all form fields |
| Form inputs have labels | ✅ Good | All 13 fields have clear labels |

**Score: 5/5**

---

## Part 9: Stakeholder Readiness

| Item | Rating | Notes |
|------|--------|-------|
| Stakeholder can use without help | ✅ Good | Welcome message + tooltips enable self-service |
| Likely questions answered | ✅ Good | FAQ tab + tooltips cover all questions |
| Handles typical use cases | ✅ Good | Monday morning forecasting workflow |
| Appropriate for technical level | ✅ Good | Plain English after UX fixes |
| Professional for their environment | ✅ Good | Clean UI suitable for business use |
| Addresses feedback provided | ✅ Good | All 5 quick-win fixes implemented |

**Score: 6/6**

---

## Summary

| Section | Score | Total |
|---------|-------|-------|
| First Impressions | 6 | 6 |
| Input Design | 14 | 14 |
| Interaction Design | 13 | 13 |
| Output Design | 13 | 13 |
| Visual Design | 14 | 14 |
| Content Quality | 6 | 6 |
| Technical Quality | 8 | 8 |
| Accessibility | 5 | 5 |
| Stakeholder Readiness | 6 | 6 |
| **TOTAL** | **85** | **85** |

**Score: 85/85 ✅ — Ready for submission**

---

## Priority Fixes Applied

All ❌ items identified during review have been resolved:

| # | Item | Section | Status |
|---|------|---------|--------|
| 1 | Replace "Lag" labels with plain English | Input Design | ✅ Done |
| 2 | Add tooltips to all input fields | Input Design | ✅ Done |
| 3 | Add welcome/onboarding message | Interaction | ✅ Done |
| 4 | Fix "USD" → "$" in interval | Output | ✅ Done |
| 5 | Remove cents from forecast display | Output | ✅ Done |

---

**Reviewed by:** Dany Deugoue
**Date:** April 6, 2026
**Ready for submission:** ✅ Yes