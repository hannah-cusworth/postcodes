from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


class MainView(TemplateView):
	template_name = "postcode_site/index.html"
	def get(self, request):
		return render(request, self.template_name)

