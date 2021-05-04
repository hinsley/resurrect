# gpt3.py
# Provides an interface for generating new interview content
# with OpenAI's GPT-3 API.

import openai

with open("openai-api-key.txt") as f:
    openai.api_key = f.read().strip()

interviewees = {
    "Hammurabi": {
        "title": "Hammurabi, king of Babylon",
        "nominal": "Hammurabi",
    },
    "Sun Tzu": {
        "title": "Sun Tzu",
        "nominal": "Tzu",
    },
    "Confucius": {
        "title": "Confucius",
        "nominal": "Confucius",
    },
    "Socrates": {
        "title": "Socrates",
        "nominal": "Socrates",
    },
    "Alexander the Great": {
        "title": "Alexander III of Macedon",
        "nominal": "Alexander",
    },
    "Plato": {
        "title": "Plato",
        "nominal": "Plato",
    },
    "Aristotle": {
        "title": "Aristotle",
        "nominal": "Aristotle",
    },
    "Epicurus": {
        "title": "Epicurus",
        "nominal": "Epicurus",
    },
    "Zeno of Citium": {
        "title": "Zeno of Citium",
        "nominal": "Zeno",
    },
    "Ashoka the Great": {
        "title": "Ashoka the Great",
        "nominal": "Ashoka",
    },
    "Julius Caesar": {
        "title": "Julius Caesar",
        "nominal": "Julius",
    },
    "Cleopatra": {
        "title": "Cleopatra VII Philopator",
        "nominal": "Cleopatra",
    },
    "Augustus Caesar": {
        "title": "Augustus Caesar",
        "nominal": "Augustus",
    },
    "Lucius Seneca": {
        "title": "Lucius Annaeus Seneca the Younger",
        "nominal": "Seneca",
    },
    "Claudius Ptolemy": {
        "title": "Claudius Ptolemy",
        "nominal": "Ptolemy",
    },
    "Marcus Aurelius": {
        "title": "Marcus Aurelius Antoninus",
        "nominal": "Aurelius",
    },
    "Muhammad al-Khwarizmi": {
        "title": "Muhammad ibn Musa al-Khwarizmi",
        "nominal": "al-Khwarizmi",
    },
    "Christopher Columbus": {
        "title": "Christopher Columbus",
        "nominal": "Columbus",
    },
    "Leonardo da Vinci": {
        "title": "Leonardo da Vinci",
        "nominal": "da Vinci",
    },
    "Niccolo Machiavelli": {
        "title": "Niccolò di Bernardo dei Machiavelli",
        "nominal": "Machiavelli",
    },
    "Nicolaus Copernicus": {
        "title": "Nicolaus Copernicus",
        "nominal": "Copernicus",
    },
    "Pocahontas": {
        "title": "Pocahontas",
        "nominal": "Pocahontas",
    },
    "Johannes Kepler": {
        "title": "Johannes Kepler",
        "nominal": "Kepler",
    },
    "Galileo Galilei": {
        "title": "Galileo di Vincenzo Bonaiuti de' Galilei",
        "nominal": "Galileo",
    },
    "Rene Descartes": {
        "title": "René Descartes",
        "nominal": "Descartes",
    },
    "John Locke": {
        "title": "John Locke",
        "nominal": "Locke",
    },
    "Gottfried Leibniz": {
        "title": "Gottfried Wilhelm Leibniz",
        "nominal": "Leibniz",
    },
    "Isaac Newton": {
        "title": "Sir Isaac Newton",
        "nominal": "Newton",
    },
    "Johann Sebastian Bach": {
        "title": "Johann Sebastian Bach",
        "nominal": "Bach",
    },
    "David Hume": {
        "title": "David Hume",
        "nominal": "Hume",
    },
    "Leonhard Euler": {
        "title": "Leonhard Euler",
        "nominal": "Euler",
    },
    "Benjamin Franklin": {
        "title": "Benjamin Franklin",
        "nominal": "Franklin",
    },
    "Catherine the Great": {
        "title": "Catherine II the Great",
        "nominal": "Catherine II",
    },
    "George Washington": {
        "title": "George Washington",
        "nominal": "Washington",
    },
    "Immanuel Kant": {
        "title": "Immanuel Kant",
        "nominal": "Kant",
    },
    "Joseph-Louis Lagrange": {
        "title": "Joseph-Louis Lagrange",
        "nominal": "Lagrange",
    },
    "Napoleon Bonaparte": {
        "title": "Napoléon Bonaparte",
        "nominal": "Napoléon",
    },
    "Ada Lovelace": {
        "title": "Augusta Ada King, Countess of Lovelace",
        "nominal": "Ada",
    },
    "Carl Gauss": {
        "title": "Johann Carl Friedrich Gauss",
        "nominal": "Gauss",
    },
    "Soren Kierkegaard": {
        "title": "Søren Aabye Kierkegaard",
        "nominal": "Kierkegaard",
    },
    "Augustin-Louis Cauchy": {
        "title": "Baron Augustin-Louis Cauchy",
        "nominal": "Cauchy",
    },
    "Abraham Lincoln": {
        "title": "Abraham Lincoln",
        "nominal": "Lincoln",
    },
    "Bernhard Riemann": {
        "title": "Bernhard Riemann",
        "nominal": "Riemann",
    },
    "Charles Babbage": {
        "title": "Charles Babbage",
        "nominal": "Babbage",
    },
    "Cornelius Vanderbilt": {
        "title": "Cornelius Vanderbilt",
        "nominal": "Vanderbilt",
    },
    "Louis Pasteur": {
        "title": "Louis Pasteur",
        "nominal": "Pasteur",
    },
    "Friedrich Nietzsche": {
        "title": "Friedrich Wilhelm Nietzsche",
        "nominal": "Nietzsche",
    },
    "Andrew Carnegie": {
        "title": "Andrew Carnegie",
        "nominal": "Carnegie",
    },
    "Srinivasa Ramanujan": {
        "title": "Srinivasa Ramanujan",
        "nominal": "Ramanujan",
    },
    "Thomas Edison": {
        "title": "Thomas Alva Edison",
        "nominal": "Edison",
    },
    "Marie Curie": {
        "title": "Marie Skłodowska Curie",
        "nominal": "Curie",
    },
    "Nikola Tesla": {
        "title": "Nikola Tesla",
        "nominal": "Tesla",
    },
    "Mahatma Gandhi": {
        "title": "Mahātmā Mohandas Karamchand Gandhi",
        "nominal": "Gandhi",
    },
    "Alan Turing": {
        "title": "Alan Mathison Turing",
        "nominal": "Turing",
    },
    "Albert Einstein": {
        "title": "Albert Einstein",
        "nominal": "Einstein",
    },
    "John von Neumann": {
        "title": "John von Neumann",
        "nominal": "von Neumann",
    },
    "Erwin Schrodinger": {
        "title": "Erwin Rudolf Josef Alexander Schrödinger",
        "nominal": "Schrödinger",
    },
    "Robert Oppenheimer": {
        "title": "J. Robert Oppenheimer",
        "nominal": "Oppenheimer",
    },
    "Elvis Presley": {
        "title": "Elvis Aaron Presley",
        "nominal": "Elvis",
    },
    "Richard Feynman": {
        "title": "Richard Phillips Feynman",
        "nominal": "Feynman",
    },
    "Grace Hopper": {
        "title": "Grace Brewster Murray Hopper",
        "nominal": "Hopper",
    },
    "Isaac Asimov": {
        "title": "Isaac Asimov",
        "nominal": "Asimov",
    },
    "Linus Pauling": {
        "title": "Linus Carl Pauling",
        "nominal": "Pauling",
    },
    "Paul Erdos": {
        "title": "Paul Erdős",
        "nominal": "Erdős",
    },
    "Ronald Reagan": {
        "title": "Ronald Wilson Reagan",
        "nominal": "Reagan",
    },
    "Maryam Mirzakhani": {
        "title": "Maryam Mirzakhani",
        "nominal": "Mirzakhani",
    },
    "Stephen Hawking": {
        "title": "Stephen William Hawking",
        "nominal": "Hawking",
    },
}

def new_transcript(interviewee: str) -> str:
    """
    Generates a fresh transcript.
    """

    return f"The following is an excerpt of a transcript from an informal interview with {interviewees[interviewee]['title']}.\n\nInterviewer: "

parameters = {
    "engine": "davinci",
    "frequency_penalty": 0.2,
    "max_tokens": 200,
    "temperature": 0.55,
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
