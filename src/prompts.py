MEETING_MINUTES_PROMPT = """
Analyze the following meeting transcript and generate
professional and structured meeting minutes.

Use the following sections when the information is available:

# Meeting Overview

# Participants

# Agenda

# Discussion Summary

# Key Decisions

# Action Items

# Important Points

# Next Steps

Rules:

- Use only information available in the transcript.
- Do not invent names, decisions, dates or action items.
- Keep the summary concise but informative.
- Remove unnecessary repetition and filler words.
- Clearly identify important decisions and tasks.
- If a section has no relevant information, omit it.

Meeting Transcript:

{transcript}
"""