from django.shortcuts import render

from timeline.models import Event

def index(request):
	return render(request, 'base.html')

def timeline(request):
	events = Event.objects.all()
	return render(request, 'timeline/timeline.html', {
		'events': events,
	})

def definitions(request):
	return render(request, 'timeline/definitions.html')

def history(request):
	return render(request, 'timeline/history.html')

def references(request):
	return render(request, 'timeline/references.html')