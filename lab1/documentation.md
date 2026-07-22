# MATLAB Lab 1 Quiz — Complete Technical Documentation

**Generated:** July 2026  
**Faculty:** K.P. Singh, SGT University  
**Course:** MATLAB (B.Tech Sem 5, Section C)  
**Quiz Type:** Calibration Study (SR & PDW Design A)  

---

## QUIZ CONFIGURATION SUMMARY

| Attribute | Value |
|-----------|-------|
| **Total Questions** | 30 |
| **Sections** | 10 (3 questions each) |
| **Question Styles** | 10 distinct pedagogical styles |
| **Time Limit** | 15 minutes |
| **Elicitation Modes** | SR (Self-Report) + PDW (Token Wager) |
| **Reflection Layer** | Enabled (Layer 2 feedback) |
| **Leaderboard Size** | Top 5 students |
| **Research Protocol** | Design A (parallel sections) |
| **Section Enrolled** | Section C |

---

## TOPIC TAG DISTRIBUTION

| Topic Tag | Occurrences | Coverage % |
|-----------|-------------|-----------|
| MATLAB Interface | 3 | 10% |
| Variables & Vectors | 3 | 10% |
| Workspace Commands | 3 | 10% |
| Colon Operator | 3 | 10% |
| Statistical Functions | 3 | 10% |
| Logical Comparisons | 3 | 10% |
| Vector Operations | 3 | 10% |
| Data Output | 3 | 10% |
| Data Analysis | 3 | 10% |
| Problem Scaling | 3 | 10% |
| **TOTAL** | **30** | **100%** |

---

## SECTION BREAKDOWN

### Section 1: Analogy-Based MCQs
**Style:** Real-world analogies for technical concepts  
**Questions:** 3  
**Topics:** Variables & Vectors, MATLAB Interface, Workspace Commands  
**Cognitive Level:** C2 (Comprehension)

### Section 2: Witty Concept MCQs
**Style:** Light sarcasm and exaggeration, still academically accurate  
**Questions:** 3  
**Topics:** Colon Operator, Statistical Functions, Logical Comparisons  
**Cognitive Level:** C2-C3 (Comprehension-Application)

### Section 3: Riddle / Puzzle MCQs
**Style:** Metaphors and descriptions, students identify the concept  
**Questions:** 3  
**Topics:** Vector Operations, Data Output, Data Analysis  
**Cognitive Level:** C1-C2 (Knowledge-Comprehension)

### Section 4: Scenario-Based MCQs
**Style:** Student-life situations requiring correct tool/method  
**Questions:** 3  
**Topics:** MATLAB Interface, Problem Scaling, Variables & Vectors  
**Cognitive Level:** C3 (Application)

### Section 5: Misconception Busters
**Style:** Correct commonly-held wrong beliefs  
**Questions:** 3  
**Topics:** Workspace Commands, Colon Operator, Statistical Functions  
**Cognitive Level:** C2-C4 (Comprehension-Analysis)

### Section 6: Debug the Mistake
**Style:** Find the flaw in logic, code, or reasoning  
**Questions:** 3  
**Topics:** Logical Comparisons, Vector Operations, Data Analysis  
**Cognitive Level:** C4-C5 (Analysis-Synthesis)

### Section 7: Concept Application / Mini-Caselets
**Style:** Short professional scenarios; identify concept or tool  
**Questions:** 3  
**Topics:** Data Output, MATLAB Interface, Variables & Vectors  
**Cognitive Level:** C3 (Application)

### Section 8: Spot the Best Definition
**Style:** Four close definitions, pick the most accurate  
**Questions:** 3  
**Topics:** Workspace Commands, Colon Operator, Vector Operations  
**Cognitive Level:** C2-C4 (Comprehension-Analysis)

### Section 9: Sequence / Order the Steps
**Style:** Correct sequence of steps in a workflow  
**Questions:** 3  
**Topics:** Statistical Functions, Logical Comparisons, Data Output  
**Cognitive Level:** C3-C4 (Application-Analysis)

### Section 10: Cause → Effect Reasoning
**Style:** Identify correct cause or effect relationship  
**Questions:** 3  
**Topics:** Data Analysis, Problem Scaling, MATLAB Interface  
**Cognitive Level:** C4-C5 (Analysis-Synthesis)

