from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
import os
from django.conf import settings


# Create your views here.
def login_page(request):
    context = {
        "title": "Please Try Again hehehe!"
    }

    return render(request, "login.html", dict(context=context))


def admin_login(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'config.txt')
    config =  open(file_path,"r")
    test = config.read()
    print(type(test))
    check = test.split("\n")
    print(check[2])
    if request.POST["username"] == check[2] and request.POST["password"] == check[2]:
        return admin_panel(request)
    else:
        return render(request, "login.html")


def admin_panel(request):
    return render(request, "admin_panel.html")

def admin_form(request, form_id):
    if form_id == "1":
        return render(request, "admin_panel.html")
    elif form_id == "2":
        return render(request, "admin_panel.html")




