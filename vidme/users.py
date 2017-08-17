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

"""All user information should be gotten through this submodule."""

user_cache = {}

def get_user_info(user_id):
	if user_id in user_cache:
		return user_cache[user_id]
	else:
		return fetch_user_info(user_id)

def update_user_info(user_id, info):
	if user_id in user_cache:
		user_info_c = collections.Counter(user_cache[user_id])
		user_info_c.update(info)
	else:
		user_cache[user_id] = info

def fetch_user_info(user_id):
	res = gateway.get("user/{0}", url_args=[user_id])
	
	if res.json()["status"]:
		update_user_info(user_id, res.json()["user"])
		return res.json()["user"]