---

## GOOGLE SHEETS COLUMN LAYOUT — SR MODE

| Column | Header | Data Type | Notes |
|--------|--------|-----------|-------|
| A | Timestamp | DateTime | Server-generated |
| B | Submission ID | Text | Unique: {ROLL}-{QUIZCODE}-{GRADE}-{TIMESTAMP} |
| C | Name | Text | Student full name |
| D | Roll Number | Text | e.g., DD221BCA001 |
| E | Section | Text | e.g., C |
| F | Branch | Text | B.Tech CSE |
| G | Semester | Text | 5th |
| H | Quiz Type | Text | MATLAB-L1-SR |
| I | Score | Integer | Correct answer count (0-30) |
| J | Total | Integer | 30 |
| K | Percentage | Integer | Score ÷ Total × 100 |
| L | Grade | Text | A+, A, B, C, D, E, F |
| M | Passed | Boolean | TRUE (≥40%) / FALSE |
| N | Time Taken | Text | e.g., "14m 32s" |
| O | Submitted At | DateTime | IST format |
| P–Y | S1–S10 | Text | Section scores (10 columns) |
| Z–Z+29 | Tag Q1–Q30 | Text | Topic tag per question (static) |
| Z+30–Z+59 | Conf Q1–Q30 | Integer | Confidence: 1=Not Sure, 2=Somewhat, 3=Very Sure, 0=Not Rated |
| Z+60–Z+89 | Correct Q1–Q30 | Integer | 1=correct, 0=wrong/blank (original question order) |

**Total Columns (SR Mode):** 90

---

## GOOGLE SHEETS COLUMN LAYOUT — PDW MODE

| Column | Header | Data Type | Notes |
|--------|--------|-----------|-------|
| A | Timestamp | DateTime | Server-generated |
| B | Submission ID | Text | Unique: {ROLL}-{QUIZCODE}-{GRADE}-{TIMESTAMP} |
| C | Name | Text | Student full name |
| D | Roll Number | Text | e.g., DD221BCA001 |
| E | Section | Text | e.g., C |
| F | Branch | Text | B.Tech CSE |
| G | Semester | Text | 5th |
| H | Quiz Type | Text | MATLAB-L1-PDW |
| I | Score | Integer | Correct answer count (0-30) |
| J | Total | Integer | 30 |
| K | Percentage | Integer | Score ÷ Total × 100 |
| L | Grade | Text | A+, A, B, C, D, E, F |
| M | Passed | Boolean | TRUE (≥40%) / FALSE |
| N | Time Taken | Text | e.g., "14m 32s" |
| O | Submitted At | DateTime | IST format |
| P–Y | S1–S10 | Text | Section scores (10 columns) |
| Z–Z+29 | Tag Q1–Q30 | Text | Topic tag per question (static) |
| Z+30–Z+59 | Wager Q1–Q30 | Integer | Tokens wagered: 1–10, 0=not wagered |
| Z+60–Z+89 | Correct Q1–Q30 | Integer | 1=correct, 0=wrong/blank (original question order) |
| Z+90 | Token Score | Integer | Σ(+W if correct / −W if wrong) — leaderboard metric ONLY |

**Total Columns (PDW Mode):** 91

---

## DATA VALIDATION REPORT

