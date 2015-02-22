from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
        return render_to_response("index.html", None, RequestContext(request))

def search(request):
        return render_to_response("search.html", None, RequestContext(request))

def agreements(request):
        return render_to_response("agreements.html", None, RequestContext(request))

def disclosure(request):
        return render_to_response("disclosure.html", None, RequestContext(request))

def search(request):
        return render_to_response("search.html", None, RequestContext(request))

def tag(request):
        return render_to_response("tag.html", None, RequestContext(request))
