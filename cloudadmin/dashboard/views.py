from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def home(request):

    context = {
        "title" : "Please Try Again hehehe!"
    }

    return render(request, "index.html", dict(context=context))