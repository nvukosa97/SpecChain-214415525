"""generates structured specs from personas"""

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

file = BASE_DIR / "personas" / "personas_auto.json"

with open(file, "r", encoding="utf-8") as f:
    file_content = f.read()



prompt = f"""
You are analyzing customer reviews for a mental health application.

You created personas that provides the group's constraints, common goals, pain points, and context.
Here are the personas:
{file_content}

Use the personas to derive a structured specification describing what the system should support. 

Each requirement must include: a unique requirement ID, a description of system behavior, the persona that motivated the requirement, traceability to the review group, and acceptance criteria

Generate 2 to 4 requirements for each persona

Return a markdown file in the following format, please follow the exact format as it will be parsed by a script:
## Requirements for Frustrated User (P1)
### Requirement ID: FR_auto_1
- Description: The system shall handle user interactions without crashing or freezing.

- Source Persona: Frustrated User (P1)
- Traceability: Derived from review group A1
- Acceptance Criteria: Given the user interacts with the app, When the interaction completes, Then the application must remain stable, and the user's progress must be saved successfully.

### Requirement ID: FR_auto_2
- Description: The system shall provide quick response times to user inputs.

- Source Persona: Frustrated User (P1)
- Traceability: Derived from review group A1
- Acceptance Criteria: Given the user provides input, When the system processes the input, Then the system must respond within a reasonable time frame (e.g., < 2 seconds).

## Requirements for Disappointed User (P2)
### Requirement ID: FR_auto_3
- Description: The system shall provide insightful and helpful advice to users.

- Source Persona: Disappointed User (P2)
- Traceability: Derived from review group A2
- Acceptance Criteria: Given the user requests advice, When the system provides a response, Then the response must be relevant, helpful, and empathetic.
"""

response = get_completion(prompt)

file = BASE_DIR / "spec" / "spec_auto.md"

if response is not None:
   
    with open(file, "w", encoding="utf-8") as f:
        f.write(response)
