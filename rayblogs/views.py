from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from blogs.models import Blogs
from django.core.paginator import Paginator
from signin.models import Users



def home(request):
    
    ele={
        "element": Blogs.objects.all().order_by("date_of_post").reverse()
    }
    
    return render(request,"home.html",ele)

def signin(request):
    
    if request.method=="POST":
        fname=request.POST.get("fristname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        phone_num=request.POST.get("phone")
        Username=request.POST.get("Uname")
        password=request.POST.get("pass")

        Updata=Users.objects.create(first_name=fname,last_name=lname,email=email,phone_number=phone_num,user_name=Username,password=password)
        Updata.save()
        
        return HttpResponseRedirect("/")
        
    return render(request,"signin.html")



def login(request):
    
    if request.method=="POST":
        Username=request.POST.get("Uname")
        password=request.POST.get("pass")

        Sdata=Users.objects.filter(user_name=Username,password=password)
        
        if Sdata:
            print("You LogedIn!!")
        else:
            print("Who are you???")
        
        return HttpResponseRedirect("/")
    return render(request,"login.html")


def Dblog(request,link):
    ele={
        "element":Blogs.objects.get(A_slug=link)
    }
    return render(request,"Dblog.html",ele)


def search(request):
    s=""
    data=Blogs.objects.all()
    if request.method=="GET":
        s=request.GET.get("usearch")
        data=Blogs.objects.filter(titel__icontains=s)
        ele={
            "data":data,
        }
    
    return render(request,"search.html",ele)

def blog(request):
    data=Blogs.objects.all()
    page=Paginator(data,12)
    x=request.GET.get("page")
    filan=page.get_page(x)
    
    co=page.num_pages
    
    ele={
        "element":filan,
        "r":range(1,co+1)
    }
    return render(request,"allblogs.html",ele)


