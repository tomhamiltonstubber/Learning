from django.shortcuts import render
from django.http import HttpResponse

def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")