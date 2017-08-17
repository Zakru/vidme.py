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

user_info_cache = {}

def get_user_info(user_id):
	if user_id in user_info_cache:
		return user_info_cache[user_id]
	else:
		return fetch_user_info(user_id)

def update_user_info(user_id, info):
	if user_id in user_info_cache:
		user_info_c = collections.Counter(user_info_cache[user_id])
		user_info_c.update(info)
		user_info_cache[user_id] = dict(user_info_c)
	else:
		user_info_cache[user_id] = info

def fetch_user_info(user_id):
	res = gateway.get("user/{0}", url_args=[user_id])
	
	if res.json()["status"]:
		update_user_info(user_id, res.json()["user"])
		return res.json()["user"]

user_cache = {}

def get_user(user_id):
	if user_id in user_cache:
		return user_cache[user_id]
	else:
		return fetch_user(user_id)

def update_user(user_id, info):
	if user_id in user_cache:
		user_c = collections.Counter(user_cache[user_id].info)
		user_c.update(info)
		user_cache[user_id] = User(dict(user_c))
	else:
		user_cache[user_id] = User(info)

def fetch_user(user_id):
	update_user(user_id, get_user_info(user_id))
	return get_user(user_id)

class User:
	def __init__(self, info):
		self.avatar = info["avatar"]
		self.avatar_ai = info["avatar_ai"]
		self.avatar_url = info["avatar_url"]
		self.bio = info["bio"]
		self.comments_scores = info["comments_scores"]
		self.cover = info["cover"]
		self.cover_ai = info["cover_ai"]
		self.cover_url = info["cover_url"]
		self.displayname = info["displayname"]
		self.follower_count = info["follower_count"]
		self.full_url = info["full_url"]
		self.ga_id = info["ga_id"]
		self.likes_count = info["likes_count"]
		self.username = info["username"]
		self.user_id = info["user_id"]
		self.videos_scores = info["videos_scores"]
		self.video_count = info["video_count"]
		self.video_views = info["video_views"]
		self.watching_count = info["watching_count"]
		
		self.info = info