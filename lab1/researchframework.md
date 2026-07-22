# Research Conceptual Framework
## MATLAB Lab 1 Metacognitive Calibration Pilot Study

**Status:** Pilot Study (Phase 1 of larger calibration research program)  
**Sample:** ~60 students, 1 cohort, 1 semester  
**Questions:** 30 MCQs across 10 topics  
**Elicitation:** SR (self-report) + PDW (token wager) parallel design  
**Generated:** July 2026

---

## 1. HONEST SCOPE STATEMENT

### What This IS
✅ A **pilot study** to establish feasibility and measurement protocols for metacognitive calibration research in MATLAB  
✅ A **single-cohort proof-of-concept** for dual-elicitation design (SR vs PDW)  
✅ A **foundational dataset** that can be extended to multi-cohort longitudinal tracking  
✅ **Chapter content for PhD dissertation** (methodology + preliminary findings)  
✅ A **benchmark** for future MATLAB calibration research at SGT and elsewhere  

### What This IS NOT
❌ A **standalone journal publication** (n=60, single cohort insufficient)  
❌ Generalizable beyond **this lab, this cohort, this semester**  
❌ Evidence of **causal effects** (no control group, no intervention manipulation)  
❌ Ready for **peer-reviewed journal submission** (underpowered for independent effects)  
❌ A **conclusive comparison** of SR vs PDW (needs multiple cohorts with random assignment)  

---

## 2. RESEARCH QUESTIONS (Realistic Scope)

### Primary Research Question (Answerable with n=60, 30 items)
**RQ1:** What is the pattern and magnitude of metacognitive calibration (overconfidence/underconfidence) among students in MATLAB Lab 1, stratified by topic?

**Answerable:** ✅ YES
- Can compute per-student, per-topic Brier scores
- Can identify topics with systematic bias
- Can describe overconfidence/underconfidence patterns
- **Limitation:** Generalizability to other cohorts unknown; descriptive only

---

### Secondary Research Question (Exploratory, Underpowered)
**RQ2:** Do students show differential calibration patterns when using token-wager vs self-report confidence elicitation?

**Answerable:** ⚠️ PARTIALLY (underpowered)
- Can compare SR-group calibration vs PDW-group calibration
- Can describe differences in point estimates (means, SDs)
- **Limitation:** Cannot test statistical significance reliably (n=30 per condition); effect sizes may be inflated; cannot attribute causation to elicitation mode vs group differences

---

### Tertiary Research Question (Descriptive Only)
**RQ3:** Which topics show strongest/weakest calibration accuracy?

**Answerable:** ✅ YES (descriptive)
- Rank topics by Brier score
- Identify topics with highest overconfidence
- **Limitation:** Only 3 items per topic (unstable Brier estimates); cannot generalize to other semesters; no statistical tests for topic differences

---

## 3. COURSE ALIGNMENT (Why Lab 1 Matters)

### Syllabus Position
Lab 1 (Week 1–2) covers **foundational concepts** from:
- **Syllabus Topic #1:** Introduction to MATLAB (environment, basic commands)
- **Syllabus Topic #2:** Matrix Operations — **introduction only** (vectors, basic operations)

### Assessment Topics (10 categories, 3 questions each)

| # | Topic | Syllabus Alignment | Why Important |
|---|-------|-------------------|----------------|
| 1 | MATLAB Interface | Topic #1 | Entry point; foundational |
| 2 | Variables & Vectors | Topic #2 (intro) | Core data structure |
| 3 | Workspace Commands | Topic #1 | Essential for lab workflow |
| 4 | Colon Operator | Topic #2 (intro) | Used in 50% of later labs |
| 5 | Statistical Functions | Topic #2 (intro) | Common in data analysis |
| 6 | Logical Comparisons | Topic #1 | Gates conditional logic |
| 7 | Vector Operations | Topic #2 (intro) | Mathematical foundation |
| 8 | Data Output & Formatting | Topic #1 | Communication skill |
| 9 | Data Analysis Workflow | Topic #2 (intro) | Conceptual framework |
| 10 | Problem Scaling | Topic #2 (intro) | Motivation for matrices |

