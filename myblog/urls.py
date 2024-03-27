'''This third import is used to import the path function'''
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name="blog_posts"),
    path('myposts/', views.userposts, name="userposts"),
    path('create/', views.createpost, name="createpost"),
    path('edit/<slug:editpostslug>', views.editpost, name="edit"),
    path('delete/<slug:deletepostslug>', views.deletepost, name="delete"),
    path('postdetails/<slug:postslug>', views.postdetails, name="postdetails"),
    path('user_postdetails/<slug:postslug>', views.user_postdetails, name="user_postdetails"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
