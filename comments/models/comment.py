from django.db import models

class Comment(models.Model):
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.post", on_delete=models.CASCADE)
    text = models.TextField("comments")
    
    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        
        def __str__(self):
            return f"{self.text}"