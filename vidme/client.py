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

from . import gateway
import collections

class Client:
	"""
	Client is used to interact with the Vidme API in different ways.
	The Client includes the user ID and the access token used
	to identify the application.
	"""
	authorized = False
	read_only = False
	access_token = ""
	user_id = ""
	
	def __init__(self, client_id):
		"""
		Initialize the Client
		
		:param client_id: The OAuth client ID
		"""
		if len(client_id) != 32:
			raise ValueError("Must provide appropriate OAuth client ID!")
			return
		self.client_id = client_id
	
	def __del__(self):
		if self.authorized:
			raise Exception("Authorization session not closed!")
	
	def authorize(self, key_secret, username, password):
		headers = {"Authorization": key_secret}
		data = {"username": username, "password": password}
		
		res = gateway.post("auth/create", headers=headers, data=data)
		
		if res.json()["status"] == False:
			j = res.json()
			err_msg = str(res.status_code) + " " + j["error"]
			raise Exception(err_msg)
		else:
			j = res.json()
			self.authorized = True
			self.read_only = len(key_secret.split(":")) < 2 or len(key_secret.split(":")[1]) == 0
			self.access_token = j["auth"]["token"]
			self.user_id = j["auth"]["user_id"]
	
	def close(self):
		self.http_post("auth/delete")
		self.authorized = False
		self.read_only = False
		self.access_token = ""
		self.user_id = ""
	
	def http_get(self, url, *, url_args=[], headers={}, data={}):
		if not self.authorized:
			raise ValueError("Must be authorized before using API requests from client!")
			return
		
		headers_c = collections.Counter(headers)
		headers_c.update({"AccessToken": self.access_token})
		headers_f = dict(headers_c)
		return gateway.get(url, url_args=url_args, headers=headers_f, data=data)
	
	def http_post(self, url, *, url_args=[], headers={}, data={}):
		if not self.authorized:
			raise ValueError("Must be authorized before using API requests from client!")
			return
		if self.read_only:
			raise ValueError("Must not be authorized in read-only mode!")
			return
		
		headers_c = collections.Counter(headers)
		headers_c.update({"AccessToken": self.access_token})
		headers_f = dict(headers_c)
		return gateway.post(url, url_args=url_args, headers=headers_f, data=data)
	
	def notifications_list(self):
		if self.read_only:
			raise Exception("Must not be authorized in read-only mode!")
			return
		
		res = self.http_get("notifications")
		
		j = res.json()
		if j["status"] == False:
			err_msg = str(res.status_code) + " " + j["error"]
			raise Exception(err_msg)
			return
		else:
			return j["notifications"]
