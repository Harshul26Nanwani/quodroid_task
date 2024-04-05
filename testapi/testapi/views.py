from django.http import HttpResponse


def index(request):
    return HttpResponse("All , Ok")

from django.http import JsonResponse

def tests(request):
    if request.method=='POST':
	    return JsonResponse({"tests":[{"title":"Open google.com","steps":["Open Browser    browser=chrome","Go To    url=https://google.com"]}]})
    else:
        return JsonResponse({"Error no data found": ""})