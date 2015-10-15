import requests
import sys
import os
import time
import re
import urllib
from urlparse import urlparse, parse_qs
from lxml.cssselect import CSSSelector
from lxml.html import fromstring
from slugify import slugify
import datetime
import webbrowser


def select_first_html(html, selector):
  matches = CSSSelector(selector)(fromstring(html))
  if not len(matches):
    return None
  return matches[0]


def select_first(url, selector):
  print "Fetching %s" % url
  html = requests.get(url).text
  return select_first_html(html, selector)


def google_url(search):
  return "https://www.google.com/search?hl=en&q=%s" % urllib.quote(search)


def google_first(search):
  result = select_first(google_url(search), "h3.r a")
  if result is None or len(result) == 0:
    return None
  href = result.attrib["href"]
  q = parse_qs(urlparse(href).query)["q"][0]
  return q


if __name__ == "__main__":

  print "Adding a new talk."

  talk = {
    "Template": "talk",
    "Curator": "sylvinus"
  }
  speaker = {}

  conference = raw_input("Name of the conference? ").lower().strip()
  assert conference
  assert re.search("^[a-z]+$", conference)

  edition = int(raw_input("Year of the conference? [2015] ") or "2015")
  assert edition >= 2012

  talk["Conference"] = "%s-%s" % (conference, edition)

  with open("conferences/%s-%s.md" % (conference, edition), "r") as f:
    conference_data = {line.split(": ")[0]: line.split(": ")[1].strip() for line in f.readlines()}

    print conference_data
    for k in ("Photos", "Name", "Date"):
      assert k in conference_data

  print "Conference: %s on %s" % (conference_data["Name"], conference_data["Date"])

  talk["Filmed"] = conference_data["Date"]
  talk["Date"] = str(datetime.datetime.now())[0:19]

  speaker["Name"] = raw_input("Speaker name? ")

  speaker_twitter = google_first("site:twitter.com %s" % speaker["Name"])

  if speaker_twitter:
    speaker_twitter = re.sub(".*/", "", speaker_twitter)

  speaker["Twitter"] = raw_input("Speaker twitter username? [%s] " % speaker_twitter) or speaker_twitter

  speaker_slug = raw_input("Speaker slug? [%s] " % speaker_twitter) or speaker_twitter
  talk["Author"] = speaker_slug

  if not os.path.isfile("contributors/%s.md" % speaker_slug):
    speaker_github = google_first("site:github.com %s" % speaker["Name"])

    if speaker_github:
      speaker_github = re.sub(".*/", "", speaker_github)

    speaker["Github"] = raw_input("Speaker github username? [%s] " % speaker_github) or speaker_github

    speaker["Oneliner"] = raw_input("Speaker oneliner? ")

    with open("contributors/%s.md" % speaker_slug, "w") as f:
      f.write("\n".join([
        "%s: %s" % (k, v) for k, v in speaker.items() if v.strip()
      ]))

  video = google_first("site:youtube.com %s %s %s" % (conference, edition, speaker["Name"]))
  if video:
    elt_title = select_first(video, "#eow-title")
    if elt_title:
      full_title = elt_title.attrib["title"].encode("utf-8")
      if "%s %s" % (conference, edition) in full_title.lower():
        talk["Video"] = video
        print "Youtube URL: %s" % talk["Video"]

  if not talk.get("Video"):
    talk["Video"] = raw_input("Youtube URL? ")
    full_title = select_first(talk["Video"], "#eow-title").attrib["title"].encode("utf-8")

  assert "/watch?" in talk["Video"]

  talk["Title"] = unicode(" - ".join(full_title.split(" - ")[2:]))
  print "Talk title: %s" % repr(talk["Title"])

  slug = slugify("%s %s" % (speaker["Name"], talk["Title"]))
  print "Slug: %s" % slug

  path = "%s/%s/%s" % (talk["Filmed"][0:4], talk["Filmed"][5:7], slug)

  webbrowser.open(google_url("%s %s %s slides" % (speaker["Name"], conference, edition)))
  talk["Slides"] = raw_input("Talk slides? ")

  talk["Summary"] = raw_input("Talk summary? ")

  talk["Tags"] = raw_input("Talk tags? (comma-separated, e.g. 'golang, dependencies') ")

  talk["Category"] = raw_input("Talk category? (e.g. 'Backend') ")

  webbrowser.open(conference_data["Photos"])
  talk["Image"] = raw_input("Photo URL? (On Flickr, copy Link Address of the Large image) ")

  dirname = os.path.dirname(path)
  if not os.path.isdir(dirname):
    os.mkdir(dirname)

  with open("%s.md" % path, "w") as f:
    f.write("\n".join([
      "%s: %s" % (k, v) for k, v in talk.items() if v.strip()
    ]))

  print "Successfully written Markdown files! Testing in your browser in 5 seconds..."
  time.sleep(5)
  webbrowser.open("http://local.thedotpost.com:8000/%s" % path)
