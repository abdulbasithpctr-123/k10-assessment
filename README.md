# K10 Psychological Distress Assessment

A web-based K10 Psychological Distress Assessment tool developed as a freelance project for **Andalucia Foundation**.

The application provides a simple, supportive way for users to complete the K10 questionnaire, receive a total score, and view a corresponding result category with a short, encouraging message.

**Live Demo:** [Try the K10 Assessment](https://k10-assessment-ndfy.vercel.app/)

## About the Project

The K10 (Kessler Psychological Distress Scale) is a 10-question screening scale that explores how a person has felt over the past 30 days.

This project transforms the questionnaire into an accessible web experience, combining automated scoring with a calm visual design and supportive feedback. Small illustrated characters respond to assessment results to make the experience feel more like a gentle check-in than a clinical form.

## Features

- **10-question assessment:** Answer the K10 screening questions.
- **Automated scoring:** Calculate a total score out of 50 based on responses.
- **Result categorization:** Display a result category based on the total score.
- **Supportive feedback:** Provide a short message corresponding to the result.
- **Responsive, user-friendly interface:** Designed for a clear and approachable assessment experience.
- **Illustrated result characters:** Add a friendly visual element to the results.
- **Responsible messaging:** Clearly communicate that the application is a screening tool, not a diagnostic instrument.

## Assessment Score Categories

| Total Score | Result Category |
|---|---|
| Below 20 | Doing Well |
| 20–24 | Needs Mild Attention |
| 25–29 | Needs Moderate Attention |
| 30–50 | Needs Immediate Attention |

The application uses these categories to present supportive feedback. They should not be interpreted as a clinical diagnosis.

## Technology Stack

- **Python** — Application logic
- **Flask** — Web framework
- **Jinja** — HTML templating
- **HTML5** — Page structure
- **CSS3** — Styling and visual design
- **Git and GitHub** — Version control and source-code management
- **Vercel** — Deployment and hosting

## User Experience and Design

Because mental health is a sensitive subject, the design prioritizes:

- Calm and approachable visual styling
- Clear, easy-to-understand wording
- Supportive, non-judgmental result messages
- Illustrated characters that respond to the result
- A clear disclaimer about the purpose and limitations of the assessment

The goal is to make the experience approachable while communicating the results responsibly.

## How It Works

1. The user opens the assessment application.
2. The user answers all 10 questions.
3. The application calculates the total score from the selected responses.
4. The total score is mapped to a result category.
5. The application displays the result and a corresponding supportive message.

## Running Locally

To run the project locally, first clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask application using the entry point configured in your repository. For example, if the main file is `app.py`:

```bash
python app.py
```

Open the local URL displayed in your terminal, commonly `http://127.0.0.1:5000/`.

**Note:** The exact commands and dependencies may vary depending on your repository structure and deployment configuration.

## Important Disclaimer

This application is intended for **screening and informational purposes only**. It does not provide a medical or psychological diagnosis and is not a substitute for professional evaluation, advice, or treatment.

Anyone concerned about their mental health should consider speaking with a qualified mental health professional.

## Project Information

- **Project type:** Freelance web development
- **Client:** Andalucia Foundation
- **Status:** Deployed
- **Live application:** [https://k10-assessment-ndfy.vercel.app/](https://k10-assessment-ndfy.vercel.app/)

## Acknowledgements

Thank you to the **Andalucia Foundation team** for the opportunity to work on this project.

---

*Developed with a focus on usability, thoughtful design, and responsible mental health communication.*
