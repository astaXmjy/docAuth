from django.db import models

class Aadhar(models.Model):
    image=models.ImageField(upload_to='images/')


