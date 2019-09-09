import  urllib2
url = "http://www.nostarch.com"

headers = {}
headers['User-Agent'] = 'Googlebot'

request = urllib2.Reqest(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()
