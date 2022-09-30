from django.db import models


class Category(models.Model):
	ismi = models.CharField(max_length=200)


	def __str__(self):
		return self.name


class News(models.Model):
	tittle = models.CharField(max_length=250,null=False,blank=False)
	rasmi = models.ImageField(upload_to='images/',blank=True)
	tekst = models.TextField()
	kategoriy = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title





class Post(models.Model):
	post_nomi = models.CharField(max_length=200)
	post_taf = models.TextField()
