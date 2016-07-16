# Create your views here.

from django.http import  HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from models import Session
from django.template import RequestContext
from django.core.urlresolvers import reverse
from bot.iabot import iabot
import datetime


def ask(request):
	numbot = int(request.GET['n'])
	print "num bot is ", numbot
	sbot = iabot()
	response = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")
	response += "</small></div><div class='media-body'><p>"
	response += str(sbot.responde(request.GET['q'], numbot))
	# response = "hola mundo"
	return HttpResponse(response)

def home(request):
    return render_to_response('chat/home.html', { "rang" : range(6)}, context_instance=RequestContext(request))

def interact(request):
	usuario = str(request.GET['n'])
	if usuario is '':
		usuario = "Invitado"
	numbot = int(request.GET['numbot'])
	nombbot = "bot normal"
	if numbot is 2:
		nombbot = "bot Vendedor"
	elif numbot is 3:
		nombbot = "bot Sistema de Atencion al Cliente."
	s = Session(user_name=format(usuario), start_date=datetime.datetime.now(), user_avatar=format(request.GET['img_avatar']))	
	s.save()
	count_data = Session.objects.count()
	n = 5
	if count_data < 5:
		n = count_data
	return render_to_response('chat/interact.html',{'session' : s , 'user_list': Session.objects.all()[count_data - n:], 'numero':count_data, 'total':n, 'nombbot':nombbot, 'numbot':numbot}, context_instance=RequestContext(request))
