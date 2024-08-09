from django.db import models 

class CreatePost(models.Model):
    title = models.CharField(max_length=100, default="unknown")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title
