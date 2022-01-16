from django import template
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "__base__.html"

class AddRoom(TemplateView):
    template_name = "add_room.html"