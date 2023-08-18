#!/usr/bin/python3
"""
Module to fetch and display the status of https://alu-intranet.hbtn.io
"""


import requests

def fetch_and_display_status():
    """
    Fetches the status of https://alu-intranet.hbtn.io and displays response details.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == '__main__':
    fetch_and_display_status()