#!/usr/bin/env python
import cookielib
import socket
import urllib
import urllib2

url = 'http://eztv.it/'
http_header = {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
                "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
                "Accept-Language" : "en-us,en;q=0.5",
                "Accept-Charset" : "Accept-Charset: windows-1251,utf-8;q=0.7,*;q=0.3",
                "Content-type": "application/x-www-form-urlencoded",
                "Host" : "eztv.it",
                "Referer" : "http://eztv.it/"
                }

params = {
  'SearchString1' : 'How+I+met+your+mother',
  'SearchString' : '',
  'search' : 'Search',
}

# setup socket connection timeout
timeout = 15
socket.setdefaulttimeout(timeout)

# setup cookie handler
cookie_jar = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(cookie_jar)

# setup proxy handler, in case some-day you need to use a proxy server
proxy = {} # example: {"http" : "www.blah.com:8080"}

# create an urllib2 opener()
#opener = urllib2.build_opener(proxy, cookie) # with proxy
opener = urllib2.build_opener(cookie) # we are not going to use proxy now

# create your HTTP request
req = urllib2.Request(url, urllib.urlencode(params), http_header)

# submit your request
res = opener.open(req)
html = res.read()

# save retrieved HTML to file
open("tmp.html", "w").write(html)
print html
