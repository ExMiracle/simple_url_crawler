from typing import List

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from url_finder.forms import URLForm


def index(request):
    context = {'form': URLForm()}
    return render(request, 'index.html', context)


def find_urls(request):
    if not (request.method == "POST" and request.POST):
        return HttpResponseBadRequest

    form = URLForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest

    url = form.cleaned_data['url']
    context = {
        'links': _find_urls(url),
        'original_url': url,
    }
    return render(request, 'found_urls.html', context)


def _find_urls(url: str) -> List[str]:
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = list({link.get('href') for link in soup.find_all('a')})
        return sorted(links)
    # todo: what if there is an error? should return that site is unavailable with a status code
    return []
