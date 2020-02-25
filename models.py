from django.db import models

class Course(models.Model):
	adcourse=models.CharField(max_length=50)
	basiccourse=models.CharField(max_length=50)
	countryname=models.CharField(max_length=50)
	statename=models.CharField(max_length=50)
	message=models.CharField(max_length=50)
	def __str__(self):
		return "Advance Course:"+self.adcourse +" basiccourse is "+self.basiccourse +" Country "+self.countryname +" Statename is "+self.statename +" Message is "+self.message