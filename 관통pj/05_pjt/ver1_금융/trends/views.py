from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .foms import KeywordForm

from bs4 import BeautifulSoup
from selenium import webdriver
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np


def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        keyword_form = KeywordForm(request.POST)
        if keyword_form.is_valid():
            keyword_form.save()
            return redirect('trends:keyword')
    else:
        keyword_form = KeywordForm()
    context = {
        'keywords': keywords,
        'keyword_form': keyword_form,
    }
    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    def get_google_data(word):
        url = f'https://www.google.com/search?q={word}'

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_stats = soup.select_one("div#result-stats")
        num = ''
        for i in result_stats.text:
            if i.isdigit():
                num += i
            elif i == '개':
                break
        return num
    

    keywords = Keyword.objects.all()
    for keyword in keywords:
        if Trend.objects.filter(name=keyword.name, search_period='all'):
            trend = Trend.objects.get(name=keyword.name, search_period='all')
            trend.result = get_google_data(keyword.name)
            trend.save()
        else:
            trend = Trend()
            trend.name = keyword.name
            trend.result = get_google_data(keyword.name)
            trend.search_period = 'all'
            trend.save()
    trends = Trend.objects.filter(search_period='all')
    context = {
        'trends': trends
    }
    return render(request, 'trends/crawling.html', context)



def crawling_histogram(request):
    trends_all = Trend.objects.filter(search_period='all')
    name = []
    result = []
    for trend_all in trends_all:
        name.append(trend_all.name)
        result.append(trend_all.result)
    index = np.arange(len(name))
    plt.clf()
    
    plt.figure(figsize=(8,6))
    plt.bar(index, result, label="Trends")
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(index, name, rotation=45)
    plt.grid(True)
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    def get_google_data(word):
        url = f'https://www.google.com/search?q={word}&tbs=qdr:y'

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_stats = soup.select_one("div#result-stats")
        num = ''
        for i in result_stats.text:
            if i.isdigit():
                num += i
            elif i == '개':
                break
        return num

    keywords = Keyword.objects.all()
    for keyword in keywords:
        if Trend.objects.filter(name=keyword.name, search_period='year'):
            trend = Trend.objects.get(name=keyword.name, search_period='year')
            trend.result = get_google_data(keyword.name)
            trend.save()
        else:
            trend_yaer = Trend()
            trend_yaer.name = keyword.name
            trend_yaer.result = get_google_data(keyword.name)
            trend_yaer.search_period = 'year'
            trend_yaer.save()
    
    trends_year = Trend.objects.filter(search_period='year')
    name = []
    result = []
    for trend_year in trends_year:
        name.append(trend_year.name)
        result.append(trend_year.result)
    index = np.arange(len(name))
    plt.clf()
    
    plt.figure(figsize=(8,6))
    plt.bar(index, result, label="Trends")
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(index, name, rotation=45)
    plt.grid(True)
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_advanced.html', context)
