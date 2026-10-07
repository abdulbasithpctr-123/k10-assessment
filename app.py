from pathlib import Path

from flask import Flask, render_template, request

PROJECT_DIR = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(PROJECT_DIR / "templates"),
    static_folder=str(PROJECT_DIR / "static"),
)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    SEND_FILE_MAX_AGE_DEFAULT=0,
)


# ============================================================
# K10 QUESTIONS
# ============================================================

QUESTIONS = [
    "During the last 30 days, about how often did you feel tired out for no good reason?",
    "During the last 30 days, about how often did you feel nervous?",
    "During the last 30 days, about how often did you feel so nervous that nothing could calm you down?",
    "During the last 30 days, about how often did you feel hopeless?",
    "During the last 30 days, about how often did you feel restless or fidgety?",
    "During the last 30 days, about how often did you feel so restless you could not sit still?",
    "During the last 30 days, about how often did you feel depressed?",
    "During the last 30 days, about how often did you feel that everything was an effort?",
    "During the last 30 days, about how often did you feel so sad that nothing could cheer you up?",
    "During the last 30 days, about how often did you feel worthless?"
]


# ============================================================
# ANSWER OPTIONS
# ============================================================

OPTIONS = [
    (1, "None of the time"),
    (2, "A little of the time"),
    (3, "Some of the time"),
    (4, "Most of the time"),
    (5, "All of the time")
]


# ============================================================
# RESULT CALCULATION
# ============================================================

def get_result(score):

    if score < 20:
        return {
            "title": "Doing Well",
            "class": "doing-well",
            "message": (
                "Your responses indicate that you are currently doing well."
            )
        }

    elif score <= 24:
        return {
            "title": "Needs Mild Attention",
            "class": "mild",
            "message": (
                "Your responses suggest that some mild attention "
                "to your emotional wellbeing may be helpful."
            )
        }

    elif score <= 29:
        return {
            "title": "Needs Moderate Attention",
            "class": "moderate",
            "message": (
                "Your responses suggest that your emotional wellbeing "
                "may need moderate attention."
            )
        }

    else:
        return {
            "title": "Needs Immediate Attention",
            "class": "immediate",
            "message": (
                "Your responses indicate a higher level of psychological "
                "distress. Consider speaking with a qualified healthcare "
                "or mental-health professional."
            )
        }


# ============================================================
# MAIN ROUTE
# ============================================================

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    score = None

    if request.method == "POST":

        answers = []

        try:

            # Read all 10 answers
            for i in range(1, 11):

                answer = int(request.form[f"q{i}"])

                # Only allow values from 1 to 5
                if answer not in [1, 2, 3, 4, 5]:
                    raise ValueError

                answers.append(answer)

            # Calculate total score
            score = sum(answers)

            # Get result category
            result = get_result(score)

        except (KeyError, ValueError):

            result = {
                "title": "Please answer every question",
                "class": "error",
                "message": (
                    "All 10 questions must be answered "
                    "before submitting the assessment."
                )
            }

    return render_template(
        "index.html",
        questions=QUESTIONS,
        options=OPTIONS,
        score=score,
        result=result
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5017, debug=False, use_reloader=False)