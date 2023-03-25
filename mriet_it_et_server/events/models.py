# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class Student(models.Model):
	name = models.CharField(max_length = 50,null=False)
	father = models.CharField(max_length = 50,null=False)
	roll = models.CharField(max_length=12,unique=True,null=False)
	college = models.CharField(max_length = 100,null=False)
	branchNyear = models.CharField(max_length = 50,null=False)
	email = models.EmailField()
	wanumber = models.BigIntegerField(null=False)
	paper = models.BooleanField(default=False)
	poster = models.BooleanField(default=False)
	codigo = models.BooleanField(default=False)
	expo = models.BooleanField(default=False)
	quiz = models.BooleanField(default=False)
	treasure = models.BooleanField(default=False)
	short = models.BooleanField(default=False)
	conn = models.BooleanField(default=False)
	circuit = models.BooleanField(default=False)
	tinker = models.BooleanField(default=False)
	logo = models.BooleanField(default=False)
	shark = models.BooleanField(default=False)


	def save(self, *args, **kwargs):
		self.roll = self.roll.upper()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.roll

class Payment(models.Model):
	student = models.OneToOneField(Student, on_delete=models.CASCADE,unique=True)
	total = models.IntegerField()
	paid = models.IntegerField(default=0)
	cash = models.BooleanField(default=False)
	verifiedBy = models.CharField(max_length=12,null=False,default="#")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if self.student.college == "MRIET":
			self.total = self.total/2
		super().save(*args, **kwargs)

	def __str__(self):
		return self.student.roll


from django.contrib.auth.models import User
class Stu_Coordinator(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	startyear=models.PositiveIntegerField(default=2020)
	dob=models.DateField(auto_now_add=True)
	branch=models.CharField(max_length=8, default=False)
	rollno=models.CharField(max_length=10,default=False)

	def save(self, *args, **kwargs):
		self.rollno = self.rollno.upper()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.rollno
