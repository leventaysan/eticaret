from __future__ import unicode_literals

from django.db import models

# Create your models here.
class products(models.Model):

    products=models.TextField()
    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir lutfen degistirmeyiniz,")
    title = models.CharField(max_length=255, null=True, blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    tags=models.CharField(max_length=20)
    create_date=models.DateTimeField(auto_now_add=True)
    pub_date=models.DateTimeField(auto_now=True)
    view_count=models.IntegerField(default=0)
    enable=models.BooleanField(default=True)
    def __unicode__(self):
        return '{}'.format(self.title)

class mainkategori(models.Model):

    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir lutfen degistirmeyiniz,")
    title = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return '{}'.format(self.title)

class subkategori(models.Model):
    categori=models.ForeignKey(mainkategori,on_delete=models.CASCADE,related_name='categori')
    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir lutfen degistirmeyiniz,")
    title = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return '{}'.format(self.title)