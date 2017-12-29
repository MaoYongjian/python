from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils import timezone
from .models import Message
# Create your views here.

def index(request):
	context = {'messages':Message.objects.order_by('publish_date')}
	return render(request,'online/index.html',context)

def save(request):
	return render(request,'online/create.html')	

@csrf_exempt
def save(request):
	username = request.POST.get('username','')
	title = request.POST.get('title','')
	content = request.POST.get('content','')
	if username and title and content:
		Message(username=username,title=title,content=content,publish_date=timezone.now()).save()
		return HttpResponseRedirect('/online/')
	else:
		context = {'username':username,'title':title,'content':content,'error':'输入信息不能为空'}
		return render(request,'online/create.html',context)	