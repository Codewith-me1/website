from django.shortcuts import render,HttpResponse
from .models import contact,userform
# Create your views here.
def main(request):
    if request.method =="POST":
        name= request.POST.get("name")
        email = request.POST.get('email')
        mess = request.POST.get("message")
        sub = request.POST.get('sub')
        em = contact(your_name=name,your_email=email,your_sub=sub,your_mess=mess)
        em.save()
    return render (request,'mega project.html')

def home(request):
    if request.method =="POST":
        name= request.POST.get("name")
        email = request.POST.get('email')
        mess = request.POST.get("message")
        sub = request.POST.get('sub')
        em = contact(your_name=name,your_email=email,your_sub=sub,your_mess=mess)
        em.save()
    return render(request,'mega project.html')
def user(request):
    if request.method=='POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        em =userform(full_name= name,email=email,message=message)
        em.save()
    return render (request,'user.html')
