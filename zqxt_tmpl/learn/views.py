from django.shortcuts import render

# Create your views here.
def home(request):
	string = '123'
	return render(request,'index.html',{'string':string})