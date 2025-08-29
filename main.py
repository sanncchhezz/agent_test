#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import AgentTest

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    while True:
        topic = input("Enter the topic for the crew to work on: ").strip()
        if topic:
            break
        else:
            print("Topic cannot be empty. Please enter a valid topic.")

    while True:
        year = input("Enter the current year (leave empty for current year): ").strip()
        if not year:
            year = str(datetime.now().year)
            break
        try:
            year_int = int(year) 
            if year_int > datetime.now().year:
                raise ValueError("Year out of range")
            year = str(year_int)
            break
        except ValueError:
            print("Invalid year. Please enter a valid year.")
    
    inputs = {
        'topic': topic,
        'current_year': year
    }
    
    try:
        AgentTest().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()

