from django import forms 
from models import Pincode

class PincodeForm(forms.ModelForm):

	class Meta:
		model = Pincode
		fields = ('pincode', 'office_name', 'district_name', 'state_name')