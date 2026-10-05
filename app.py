from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path("opportunities.db")


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            organization TEXT NOT NULL,
            category TEXT NOT NULL,
            deadline TEXT,
            eligibility TEXT,
            skills TEXT,
            priority TEXT DEFAULT 'Medium',
            summary TEXT,
            link TEXT
        )
    """)

    count = conn.execute(
        "SELECT COUNT(*) FROM opportunities"
    ).fetchone()[0]

    if count == 0:
        sample = [
            (
                "Python Developer Internship",
                "TechNova",
                "Internship",
                "2026-10-20",
                "Students with programming knowledge",
                "Python, Git",
                "High",
                "A beginner-friendly internship focused on Python development and practical projects.",
                "https://example.com"
            ),
            (
                "AI Innovation Hackathon",
                "InnovateHub",
                "Hackathon",
                "2026-10-28",
                "College students",
                "Python, AI, APIs",
                "High",
                "A team-based hackathon to build AI-powered solutions for real-world problems.",
                "https://example.com"
            ),
            (
                "Student Tech Workshop",
                "CodeCampus",
                "Workshop",
                "2026-11-05",
                "Engineering students",
                "Web Development",
                "Medium",
                "Hands-on workshop covering modern web development and deployment.",
                "https://example.com"
            )
        ]

        conn.executemany("""
            INSERT INTO opportunities
            (title, organization, category, deadline, eligibility,
             skills, priority, summary, link)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sample)

    conn.commit()
    conn.close()


@app.route("/")
def dashboard():
    conn = get_db()

    category = request.args.get("category", "")

    if category:
        opportunities = conn.execute(
            "SELECT * FROM opportunities WHERE category=? ORDER BY deadline",
            (category,)
        ).fetchall()
    else:
        opportunities = conn.execute(
            "SELECT * FROM opportunities ORDER BY deadline"
        ).fetchall()

    stats = {
        "total": conn.execute(
            "SELECT COUNT(*) FROM opportunities"
        ).fetchone()[0],

        "internships": conn.execute(
            "SELECT COUNT(*) FROM opportunities WHERE category='Internship'"
        ).fetchone()[0],

        "hackathons": conn.execute(
            "SELECT COUNT(*) FROM opportunities WHERE category='Hackathon'"
        ).fetchone()[0],

        "high": conn.execute(
            "SELECT COUNT(*) FROM opportunities WHERE priority='High'"
        ).fetchone()[0],
    }

    conn.close()

    return render_template(
        "index.html",
        opportunities=opportunities,
        stats=stats,
        category=category,
        ai_results=None,
        student_skills=""
    )


@app.route("/add", methods=["POST"])
def add():
    data = request.form

    conn = get_db()

    conn.execute("""
        INSERT INTO opportunities
        (title, organization, category, deadline, eligibility,
         skills, priority, summary, link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["title"],
        data["organization"],
        data["category"],
        data["deadline"],
        data["eligibility"],
        data["skills"],
        data["priority"],
        data["summary"],
        data["link"]
    ))

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


# 🤖 Skill Matching / Recommendation Module
@app.route("/ai-match", methods=["POST"])
def ai_match():

    skills = request.form.get("skills", "").lower()

    conn = get_db()

    opportunities = conn.execute(
        "SELECT * FROM opportunities"
    ).fetchall()

    conn.close()

    results = []

    for item in opportunities:

        opportunity_skills = item["skills"].lower()

        matched = sum(
            1
            for skill in skills.split(",")
            if skill.strip()
            and skill.strip() in opportunity_skills
        )

        if matched > 0:
            results.append((matched, item))

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    stats = {
        "total": len(opportunities),
        "internships": sum(
            1 for x in opportunities
            if x["category"] == "Internship"
        ),
        "hackathons": sum(
            1 for x in opportunities
            if x["category"] == "Hackathon"
        ),
        "high": sum(
            1 for x in opportunities
            if x["priority"] == "High"
        )
    }

    return render_template(
        "index.html",
        opportunities=opportunities,
        stats=stats,
        category="",
        ai_results=results,
        student_skills=skills
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    