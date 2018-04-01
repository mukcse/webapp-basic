# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

#by default method="get"
form = """
<form method="post">
	What is your birthday?
	<br>
	<label>
		Month
		<input type="text" name="month" value=%(month)s>
	</label>
	<label>
		Day
		<input type="text" name="day" value=%(day)s>
	</label>
	<label>
		Year
		<input type="text" name="year" value=%(year)s>
	</label>	
	<div style="color:red">%(error)s</div>
		 
	<br><br>
	<input type="submit">
</form>
"""

months = ['January',
		  'February',
		  'March',
		  'April',
		  'May',
		  'June',
		  'July',
		  'August',
		  'September',
		  'October',
		  'November',
		  'December']

month_abv = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
	if month:
		key = month[:3].lower()
		return month_abv.get(key)

def valid_day(day):
	if day.isdigit():
		day = int(day)
		if 1 <=day and day<=31:
			return day

def valid_year(year):
	if year.isdigit():
		year = int(year)
		if 1900<=year and year<=2020:
			return year

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form%{"error":error,
									  "month":month,
									  "day":day,
									  "year":year})

	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain' #by default text/html
		self.write_form()

	def post(self):	
		user_month = self.request.get("month")
		user_day = self.request.get("day")
		user_year = self.request.get("year")

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)

		if month and day and year:
			self.response.out.write("Valid")
		else: 			
			self.write_form("Invalid, please try again", user_month, user_day, user_year)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