### Conceptual Gap: What's NOT Tested
⚠️ **Syllabus Topics #3–10 (75% of course) are NOT in Lab 1:**
- Matrix operations (full treatment, inversion, factorization)
- Linear equations, polynomial operations, visualization
- Simulink, signal processing, control systems, differential equations

**Implication:** This pilot tests only foundational topics. Extending to full-course calibration requires separate studies for Labs 2–10.

---

## 4. RESEARCH DESIGN

### Elicitation Design: Parallel Conditions (Not Nested)
```
MATLAB Lab 1 (N ≈ 60)
│
├─→ Group A: SR Mode (n ≈ 30)
│   └─ 30 identical MCQs + 3-level confidence scale
│   └ Confidence: {1=Not Sure, 2=Somewhat Sure, 3=Very Sure}
│   └ Data: Per-question confidence + correctness
│
├─→ Group B: PDW Mode (n ≈ 30)
│   └─ 30 identical MCQs + token wager (1–10)
│   └ Wager: Symmetric payoff (if correct +W, if wrong −W)
│   └ Data: Per-question wager + correctness
│   └ Note: Grade based on marks only; tokens ≠ grade
│
└─→ Both groups: Identical content, different elicitation only
```

### Key Design Features
✅ **Question parallelism:** Same 30 questions, same difficulty  
✅ **Randomization:** Question order randomized per student (fairness)  
✅ **Original-order research columns:** Data stored in original question sequence (reproducibility)  
✅ **Timestamp tracking:** Submission date/time recorded  
✅ **Unique identifiers:** Submission ID for audit trail  

### Design Limitations
❌ **No control group:** Cannot isolate effect of elicitation mode vs selection bias  
❌ **No random assignment:** Groups self-selected or assigned by section (confounding possible)  
❌ **Single time point:** No measurement of learning trajectory or pre-post gains  
❌ **No comparison course:** Cannot benchmark against non-MATLAB peers  
❌ **No intervention:** Reflection feedback present but not manipulated (uncontrolled variable)  

---

## 5. MEASUREMENT & ANALYSIS

### Primary Outcome: Metacognitive Calibration
**Definition:** Alignment between subjective judgment (confidence/wager) and objective performance (correctness)

**Metric: Brier Score**
$$B = \frac{1}{n} \sum_{i=1}^{n} (J_i - O_i)^2$$

Where:
- $J_i$ = Judgment (confidence 1–3 normalized to 0–1, or wager 1–10 normalized to 0–1)
- $O_i$ = Outcome (1 if correct, 0 if wrong)
- $n$ = Number of judgments

**Interpretation:**
- $B = 0$: Perfect calibration (judgment perfectly predicts outcome)
- $B = 0.25$: Uncalibrated guess (random betting)
- $B > 0.25$: Worse than random (systematic bias)
- Range: [0, 1]

### Secondary Outcomes

**Overconfidence Index (OCI):**
$$OCI = \bar{J} - \bar{O}$$
- Positive OCI = overconfidence (says confident but gets wrong)
- Negative OCI = underconfidence
- $|\text{OCI}| > 0.15$ considered meaningful bias

**Resolution (Discrimination):**
Correlation between confidence/wager and correctness (ability to distinguish hard from easy)

**Per-Topic Brier Score:**
Brier score computed separately for each of the 10 topics (3 items per topic)

### Analysis Plan (Descriptive, Not Inferential)

**Step 1: Descriptive Statistics**
- Sample composition (N, demographics, section)
- Quiz performance (mean score, SD, grade distribution)
- Confidence/wager distributions (histograms, tables)

**Step 2: Calibration Analysis**
- Overall Brier score (both groups combined, then separate)
- Overconfidence index (OCI ± SD)
- Per-topic Brier scores (ranked by calibration quality)
- Topic-level confidence/correctness scatter plots

