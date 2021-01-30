import os
import requests

from flask import Flask
from string import Template
HTML_TEMPLATE = Template("""
  <iframe src="https://www.youtube.com/embed/${youtube_id}" frameborder="0" allowfullscreen></iframe>""")


def checkURL(url):
  resp = requests.head(url)
  if(resp.status_code == 200):
    return True
  else:
    return False


api_key = 'AIzaSyCkz_MBLJbd7cNX5A0fvuw7C_IvUCC9PWQ'
search_url = 'https://www.googleapis.com/youtube/v3/search'
app = Flask(__name__)


def search(query):
  request = {
    'part': "snippet",
    'maxResults': 1,
    'safesearch': 'moderate',
    'type': 'video',
    'videoDuration': 'short',
    'videoEmbeddable': 'true',
    'order': 'date',
    'q': query,
    'key': api_key
  }
  response = requests.get(search_url, params=request)
  print(response.text)


def related(videoId):
  request = {
    'part': "snippet",
    'maxResults': 1,
    'safesearch': 'moderate',
    'type': 'video',
    'videoDuration': 'short',
    'videoEmbeddable': 'true',
    'order': 'date',
    'relatedToVideoId': videoId,
    'key': api_key
  }
  response = requests.get(search_url, params=request)
  print(response.text)


@app.route('/')
def homepage():
  vidhtml = HTML_TEMPLATE.substitute(youtube_id='N1jUp1KztJA')
  return """<h1>Rabbithole</h1>""" + vidhtml


@app.route('/videos/<id>')
def videos(id):
  youtube_url = 'https://youtube.com/watch?v={video_id}.'.format(video_id=id)
  if True == checkURL(youtube_url):
    return HTML_TEMPLATE.substitute(youtube_id=id)
  else:
    html = """<h1>Video does not exist. Click here to return!</h1>"""
  return html, 404


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
