from django.db import models

class Post(models.Model):
    title = models.CharField(("Name"), max_length=50)
    description = models.TextField("Text")
    photo = models.ImageField( upload_to="Image/")
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return f"{self.title}"
    
    
    
    