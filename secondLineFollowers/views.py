from __future__ import print_function

import webbrowser

from django.conf import settings
from django.shortcuts import render
from requests_oauthlib import OAuth1Session
from django.http import Http404, JsonResponse
from twitter import Api, TwitterError
from json import dumps, loads
from .twitterFollowers import TwitterFollowers


def index(request):
	context = {
		'button': 'Connect Twitter account'
	}
	return render(request, "index.html", context)


def pin(request):
	oauth_client = OAuth1Session(
		settings.CONSUMER_KEY, 
		client_secret=settings.CONSUMER_SECRET, 
		callback_uri='oob'
	)

	try:
		resp = oauth_client.fetch_request_token(
			settings.REQUEST_TOKEN_URL
		)
		request.session['oauth_token'] = resp.get('oauth_token')
		request.session['oauth_token_secret'] = resp.get('oauth_token_secret')
	except ValueError:
		raise Http404

	url = oauth_client.authorization_url(settings.AUTHORIZATION_URL)
	webbrowser.open(url)
	return render(request, "pin.html", {})


def followers(request):
	error = None
	second_line_followers = {}
	pincode = request.POST.get('pin')
	try:
		oauth_client = OAuth1Session(
			settings.CONSUMER_KEY, 
			client_secret=settings.CONSUMER_SECRET,
			resource_owner_key=request.session['oauth_token'],
			resource_owner_secret=request.session['oauth_token_secret'],
			verifier=pincode
		)

		resp = oauth_client.fetch_access_token(settings.ACCESS_TOKEN_URL)
	except Exception:
		return render(request, "followers.html", 
			{'error': 'Problem with pin or communication with twitter'}
		) 
	try:
		oauth_token=resp.get('oauth_token')
		oauth_token_secret=resp.get('oauth_token_secret')
	except Exception:
		raise Http404
	
	try:
		api = Api(
			consumer_key=settings.CONSUMER_KEY, 
			consumer_secret=settings.CONSUMER_SECRET,
			access_token_key=oauth_token,
			access_token_secret=oauth_token_secret
		)

		twitterFollowers = TwitterFollowers(api)
		first_line_followers = twitterFollowers.getFollowers(None)
		second_line_followers = twitterFollowers.getSecondLine(first_line_followers)
	except TwitterError as e:
		error = e.message[0].get('message')

	if second_line_followers == {} and error == None:
		raise Http404
	
	request.session['second_line_followers'] = second_line_followers
	return render(
		request, "followers.html", 
		{'secondLineFollowers': second_line_followers, 'error': error}
	)    

def json(request):
	return JsonResponse(request.session['second_line_followers'])	
