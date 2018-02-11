from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    body = '<div style="font-family: monospace;">'
    body = body + models.Header
    body = body + '</div>'
    return HttpResponse(body)