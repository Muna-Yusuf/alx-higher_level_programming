#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request ...
   to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    letter = {"q": q}
    resp = requests.post(url, data=letter)

    try:
        pars = resp.json()
        if pars == {}:
            print(f"[{letter['pars']}] {letter['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
