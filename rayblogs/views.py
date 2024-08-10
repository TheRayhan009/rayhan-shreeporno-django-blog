from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from blogs.models import Blogs
from django.core.paginator import Paginator
from signin.models import Users
from userBlogs.models import UBlog


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
        "element": UBlog.objects.all(),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
    }
    return render(request, "home.html", ele)


def signin(request):
    
    if request.method=="POST":
        chak=False
        fname=request.POST.get("fristname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        phone_num=request.POST.get("phone")
        Username=request.POST.get("Uname")
        password=request.POST.get("pass")
        imageuserup=request.FILES.get("upimg")
        if Users.objects.filter(user_name=Username):
            chak=True
            data={
                "chak":chak,
            }
            return render(request,"signin.html",data)
        else:
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
                usersName=userdata.user_name
            request.session["tORf"] = True  
            request.session["username"] = usersName
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
        "element":UBlog.objects.get(A_slugUserBlog=link),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
    }
    return render(request,"Dblog.html",ele)


def search(request):
    s=""
    data=UBlog.objects.all()
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    # fname = request.session.get("frist_name")
    # lname = request.session.get("last_name")
    if request.method=="GET":
        s=request.GET.get("usearch")
        data=UBlog.objects.filter(Utitel__icontains=s)
        ele={
            "data":data,
            "tORf": tORf,
            "uname": uname,
            "pic":fimg,
        }
    
    return render(request,"search.html",ele)

def blog(request):
    data=UBlog.objects.all()
    page=Paginator(data,1)
    x=request.GET.get("page")
    filan=page.get_page(x)
    
    tORf = request.session.get("tORf")
    uname = request.session.get("username")
    fimg = request.session.get("profilepic")
    
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    
    co=page.num_pages
    
    ele={
        "element":filan,
        "r":range(1,co+1),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
        "fulname":fname+" "+lname,
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
    
    
    sblog=UBlog.objects.filter(Uname__iexact=uname)
    
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


def postblog(request):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    fn = fname+" "+lname
    if request.method == "POST":
        titel = request.POST.get("blogtitel")
        blog_txt = request.POST.get("blogtxt")
        blog_image = request.FILES.get("blogimg")
        blog_date = request.POST.get("blogdate")
        blog_category = request.POST.get("blogcategory")
        
        
        UblogDATA = UBlog(
            Utitel=titel,
            Upost_blog=blog_txt,
            Upost_image=blog_image,
            Udate_of_post=blog_date,
            Upost_category=blog_category,
            Uproimage=fimg,  
            Uname=uname,
            UFname=fn,
        )
        UblogDATA.save()

    ele = {
        "tORf": tORf,
        "fulname": f"{fname} {lname}",
        "pic": fimg,
    }
    
    return render(request, "postBlog.html", ele)


def logout(request):
    request.session.flush()
    return redirect("/")