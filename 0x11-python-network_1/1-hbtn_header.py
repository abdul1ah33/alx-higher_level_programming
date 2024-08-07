#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        requested_id = response.headers.get('X-Request-Id')
        print(requested_id)

if __name__ == "__main__":
    main(argv[1])

