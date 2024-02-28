from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    name="badmus"
    courses=['frontend', 'backend', 'product design', 'data science', 'cloud development']
    context={
        'n':name,
        "course_list":courses,
    }  
    return render(request, "app1/index.html", context)

def back_page_view(request):
    date="friday"
    return render(request, "backpage/index2.html", {"n":date})

# # Create your views here.
# def home_page_view(request):
#     text="welcome to my django website"
#     return HttpResponse(text)


def profile_page_view(request, username):
    text=f"welcome (username)"
    return HttpResponse(text)

def about_page_view(request):
    return HttpResponse ("welcome to about page")

def about_page_view(request):
    return render(request, "app1/about.html")

def contact_page_view(request):
    return render(request, "app1/contact.html")

def pricing_page_view(request):
    return render(request, "app1/pricing.html")
    

    