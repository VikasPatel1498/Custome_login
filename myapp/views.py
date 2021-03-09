from django.shortcuts import render,redirect
from myapp.models import Member

# Create your views here.
def index(request):
    if request.method == 'POST':
        member=Member(username=request.POST['username'],password=request.POST['password'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],)
        member.save()
        return redirect('/')
    else:
        return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def home(request):
    if request.method =="POST":
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member=Member.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'index.html',{'membre':member})
        else:
            context = {'msg':'Invalid username or password'}
            return render(request,'login.html',context)

def show(request):
    member=Member.objects.all()
    return render(request,'show.html',{'member':member})

def delete(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')