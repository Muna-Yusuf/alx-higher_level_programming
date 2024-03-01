#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as resp:
        resp_body = resp.read()
        resp_type = type(resp_body)
        resp_deco = resp_body.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {resp_type}")
        print(f"\t- content: {resp_body}")
        print(f"\t- utf8 content: {resp_deco}")
