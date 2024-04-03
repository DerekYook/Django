from django.db import models


# Create your models here.
# Notice( Title, Contents )
class Notice(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField

    # Notice Object라고 나오는 제목을 title로 나타나게 수정
    def __str__(self):
        return self.title
