from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
import time
import os
from django.views import View
import xmltodict
def index(request):
  return render(request,"index.html")


def tests(request):
    if request.method=='POST':
        # Parse response as JSON
        
        return JsonResponse({"tests":[{"title":"Open google.com","steps":["Open Browser    browser=chrome","Go To    url=https://google.com"]}]})
    else:
        return JsonResponse({"Error no data found": ""})

class TestExecutionView(View):
    def post(self, request, *args, **kwargs):
        # Parse incoming JSON payload
        tests_data = request.body.decode('utf-8')
        print(tests_data)
        # Parse tests_data and execute tests using Robot Framework
        # Capture test results
        try:
            print('Parsing Response')
        
            json_response = json.loads('{"tests":[{"title":"Open google.com","steps":["Open Browser    browser=chrome","Go To    url=https://google.com"]}]}')

        
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
                    file.close()
        
                    os.system('rcc run')
            else:
                print("No 'tests' key found in the JSON response.")
        
        except json.JSONDecodeError as e:
            print(f"Failed to parse response as JSON: {e}")
        
        with open("./output/output.xml") as xml_file:
     
            data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()
     
    # generate the object using json.dumps() 
    # corresponding to json data
     
            json_data = json.dumps(data_dict)
            rstr=str(json_data).replace('@','')
            json_data=json.loads(rstr)
        
        test_results = json_data
        # Format test results and return as JSON response
        return JsonResponse({'results': test_results})
    def get(self, request, *args, **kwargs):
        return render(request,"index.html")