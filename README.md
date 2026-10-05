# OpportunityAI – AI College Opportunity Tracker

An automated AI workflow and web dashboard that helps college students discover and prioritize internships, hackathons, scholarships, workshops, and competitions.

## Problem
Student opportunities are scattered across multiple websites and platforms. Students can miss relevant opportunities and deadlines.

## Planned Solution
- Collect opportunity information automatically
- Use an LLM to summarize and categorize opportunities
- Extract deadlines, eligibility, and skills
- Assign a priority score
- Store results in a database
- Display everything through a web dashboard
- Run the collection/analysis workflow automatically with GitHub Actions

## Current MVP
The current version contains a Flask dashboard, SQLite database, filters, statistics, and manual opportunity entry. AI collection and scheduled automation will be added next.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Team
- Add member names here

## License
For educational/project submission use.
