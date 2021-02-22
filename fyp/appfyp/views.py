from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView
from .models import Person

def home (request):
	count = User.objects.count()
	return render(request, 'home.html', {
		'count': count
		})


def contact (request):
	return render(request, 'contact.html')


def About (request):
	return render(request, 'About.html')


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {
		'form': form
		})



class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')


# next one is also there mixed login 

@login_required
def secret_page(request):
	context ={}
	if request.method =='POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
		
	return render(request, 'secret_page.html', context)



# def upload(request):
# 	return render(request,'upload.html')
