import email
from multiprocessing import context
from pyexpat.errors import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from app.models import *
from vender.models import *
from django.contrib import messages
from .forms import beauticionform, caterersform, coupled, photographerform, venueform
from django.core.paginator import Paginator
# Create your views here.
def reg(request):
     if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conformpassword=request.POST['conformpassword']
        phonenumber = request.POST['phonenumber']
        if (password==conformpassword):
            register=regdetail.objects.all()
            for i in register:
                if i.email==email:
                    messages.error(request,'email already exist.please login')
                    return render(request,'index.html')
            obj =regdetail(username=username,email=email,password=password,conformpassword=conformpassword,phonenumber=phonenumber)
            obj.save()
            return redirect('login1')
        else:
            messages.error(request,'please check your password')
            return render(request,'index.html')
     else:
        return render(request,'index.html')
def login1(request):
    if request.method=='POST':
        email = request.POST['email']
        password=request.POST['password']
        count = regdetail.objects.filter(email=email,password=password).count()
        obj = regdetail.objects.filter(email=email,password=password)
        print(count)
        if count>0:
            request.session['is_logged']=email
            request.session['uniqu']=obj[0].email
            return redirect('coupledashboard')
    return render(request,'loginn.html')
def logout1(request):
    if request.session.has_key('is_logged'):
        del request.session['is_logged']
        del request.session['uniqu']
        return redirect('login1')
    return redirect('coupledashboard')
def coupleprofile(request):
    if request.method == 'POST':
        # image=request.POST['image']
        # couplename=request.POST['couplename']
        # email=request.POST['email']
        # phone=request.POST['phone']
        # descriptions=request.POST['descriptions']
        # obj = coupledetail(image=image,couplename=couplename,email=email,phone=phone,descriptions=descriptions)
        # obj.save()
        form = coupled(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            img_object=form.instance
            return render(request,'form.html',{'form':form,'img_obj':img_object})
        
        # return HttpResponse('sucess')
    else:
        form = coupled()
    return render(request,'form.html')
def coupledashboard(request):
    return render(request,'couple-dashboard-overview.html')
# def coupletodolist(request):
#     return render(request,'couple-dashboard-todolist-2.html')
def coupleguest(request):
    if request.method=='POST':
        obj = venueform(request.POST,request.FILES)
        print(obj)
        if obj.is_valid():
            try:
                obj.save()
                return redirect('viewvenue')
            except:
                pass
    else:
        obj=venueform()
    return render(request,'venue.html',{'form':obj})
def viewvenue(request):
    obj = venuedetail.objects.all()
    viewvenue_page=Paginator(obj,6)
    page_num = request.GET.get('page')
    page = viewvenue_page.get_page(page_num)
    context={
        'count':viewvenue_page.count,
        'page':page
    }
    return render(request,'couple-dashboard-todolist-2.html',context)
# def photographertodolist(request):
#     return render(request,'photographertodolist.html')
def photographerguests(request):
    if request.method=='POST':
        obj = photographerform(request.POST,request.FILES)
        if obj.is_valid():
            try:
                obj.save()
                return redirect('viewphotographer')
            except:
                pass
    else:
        obj=photographerform()
    return render(request,'photo.html',{'form':obj})
def viewphotographer(request):
    obj = photographerdetail.objects.all()
    viewphotographer_page=Paginator(obj,6)
    page_num= request.GET.get('page')
    page = viewphotographer_page.get_page(page_num)
    context={
        'count':viewphotographer_page.count,
        'page':page
    }
    return render(request,'photographertodolist.html',context)
# def caterestodolist(request):
#     return render(request,'catererstodolist.html')
def caterersguests(request):
    if request.method=='POST':
        obj = caterersform(request.POST,request.FILES)
        if obj.is_valid():
            try:
                obj.save()
                return redirect('viewcaterers')
            except:
                pass
    else:
        obj=caterersform()
    return render(request,'cake.html',{'form':obj})
def viewcaterers(request):
    obj = cakedetail.objects.all()
    viewcaterers_page=Paginator(obj,6)
    page_num= request.GET.get('page')
    page = viewcaterers_page.get_page(page_num)
    context={
        'count':viewcaterers_page.count,
        'page':page
    }
    return render(request,'catererstodolist.html',context)
# def beauticiontodolist(request):
#     return render(request,'beauticiontodolist.html')
def beauticionguest(request):
    if request.method=='POST':
        obj = beauticionform(request.POST,request.FILES)
        if obj.is_valid():
            try:
                obj.save()
                return redirect('viewbeauticion')
            except:
                pass
    else:
        obj=beauticionform()
    return render(request,'beauticions.html',{'form':obj})
def viewbeauticion(request):
    obj = beautisiondetail.objects.all()
    viewbeauticion_page=Paginator(obj,6)
    page_num= request.GET.get('page')
    page = viewbeauticion_page.get_page(page_num)
    context={
        'count':viewbeauticion_page.count,
        'page':page
    }
    return render(request,'beauticiontodolist.html',context)