from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import BlogModel
from .forms import BlogForm
from django.http import Http404
# Create your views here.
def index(request):
    blogs = BlogModel.objects.all()
    return render(request, "blog/index.html", {
        'blogs' : blogs,
    })


def delete(request, item_id):
    blog = get_object_or_404(BlogModel, id=item_id)
    blog.delete()
    return(redirect(reverse('blog:index')))


def blog(request, item_id):
    blog = get_object_or_404(BlogModel, id=item_id)
    return render(request, "blog/blog.html", {
        'blog' : blog
    })



def update(request, item_id):
    try:
        blog = BlogModel.objects.get(id=item_id)
        if request.method == "POST":
            blog.name = request.POST.get("name")
            blog.content = request.POST.get("content")
            blog.creation_date = request.POST.get("creation_date")
            blog.save()
            return(redirect(reverse('blog:blog', kwargs={'item_id' : blog.id})))  
        else:
            form = BlogForm(instance=blog)
            return render(request, "blog/update.html", {
                'form' : form,
                'id' : item_id,
                })
    except blog.DoesNotExist:
        raise Http404("This object does not exist")
    

def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            blog = BlogModel(name = clean["name"],
                              creation_date = clean['creation_date'],
                              content = clean['content'])
            blog.save()
            return(redirect(reverse('blog:blog', kwargs={'item_id' : blog.id})))
    return render(request, "blog/create.html", {
        'form' : BlogForm()
    })
