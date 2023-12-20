from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User, Article, Comment, Category
 
# получение данных из бд
def index(request):
    Category = Category.objects.all()
    return render(request, "index.html", {"Category": Category})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        Category = Category()
        Category.name = request.POST.get("name")
        Category.description = request.POST.get("category")
        Category.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        Category = Category.objects.get(id=id)
 
        if request.method == "POST":
             Category.name = request.POST.get("name")
             Category.description = request.POST.get("category")
             Category.save()
             return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"Category": Category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        Category = Category.objects.get(id=id)
        Category.delete()
        return HttpResponseRedirect("/")
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")