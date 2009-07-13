#!/usr/bin/python

# The MIT License
#
# Copyright (c) 2009 Osvaldo Jair Gaxiola Mercado
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''A wrapper library for File Social http://filesocial.com'''

__author__ =  'Jair Gaxiola'
__email__ = 'jyr.gaxiola@gmail.com'
__license__ = 'MIT License'
__version__ = '0.0.1'

from urllib2 import Request, urlopen
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

class Api:
    def __init__(self, filename = None, username = None, password = None, typeUpload = None):
        """
            filename, username and password are required, message is optional and specifies typeUpload 
            0 not publishes them on Twitter, 1 publishes them on Twitter
        """
        
        self.filename = open(filename)
        self.username = username
        self.password = password
        self.typeUpload = int(typeUpload)
        
        if self.typeUpload == 0:
            self.url = 'http://filesocial.com/api/upload'
        else:
            self.url = 'http://filesocial.com/api/uploadAndPost'
        
    def upload(self, message = None):
        self.message = message
        
        register_openers()
        self.params = {'file':self.filename, 'username': self.username, 'password':self.password, 'message':self.message}
        self.data, self.headers = multipart_encode(self.params) 
        self.req = Request(self.url, self.data, self.headers)
        self.result = urlopen(self.req)
        print self.result.read()
    
    def info(self, filename = None):
        self.filename = filename
        self.url = "http://filesocial.com/api/info/file_hash.xml"
        self.info = urlopen(self.url)
        print self.info.read()