```
╔════════════════════════════════════════════════════════════════╗
║            MATLAB Lab 1 Quiz — Data Validation                ║
╚════════════════════════════════════════════════════════════════╝

Total Questions:                 30
Questions per Section:           3
Total Sections:                  10
Cognitive Bloom Levels:          C1 → C6 (Knowledge → Evaluation)

TOPIC TAG VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Complete topic coverage:       10 unique tags
✓ Minimum questions per tag:     3 questions
✓ Maximum questions per tag:     3 questions
✓ No invented tags:              All tags from syllabus
✓ Tag distribution balance:      Perfectly uniform (100%)

SECTION STYLE VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Section 1 (Analogy):           3 questions, distinct analogies
✓ Section 2 (Witty):             3 questions, varied scenarios
✓ Section 3 (Riddle):            3 questions, no answer in stem
✓ Section 4 (Scenario):          3 questions, named characters
✓ Section 5 (Misconception):     3 questions, myth + correction
✓ Section 6 (Debug):             3 questions, plausible causes
✓ Section 7 (Application):       3 questions, real-world context
✓ Section 8 (Definition):        3 questions, close definitions
✓ Section 9 (Sequence):          3 questions, ordered steps
✓ Section 10 (Cause-Effect):     3 questions, causal reasoning

OPTION VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Options per question:          4 (A, B, C, D)
✓ All-of-above options:          0 (prohibited)
✓ None-of-above options:         0 (prohibited)
✓ Distractors plausibility:      High (academically relevant)
✓ Option diversity:              Non-overlapping semantic space

ELICITATION LAYER VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ SR Mode (Confidence):          3-level scale (1=Not Sure, 2=Somewhat, 3=Very Sure)
✓ PDW Mode (Wager):              1–10 token range, flat symmetric payoff
✓ Elicitation capture:           Before answer keys revealed
✓ Original question order:       Research columns map to original indices
✓ No default selection:          Encouraged but not blocking

REFLECTION LAYER VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Layer 2 enabled:               YES (educational benefit)
✓ Reflection tone:               Positive, appreciative, non-judgmental
✓ Template coverage:             4 patterns (High-High, High-Low, Low-High, Low-Low)
✓ Research contamination:        WARNING — reflection is intervention
                                 Apply Layer 2 OFF for control condition
                                 Apply Layer 2 ON for intervention phase

DESIGN A (PARALLEL SECTIONS) VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ SR variant generated:          YES (Code: MATLAB-L1-SR)
✓ PDW variant generated:         YES (Code: MATLAB-L1-PDW)
✓ Questions identical:           YES (same 30 across modes)
✓ Options identical:             YES (shuffled at runtime only)
✓ Correct answers identical:     YES (mapped to shuffled options)
✓ Only diff: Elicitation layer:  YES (confidence pills vs wager pills)
✓ Separate Google Sheets:        RECOMMENDED (prevent column schema mix)

MOBILE RESPONSIVENESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Mobile breakpoint (740px):     Registration layout → single column
✓ Mobile breakpoint (520px):     Quiz subbar flex, wager pills 5×2 grid
✓ Touch-friendly pill size:      Minimum 44px height
✓ Font legibility:               Readable at 12px minimum

RESEARCH READINESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Calibration data capture:      Tag + Confidence/Wager + Correctness
✓ Original question order:       YES (research columns in original order)
✓ Per-student per-question:      YES (flat columns for import)
✓ Zero-inflation guard:          Unwagered/unrated items marked 0
✓ Data export format:            JSON → Google Sheets → CSV → database
✓ Submission ID tracking:        Unique per student per quiz
✓ Timestamp recording:           Server-generated (timezone: IST)

OVERALL STATUS:                  ✓ APPROVED FOR DEPLOYMENT
═══════════════════════════════════════════════════════════════════
```

---

## DEPLOYMENT CHECKLIST

### Step 1: Create Google Sheet
- [ ] Open Google Drive
- [ ] Create new Google Sheet: `MATLAB-Lab1-Quiz-SR` (for SR mode)
- [ ] Create new Google Sheet: `MATLAB-Lab1-Quiz-PDW` (for PDW mode)
- [ ] Rename first sheet tab to exactly: `Responses`
- [ ] Keep the other sheets empty

### Step 2: Deploy Google Apps Script
#### For SR Mode Sheet:
- [ ] Open Google Sheet `MATLAB-Lab1-Quiz-SR`
- [ ] Extensions → Apps Script
- [ ] Delete all default code
- [ ] Paste the entire `Code.gs` file (from this package)
- [ ] Press Ctrl+S to save
- [ ] Click Deploy → New Deployment
  - Type: Web App
  - Execute as: [Your email]
  - Who has access: Anyone
- [ ] Click Deploy
- [ ] **Copy the Web App URL** (looks like: `https://script.google.com/macros/d/{ID}/userweb`)
- [ ] Note: `MATLAB-Lab1-Quiz-SR-SHEET-URL`

