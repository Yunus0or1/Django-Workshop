from django.db import models

from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,BaseUserManager
)
# Create your models here.

class UserManager(BaseUserManager):

	def create_user(self,email,phone,username,type,password=None,is_active=True,is_staff=False,is_admin=False):
	
		if not email:
			raise ValueError("User must have an email address")
			
		if not phone:
			raise ValueError("User must have an phone number")
			
		if not password:
			raise ValueError("User must set password")
			
		if not username:
			raise ValueError("Must set a username")
		
		user_obj = self.model(
			email = self.normalize_email(email)
			
		)
		
		user_obj.set_password(password)
		user_obj.username = username
		user_obj.phone = phone
		user_obj.type = type
		user_obj.staff  = is_staff
		user_obj.admin  = is_admin
		user_obj.active = is_active
		user_obj.activated = 1
		user_obj.job = "admin"
		user_obj.workplace = "Ybazar"
		user_obj.profile_picture = "profile_pics/all_admin_pic.jpg"
		user_obj.description_of_user = "Just an admin"
		user_obj.save(using = self._db)
		
		return user_obj
		

		
	def create_staff(self,email,username,type,password=None):
		
		user = self.create_user(		
			email,
			username,
			type,
			password=password,
			is_staff  = True
		)
		
	def create_superuser(self,phone,email,username,type,password=None):
		
		user = self.create_user(		
			email,
			phone,
			username,
			type,
			password=password,
			is_staff  = True,
			is_admin = True
		)
	
	
	

class User(AbstractBaseUser):
	
	objects = UserManager()
	
	username =  models.CharField(max_length=250)
	email   =  models.EmailField(max_length=255,unique=True)
	phone   =  models.CharField(max_length=255,unique=True,blank=True)
	active  =  models.BooleanField(default=True)
	admin  =  models.BooleanField(default=False)
	staff  =  models.BooleanField(default=False)
	type = models.CharField(max_length=250)
	job = models.CharField(max_length=250,blank=True)
	workplace = models.CharField(max_length=250,blank=True)
	description_of_user = models.CharField(max_length=250,blank=True)
	attempt_to_login  =  models.IntegerField(default=0)
	activated = models.IntegerField(default=0)
	profile_picture = models.FileField(upload_to='profile_pics/',blank=True)
	
	
	
	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['email','username','type']	
	
	
	def __str__(self):
		return self.email
	
	def get_full_name(self):
		return self.email
		
	def get_short_name(self):
		return self.email 
			
	def has_perm(self,perm,obj=None):
		return True
		
	def has_module_perms(self,app_label ):
		return True
		
	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_staff(self):
		return self.staff
	

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active


class MovieInfo(models.Model):
    movie_name= models.CharField(max_length=200)
    movie_review= models.CharField(max_length=3)
    movie_release_date= models.CharField(max_length=50)
    movie_genre= models.CharField(max_length=50)
    movie_desc= models.TextField(max_length=500)

    def __str__(self):
        return self.movie_name

class MovieInfo_Test(models.Model):
    movie_test= models.CharField(max_length=200)

    def __str__(self):
        return self.movie_test