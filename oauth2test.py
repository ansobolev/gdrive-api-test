#!/usr/bin/env python

import httplib2
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from apiclient.discovery import build

flow = OAuth2WebServerFlow(client_id='1018518188744.apps.googleusercontent.com',
                       client_secret='g7ukDtHQX3Ee2YS0o--4uwvJ',
                       scope='https://www.googleapis.com/auth/drive',
                       redirect_uri='urn:ietf:wg:oauth:2.0:oob')

#retrieve if available
storage = Storage('OAuthcredentials.txt')
credentials = storage.get()

if  credentials is None:
    #step 1
    auth_uri = flow.step1_get_authorize_url() # Redirect the user to auth_uri
    print 'Go to the following link in your browser: ' + auth_uri
    code = raw_input('Enter verification code: ').strip()
    #step 2
    credentials = flow.step2_exchange(code)
else:
    print 'GDrive credentials are still current'

#authorise
http = httplib2.Http()
http = credentials.authorize(http)
print 'Authorisation successfully completed'

#build
service = build('drive', 'v2', http=http)

#store for next time
storage.put(credentials)
