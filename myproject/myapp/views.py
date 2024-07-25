from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myapp_home(request):
    return HttpResponse(
"""
<h1>hello world</h1>
<h2> i am python</h2>                     
""")