**Step 3: Group Comparison (Exploratory, Underpowered)**
- SR vs PDW: Brier score comparison (descriptive; DO NOT report p-values as significant)
- Effect size estimates (Cohen's d) with wide confidence intervals
- Caveats in interpretation section

**Step 4: Subgroup Analyses (If N permits)**
- By performance level (high, medium, low scorers)
- By topic (which topics most/least overconfident?)
- By elicitation mode + performance interaction

### Statistical Limitations (Be Explicit)
⚠️ **Sample Size:** n ≈ 60 total (30 per condition)
- Typical calibration studies: n > 100 per condition
- This study: underpowered for detecting group effects
- Recommendation: Report descriptive statistics, NOT p-values or significance tests
- Any p-values reported should emphasize effect size + CI, not point estimate

⚠️ **Per-Topic Power:** Only 3 items per topic
- Brier score estimates unstable (wide CIs expected)
- Cannot reliably rank topics
- Only useful for descriptive patterns, not statistical inference

⚠️ **Design Confounds:**
- Selection bias (groups by section, not randomized)
- Uncontrolled variables (reflection feedback, instructor, environment)
- No baseline measurement (cannot control for prior ability)

---

## 6. HONEST ASSESSMENT: What This Enables vs. What It Doesn't

### ✅ What This Enables (Realistic Scope)

1. **PhD Dissertation Chapter**
   - Methodology section: Dual-elicitation design, measurement protocols
   - Results section: Per-topic calibration patterns in MATLAB Lab 1
   - Discussion: Implications for MATLAB pedagogy, limitations, future directions
   - Length: ~15–20 pages, realistic scope for PhD work

2. **Institutional Report** (For SGT Faculty)
   - "How well do MATLAB Lab 1 students understand their own knowledge?"
   - "Which topics need more instructor support?" (topic-level Brier scores)
   - "How does confidence elicitation affect student engagement?" (qualitative + tokens)
   - Actionable: Topic-specific recommendations for Lab 1 revision

3. **Foundation for Larger Study**
   - Proves feasibility of online calibration assessment in MATLAB
   - Establishes measurement protocols (replicable for other labs, other cohorts)
   - Generates pilot effect sizes for power calculation of future RCTs
   - If you extend to Labs 2–10 + multiple cohorts + years: publishable corpus

4. **Conference Presentation** (Maybe)
   - "Metacognitive Calibration in Introductory MATLAB: A Single-Lab Pilot Study"
   - Venue: ASEE (American Society for Engineering Education) Annual Conference
   - Format: Research Brief or Poster (not full paper — underpowered for full contribution)
   - Framing: "Proof-of-concept for dual-elicitation design; larger study underway"

---

### ❌ What This Does NOT Enable (Stop Pretending)

1. **Journal Publication (Standalone)**
   - **Reality check:** 30 questions, 1 cohort, n=60 is **pilot data, not research**
   - Journals like *Computers & Education*, *IEEE Trans. Education* expect:
     - n > 100 per condition
     - Multiple institutions OR multiple semesters (replication)
     - Pre-registered hypotheses + pre-analysis plan
     - Comparison to established benchmarks
   - **Your data fails all these criteria**
   - Desk reject likely within 2 weeks

2. **Causal Claims**
   - Cannot say "SR mode causes better calibration" (no random assignment)
   - Cannot say "overconfidence causes poor exam performance" (no follow-up outcome)
   - Can only describe: "These students showed overconfidence; these were less overconfident"
   - Inference: Strictly descriptive

3. **Generalization**
   - Cannot claim results apply to:
     - Other MATLAB courses (different instructor, curriculum)
     - Other institutions (different student body, prerequisites)
     - Other semesters (changes to lab, content, support)
   - Scope: This cohort, this semester, this lab only

4. **Effect Size Estimates**
   - Do NOT trust point estimates of SR vs PDW differences
   - Confidence intervals will be wide (n=30 per condition)
   - Any observed difference may be:
     - Sampling noise (noise floor for n=30)
     - Selection bias (section A vs B, not randomized)
     - Instructor effects (different TA, timing, support)
   - Honest estimate: 60–80% chance observed difference is spurious

---

## 7. HOW TO POSITION THIS CORRECTLY IN YOUR PhD

### In Your Dissertation Proposal
**Frame as:** "Pilot Study of Metacognitive Calibration Assessment in MATLAB Lab 1"

**Language:**
- "This single-cohort study establishes measurement protocols and describes calibration patterns..."
- "Results are hypothesis-generating for larger cross-institutional study..."
- "We acknowledge limitations: small n per condition, single lab, no control group..."

### In Your Dissertation Chapters

**Chapter 3 (Methodology):**
- Section 3.1: Dual-elicitation design rationale (why SR + PDW?)
- Section 3.2: Measurement protocol (Brier score, per-topic analysis)
- Section 3.3: Study design (parallel, not randomized; acknowledged limitation)
- Section 3.4: Analysis plan (explicit: descriptive not inferential)

**Chapter 4 (Results):**
- Describe calibration patterns (Brier scores per topic, overconfidence index)
- Show visualizations (Brier by topic, confidence vs correctness scatter)
- Report effect sizes with wide CIs (not p-values)
- **Title:** "Preliminary Findings on MATLAB Lab 1 Calibration (Pilot Data)"

**Chapter 5 (Discussion):**
- Interpret patterns in context of MATLAB pedagogy
- Acknowledge design limitations explicitly
- Propose next phase: "Extending this pilot to Labs 2–10 and multiple cohorts would..."
- Discuss practical implications: "Topic X showed high overconfidence; instructor should..."

### In Appendices
- Full survey instrument (30-question item pool with tags, correct answers)
- Raw data tables (Brier by student, by topic)
- Sample Google Sheets export (anonymized)
- Reproducibility: Exact code/formulas for Brier score computation

---

## 8. PATH TO REAL RESEARCH (Multi-Phase Program)

If you want to build from this pilot to publishable research:

### Phase 1 (Current): Pilot Study ← You Are Here
- **Timeline:** Semester 1
- **N:** ~60 (1 cohort)
- **Output:** Dissertation chapter + conference abstract
- **Goal:** Establish protocols, identify patterns

### Phase 2: Multi-Cohort Replication (Year 2)
- **Timeline:** 2–3 more semesters
- **N:** ~200+ (4 cohorts, 3 sections each)
- **Change:** Randomize elicitation mode (A/B test, not self-selected sections)
- **Output:** Publishable: "SR vs PDW Calibration: Multi-Cohort RCT" (now defensible)

### Phase 3: Extended Course (Year 2–3)
- **Timeline:** Full year (10 labs + exams)
- **N:** ~200 (longitudinal tracking through course)
- **Measure:** Calibration trajectory (Lab 1 → Lab 10), relationship to final exam
- **Output:** Publishable: "Metacognitive Calibration Trajectory in MATLAB Course"

### Phase 4: Multi-Institution (Year 3–4)
- **Timeline:** 2+ universities, parallel implementation
- **N:** ~300+
- **Measure:** Robustness across institutions, instructors, student populations
- **Output:** Publishable: "Generalizable Findings on MATLAB Calibration; Meta-Analysis"

**At Phase 2 (n > 100, RCT, multiple cohorts), you can submit to journals.**  
**At Phase 3 (longitudinal + outcomes), you can claim impact on learning.**  
**At Phase 4 (multi-site), results are generalizable.**

---

## 9. OPERATIONAL NEXT STEPS

### Before Next Lab Period
- [ ] Deploy SR + PDW quizzes to Google Sheets
- [ ] Test end-to-end
- [ ] Create 5-minute student tutorial (how to take quiz)

### Week 1–2: Quiz Administration
- [ ] Administer SR mode to Section C1 (or assign randomly)
- [ ] Administer PDW mode to Section C2 (or other group)
- [ ] Record responses, collect data

### Week 3: Data Analysis
- [ ] Download CSV from Google Sheets
- [ ] Compute Brier score per student, per topic
- [ ] Create visualizations (Brier by topic, confidence vs correctness)
- [ ] Identify topics with highest overconfidence

### Week 4: Reporting
- [ ] Draft methods section (design, sample, measurement)
- [ ] Write preliminary results (no significance tests; describe patterns)
- [ ] Create figure: "Brier Score by Topic"
- [ ] Note limitations explicitly

### Future (If Extending to Phase 2)
- [ ] Plan randomization for next cohorts
- [ ] Establish power calculation (how many n for significance?)
- [ ] Design full-year tracking (connect to future labs)
- [ ] Write pre-analysis plan (AsPredicted.org or OSF)

---

## 10. THE HONEST REALITY CHECK

**This pilot study will:**
- ✅ Give you authentic dissertation content (methodology + findings)
- ✅ Produce real data you can analyze and report
- ✅ Let you claim: "I conducted original research on metacognition in MATLAB"
- ✅ Serve as foundation for larger, publication-grade work

**This pilot study will NOT:**
- ❌ Be a standalone journal paper (underpowered, single cohort)
- ❌ Prove causation or generalize to other contexts
- ❌ Produce publishable effect size estimates (wide CIs, small n)
- ❌ Make you "done" with calibration research (it's a beginning, not an end)

**The Real Value:**
You're building a **research program**, not one paper. This pilot is Phase 1. If you execute it well — rigorous protocol, honest limitations, clear next steps — you can scale to 2–3 publishable studies over 2–3 years.

**Compare to:**
- Bad approach: "30 questions = 2 papers, PhD done"
- Good approach: "30 questions = proof-of-concept, foundation for 2-year research program leading to 2–3 publications + dissertation"

You're doing the latter. That's real research.

---

## SUMMARY TABLE

| Aspect | Reality |
|--------|---------|
| **Sample Size** | n ≈ 60, underpowered for group comparisons |
| **Scope** | Single lab, single semester, single institution |
| **Generalizability** | None (pilot data only) |
| **Best Framing** | Proof-of-concept + PhD dissertation chapter |
| **Publication Potential (Standalone)** | No (underpowered, limited scope) |
| **Conference Presentation** | Maybe (ASEE poster/brief, as pilot study) |
| **Foundation for Larger Study** | Yes (excellent; Phase 1 of multi-phase program) |
| **Timeline to Publishable Result** | 2–3 years (after Phases 2–3) |
| **Honest Assessment** | Legitimate research, realistic scope, valuable foundation |

---

## REFERENCES & FRAMEWORK

### Foundational Calibration Literature
- **Dunlosky, J., & Metcalfe, J. (2009).** Metacognition. SAGE Publications.
  - Defines calibration, Brier score, overconfidence
- **Brier, G. W. (1950).** Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1–3.
  - Original Brier score formulation
- **Prelec, D. (2004).** A Bayesian truth serum for subjective data. *Science*, 306(5695), 462–466.
  - Token wagering / prediction markets theory

### Engineering Education Context
- **Felder, R. M., & Silverman, L. K. (1988).** Learning and teaching styles in engineering education. *Journal of Engineering Education*, 78(7), 674–681.
- **Bjork, E. L., & Bjork, R. A. (1996).** Continuing the search for protective mechanisms. In J. Metcalfe & A. P. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 75–107). MIT Press.

### MATLAB-Specific Education
- **Clements, D. H., & Sarama, J. (2004).** Learning trajectories in mathematical education. *Mathematical Thinking and Learning*, 6(2), 181–206.
  - Framework for learning progressions (applicable to programming)

---

**Document Version:** 1.0 (Honest, Rigorous, No Sugarcoating)  
**Date:** July 22, 2026  
**Status:** Ready for PhD Use  
**Tone:** Realistic assessment of research scope and limitations
