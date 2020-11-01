from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Updates,Hospital,Specilization
from api.models import f_users
from django.core.paginator import Paginator
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    #return HttpResponse('hello')
    return render(request, 'login.html')

def dashboard(request):
    return render(request,'dashboard.html')
    #return HttpResponse('hello akhil home')

def userlist(request):
    data=f_users.objects.all()
    paginator=Paginator(data,4)
    page=request.GET.get('page',1)
    data=paginator.get_page(page)
    return render(request,'userlist.html',{'data':data})

def updatelist(request):
    data = Updates.objects.all()
    paginator = Paginator(data, 4)
    page = request.GET.get('page', 1)
    data = paginator.get_page(page)
    return render(request, 'updates.html', {'data': data})

def adduser(request):
    return render(request,'add-user.html')

def addupdate(request):
    return render(request,'add-update.html')

def saveuser(request):
    if request.method=="POST":
        Name=request.POST.get('projectname')
        des=request.POST.get('description')
        img=request.POST.get('img')
        #img="ImageNotFound"
        msg=Updates.objects.create(title=Name,description=des,image=img)
        msg.save()
        #messages.info(request,"Project Added Sucessfully")
        #return render(request,'userlist.html')
        return redirect("userlist")
def saveupdate(request):
    if request.method=="POST":
        Name_EN=request.POST.get('ProjectName(EN)')
        Name_AR=request.POST.get('ProjectName(AN)')
        des_EN=request.POST.get('ProjectDescription(EN)')
        des_AR=request.POST.get('ProjectDescription(AR)')
        #img=request.POST.get('image')
        update_id=request.POST.get('updateid')
        print("uid:",update_id)
        img=request.FILES['img']
        #img="IMAGE NOT FOUND"
        if update_id is not None:
            msg=Updates.objects.filter(id=update_id).update(title_EN=Name_EN,title_AR=Name_AR,description_EN=des_EN,description_AR=des_AR,image=img)    
            #msg.save()
        else:
            msg=Updates.objects.create(title_EN=Name_EN,title_AR=Name_AR,description_EN=des_EN,description_AR=des_AR,image=img)
            msg.save()
        #messages.info(request,"Project Added Sucessfully")
        #return render(request,'userlist.html')
        return redirect("updatelist")

def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        print("uname",user_name)
        print("password",password)
        user=auth.authenticate(username=user_name,password=password)
        print("user:",user)
        if user is not None:
            auth.login(request,user)
            return redirect('admindashboard')
        else:
            #messages.info(request,"Wrong Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def mylogin(request):
    return render(request,'login.html')

def Deleteupdate(request,id):
    context = Updates.objects.filter(id=id).update(is_delete=1)
    #context.delete() #permanet delete
    return redirect('updatelist')
def Deleteuser(request,id):
    context = f_users.objects.get(id=id)
    context.delete()
    return redirect('userlist')
def Updateedit(request,id):
    #context=Updates.objects.filter(id=id).values('title','description')
    #context=Updates.objects.get(id=id)
    context=Updates.objects.filter(id=id)
    return render(request,'add-update.html',{'context':context})

########################By Dhurub#######################################

def hospitallist(request):
    data = Hospital.objects.all()
    paginator = Paginator(data, 4)
    page = request.GET.get('page', 1)
    data = paginator.get_page(page)
    return render(request,'hospitallist.html', {'data': data})

def hospitaledit(request,id):
    context=Hospital.objects.filter(id=id)
    return render(request,'add-hospital.html',{'context':context})

def addhospital(request):
    return render(request,'add-hospital.html')

def Savehospital(request):
    if request.method=="POST":
        Name_EN=request.POST.get('Hospital_EN')
        Name_AR=request.POST.get('Hospital_AR')
        #des=request.POST.get('description')
        #img=request.POST.get('image')
        update_id=request.POST.get('updateid')
        #print("uid:",update_id)
        #img=request.FILES['img']
        #img="IMAGE NOT FOUND"
        if update_id is not None:
            msg=Hospital.objects.filter(id=update_id).update(title_EN=Name_EN,title_AR=Name_AR)    
            #msg.save()
        else:
            msg=Hospital.objects.create(title_EN=Name_EN,title_AR=Name_AR)
            msg.save()
        #messages.info(request,"Project Added Sucessfully")
        #return render(request,'userlist.html')
        return redirect("hospitallist")

def Deletehospital(request,id):
    context = Hospital.objects.filter(id=id).update(is_delete=1)
    #context.delete() #permanet delete
    return redirect('hospitallist')

def Specilizationlist(request):
    data = Specilization.objects.all()
    paginator = Paginator(data, 4)
    page = request.GET.get('page', 1)
    data = paginator.get_page(page)
    return render(request,'Specilizationlist.html', {'data': data})

def addspecilization(request):
    return render(request,'add-specilization.html')

def Savespecilization(request):
    if request.method=="POST":
        Name_EN=request.POST.get('Specilization_EN')
        Name_AR=request.POST.get('Specilization_AR')
        #des=request.POST.get('description')
        #img=request.POST.get('image')
        update_id=request.POST.get('updateid')
        #print("uid:",update_id)
        #img=request.FILES['img']
        #img="IMAGE NOT FOUND"
        if update_id is not None:
            msg=Specilization.objects.filter(id=update_id).update(title_EN=Name_EN,title_AR=Name_AR)    
            #msg.save()
        else:
            msg=Specilization.objects.create(title_EN=Name_EN,title_AR=Name_AR)
            msg.save()
        #messages.info(request,"Project Added Sucessfully")
        #return render(request,'userlist.html')
        return redirect("Specilizationlist")

def Specilizationedit(request,id):
    context=Specilization.objects.filter(id=id)
    return render(request,'add-specilization.html',{'context':context})

def Deletespecilization(request,id):
    context = Specilization.objects.filter(id=id).update(is_delete=1)
    #context.delete() #permanet delete
    return redirect('Specilizationlist')










