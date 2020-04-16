from django.http import HttpResponse
import json

a={}

def getScores(request):

    return HttpResponse(json.dumps(a))


def postScore(request):
    name=request.GET.get('name', '')
    score=request.GET.get('score', '')
    #a[name]=time[:2]+":"+time[2:]
    a[name] = score
    return HttpResponse(json.dumps(a))