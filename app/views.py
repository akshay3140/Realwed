import email
from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from app.models import *
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def fun(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conformpassword=request.POST['conformpassword']
        areyou = request.POST['areyou']
        if (password==conformpassword):
            register=reg.objects.all()
            for i in register:
                if i.email==email:
                    messages.error(request,'email already taken.please login')
                    return render(request,'registration.html')
            obj =reg(firstname=firstname,lastname=lastname,username=username,email=email,password=password,conformpassword=conformpassword,areyou=areyou)
            obj.save()
            return redirect('login')
        else:
            messages.error(request,'please check your conform password')
            return render(request,'registration.html')
    else:
        return render(request,'registration.html')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password=request.POST['password']
        count = reg.objects.filter(email=email,password=password).count()
        obj = reg.objects.filter(email=email,password=password)
        print(count)
        if count>0:
            request.session['is_logged'] = email
            request.session['uniqu'] = obj[0].email
            return redirect('indexpage')
    return render(request,'login.html')
def indexpage(request):
    return render(request,'indexpage.html')
def aboutus(request):
    return render(request,'about-us.html')
def contactus(request):
    return render(request,'contact-us.html')
def photographer(request):
    objj = photographerdetail.objects.all()
    photographer_page=Paginator(objj,6)
    page_num=request.GET.get('page')
    page=photographer_page.get_page(page_num)
    context={
        'count':photographer_page.count,
        'page':page
    }
    return render(request,'supplier-photographer-list.html',context)
def venues(request):
    obj = venuedetail.objects.all()
    venue_page=Paginator(obj,6)
    page_num=request.GET.get('page')
    page=venue_page.get_page(page_num)
    context={
        'count':venue_page.count,
        'page':page
    }
    
    return render(request,'supplier-venues-list.html',context)
def cake(request):
    ob= cakedetail.objects.all()
    cake_page=Paginator(ob,6)
    page_num=request.GET.get('page')
    page=cake_page.get_page(page_num)
    context={
        'count':cake_page.count,
        'page':page
    }
    return render(request,'supplier-cake-list.html',context)
def beautision(request):
    obj = beautisiondetail.objects.all()
    beautision_page=Paginator(obj,6)
    page_num=request.GET.get('page')
    page=beautision_page.get_page(page_num)
    context={
        'count':beautision_page.count,
        'page':page
    }
    return render(request,'beautision.html',context)
def beauticion(request,id):
    obj = beautisiondetail.objects.filter(id=id)
    return render(request,'beauticion_detail.html',{'deep':obj})
def cake2(request):
    return redirect('couple')
def couple(request):
    return render(request,'couple-dashboard-todolist.html')
def logout(request):
    if request.session.has_key("is_logged"):
        del request.session["is_logged"]
        del request.session['uniqu']
        return redirect("login")
    return redirect('login')
def venue_detail(request,id):
    obj = venuedetail.objects.filter(id=id)
    return render(request,'venuedetail.html',{'akki':obj})
def photographer_detail(request,id):
    obj= photographerdetail.objects.filter(id=id)
    return render(request,'photographer_detail.html',{'dax':obj})
def cake_detail(request,id):
    obj = cakedetail.objects.filter(id=id)
    return render(request,'cakedetail.html',{'fun':obj})
def search(request):
    query=request.GET['query']
    obj = venuedetail.objects.filter(price__icontains=query)
    return render(request,'search.html',{'akki':obj})
def searchcake(request):
    find = request.GET['find']
    obj = cakedetail.objects.filter(cakename__icontains=find)
    return render(request,'searchcake.html',{'fun':obj})
def searchphoto(request):
    found = request.GET['found']
    obj = photographerdetail.objects.filter(city__icontains=found)
    return render(request,'searchphoto.html',{'dax':obj})
def searchbeauticion(request):
    data = request.GET['data']
    obj = beautisiondetail.objects.filter(bcity__icontains=data)
    return render(request,'searchbeauticion.html',{'deep':obj})