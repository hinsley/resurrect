# gpt3.py
# Provides an interface for generating new interview content
# with OpenAI's GPT-3 API.

import openai

with open("openai-api-key.txt") as f:
    openai.api_key = f.read()

interviewees = {
    "Albert Einstein": {
        "title": "Albert Einstein",
        "nominal": "Einstein",
    },
    "Bernhard Riemann": {
        "title": "Bernhard Riemann",
        "nominal": "Riemann",
    },
    "Isaac Newton": {
        "title": "Sir Isaac Newton",
        "nominal": "Newton",
    },
}

def new_transcript(interviewee: str) -> str:
    """
    Generates a fresh transcript.
    """

    return f"The following is an excerpt of a transcript from an informal interview with {interviewees[interviewee]["title"]}.\n\nInterviewer: "

parameters = {
    "engine": "davinci",
    "frequency_penalty": 0.1,
    "max_tokens": 200,
    "temperature": 0.5,
    "stop": "Interviewer:",
}

def query(context: str, interviewee: str) -> str:
    """
    Takes an interview transcript as context and appends the interviewee nominal prompt
    before submitting a completion query to GPT-3. Returns the entire transcript, so
    no further concatenation is required.
    """
    # Append the nominal prompt for the interviewee.
    context += f"\n\n{interviewees[interviewee]['nominal']}:"

    # Warning: This can consume a LOT of tokens. This should be limited
    # before going to production.
    while not context.endswith("\n\n"):
        response = openai.Completion.create(prompt=context, **parameters)

        context += response["choices"][0]["text"]

    # The "stop" parameter supplied to GPT-3 does not get included in
    # the completion.
    context += "Interviewer: "

    return context


summarization_parameters = {
    "engine": "davinci-instruct-beta",
    "frequency_penalty": 0.3,
    "max_tokens": 256,
    "temperature": 0,
    "stop": "'''",
}

def summarize(context: str) -> str:
    summary_prompt = f"""Briefly summarize the following interview transcript:

'''
{context}
'''"""
    
    response = openai.Completion.create(prompt=summary_prompt, **summarization_parameters)
    return response.choices[0]["text"]
