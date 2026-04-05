"""automated persona generation pipeline"""

import subprocess
import sys

def install_if_missing(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = [
    "openai",
    "groq"
    
]

for p in packages:
    install_if_missing(p)

import openai
import os
from groq import Groq
from openai import OpenAI
from time import sleep



import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

#client = OpenAI(
#    api_key=os.environ.get("OPENAI_API_KEY")
#)

def get_completion(prompt, model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0):
    """
    Get a response from OpenAI's chat model.

    Args:
        prompt (str): Input text to send to model
        model (str, optional): OpenAI model name. Default: "gpt-3.5-turbo"
        temperature (float, optional): Response randomness (0-1). Default: 0

    Returns:
        str: Model's response text, or None if error occurs
    """
    try:
        # Make API call to OpenAI's chat completion endpoint
        response = client.chat.completions.create(
            model=model,           # Specify which model to use (e.g., gpt-3.5-turbo)
            messages=[             # Format prompt as a message array
                {
                    "role": "user",    # Set message role as user
                    "content": prompt  # The actual prompt text
                }
            ],
            response_format={"type": "json_object"},
            temperature=temperature    # Control response randomness (0=focused, 1=creative)
        )
        # Extract and return just the message content from the first response
        return response.choices[0].message.content
    except Exception as e:
        # Handle any API errors and print the error message
        print(f"An error occurred: {e}")
        return None

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

path = BASE_DIR / "data" / "reviews_clean.jsonl"

def load_file(file, n_lines=700):
    lines = []
    with open(file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= n_lines:
                break
            lines.append(line)
    return lines

file_content = load_file(path)




prompt = f"""
You are analyzing customer reviews for a mental health application.
Here are the reviews:
{file_content}
Use the provided reviews to identify groups of similar feedback. 
Create 15 groups of reviews that represent distinct types of users or user situations. 
Each group must contain at least several related reviews and clearly represent a common theme.

The themes should be specific as they will be used to create personas to generate requirements for the application later on.
Avoid generic themes like "Positive Experience". 

Return a JSON in the following format:
{{
  "groups": [
    {{
      "group_id": "A1",
      "theme": "Workout logging issues",
      "review_ids": ["rev_12", "rev_33", "rev_41", "rev_92"],
      "example_reviews": [
        "The app crashes whenever I try to log a run.",
        "Logging workouts causes the app to freeze."
      ]
    }}
  ]
}}
"""

response = get_completion(prompt)

file = BASE_DIR / "data" / "review_groups_auto.json"

if response is not None:
    data = json.loads(response)  # convert JSON string to Python object
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved response to {file}")
else:
        raise Exception("No response to save.")



with open(file, "r", encoding="utf-8") as f:
    file_content2 = f.read()

prompt2 = f"""
You are analyzing customer reviews for a mental health application.

You created 15 groups of reviews that represent distinct types of users or user situations. 
Each group contains at least several related reviews and clearly represent a common theme.

Here are the groups:
{response}

Use the review groups from to create personas that provides the group's constraints, common goals, pain points, and context. 
Each persona must reference the review group it was derived.
The personas should be detailed and specific as they will be used to generate requirements for the application.


Return a JSON in the following format:
{{  "personas": [
    {{
      "id": "P1",
      "name": "Frequent Activity Tracker",
      "description": "A user who relies on the app to log workouts frequently and expects stable performance.",
      "derived_from_group": "G1",
      "goals": [
        "Track workouts consistently",
        "Log activity quickly",
        "Track workouts consistently",
        "Log activity quickly",
              ],
      "pain_points": [
        "App crashes during logging",
        "Workout data sometimes disappears",
        "App crashes during logging",
        "Workout data sometimes disappears"      ],
      "context": [
        "Logging activities immediately after workouts",
        "Using the app during outdoor exercise",
              ],
      "constraints": [
        "Logging must be reliable",
        "Data should not be lost",
        "Data should not be lost"        ],
      "evidence_reviews": [
        "rev_12",
        "rev_45",
        "rev_12",
        "rev_45"        ]
    }}  ] }}
"""

response2 = get_completion(prompt2)



file = BASE_DIR / "personas" / "personas_auto.json"

if response2 is not None:
    data = json.loads(response2)  # convert JSON string to Python object
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved response to {file}")
else:
    raise Exception("No response to save.")