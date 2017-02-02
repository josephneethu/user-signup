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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
"""
form="""

<h1> Signup</h1>
<form method ="post">
    <table>
        <tbody>
            <tr>
                <td> <label>Username</label> </td>
                <td><input name = "username" type = "text"></td>
                <td class="error">%(username_error)s</td>
            </tr>
            <tr>
                <td><label>Password </label></td>
                <td><input name = "password" type = "password"></td>
                <td class ="error">%(password_error)s</td>
            </tr>
            <tr>
                <td><label> Verify Password</label></td>
                <td><input name = "verify" type ="password"></td>
                <td class="error">%(verify_password_error)s</td>
            </tr>
            <tr>
                <td><label> Email (optional)</label></td>
                <td><input name ="email" type = "email"></td>
                <td class="error">%(email_error)s</td>
            </tr>
        </tbody
    </table>
    <br>
<input type ="submit">
</form>
"""
page_footer = """
</body>
</html>
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

    def write_form(self,username_error ="",password_error="",verify_password_error="",email_error=""):
        self.response.write(page_header+form+page_footer %{"username_error":username_error,
                                                            "password_error":password_error,
                                                            "verify_password_error":verify_password_error,
                                                            "email_error":email_error
                                                        })
    def get(self):
        self.write_form()

    def post(self):
        flag = False

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')


        if not valid_username(username):
            flag = True

        if not valid_password(password):
            flag = True
        elif password != verify:
            flag = True
        if not valid_email(email):
            flag = True
        if flag :
            self.write_form(page_header+form+page_footer,username_error,password_error,verify_password_error,email_error)
        else:
            self.redirect('/welcome?username='+username)
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("Welcome  " +username)
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome',WelcomeHandler)
], debug=True)
