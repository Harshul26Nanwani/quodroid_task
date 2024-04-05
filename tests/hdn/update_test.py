import requests
import json
import time
 
import os
def get_response(endpoint_url):
    try:
        response = requests.post(endpoint_url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
 
# Example usage
endpoint = input("Enter the endpoint URL: ")
default_delay=1
time.sleep(default_delay)
print('Sending Request')
time.sleep(default_delay)
 
response = get_response(endpoint)
print('Recieved Response')
time.sleep(default_delay)
# Parse response as JSON
try:
    print('Parsing Response')
 
    json_response = json.loads(response)
    time.sleep(default_delay)
 
    # Do something with the parsed JSON data
    # For example, print the JSON response
    if 'tests' in json_response:
        print("Tests found in the JSON response:")
        print('Updating the test file')
        filetask= open('./tasks.robot', 'w')
        # Clear the file
        filetask.__del__()
        filetask.close()   
        # Update the data in the file
        with open('./tasks.robot', 'a') as file:
            file.write('*** Settings ***' + '\n')
            file.write('Documentation       Custom Script Started' + '\n')
            file.write('Library             RPA.Browser.Selenium' + '\n')
            file.write('*** Tasks ***' + '\n')
 
 
            file.write(json_response['tests'][0]['title'] + '\n')
 
            for step in json_response['tests'][0]['steps']:
                file.write('    '+step + '\n')
            time.sleep(default_delay)
            file.close()
            print('Test Updated')
            print('Running the test') 
            time.sleep(default_delay)
 
            os.system('rcc run')
    else:
        print("No 'tests' key found in the JSON response.")
 
except json.JSONDecodeError as e:
    print(f"Failed to parse response as JSON: {e}")
