import json
import urllib2
import pprint

API_KEY = 'AIzaSyDCDSuNggEx-ouiWg5hKxPmf3b09SrKRBA'
BASE_URL = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&maxResults=10'
REQUEST_URL = BASE_URL + '&key='+ API_KEY

def data_request(request_url, query):
    URL = request_url + '&q=' + query
    print URL
    req = urllib2.Request(URL)
    response = urllib2.urlopen(req)
    data = response.read()
    return data

data = data_request(REQUEST_URL, 'tricking')
data_dict = json.loads(data)
pprint.pprint(data_dict['items'])
