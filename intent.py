def detect_intent(text):

    text = text.lower()

    # Comparison queries
    if "compare" in text or "difference" in text:
        return "comparison"

    # Refinement queries
    if "also" in text or "add" in text:
        return "refinement"

    # Very vague queries
    if len(text.split()) < 4:
        return "vague"

    return "recommendation"