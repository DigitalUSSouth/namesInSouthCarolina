from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.urls import resolve

class MainPage(View):
    """ Main Page View Controller
    This class works as the main view controller for Names of SC.

    There is the standard GET and POST handler methods as well as
    functions that correlate to their path names in the urls.py
    """
    def get(self, request:dict) -> HttpResponse:
        url_name = resolve(request.path_info).url_name
        if url_name == 'home':
            return self.Home(request) 
        elif url_name == 'map':
            return self.Map(request)
        elif url_name == 'regions':
            return self.Regions(request)
        elif url_name == 'counties':
            return self.Counties(request)
        elif url_name == 'authors':
            return self.Authors(request)
   
    def post(self, request:dict) -> HttpResponse:
        return HttpResponse("POST Response")

    def Home(self, request:dict) -> HttpResponse:
        return render(request, 'display/home.html', {})

    def Map(self, request:dict) -> HttpResponse:
        return render(request, 'display/map.html', {})

    def Regions(self, request:dict) -> HttpResponse:
        return render(request, 'display/regions.html', {})

    def Counties(self, request:dict) -> HttpResponse:
        return render(request, 'display/counties.html', {})

    def Authors(self, request:dict) -> HttpResponse:
        return render(request, 'display/authors.html', {})
