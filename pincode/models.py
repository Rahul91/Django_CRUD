from django.db import models

# Create your models here.

class Pincode(models.Model):
	pincode =  models.CharField(max_length=10)
	office_name = models.CharField(max_length=50)
	district_name = models.CharField(max_length=50)
	state_name = models.CharField(max_length=50)


	def __unicode__(self):
		return u'%s' %(self.pincode)