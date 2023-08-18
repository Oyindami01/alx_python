#!/usr/bin/python3

"""
Search User Script

This script takes a letter as input and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
It processes the response based on JSON formatting and content.


"""

import sys
import requests

def main():
    """
    Sends a POST request to search for a user based on the provided letter.

    Usage: python search_user.py <letter>

    Args:
        letter (str): The letter to use as a search parameter.

    Returns:
        None
    """
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    #prepare the data to be sent in the POST request
    data = {"q": letter}

    try:
        #send a POST request to a specified URL with the letter data
        response =  requests.post('http://0.0.0.0:5000/search_user', data=data)

        #Parse the JSON response
        try:
            json_response = response.json()
            if isinstance(json_response, dict) and 'id' in json_response and 'name' in json_response:
                print("[{}] {}".format(json_response['id'], json_response['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    

if __name__ == "__main__":
    main()