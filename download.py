from flickrapi import FlickrAPI
import urllib.request
import requests
from pprint import pprint
from dotenv import load_dotenv
import os, time, sys


load_dotenv()
key = os.environ.get('FRICKR_KEY')
secret = os.environ.get('FRICKR_SECRET')
wait_time = 1

animal_name = sys.argv[1]
save_dir = "../images/" + animal_name

#print('animal_name=',animal_name)
#print('save_dir=',save_dir)
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animal_name,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url = photo['url_q']
    filename = save_dir + '/' + photo['id'] + '.jpg'

    r = requests.get(url, allow_redirects=False, timeout=10)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            f.write(r.content)
    else:
        e = Exception("HTTP status: " + response.status_code)
        raise e
    time.sleep(wait_time)
