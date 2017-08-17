"""
MIT License

Copyright (c) 2017 Zakru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests

url_prefix = "https://api.vid.me/"

def get(url, *args, **kwargs):
	url_f = url
	if "url_args" in kwargs:
		url_f = url.format(*(kwargs["url_args"]))
	
	kwargs.pop("url_args", None)
	return requests.get(url_prefix + url_f, *args, **kwargs)

def post(url, *args, **kwargs):
	url_f = url
	if "url_args" in kwargs:
		url_f = url.format(*(kwargs["url_args"]))
	
	kwargs.pop("url_args", None)
	return requests.post(url_prefix + url_f, *args, **kwargs)
