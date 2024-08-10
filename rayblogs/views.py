from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from blogs.models import Blogs
from django.core.paginator import Paginator
from signin.models import Users



# def all(request):
#     tORf = request.session.get("tORf", False)
#     uname = request.session.get("username", "")
#     data = {
#         "tORf": tORf,
#         "uname": uname,
#     }
#     return render(request, "all.html", data)

def home(request):
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    ele = {
        "element": Blogs.objects.all().order_by("date_of_post").reverse(),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
    }
    return render(request, "home.html", ele)


def signin(request):
    
    if request.method=="POST":
        fname=request.POST.get("fristname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        phone_num=request.POST.get("phone")
        Username=request.POST.get("Uname")
        password=request.POST.get("pass")
        imageuserup=request.FILES.get("upimg")
        Updata=Users(first_name=fname,last_name=lname,email=email,phone_number=phone_num,user_name=Username,password=password,USER_image=imageuserup)
        Updata.save()
        
        return HttpResponseRedirect("/login")
        
    return render(request,"signin.html")



def login(request):
    if request.method == "POST":
        Username = request.POST.get("Uname")
        password = request.POST.get("pass")
        Sdata = Users.objects.filter(user_name=Username, password=password)
        if Sdata:
            userdata=Users.objects.get(user_name=Username,password=password)
            if userdata:
                pro_pic = userdata.USER_image.url
                fname=userdata.first_name
                lname=userdata.last_name
                email=userdata.email
                phone=userdata.phone_number
            print("You Logged In!!")
            request.session["tORf"] = True  
            request.session["username"] = Username
            request.session["profilepic"] = pro_pic
            request.session["frist_name"] = fname
            request.session["last_name"] = lname
            request.session["email"] = email
            request.session["phone_num"] = phone
            return redirect("/")
        else:
            request.session["tORf"] = False
            return redirect("/login")
        
    return render(request, "login.html")



def Dblog(request,link):
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    ele={
        "element":Blogs.objects.get(A_slug=link),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
    }
    return render(request,"Dblog.html",ele)


def search(request):
    s=""
    data=Blogs.objects.all()
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    if request.method=="GET":
        s=request.GET.get("usearch")
        data=Blogs.objects.filter(titel__icontains=s)
        ele={
            "data":data,
            "tORf": tORf,
            "uname": uname,
            "pic":fimg,
        }
    
    return render(request,"search.html",ele)

def blog(request):
    data=Blogs.objects.all()
    page=Paginator(data,1)
    x=request.GET.get("page")
    filan=page.get_page(x)
    
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    
    co=page.num_pages
    
    ele={
        "element":filan,
        "r":range(1,co+1),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
    }
    return render(request,"allblogs.html",ele)


def myprofile(request):
    
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    email = request.session.get("email")
    phone = request.session.get("phone_num")
    
    sblog=Blogs.objects.all()
    
    ele={
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
        "fulname":fname+" "+lname,
        # "lname":lname,
        "email":email,
        "phone":phone,
        "blogs":sblog,
    }
    
    return render(request,"Uprofile.html",ele)

def logout(request):
    request.session.flush()
    return redirect("/")