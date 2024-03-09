from django.db import models

# Create your models here.
# Data 선정
# 글
# 답글
# 댓글
# 사용자
# 카테고리

# class Topic(models.Model):
#     title = models.CharField(100)
    
#     author = models.ForeignKey("User", on_delete=models.CASCADE, )
    
#     created = models.DateTimeField(auto_add_now=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     content = models.TextField()