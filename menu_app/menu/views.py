from django.shortcuts import render

#my imports
from django.http import HttpResponse
from django.template import loader

from .models import MenuItem

# Create your views here.

def index(request):
    menu_item_list = MenuItem.objects.order_by("item_id")
    template = loader.get_template("menu/index.html")
    context = {
        "menu_item_list": menu_item_list,
    }
    return HttpResponse(template.render(context, request))


"""
 def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
 """