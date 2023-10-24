from django.shortcuts import render, redirect
from django.conf import settings
from .models import PostModel, SecPI1_Model, MastersModel

def beaty_view(request):
    if request.method == "POST":
        img = request.FILES["img"]
        text = request.POST["text"]
        obj_1 = PostModel(img=img, text=text)
        obj_1.save()
        return redirect("beaty")
    obj = PostModel.objects.all()
    sec_img = SecPI1_Model.objects.all()
    return render(request, template_name="index.html", context={"posts":obj, "sec_img":sec_img})


def master_view(request):
    master = MastersModel.objects.all()
    return render(request, template_name="masters.html", context={"master":master})

def contacts_view(request):
    return  render(request, template_name="contacts.html")