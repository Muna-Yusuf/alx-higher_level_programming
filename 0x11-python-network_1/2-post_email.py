#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request ...
   to the passed URL with the email as a parameter, and ...
   displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    _email = {'email': email}
    par_encoded = parse.urlencode(_email).encode('ascii')

    with request.urlopen(url, data=par_encoded) as re:
        print(re.read().decode('utf-8'))
