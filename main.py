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
        table {
        border : 1px solid black;
        background-color: #ff9999;
        }
        td {
        padding: 8px;
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
        </tbody>
    </table>
    <br>
    <br>
        <div>
            <input type ="submit">
        </div>
</form>
"""
page_footer = """

</html>
"""
welcome_page = """
    <body>
    <h2> Welcome, %(username)s !! </h2>
    </body>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PWD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PWD_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):

    def write_form(self,username_error ="",password_error="",verify_password_error="",email_error=""):
        self.response.write (page_header+form %{'username_error':username_error,
                                                'password_error':password_error,
                                                'verify_password_error':verify_password_error,
                                                'email_error':email_error}+page_footer)
    def get(self):
        self.write_form()

    def post(self):
#  pulls data enterd by the user
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')


        if valid_username(username) and valid_password(password)and valid_email(email)and(password == verify):

            self.redirect('/welcome?username='+username)
        else:
    # dictionary for error messages
            params = {}
# if any of the above fields arent valid - display the error message
            if not valid_username(username):
                params['username_error'] = ("That is not a valid user name")
            else:
                params['username_error'] = ("")
            if not valid_password(password):
                params['password_error'] = ("The password you entered is not valid")
            else:
                params['password_error']  = (" ")
            if not (password == verify):
                params['verify_password_error']  = ("The passwords you entered don't match")
            else:
                params['verify_password_error'] = (" ")
            if not valid_email(email) :
                params['email_error']    = ("Thats not a valid email")
            else:
                params['email_error']    = ("")

            self.write_form(**params)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.write(page_header+welcome_page %{'username':username}+page_footer)
        else:
            self.redirect('/')
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome',WelcomeHandler)
], debug=True)
