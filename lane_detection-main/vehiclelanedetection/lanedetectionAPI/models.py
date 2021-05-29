from django.db import models

# Create your models here.


class FindLane(models.Model):
    input_img = models.ImageField(upload_to='input_imgs')
    output_img = models.ImageField(upload_to='output_imgs')