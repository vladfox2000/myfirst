from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import adress, photo
from django.urls import reverse
from .forms import adressForm


def index1(request):
	return render(request, 'book/start.html')


def index(request):
	persons = adress.objects.order_by('first_name')
	return render(request, 'book/list.html', {'persons': persons})


def detail(request, adress_id):
	try:
		a = adress.objects.get( id = adress_id )
	except:
		raise Http404("Пользователь не найден")

	live_photo = a.photo_set.order_by('id')[:10]

	return render(request, 'book/detail.html', {'adress': a, 'live_photo': live_photo})



def live_photo(request, adress_id):
	try:
		a = adress.objects.get( id = adress_id )
	except:
		raise Http404("Пользователь не найден")

	a.photo_set.create(img = request.POST['img'], photo_des = request.POST['des'])

	return HttpResponseRedirect( reverse('book:detail', args = (a.id,)) )

def add_person(request):
	error = ''
	if request.method == 'POST':
		form = adressForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/book')
		else:
			error = 'Неверно заполненная форма'
	form = adressForm()
	list = {
		'form': form,
		'error': error
	}
	return render(request, 'book/new.html', list)
	
