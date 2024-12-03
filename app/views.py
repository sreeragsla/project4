from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'Name':'Sreerag','Age':25}
    return render(request,'jinja_print.html',context=d)

