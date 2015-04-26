from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from pincode.models import Pincode
from forms import PincodeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


#from haystack.query import SearchQuerySet
# Create your views here.

def pincodes(request):
	args = {}
	args.update(csrf(request))

	args['pincodes'] = Pincode.objects.all()
	return render(request,"pincodes.html", args)


def pincodes_pincode(request):
	args = {}
	args.update(csrf(request))

	args['pincodes'] = Pincode.objects.all().order_by('pincode')
	return render(request,"pincodes.html", args)

def pincodes_state(request):
	args = {}
	args.update(csrf(request))

	args['pincodes'] = Pincode.objects.all().order_by('state_name')
	return render(request,"pincodes.html", args)

def pincodes_district(request):
	args = {}
	args.update(csrf(request))

	args['pincodes'] = Pincode.objects.all().order_by('district_name')
	return render(request,"pincodes.html", args)

'''
def pincode_single(request, pincode_id=1):
	return render(request,"pincode.html", {'pincode' : Pincode.objects.get(id=pincode_id)})
'''

def pincode_single(request, pincode_id=1):
	return render(request,"pincode_single.html", {'pincode' : Pincode.objects.get(id=pincode_id)})

def create(request):
	if request.POST:
		form = PincodeForm(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/pincode/all')

	else:
		form = PincodeForm()

		args ={}
		args.update(csrf(request))

		args['form'] = PincodeForm()
		return render(request, "create_entry.html", args)

'''
def update(request, pincode_id=1):
	if request.POST:
		form = PincodeForm(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/pincode/get/{{ pincode_id }}')

	else:
		form = PincodeForm()

		args ={}
		args.update(csrf(request))

		args['form'] = PincodeForm()
		return render(request, "update_entry.html", args)
		'''

def update(request, pincode_id=1):
	if request.POST:
		form = PincodeForm(request.POST)
		if form.is_valid():
			pincode = form.cleaned_data['pincode']
			office_name = form.cleaned_data['office_name']
			district_name = form.cleaned_data['district_name']
			state_name = form.cleaned_data['state_name']

			new = Pincode.objects.get(id=pincode_id)
			new.pincode = pincode
			new.office_name = office_name
			new.district_name = district_name
			new.state_name = state_name
			new.save()
			
			return HttpResponseRedirect('/pincode/all/')
	else:
		form = PincodeForm()
		args ={}
		args.update(csrf(request))
		args['form'] = PincodeForm()
		
		return render(request,"update_entry.html", args)
'''
def search(request, id):
	args = {}
	args.update(csrf(request))

	args['pincodes'] = Pincode.objects.filter(pincode__contains=id)
	return render(request, "search_items.html",args)


def search_items(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	
	form = PincodeForm()
	args ={}
	args.update(csrf(request))
	args['form'] = PincodeForm()
	return render(request,"search_items.html", args)
'''
def search_pincodes(request):
	if request.mehod == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	pincodes = Pincode.objects.filter(pincode__contains=search_text)
	return render(request, "ajax_search.html", {'pincodes' : pincodes})