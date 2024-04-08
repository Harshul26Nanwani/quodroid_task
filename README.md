# QuoDroid Task

The core objective of this challenge is to create a system that can accept a detailed API call,
execute the testing steps provided within as a Robot Framework test, and subsequently
return the test output. This entails developing an application using Python and Django that
exposes an API endpoint. This endpoint should accept a POST request structured as
follows, execute the detailed steps using the Robot Framework, and return the results:
### API Call Content:
Endpoint: http://127.0.0.1:8000/testai/tests/v1/execute   
Method: POST   
Headers: Content-Type: application/json   
Body: 
```json
{
"tests":[
{
"title":"Open google.com",
"steps":[
"Open Browser browser='chrome'",
"Go To url='https://google.com'"
]
}
]
}
```
Description: The JSON payload contains an array under the key TESTS, with each item
in the array representing a single test case. Each test case has a TITLE and an array of

STEPS. Each step is a command to be executed by the Robot Framework, such as
opening a browser or navigating to a URL.



### How To Run:-
1) Open terminal
2) ```cd testapi ```
3) Open views.py in folder testapi.
4) ```python manage.py runserver```
Note:- API is now running at localhost http://127.0.0.1:8000/testai/tests/v1/execute and to run tests goto localhost:8000/

