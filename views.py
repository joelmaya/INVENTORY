from django.shortcuts import render,redirect,get_object_or_404
from . forms import OrderForm, OrderUpdateForm, IssueForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from . models import order,product
from django.http import HttpResponse
from django.contrib import messages
import csv




def purchase(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully saved')

			return redirect('invent:home')


	else:
		form = OrderForm()
	context = {
	'form':form
	}
	return render (request, 'stock/order_form.html',context)

class OrderCreateView(LoginRequiredMixin,CreateView):
	model = order
	fields = ['product','quantity', 'delivery_address', 'Telephone', 'currency']


	def form_valid(self,form):

		form.instance.Distributor = self.request.user
		return super().form_valid(form)




def Update(request, pk):
	qs = order.objects.get(id=pk)
	form = OrderUpdateForm(instance=qs)
	if request.method == 'POST':
		form = OrderUpdateForm(request.POST, instance=qs)

		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Updated')

			return redirect('invent:home')


	else:
		form = OrderUpdateForm(instance=qs)
	context = {
	'form':form
	}
	return render (request, 'stock/order_update.html',context)

def delete_view(request, pk):
	query_set = order.objects.get(id=pk)
	if request.method == 'POST':
		query_set.delete()
		messages.success(request, 'Successfully deleted')
		return redirect('invent:home')


	return render(request, 'stock/order_delete.html')




def Issues_view(request, pk):
	QuerySet = order.objects.get(id=pk)
	if request.method == 'POST':
		form = IssueForm(request.POST, instance=QuerySet)
		if form.is_valid():
			instance=form.save(commit=True)
			if instance.quantity >= instance.Issue_quantity:
			    instance.quantity -= instance.Issue_quantity
			    messages.success(request, 'ISSUES SUCCESSFULLY   ' + str(instance.quantity) + str(instance.product) + " is now left in store")
			    instance.save()

			else:
				messages.success(request, 'ISSUES UNSUCCESSFULLY   ' + "  only   " + str(instance.quantity) + "  bag  " + " of " +  str(instance.product) +  " is now left in store")

			return redirect('invent:home')

	else:
		form = IssueForm()
	context = {
	  'form':form,
	  'instance':QuerySet,
	}

	return render(request, 'stock/issues_item.html', context)





