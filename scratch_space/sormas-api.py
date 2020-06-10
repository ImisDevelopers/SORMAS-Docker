import json
from datetime import datetime
from uuid import uuid4

import requests

rest = "https://sormas-docker-test.com/sormas-rest/"

s = requests.Session()
s.verify = False
s.auth = ('SurvOff', 'SurvOff')

now = '%s'.format(datetime.utcnow())
uuid = '%s'.format(uuid4())

payload = [
    {
        "creationDate": now,
        "changeDate": now,
        "uuid": uuid,
        "firstName": "FirstName",
        "lastName": "LastName"
    }
]

p = s.post(rest + '/persons/push', json=json.dumps(payload))
print(p.text)
g = s.get(rest + '/persons/uuids')
print(g.text)