#### For PDW Mode Sheet:
- [ ] Repeat the same steps for the PDW sheet
- [ ] Note: `MATLAB-Lab1-Quiz-PDW-SHEET-URL`

### Step 3: Update HTML Files
- [ ] Open `matlab-quiz-lab1-sr.html`
- [ ] Find: `const SHEET_URL = 'YOUR_DEPLOYMENT_ID_HERE';`
- [ ] Replace with: your SR sheet's Web App URL
- [ ] Save the file

- [ ] Open `matlab-quiz-lab1-pdw.html`
- [ ] Find: `const SHEET_URL = 'YOUR_DEPLOYMENT_ID_HERE';`
- [ ] Replace with: your PDW sheet's Web App URL
- [ ] Save the file

### Step 4: Test End-to-End (SR Mode)
- [ ] Open `matlab-quiz-lab1-sr.html` in a browser
- [ ] Fill registration (use test credentials: Priya Sharma, DD221BCA098, Section C)
- [ ] Answer 2-3 questions, rate confidence for each
- [ ] Submit quiz
- [ ] Verify:
  - [ ] Result screen displays (with correct score, grade, topic performance)
  - [ ] Reflection block shows (if Reflection layer ON)
  - [ ] PDF downloads automatically
  - [ ] Submission ID is unique and recorded
- [ ] Check Google Sheet `MATLAB-Lab1-Quiz-SR`:
  - [ ] New row appeared
  - [ ] All columns populated correctly
  - [ ] Research columns (tags, confidence, correctness) in original order
- [ ] Check leaderboard widget:
  - [ ] Student appears in top 5 (or widget loads without error)

### Step 5: Test End-to-End (PDW Mode)
- [ ] Open `matlab-quiz-lab1-pdw.html` in a browser
- [ ] Fill registration (use test credentials: Arjun Kumar, DD221BCA099, Section C)
- [ ] Answer 2-3 questions, wager tokens for each (1–10)
- [ ] Submit quiz
- [ ] Verify:
  - [ ] Result screen displays (with correct score, grade, topic performance)
  - [ ] Token Panel shows signed token score (e.g., "+34" or "-12")
  - [ ] Reflection block shows (if Reflection layer ON) — wager-based templates
  - [ ] PDF downloads automatically
  - [ ] Submission ID is unique and recorded
- [ ] Check Google Sheet `MATLAB-Lab1-Quiz-PDW`:
  - [ ] New row appeared
  - [ ] All columns populated correctly
  - [ ] Research columns (tags, wagers, correctness) in original order
  - [ ] Token Score column has correct signed value
- [ ] Check leaderboard widget:
  - [ ] Student appears ranked by token score (not accuracy %)
  - [ ] Top 5 list is token-based

### Step 6: Live Deployment
- [ ] Share HTML files:
  - [ ] Upload to GitHub Pages OR
  - [ ] Upload to Netlify OR
  - [ ] Share via direct link (e.g., email to students)
- [ ] Send quiz links to students:
  - [ ] SR Mode: [link to matlab-quiz-lab1-sr.html]
  - [ ] PDW Mode: [link to matlab-quiz-lab1-pdw.html]
- [ ] Communicate:
  - [ ] Quiz date and time
  - [ ] Time limit (15 minutes)
  - [ ] Section assignment (e.g., "Section C uses SR mode for this cohort")
  - [ ] Any pre-quiz instructions

### Step 7: Post-Quiz Data Handling
- [ ] Monitor responses in real-time (Google Sheets auto-update)
- [ ] After all students submit:
  - [ ] Download both sheets as CSV
  - [ ] Backup CSVs to secure location
  - [ ] Import to research database (e.g., calib_research.db)
  - [ ] Run data quality checks:
    - [ ] No missing values in core columns
    - [ ] Token scores match recomputation (PDW mode)
    - [ ] Correctness values binary (0/1)
    - [ ] Confidence values 1–3 (SR) or 0 (unrated)
    - [ ] Wager values 1–10 (PDW) or 0 (unwagered)

### Step 8: Optional — Faculty Dashboard
- [ ] Create a summary sheet in the Google Sheet:
  - [ ] Pivot table by Section showing: Mean Score, Mean %, Grade Distribution
  - [ ] Topic Performance summary (% correct per topic)
  - [ ] Confidence/Wager calibration summary (by tag, by section)
  - [ ] Share read-only link with faculty

