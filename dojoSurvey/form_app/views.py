from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['lang']
    comment = request.POST['comment']

    #note for checkbox and radio elements, they are multi-valued so you need to use the get method which assigns a default value if it is not selected
    g1 = request.POST.get('gender1', "Not Given")
    g2 = request.POST.get('gender2', "Not Given")
    g3 = request.POST.get('gender3', "Not Given")
    v1 = request.POST.get('vehicle1','')
    v2 = request.POST.get('vehicle2','')
    v3 = request.POST.get('vehicle3','')

    context={
    "name": name,
    "location": location,
    "lang": language,
    "comment": comment,
    "gender1": g1,
    "gender2": g2,
    "gender3": g3,
    "vehicle1": v1,
    "vehicle2": v2,
    "vehicle3": v3
    }

    return render(request,"result.html",context)
