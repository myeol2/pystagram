from django.db import models

# Create your models here.

class Photo(models.Model):

    # id will be generated automatically (django cares this for you!)
    # id = "idx for discriminating files"
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    # model class의 delete를 override. Field의 delete로 먼저 파일지우고, DB안의 객체 지움 
    def delete(self, *args, **kwargs):
        # 아래 delete는 ImageField의 instance로, 연결된 file을 지운다
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

