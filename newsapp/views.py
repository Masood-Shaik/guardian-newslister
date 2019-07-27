from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def index(req):
    try:
        search_string = req.GET['search_string']
        new_data = get_json(search_string)
        return render(req,'index.html',{'data':new_data})
    except:
        return render(req, 'index.html')


#function takes search string as parameter and returns a json
def get_json(search_string):

    url1 = 'http://content.guardianapis.com/search?api-key=test&q='
    url2='&show-fields=thumbnail,headline&show-tags=keyword&page=1&page-size=10'
    url = url1+search_string+url2
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.content
        my_json = response_json.decode('utf8')
        print(type(my_json))
        data = json.loads(str(my_json))
        new_data = data['response']['results']
        return new_data