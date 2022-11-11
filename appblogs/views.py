from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import article



class ArticleList(ListView):
    model = article
    
# Create your views here.
    
def detailspage(request, page_id):
    
    mydata = article.objects.filter(id = page_id).values()
    details = loader.get_template('details.html')
    context = {
        'mybooks' : mydata,
        }
    return HttpResponse(details.render(context,request))

