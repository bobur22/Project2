from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    img = models.ImageField(upload_to="post/")
    text = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text

class SecPI1_Model(models.Model):
    img = models.ImageField(upload_to="secPI1/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.admin_id.last_name} => {self.img.name}"




class MastersModel(models.Model):
    img = models.ImageField(upload_to="master/")
    text_n = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text_n

# class ContactIMGModel(models.Model):
#     img = models.ImageField(upload_to="contact/")
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#
# class ContactModel(models.Model):
#     contacts = models.CharField(max_length=50)
#     tel_n = models.CharField(max_length=20)
#     text = models.CharField(max_length=40)





