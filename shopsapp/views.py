from django.shortcuts import render,redirect
from shopsapp.models import catdb,prodb
from frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages


# Create your views here.

def shoppg(req):
    return render(req,"index.html")

def add(req):
    return render(req,"Addcategory.html")

def save_category(req):
    if req.method=="POST":
        n=req.POST.get('cname')
        d=req.POST.get('desc')
        im=req.FILES['img']
        obj=catdb(CategoryName=n,Description=d,Image=im)
        obj.save()
        messages.success(req,"category saved successfully")
        return redirect(add)

def dis(req):
    cat=catdb.objects.all()
    return render(req,"displaycat.html",{'cat':cat})

def editcat(req,dataid):
    data=catdb.objects.get(id=dataid)
    return render(req,"edit.html",{'data':data})

def update(req,dataid):
    if req.method=="POST":
        n=req.POST.get('cname')
        d=req.POST.get('desc')
        try:
            im=req.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(CategoryName=n,Description=d,Image=file)
        messages.success(req, "category updated successfully")
        return redirect(dis)

def delete_cat(req,dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(req, "deleted  successfully")
    return redirect(dis)

def pro(req):
    category=catdb.objects.all()
    return render(req,"Addproduct.html",{'category':category})

def savepro(req):
    if req.method=="POST":
        n=req.POST.get('cat')
        p=req.POST.get('pname')
        d=req.POST.get('desc')
        pr=req.POST.get('price')
        im=req.FILES['image']
        obj=prodb(CategoryName=n,ProductName=p,Description=d,Price=pr,Image=im)
        obj.save()
        messages.success(req, "product saved successfully")
        return redirect(pro)

def dispro(req):
    product=prodb.objects.all()
    return render(req,"displaypro.html",{'product':product})

def editpro(req,proid):
    product=prodb.objects.get(id=proid)
    category = catdb.objects.all()
    return render(req,"editpro.html",{'product':product,'category':category})

def updatepro(req,proid):
    if req.method == "POST":
        n = req.POST.get('cat')
        p = req.POST.get('pname')
        d = req.POST.get('desc')
        pr = req.POST.get('price')
        try:
            im = req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=prodb.objects.get(id=proid).Image
        prodb.objects.filter(id=proid).update(CategoryName=n,ProductName=p,Description=d,Price=pr,Image=file)
        messages.success(req, "updated successfully")
        return redirect(dispro)

def deletepro(req,proid):
    product=prodb.objects.filter(id=proid)
    product.delete()
    messages.warning(req, "deleted  successfully")
    return redirect(dispro)

def adminlog(req):
    return render(req,"Adminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(shoppg)
            else:
                return redirect(adminlog)
        else:
            return redirect(adminlog)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlog)

def viewcontact(req):
    data=contactdb.objects.all()
    return render(req,"viewcontact.html",{'data':data})

# def delete(req,dataid):
#     data=contactdb.objects.filter(id=dataid)
#     data.delete()
#     return redirect(viewcontact)












