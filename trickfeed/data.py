import json
import urllib2
import pprint


def data_request(request_url, query):
    URL = request_url + '&q=' + query
    # print URL
    req = urllib2.Request(URL)
    response = urllib2.urlopen(req)
    data = response.read()
    return data

try:
    from settings_local import REQUEST_URL

    data = data_request(REQUEST_URL, 'tricking')
    data_dict = json.loads(data)
    pprint.pprint(data_dict['items'])

except:
    print 'KEY NOT FOUND.'