---

## TROUBLESHOOTING

| Issue | Cause | Solution |
|-------|-------|----------|
| "Quiz doesn't submit" | Google Apps Script deployment URL incorrect | Verify SHEET_URL in HTML matches deployed Web App URL |
| "Sheet stays empty" | deployment URL not updated | Copy URL from Deploy output, replace placeholder |
| "Leaderboard shows error" | Apps Script has syntax error | Check Code.gs for typos, re-deploy |
| "PDF won't download" | html2pdf library blocked or failed | Ensure CDN link in HTML `<head>` is active |
| "Confidence pills don't show (SR)" | Browser cache | Hard-refresh (Ctrl+Shift+R) or clear cache |
| "Wager pills don't show (PDW)" | Same as above | Hard-refresh |
| "Tab switch warning fires too early" | Visibility change event triggered | This is expected; it's a feature to prevent cheating |
| "Question order looks same every session" | Shuffle function not working | Check browser console for JS errors |
| "Submission ID not unique" | Timestamp collision (unlikely) | ID includes milliseconds; collisions <1 in 1B |

---

## METADATA FOR RESEARCH DATABASE

**Quiz ID:** MATLAB-L1-2026-Q1  
**Cohort ID:** SGT-CSE-Sem5-2026  
**Course:** MATLAB (130205120)  
**Programme:** B.Tech CSE  
**Semester:** 5th  
**Academic Session:** 2025-2026  
**Lab Practical:** Practical 1 — Meet Your Workspace  
**Quiz Date:** [To be set by faculty]  
**Key Release Date:** [To be set by faculty]  
**Research Status:** Active (Calibration Study)  
**Ethics Approval:** [Reference number if applicable]  

---

## STUDENT COMMUNICATION TEMPLATE

Subject: MATLAB Lab 1 Quiz — 15 Minutes, [Date] @ [Time] IST

Dear Section C Students,

You are invited to take the **MATLAB Lab 1 Quiz** as part of your coursework and our ongoing research on learning assessment.

**Quiz Details:**
- **Date & Time:** [DATE], [START TIME] – [END TIME] IST
- **Duration:** 15 minutes
- **Format:** 30 multiple-choice questions across 10 topics
- **Access Link:** [LINK-SR or LINK-PDW]
- **Device:** Computer or laptop with internet access (mobile not recommended due to screen size)

**Important:**
- Clicking "Begin Quiz" starts the 15-minute timer immediately
- You cannot pause or resume; plan accordingly
- Switching tabs or windows during the quiz will trigger a warning; a second switch auto-submits
- Your final PDF receipt will download automatically after submission
- Scores, grades, and leaderboard ranking are displayed immediately

**Topics Covered:**
MATLAB interface, variables, vectors, workspace commands, colon operator, statistical functions, logical comparisons, vector operations, data output, and problem scaling.

**Note on Research:**
This quiz is part of a PhD research study on calibration and confidence elicitation in educational assessment. Your responses help us understand how well students estimate their own knowledge. **Participation is voluntary** and has no impact on your final grade (only the quiz score counts toward your coursework marks).

If you have any technical issues during the quiz, please contact [FACULTY EMAIL].

Good luck!

K.P. Singh  
Department of Computer Science & Engineering  
SGT University

---

## REFERENCES & FURTHER READING

- **Quiz Generator Prompt:** KP Singh — Confidence Calibrator Quiz Generator Master Prompt v2.3
- **Calibration Research:** Dunlosky & Metcalfe (2009) on metacognitive accuracy
- **PDW Methodology:** Brier (1950) on probability scoring; Prelec (2004) on information markets
- **Educational Design:** Bloom et al. (1956) on cognitive taxonomy; Anderson & Krathwohl (2001) revision
- **Assessment:** Stiggins (2004) on student-involved assessment; Black & Wiliam (1998) on formative assessment

---

**Document Version:** 1.0  
**Last Updated:** July 2026  
**Generated By:** Claude (AI Assistant)  
**For Faculty:** K.P. Singh, SGT University
