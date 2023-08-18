#!/usr/bin/python3

"""
Module to send a POST request to a URL with an email parameter and display the response body
"""

import requests
import sys

def send_post_request_and_display_response(url, email):
    """
    Sends a POST request to the given URL with the email parameter and displays the response body.
    """
    
    data = {'email': email}
    response = requests.post(url, data=data)
    
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    send_post_request_and_display_response(url, email)