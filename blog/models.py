from django.db import models

# Create your models here.
class Blogs(models.Model):
    img = models.ImageField(upload_to='images/')
    text = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateField()


    def summary(self):
        return self.text[:100]
        