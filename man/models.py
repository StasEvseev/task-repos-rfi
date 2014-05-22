from django.db import models

# Create your models here.

class Man(models.Model):
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    follow_mans = models.ManyToManyField('self')

    def count_followers(self):
    	foll = Man.objects.filter(follow_ids__icontains=self.id)
    	return foll.count()
    count_followers.allow_tags = True

    def count_follow(self):
    	return len(self.follow_ids.split())
    count_follow.allow_tags = True