#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import re


form="""

<h1> Signup</h1>
<form method ="post">
    <table>
        <tbody>
            <tr>
                <td> <label>Username</label> </td>
                <td><input name = "username" type = "text" value =""></td>
                <td style="color:red"></td>
            </tr>
            <tr>
                <td><label>Password </label></td>
                <td><input name = "password" type = "password" value =""></td>
                <td style="color:red "></td>
            </tr>
            <tr>
                <td><label> Verify Password</label></td>
                <td><input name = "verify" type ="password" value =""></td>
                <td style="color:red " ></td>
            </tr>
            <tr>
                <td><label> Email (optional)</label></td>
                <td><input name ="email" type = "email" value =""></td>
                <td style="color:red " ></td>
            </tr>
        </tbody
    </table>
    <br>
    <input type ="submit">
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PWD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PWD_RE.match(password)

#def verify_password():
#    return verify
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    def post(self):
        self.response.write(form)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
