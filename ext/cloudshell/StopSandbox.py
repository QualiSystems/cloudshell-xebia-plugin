import json


domain = 'Global'
request = HttpRequest(cloudshell_server)
headers = {'Accept': '*/*'}
body = '{"username": "%(username)s", "password": "%(password)s", "domain": "%(domain)s"}' % {"username": cloudshell_server["username"], "password": cloudshell_server["password"], "domain": domain}
response = request.put(context='/api/login', body=body, contentType='application/json', headers=headers)

if response.getStatus() != 200:
    raise Exception("Failed to login to Cloudshell Server")

token = response.getResponse()[1:-1]
headers['Authorization'] = 'Basic ' + token
api = '/api/v1/sandboxes/%(sandbox_id)s/stop' % {"sandbox_id": sandbox_id}
response = request.post(api, body='', headers=headers)

if response.getStatus() != 200:
    raise Exception('Failed to stop sandbox')

print "Sandbox " + sandbox_id + " ended."
