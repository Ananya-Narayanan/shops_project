from django.shortcuts import render,redirect
from shopsapp.models import  catdb,prodb
from frontend.models import contactdb,registerdb,cartdb
from django.contrib import messages

# Create your views here.

def homepg(req):
    cat=catdb.objects.all()
    return render(req,"home.html",{'cat':cat})

def product(req):
    pro=prodb.objects.all()
    return render(req,"products.html",{'pro':pro})

def singlepro(req,proid):
    data=prodb.objects.get(id=proid)
    return render(req,"single_product.html",{'data':data})

def profilter(req,cat_name):
    data=prodb.objects.filter(CategoryName=cat_name)
    return render(req,"products_filtered.html",{'data':data})

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contactus.html")

def services(req):
    return render(req,"services.html")

def savedata(req):
    if req.method=="POST":
        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        e=req.POST.get('email')
        ad=req.POST.get('address')
        c=req.POST.get('city')
        co=req.POST.get('country')
        m=req.POST.get('msg')
        obj=contactdb(Firstname=fn,Lastname=ln,Email=e,Address=ad,City=c,Country=co,message=m)
        obj.save()
        return redirect(contact)

def register(req):
    return render(req,"register.html")

def saveregister(req):
    if req.method=="POST":
        n=req.POST.get('name')
        m = req.POST.get('mob')
        e=req.POST.get('email')
        u = req.POST.get('user')
        p=req.POST.get('pass')
        obj=registerdb(Name=n,Mobile=m,Email=e,Username=u,Password=p)
        obj.save()
        return redirect(register)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if registerdb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request,"Logined successfully")
            return redirect(homepg)
        else:
            messages.warning(request, "incorrect username/passwword")
            return redirect(register)
    return redirect(register)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(userlogin)

def cart(request):
    data=cartdb.objects.filter(username=request.session['Username'])
    total_price=0
    for i in data:
        total_price=total_price+i.Totalprice
    return render(request,"cart.html",{'data':data,'total_price':total_price})

def savecart(req):
    if req.method=="POST":
        tp=req.POST.get('tprice')
        u=req.POST.get('username')
        d=req.POST.get('desc')
        p=req.POST.get('pname')
        q=req.POST.get('qty')
        pr=req.POST.get('price')
        obj=cartdb(username=u,productname=p,description=d,quantity=q,Totalprice=tp,price=pr)
        obj.save()
        return redirect(cart)

def delete_cart(request,dataid):
    dele=cartdb.objects.filter(id=dataid)
    dele.delete()
    return redirect(cart)

def checkout(request):
    data=cartdb.objects.filter(username=request.session['Username'])
    total_price=0
    for i in data:
        total_price=total_price+i.Totalprice
    return render(request,"checkout.html",{'data':data,'total_price':total_price})

def place_order(request):
    messages.success(request, "placed order successfully")
    return redirect(checkout)

