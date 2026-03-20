from workflows.main_workflow import route_query

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

def main():
    print("=== Agentic AI System: Project Pragna ===")

    while True:
        query = input("\nEnter your query (or type 'exit'): ").strip()

        if query.lower() == "exit":
            print("Exiting...")
            break

        if not query:
            print("Please enter a valid query.")
            continue

        response = route_query(query)
        print("\nResponse:\n", response)


if __name__ == "__main__":
    main()
