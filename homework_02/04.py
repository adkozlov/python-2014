#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import sys
import urllib.request
import json

if __name__ == '__main__':
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&rsz=8' % '%20'.join(sys.stdin.readline().strip().split())
	json_responce = json.loads(urllib.request.urlopen(url).read().decode("utf8"))

	print(set(result['visibleUrl'].split('.')[-1] for result in json_responce['responseData']['results'] if 'visibleUrl' in result))