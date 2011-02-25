#!/usr/bin/env python
"""Google Shorten Url Simple Helper

Usage:
	import googl

	Shorten Url:
		print googl.short("http://zeuik.com")
		print googl.shorten("http://zeuik.com")
	
		Retrun all response:
			print googl.short("http://zeuik.com", True)
			print googl.shorten("http://zeuik.com", True)
	
	Expend Url:
		print googl.expend("http://goo.gl/i002")
		
		Return all response:
			print googl.expend("http://goo.gl/i002", True)

	Error example (will return ""):
		print googl.expend("http://zeuik.com")
"""

__author__ = "Zeuxis Lo <http://studio.zeuik.com/>"


import urllib, urllib2

try:
	import json
except ImportError, e:
	import simplejson as json

class GoogleUrlShort(object):
	api_url = "https://www.googleapis.com/urlshortener/v1/url"

	def __init__(self, url):
		self.url = url
		
	def short(self, all_response = False):
		header = { "Content-Type": "application/json" }
		params = { "longUrl": self.url }
		
		try:
			response = urllib2.urlopen(urllib2.Request(self.api_url, json.dumps(params), header))
		except urllib2.HTTPError, e:
			if e.code:
				response = e.fp
		
		json_data = response.read()
		
		if all_response is True:
			return json_data
		else:
			return json.loads(json_data)['id'] if "id" in json_data else ""
		
	def expend(self, all_response = False):
		json_data = urllib.urlopen("https://www.googleapis.com/urlshortener/v1/url?shortUrl=%s" % self.url).read()
		
		if all_response == True:
			return json_data
		else:
			return json.loads(json_data)['longUrl'] if "longUrl" in json_data else ""

def short(*data):
	return shorten(*data)

def shorten(url, all_response = False):
	return GoogleUrlShort(url).short(all_response)

def expend(url, all_response = False):
	return GoogleUrlShort(url).expend(all_response)