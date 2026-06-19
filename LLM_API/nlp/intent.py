def classify_intent(query):
    query = query.lower()

    if any(w in query for w in ["fee", "cost", "price", "charges"]):
        return "FEES"
    if any(w in query for w in ["admission", "apply", "eligibility", "enroll"]):
        return "ADMISSION"
    if any(w in query for w in ["faculty", "professor", "teacher", "staff"]):
        return "FACULTY"
    if any(w in query for w in ["program", "degree", "course", "curriculum"]):
        return "PROGRAM"

    return "GENERAL"
