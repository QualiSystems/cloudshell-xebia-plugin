import datetime
import json

def iso8601(value):
    # split seconds to larger units
    seconds = value.total_seconds()
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    days, hours, minutes = map(int, (days, hours, minutes))
    seconds = round(seconds, 6)

    ## build date
    date = ''
    if days:
        date = '%sD' % days

    ## build time
    time = u'T'
    # hours
    bigger_exists = date or hours
    if bigger_exists:
        time += '{:02}H'.format(hours)
    # minutes
    bigger_exists = bigger_exists or minutes
    if bigger_exists:
		time += '{:02}M'.format(minutes)
	  
    return u'P' + date + time

domain = 'Global'
body = '{"username": "%(username)s", "password": "%(password)s", "domain": "%(domain)s"}' % {"username": cloudshell_server["username"], "password": cloudshell_server["password"], "domain": domain}
request = HttpRequest(cloudshell_server)
headers = {'Accept': '*/*'}
response = request.put(context='/api/login', body=body, contentType='application/json', headers=headers)

if response.getStatus() != 200:
    raise Exception("Failed to login to Cloudshell Server")

token = response.getResponse()[1:-1]
headers['Authorization'] = 'Basic ' + token
content = '{"duration": "' + iso8601(datetime.timedelta(minutes=int(duration))).encode('utf8') + '", "name": "' + reservation_name + '"}'
api = '/api/v1/blueprints/{0}/start'.format(blueprint_id)
response = request.post(api, body=content, contentType='application/json', headers=headers)


print response.getStatus()
print response.getResponse()

if response.getStatus() != 200:
    raise Exception('Failed to start sandbox')

reservation = json.loads(response.getResponse())
sandbox_id = reservation["id"]
print 'Started sandbox on cloudshell server. \nSandbox id is ' + sandbox_id