from django.http import HttpResponse
from django.shortcuts import render
    
def base(request):
    return render (request, ' base/base.html' )

def site_map(request):
	return render(request,'sitemap.xml')

