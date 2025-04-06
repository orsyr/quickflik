from django.shortcuts import render
from .models import *
import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    # Movie data in the form of an array of objects
    # movie_data = [
    #     {
    #         "name": "John Wick",
    #         "year": "2014"
    #     }, 
    #     {
    #         "name": "The Batman",
    #         "year": "2022"
    #     }, 
    #     {
    #         "name": "Harry Potter",
    #         "year": "2009"
    #     }
    # ]

    movie_data = Movie.objects.all()
    
    return render(request, 'home.html', {"movie": movie_data})


def about(request):
    return render(request, 'about.html', {})

def movie(request, movie_id):
    movie_data = Movie.objects.get(id=movie_id)
    return render(request, 'movie.html', {"movie": movie_data})


def scrapedata(request):

    

    res = requests.get('https://news.ycombinator.com/news')
    #print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')

    def create_custom_hn(links, subtext):
      hn = []
      for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)

        hn.append({'title': title, 'link': href})
      return hn

    hacker_news = (create_custom_hn(links, subtext))

    
    return render(request, 'scrapedata.html', {"hacker":hacker_news})