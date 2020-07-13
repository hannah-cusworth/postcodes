from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


class MainView(TemplateView):
	template_name = "postcode_site/index.html"
	def get(self, request):
		context = {"postcode":"Nothing yet..."}
		return render(request, self.template_name, context)

	def post(self, request):
		postcode = request.POST["postcode_input"].strip()
		context = {"postcode": postcode}
		return render(request, self.template_name, context)
