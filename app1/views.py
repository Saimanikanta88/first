from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f1(request):
    return HttpResponse("<marquee>sai manikanta srikant Tarun kumar</marquee>")
def f2(request):
    return HttpResponse("<h1>sai manikanta</h1>")