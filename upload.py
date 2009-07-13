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

__author__ =  'jyr.gaxiola@gmail.com'
__version__ = '0.0.1'


from filesocial import Api
import sys

if len(sys.argv) == 7 or len(sys.argv) < 5:
    print "Usage: \n\t python upload.py \'file\' \'username\' \'password\' \'typeUpload\' \'message\'"
    print "Info:"
    print "\tfilename, username and password are required, message is optional"
    print "\n\ttypeUpload:"
    print "\t\t 0 - not publishes them on Twitter"
    print "\t\t 1 - publishes them on Twitter"
    sys.exit(1)

filename = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
typeUpload = sys.argv[4]

if len(sys.argv) == 6:
    message = sys.argv[5]
else:
    message = ''
    

api = Api(filename, username, password, typeUpload)
query = api.upload(message)