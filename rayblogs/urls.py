from django.contrib import admin
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("signin/",views.signin,name="signin"),
    path("login/",views.login,name="signin"),
    path("blog/",views.blog,name="blog"),
    path("blog/<slug:link>",views.Dblog,name="Dblog"),
    path("search/",views.search,name="search"),
    path('logout/', views.logout, name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('postblog/', views.postblog, name='postblog'),
    path('image/', views.image, name='image'),
    path('postimage/', views.postimage, name='postimage'),
    path('edit/<slug:link>', views.edit, name='edit'),
    # path('profile/<str:username>/', views.profile, name='profile'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
