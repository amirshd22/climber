from django.db import models

# Create your models here.
class Blogs(models.Model):
    img = models.ImageField(blank=True)
    text = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.text[:100]
        


class PostImage(models.Model):
    post = models.ForeignKey(Blogs, default=None ,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')