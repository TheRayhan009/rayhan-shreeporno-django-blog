from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from blogs.models import Blogs
from django.core.paginator import Paginator
from signin.models import Users
from userBlogs.models import UBlog
from comments.models import Comment
from UserImages.models import UPImage
from datetime import datetime
from likes.models import Likes
from dislikes.models import DisLikes

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
        "element": UBlog.objects.all().order_by("Udate_of_post").reverse(),
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
    UPcomment=request.POST.get("Ucomment")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    PTslug=UBlog.objects.get(A_slugUserBlog=link).A_slugUserBlog
    CUimage=fimg[6:]
    if request.method=="POST":
        Sdata=Comment(Ucomment=UPcomment,UPBslug=PTslug,Ucomment_image=CUimage,PURname=f"{fname} {lname}")
        Sdata.save()
    comments = comments = Comment.objects.filter(UPBslug=PTslug)
    comments=comments[::-1]
        
    ele={
        "element":UBlog.objects.get(A_slugUserBlog=link),
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
        "com":comments
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
    page=Paginator(data,12)
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
    simg=UPImage.objects.filter(PUname__iexact=fname+" "+lname)
    tliks=0
    tdisliks=0
    for e in simg:
        tliks+=e.Plikes
        tdisliks+=e.Pdislikes
        
    num_of_blogs=len(sblog)
    ele={
        "tORf": tORf,
        "uname": uname,
        "pic":fimg,
        "fulname":fname+" "+lname,
        # "lname":lname,
        "email":email,
        "phone":phone,
        "blogs":sblog,
        "num_of_blogs":num_of_blogs,
        "images":simg,
        "likes":tliks,
        "dislike":tdisliks,
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
        "uname":uname,
    }
    
    return render(request, "postBlog.html", ele)


def image(request):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    
    ele = {
        "tORf": tORf,
        "fulname": f"{fname} {lname}",
        "pic": fimg,
        "uname":uname,
        "ImageData":UPImage.objects.all().order_by("Pdate").reverse(),
    }
    
    return render(request,"image.html",ele)
    
def postimage(request):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    CUimage=fimg[6:]
    if request.method=="POST":
        Uimg = request.FILES.get("image")
        Utitel=request.POST.get("title")
        Udata=UPImage(
            UPimage=Uimg,
            UPtitel=Utitel,
            PUimage=CUimage,
            PUname=f"{fname} {lname}",
        )
        Udata.save()
    
    ele = {
        "tORf": tORf,
        "fulname": f"{fname} {lname}",
        "pic": fimg,
        "uname":uname,
    }
    
    return render(request,"postImage.html",ele)


def edit(request,link):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    
    blog_data=UBlog.objects.get(A_slugUserBlog=link)
    
    if request.method=="POST":
        titel = request.POST.get("blogtitel")
        blog_txt = request.POST.get("blogtxt")
        blog_image = request.FILES.get("blogimg")
        blog_date = request.POST.get("blogdate")
        if "." in blog_date:
            date_object = datetime.strptime(blog_date, "%b. %d, %Y")
        else:
            date_object = datetime.strptime(blog_date, "%B %d, %Y")
        blog_date = date_object.strftime("%Y-%m-%d")
        blog_category = request.POST.get("blogcategory")
        
        blog_data.Utitel=titel
        blog_data.Upost_blog=blog_txt
        if blog_image:
            blog_data.Upost_image=blog_image
        blog_data.Udate_of_post=blog_date
        blog_data.Upost_category=blog_category

        blog_data.save()
        return redirect(f"/blog/{link}")
        
    ele = {
        "tORf": tORf,
        "fulname": f"{fname} {lname}",
        "pic": fimg,
        "uname":uname,
        "blog_data":blog_data,
        
    }
    
    return render(request,"Bedit.html",ele)

def delete(request,link):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    
    blog_data=UBlog.objects.get(A_slugUserBlog=link)
    
    if request.method=="POST":
        userIsSure=request.POST.get("sure")
        userIsNotSure=request.POST.get("notsure")
        if "sure" in request.POST:
            blog_data.delete()
            return redirect(f"/myprofile/")
        elif "notsure" in request.POST:
            return redirect(f"/myprofile/")
        
    ele = {
        "tORf": tORf,
        "fulname": f"{fname} {lname}",
        "pic": fimg,
        "uname":uname,
        
    }
    
    return render(request,"delete.html",ele)

def like(request,link):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    DLUdata=DisLikes.objects.filter(UserName=uname,A_likeSlug=link)
    LUdata=Likes.objects.filter(UserName=uname,A_likeSlug=link)
    imgdata=UPImage.objects.get(A_imageSlug=link)
    if LUdata.exists():
        imgdata.Plikes=imgdata.Plikes - 1
        LUdata.delete()
        imgdata.save()
    else:
        if DLUdata.exists():
            imgdata.Pdislikes=imgdata.Pdislikes - 1
            DLUdata.delete()
            data=Likes(
            UserName=uname,
            A_likeSlug=link,
            )
            data.save()
            imgdata.Plikes=imgdata.Plikes + 1
            imgdata.save()
        else:
            data=Likes(
            UserName=uname,
            A_likeSlug=link,
            )
            data.save()
            imgdata.Plikes=imgdata.Plikes + 1
            imgdata.save()
    
    return redirect("/image")

def dislike(request,link):
    tORf = request.session.get("tORf")
    fname = request.session.get("frist_name")
    lname = request.session.get("last_name")
    fimg = request.session.get("profilepic")
    uname = request.session.get("username")
    LUdata=Likes.objects.filter(UserName=uname,A_likeSlug=link)
    DLUdata=DisLikes.objects.filter(UserName=uname,A_likeSlug=link)
    imgdata=UPImage.objects.get(A_imageSlug=link)
    if DLUdata.exists():
        imgdata.Pdislikes=imgdata.Pdislikes - 1
        DLUdata.delete()
        imgdata.save()
    else:
        if LUdata.exists():
            imgdata.Plikes=imgdata.Plikes - 1
            LUdata.delete()
            data=DisLikes(
            UserName=uname,
            A_likeSlug=link,
            )
            data.save()
            imgdata.Pdislikes=imgdata.Pdislikes + 1
            imgdata.save()
        else:
            data=DisLikes(
            UserName=uname,
            A_likeSlug=link,
            )
            data.save()
            imgdata.Pdislikes=imgdata.Pdislikes + 1
            imgdata.save()
    
    return redirect("/image")

def logout(request):
    request.session.flush()
    return redirect("/")