import requests
import json
import csv
import sys

word = sys.argv[1]
url = "http://127.0.0.1:8000/api/v1/vocabulary/{0}".format(word)
req = requests.get(url).json()
data_format = None

if 'message' in req:
    data_format = '''
    message: {0}
    '''.format(req['message'])

else:
    data_format = '''
Word: {0}\n
short_description: {1}\n
long_description: {2}\n
first_definition: {3}\n
group_definition: {4}\n
'''.format(req['main_word'], req['short_description'], req['long_description'], req['first_definition'], req['group_definition'])

print(data_format)
