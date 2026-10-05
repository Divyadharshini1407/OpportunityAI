# OpportunityAI 🤖

## Project Overview

OpportunityAI is an automated AI workflow and web dashboard designed to help college students discover and manage opportunities such as internships, hackathons, scholarships and workshops.

The system provides a centralized dashboard where students can view opportunities, check deadlines, skills and eligibility, and find suitable opportunities based on their skills.

## Features

- College opportunity tracking
- Internship and hackathon management
- Category-based filtering
- Priority tracking
- Add new opportunities
- Skill-based opportunity matching
- Web dashboard
- SQLite database
- Automated workflow using GitHub Actions

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- GitHub Actions

## Project Structure

app.py - Flask backend
index.html - Web dashboard
style.css - Dashboard styling
opportunities.db - SQLite database
daily.yml - Automation workflow
requirements.txt - Python dependencies

## Setup Instructions

1. Install Python 3.13 or above.

2. Clone this repository.

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

python app.py

5. Open the following URL in your browser:

http://127.0.0.1:5000

## How It Works

1. Opportunities are stored in the SQLite database.
2. The Flask backend retrieves and displays opportunities.
3. Students can filter opportunities by category.
4. Students can add new opportunities.
5. The skill matching module compares student skills with opportunity skills and recommends matching opportunities.
6. GitHub Actions can be used to automate scheduled workflow tasks.

## Team Members

- Divyadharshini Esakki-125A3025
- Rishita Gowda-125A3032

## Screenshots

Dashboard screenshot can be added here.

AI Opportunity Matcher screenshot can be added here.

## Future Improvements

- Integrate a real LLM/API for intelligent opportunity summarization.
- Automatically collect opportunities from external APIs.
- Send deadline reminders to students.
- Improve AI-based recommendations.
