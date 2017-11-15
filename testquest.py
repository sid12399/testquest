import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://instruct.math.lsa.umich.edu/webwork2/ma115-065-f17/')

payload = {'username':'spittie', 'password':"The aston db11 is amazing!"}

r = requests.post('https://instruct.math.lsa.umich.edu/webwork2/ma115-065-f17/', auth=HTTPBasicAuth('spittie', 'The aston db11 is amazing!'))

print (r.url)
