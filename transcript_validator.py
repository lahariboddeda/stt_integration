def validate_transcript(text):

    if not text:
        return False, "Transcript is empty"

    if len(text.strip()) < 3:
        return False, "Transcript too short"

    if text.strip() == ".....":
        return False, "Invalid transcript"

    return True, "Valid transcript"