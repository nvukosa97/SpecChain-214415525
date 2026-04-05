"""generates tests from specs"""
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
from dotenv import load_dotenv
load_dotenv()

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

file = BASE_DIR / "spec" / "spec_auto.md"

with open(file, "r", encoding="utf-8") as f:
    file_content = f.read()



prompt = f"""
You are analyzing customer reviews for a mental health application.

You created personas that provides the group's constraints, common goals, pain points, and context.
You derived a structured specification describing what the system should support. 
Each requirement includes: a unique requirement ID, a description of system behavior, the persona that motivated the requirement, traceability to the review group, and acceptance criteria

Here is the specification:
{file_content}

Create validation tests based on the generated specifications. 
Each requirement must include at least 1 validation scenario that describes how it could be verified
Each requirement must include at least 1 validation scenario that describes how it could be verified
Each requirement must include at least 1 validation scenario that describes how it could be verified

Each test scenario must contain: a unique test ID, the requirement it validates, a short scenario description, a list of steps describing how the test would be executed, and the expected outcome

Return a JSON file with the following format:
{{
  "tests": [
    {{
      "test_id": "T_auto_1",
      "requirement_id": "FR_auto_1",
      "scenario": "Logging a workout without crashing",
      "steps": [
        "Open the workout logging screen",
        "Enter workout details",
        "Submit the workout"
      ],
      "expected_result": "The workout is saved successfully and the application remains stable."
    }}
  ]
}}

"""

response = get_completion(prompt)

file = BASE_DIR / "tests" / "tests_auto.json"

if response is not None:
    data = json.loads(response)  # convert JSON string to Python object
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved response to {file}")
else:
    print("No response to save.")