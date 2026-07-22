# ═══════════════════════════════════════════════════════════════════════════
# MATLAB Lab 1 Quiz — Metadata Package v1.1
# Auto-generated from Quiz Generator v2.3
#
# Used by:
#   - Quiz_Registration.ipynb
#   - Quiz_Response_Import.ipynb
#   - Research_Notebook.ipynb
#   - Dataset_Export.ipynb
#
# Import Instructions:
#   1. Paste this entire file into Cell A3 of your Colab notebook
#   2. Run the cell
#   3. All metadata is now available as Python dictionaries
#   4. Use quiz_metadata, quiz_id, cohort_id, etc. in downstream cells
# ═══════════════════════════════════════════════════════════════════════════

quiz_metadata = {
    "quiz_id": "SGT_CSE_L1_Q1",
    "quiz_title": "MATLAB Lab 1 — Meet Your Workspace",
    "cohort_id": "SGT_CSE_Sem5_2026",
    "course_name": "MATLAB",
    "course_code": "130205120",
    "programme": "B.Tech CSE",
    "semester": "5th",
    "academic_session": "2025-2026",
    "lab_practical": "Practical 1 — Meet Your Workspace",
    "quiz_number": 1,
    "question_count": 30,
    "total_marks": 30,
    "duration_minutes": 15,

    "research_mode": True,
    "confidence_capture": True,
    "elicitation_mode": "SR",  # Change to "PDW" for token wager variant
    "confidence_scale": "3-level self-report (Not Sure / Somewhat Sure / Very Sure)",
    "metadata_version": "1.1",

    "sr_config": {
        "elicitation_mode": "SR",
        "confidence_levels": {
            1: "Not Sure",
            2: "Somewhat Sure",
            3: "Very Sure",
            0: "Not Rated"
        },
        "default_selection": False,
        "blocking_on_unanswered": False
    },

    "pdw_config": {
        "elicitation_mode": "PDW",
        "wager_min": 1,
        "wager_max": 10,
        "payoff_rule": "flat_symmetric",  # +W if correct, -W if wrong
        "difficulty_multipliers": False,
        "grade_impact": False,
        "leaderboard_metric": "token_score",
        "design_arm": "A",  # A = parallel sections (SR vs PDW), B = alternation
        "section_mode_map": {
            "C": "SR"  # Section C runs in SR mode for this cohort
            # Modify for each cohort: "B1": "PDW", "B2": "SR", etc.
        },
        "default_wager": None,
        "blocking_on_unwagered": False
    },

    "reflection_layer": {
        "enabled": True,
        "content_type": "educational_feedback",
        "interventional": True,
        "warning": "Reflection is an intervention. Use Layer OFF for control condition."
    },

    "questions": [
        {
            "question_id": "Q1",
            "question_number": 1,
            "section_number": 1,
            "section_name": "Analogy-Based MCQs",
            "topic_tag": "Variables & Vectors",
            "question_style": "Analogy",
            "marks": 1,
            "bloom_level": "C2 (Comprehension)"
        },
        {
            "question_id": "Q2",
            "question_number": 2,
            "section_number": 1,
            "section_name": "Analogy-Based MCQs",
            "topic_tag": "MATLAB Interface",
            "question_style": "Analogy",
            "marks": 1,
            "bloom_level": "C2 (Comprehension)"
        },
        {
            "question_id": "Q3",
            "question_number": 3,
            "section_number": 1,
            "section_name": "Analogy-Based MCQs",
            "topic_tag": "Workspace Commands",
            "question_style": "Analogy",
            "marks": 1,
            "bloom_level": "C2 (Comprehension)"
        },
        {
            "question_id": "Q4",
            "question_number": 4,
            "section_number": 2,
            "section_name": "Witty Concept MCQs",
            "topic_tag": "Colon Operator",
            "question_style": "Witty Concept",
            "marks": 1,
            "bloom_level": "C2-C3 (Comprehension-Application)"
        },
        {
            "question_id": "Q5",
            "question_number": 5,
            "section_number": 2,
            "section_name": "Witty Concept MCQs",
            "topic_tag": "Statistical Functions",
            "question_style": "Witty Concept",
            "marks": 1,
            "bloom_level": "C2-C3 (Comprehension-Application)"
        },
        {
            "question_id": "Q6",
            "question_number": 6,
            "section_number": 2,
            "section_name": "Witty Concept MCQs",
            "topic_tag": "Logical Comparisons",
            "question_style": "Witty Concept",
            "marks": 1,
            "bloom_level": "C2-C3 (Comprehension-Application)"
        },
        {
            "question_id": "Q7",
            "question_number": 7,
            "section_number": 3,
            "section_name": "Riddle / Puzzle MCQs",
            "topic_tag": "Vector Operations",
            "question_style": "Riddle",
            "marks": 1,
            "bloom_level": "C1-C2 (Knowledge-Comprehension)"
        },
        {
            "question_id": "Q8",
            "question_number": 8,
            "section_number": 3,
            "section_name": "Riddle / Puzzle MCQs",
            "topic_tag": "Data Output",
            "question_style": "Riddle",
            "marks": 1,
            "bloom_level": "C1-C2 (Knowledge-Comprehension)"
        },
        {
            "question_id": "Q9",
            "question_number": 9,
            "section_number": 3,
            "section_name": "Riddle / Puzzle MCQs",
            "topic_tag": "Data Analysis",
            "question_style": "Riddle",
            "marks": 1,
            "bloom_level": "C1-C2 (Knowledge-Comprehension)"
        },
        {
            "question_id": "Q10",
            "question_number": 10,
            "section_number": 4,
            "section_name": "Scenario-Based MCQs",
            "topic_tag": "MATLAB Interface",
            "question_style": "Scenario",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q11",
            "question_number": 11,
            "section_number": 4,
            "section_name": "Scenario-Based MCQs",
            "topic_tag": "Problem Scaling",
            "question_style": "Scenario",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q12",
            "question_number": 12,
            "section_number": 4,
            "section_name": "Scenario-Based MCQs",
            "topic_tag": "Variables & Vectors",
            "question_style": "Scenario",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q13",
            "question_number": 13,
            "section_number": 5,
            "section_name": "Misconception Busters",
            "topic_tag": "Workspace Commands",
            "question_style": "Misconception Buster",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q14",
            "question_number": 14,
            "section_number": 5,
            "section_name": "Misconception Busters",
            "topic_tag": "Colon Operator",
            "question_style": "Misconception Buster",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q15",
            "question_number": 15,
            "section_number": 5,
            "section_name": "Misconception Busters",
            "topic_tag": "Statistical Functions",
            "question_style": "Misconception Buster",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q16",
            "question_number": 16,
            "section_number": 6,
            "section_name": "Debug the Mistake",
            "topic_tag": "Logical Comparisons",
            "question_style": "Debug",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        },
        {
            "question_id": "Q17",
            "question_number": 17,
            "section_number": 6,
            "section_name": "Debug the Mistake",
            "topic_tag": "Vector Operations",
            "question_style": "Debug",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        },
        {
            "question_id": "Q18",
            "question_number": 18,
            "section_number": 6,
            "section_name": "Debug the Mistake",
            "topic_tag": "Data Analysis",
            "question_style": "Debug",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        },
        {
            "question_id": "Q19",
            "question_number": 19,
            "section_number": 7,
            "section_name": "Concept Application",
            "topic_tag": "Data Output",
            "question_style": "Mini-Caselet",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q20",
            "question_number": 20,
            "section_number": 7,
            "section_name": "Concept Application",
            "topic_tag": "MATLAB Interface",
            "question_style": "Mini-Caselet",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q21",
            "question_number": 21,
            "section_number": 7,
            "section_name": "Concept Application",
            "topic_tag": "Variables & Vectors",
            "question_style": "Mini-Caselet",
            "marks": 1,
            "bloom_level": "C3 (Application)"
        },
        {
            "question_id": "Q22",
            "question_number": 22,
            "section_number": 8,
            "section_name": "Spot the Best Definition",
            "topic_tag": "Workspace Commands",
            "question_style": "Definition",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q23",
            "question_number": 23,
            "section_number": 8,
            "section_name": "Spot the Best Definition",
            "topic_tag": "Colon Operator",
            "question_style": "Definition",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q24",
            "question_number": 24,
            "section_number": 8,
            "section_name": "Spot the Best Definition",
            "topic_tag": "Vector Operations",
            "question_style": "Definition",
            "marks": 1,
            "bloom_level": "C2-C4 (Comprehension-Analysis)"
        },
        {
            "question_id": "Q25",
            "question_number": 25,
            "section_number": 9,
            "section_name": "Sequence / Order the Steps",
            "topic_tag": "Statistical Functions",
            "question_style": "Sequence",
            "marks": 1,
            "bloom_level": "C3-C4 (Application-Analysis)"
        },
        {
            "question_id": "Q26",
            "question_number": 26,
            "section_number": 9,
            "section_name": "Sequence / Order the Steps",
            "topic_tag": "Logical Comparisons",
            "question_style": "Sequence",
            "marks": 1,
            "bloom_level": "C3-C4 (Application-Analysis)"
        },
        {
            "question_id": "Q27",
            "question_number": 27,
            "section_number": 9,
            "section_name": "Sequence / Order the Steps",
            "topic_tag": "Data Output",
            "question_style": "Sequence",
            "marks": 1,
            "bloom_level": "C3-C4 (Application-Analysis)"
        },
        {
            "question_id": "Q28",
            "question_number": 28,
            "section_number": 10,
            "section_name": "Cause → Effect Reasoning",
            "topic_tag": "Data Analysis",
            "question_style": "Cause-Effect",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        },
        {
            "question_id": "Q29",
            "question_number": 29,
            "section_number": 10,
            "section_name": "Cause → Effect Reasoning",
            "topic_tag": "Problem Scaling",
            "question_style": "Cause-Effect",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        },
        {
            "question_id": "Q30",
            "question_number": 30,
            "section_number": 10,
            "section_name": "Cause → Effect Reasoning",
            "topic_tag": "MATLAB Interface",
            "question_style": "Cause-Effect",
            "marks": 1,
            "bloom_level": "C4-C5 (Analysis-Synthesis)"
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════
# RESEARCH NOTEBOOK IMPORT BLOCK
# Paste the variables below into your Research Notebook cell
# ═══════════════════════════════════════════════════════════════════════════

quiz_id          = 'SGT_CSE_L1_Q1'
cohort_id        = 'SGT_CSE_Sem5_2026'
quiz_num         = 1
elicitation_mode = 'SR'  # Change to 'PDW' for wager mode

topic       = 'Lab 1: MATLAB Workspace'
max_marks   = 30
quiz_date   = '2026-07-22'  # Placeholder: set actual quiz date
key_release = '2026-07-23'  # Placeholder: set actual key release date
deadline    = '2026-07-25'  # Placeholder: set submission deadline

questions = [
    {'num': 1, 'topic': 'Variables & Vectors', 'style': 'Analogy', 'max_marks': 1},
    {'num': 2, 'topic': 'MATLAB Interface', 'style': 'Analogy', 'max_marks': 1},
    {'num': 3, 'topic': 'Workspace Commands', 'style': 'Analogy', 'max_marks': 1},
    {'num': 4, 'topic': 'Colon Operator', 'style': 'Witty Concept', 'max_marks': 1},
    {'num': 5, 'topic': 'Statistical Functions', 'style': 'Witty Concept', 'max_marks': 1},
    {'num': 6, 'topic': 'Logical Comparisons', 'style': 'Witty Concept', 'max_marks': 1},
    {'num': 7, 'topic': 'Vector Operations', 'style': 'Riddle', 'max_marks': 1},
    {'num': 8, 'topic': 'Data Output', 'style': 'Riddle', 'max_marks': 1},
    {'num': 9, 'topic': 'Data Analysis', 'style': 'Riddle', 'max_marks': 1},
    {'num': 10, 'topic': 'MATLAB Interface', 'style': 'Scenario', 'max_marks': 1},
    {'num': 11, 'topic': 'Problem Scaling', 'style': 'Scenario', 'max_marks': 1},
    {'num': 12, 'topic': 'Variables & Vectors', 'style': 'Scenario', 'max_marks': 1},
    {'num': 13, 'topic': 'Workspace Commands', 'style': 'Misconception Buster', 'max_marks': 1},
    {'num': 14, 'topic': 'Colon Operator', 'style': 'Misconception Buster', 'max_marks': 1},
    {'num': 15, 'topic': 'Statistical Functions', 'style': 'Misconception Buster', 'max_marks': 1},
    {'num': 16, 'topic': 'Logical Comparisons', 'style': 'Debug', 'max_marks': 1},
    {'num': 17, 'topic': 'Vector Operations', 'style': 'Debug', 'max_marks': 1},
    {'num': 18, 'topic': 'Data Analysis', 'style': 'Debug', 'max_marks': 1},
    {'num': 19, 'topic': 'Data Output', 'style': 'Mini-Caselet', 'max_marks': 1},
    {'num': 20, 'topic': 'MATLAB Interface', 'style': 'Mini-Caselet', 'max_marks': 1},
    {'num': 21, 'topic': 'Variables & Vectors', 'style': 'Mini-Caselet', 'max_marks': 1},
    {'num': 22, 'topic': 'Workspace Commands', 'style': 'Definition', 'max_marks': 1},
    {'num': 23, 'topic': 'Colon Operator', 'style': 'Definition', 'max_marks': 1},
    {'num': 24, 'topic': 'Vector Operations', 'style': 'Definition', 'max_marks': 1},
    {'num': 25, 'topic': 'Statistical Functions', 'style': 'Sequence', 'max_marks': 1},
    {'num': 26, 'topic': 'Logical Comparisons', 'style': 'Sequence', 'max_marks': 1},
    {'num': 27, 'topic': 'Data Output', 'style': 'Sequence', 'max_marks': 1},
    {'num': 28, 'topic': 'Data Analysis', 'style': 'Cause-Effect', 'max_marks': 1},
    {'num': 29, 'topic': 'Problem Scaling', 'style': 'Cause-Effect', 'max_marks': 1},
    {'num': 30, 'topic': 'MATLAB Interface', 'style': 'Cause-Effect', 'max_marks': 1}
]

# ═══════════════════════════════════════════════════════════════════════════
# TOPIC SUMMARY FOR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

topic_summary = {
    'MATLAB Interface': {'question_count': 3, 'questions': [2, 10, 20, 30]},
    'Variables & Vectors': {'question_count': 3, 'questions': [1, 12, 21]},
    'Workspace Commands': {'question_count': 3, 'questions': [3, 13, 22]},
    'Colon Operator': {'question_count': 3, 'questions': [4, 14, 23]},
    'Statistical Functions': {'question_count': 3, 'questions': [5, 15, 25]},
    'Logical Comparisons': {'question_count': 3, 'questions': [6, 16, 26]},
    'Vector Operations': {'question_count': 3, 'questions': [7, 17, 24]},
    'Data Output': {'question_count': 3, 'questions': [8, 19, 27]},
    'Data Analysis': {'question_count': 3, 'questions': [9, 18, 28]},
    'Problem Scaling': {'question_count': 3, 'questions': [11, 29]}
}

# ═══════════════════════════════════════════════════════════════════════════
# BLOOM'S LEVEL DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════════

bloom_distribution = {
    'C1 (Knowledge)': 3,           # Riddles
    'C2 (Comprehension)': 9,       # Analogies + Witty concepts (partial) + Definitions
    'C3 (Application)': 9,         # Scenarios + Mini-caselets + Sequences (partial)
    'C4 (Analysis)': 6,            # Definitions (partial) + Debug + Sequences (partial) + Cause-Effect (partial)
    'C5 (Synthesis)': 3,           # Cause-Effect
    'C6 (Evaluation)': 0
}

# ═══════════════════════════════════════════════════════════════════════════
# IMPORT TO DATABASE
# ═══════════════════════════════════════════════════════════════════════════
#
# After pasting and running this cell:
#
# 1. Import responses from Google Sheet CSV:
#    df_responses = pd.read_csv('MATLAB-Lab1-Quiz-SR-Responses.csv')
#
# 2. Pass metadata to item entry function:
#    item_entry.load_items(
#        metadata=quiz_metadata,
#        question_list=questions,
#        elicitation_mode=elicitation_mode
#    )
#
# 3. Import responses (tags, confidence/wagers, correctness):
#    importer.import_responses(
#        df=df_responses,
#        quiz_id=quiz_id,
#        cohort_id=cohort_id,
#        mode=elicitation_mode  # 'SR' or 'PDW'
#    )
#
# 4. Run calibration analysis:
#    calibrator.analyze_calibration(
#        quiz_id=quiz_id,
#        topic_summary=topic_summary
#    )
#
# ═══════════════════════════════════════════════════════════════════════════
