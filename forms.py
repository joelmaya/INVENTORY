from django import forms
from . models import order,product


class OrderForm(forms.ModelForm):
	Export_to_csv = forms.BooleanField(required = False)
	
	class Meta:
		model = order
		fields = "__all__"
		exclude = ['date']

class OrderUpdateForm(forms.ModelForm):
	class Meta:
		model = order
		fields = ['product','quantity']


class IssueForm(forms.ModelForm):

	class Meta:
		model= order
		fields =['product', 'Issue_quantity']
		
