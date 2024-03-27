'''This import is used to import the render function'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.


def blog_posts(request):
    '''This function shows all the blog posts'''
    if request.user.is_authenticated:
        blogposts = BlogPost.objects.order_by('-id')[:6]
        data = {
            'blogposts': blogposts
        }
        return render(request, 'blog.html', data)
    else:
        messages.info(
            request, 'Hey there! Want to read our awesome blog posts? Just log in to get started!')
        return redirect('home')


def postdetails(request, postslug):
    '''This function shows gives a detailed info of a blog post'''
    if request.user.is_authenticated:
        post = BlogPost.objects.get(post_slug=postslug)
        data = {
            'post': post,
        }
        return render(request, 'postdetails.html', data)
    else:
        messages.info(
            request, 'Log in to unlock exclusive blog content!')
        return redirect('home')


def user_postdetails(request, postslug):
    '''This function shows gives a detailed info of a blog post'''
    if request.user.is_authenticated:
        post = BlogPost.objects.get(post_slug=postslug)
        data = {
            'post': post,
        }
        return render(request, 'user_postdetails.html', data)
    else:
        messages.info(
            request, 'To explore the specifics of your blog posts, please log in.')
        return redirect('home')


def userposts(request):
    '''This function shows gives a detailed info of a blog post'''
    if request.user.is_authenticated:
        userposts = BlogPost.objects.filter(post_author=request.user)
        data = {
            'userposts': userposts
        }
        return render(request, 'userposts.html', data)
    else:
        messages.info(request, 'Get access to your blog posts by logging in!')
        return redirect('home')


def createpost(request):
    '''This function shows gives a detailed info of a blog post'''
    userpost_form = BlogPostForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            userpost_form = BlogPostForm(request.POST)
            if userpost_form.is_valid():
                post_author = request.user
                post_title = request.POST.get('post_title')
                post_description = request.POST.get('post_description')
                userpost_data = BlogPost(
                    post_author=post_author, post_title=post_title, post_description=post_description)
                userpost_data.save()
                return redirect('home')
    else:
        messages.info(
            request, 'Create your blog masterpieces by logging in now!')
        return redirect('home')

    data = {                 
        'userpost_form': userpost_form,
    }
    return render(request, 'create.html', data)


def editpost(request, editpostslug):
    if request.user.is_authenticated:
        if request.method == 'GET':
            post_to_edit = BlogPost.objects.get(post_slug=editpostslug)
            editpost_form = BlogPostForm(instance=post_to_edit)
            data = {
                'editpost_form': editpost_form
            }
            return render(request, 'edit.html', data)
        elif request.method == 'POST':
            '''
            In the line below if you don't add or mention the "instance" then, it would just
            create a new 'instance' or 'object' or 'post' and save the info there and wouldn't
            update your pre-existing information of your post.
            '''
            post_to_edit = BlogPost.objects.get(post_slug=editpostslug)
            editpost_form = BlogPostForm(request.POST, instance=post_to_edit)
            if editpost_form.is_valid():
                editpost_form.save()
                return redirect('userposts')
    else:
        messages.info(request, 'Edit your posts by logging in!')
        return redirect('home')


def deletepost(request, deletepostslug):
    if request.user.is_authenticated:
        if request.method == 'GET':
            post_to_delete = BlogPost.objects.get(post_slug=deletepostslug)
            data = {
                'post_to_delete': post_to_delete
            }
            return render(request, 'delete.html', data)
        elif request.method == 'POST':
            post_to_delete = BlogPost.objects.get(post_slug=deletepostslug)
            post_to_delete.delete()
            return redirect('userposts')
    else:
        messages.info(request, 'Log in to remove any posts you do not want!')
        return redirect('home')
