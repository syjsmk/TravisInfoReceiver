__author__ = 'user'

import httplib
import os
# conn = http.client.HTTPConnection("localhost", 8080)
# conn.request("GET", "/api/worker")

branchName = os.environ.get('TRAVIS_BRANCH')
repoSlug = os.environ.get('TRAVIS_REPO_SLUG')

print(os.environ.get('TRAVIS_BRANCH'))
print(os.environ.get('TRAVIS_REPO_SLUG'))

# print('branchName : ' + branchName)
# print('repoSlug : ' + repoSlug)

header = {
   'User-Agent': 'MyClient/1.0.0',
   'Accept': 'application/vnd.travis-ci.2+json',
   'Host': 'api.travis-ci.org'
}
conn = httplib.HTTPSConnection('api.travis-ci.org')
conn.request("GET", "/", headers=header)



response = conn.getresponse()
print('response : ', response.status, response.reason)
data = response.read()
print('data : ', data)