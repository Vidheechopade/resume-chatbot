def analyze_resume(text, skills_db):
    text_lower = text.lower()

    found_skills = [s for s in skills_db if s in text_lower]
    missing_skills = [s for s in skills_db if s not in text_lower]

    score = int((len(found_skills) / len(skills_db)) * 100)

    return found_skills, missing_skills, score
