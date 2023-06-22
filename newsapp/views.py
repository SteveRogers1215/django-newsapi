from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    #Initialize
    newsapi = NewsApiClient(api_key = '769aa079da8546bfb53169058e4e40b4')
    top = newsapi.get_top_headlines(sources = 'reuters' )

    n = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(n)):
        f = n[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    newsList = zip(news, desc, img)

    return render(request, 'index.html', context ={'newsList':newsList})
