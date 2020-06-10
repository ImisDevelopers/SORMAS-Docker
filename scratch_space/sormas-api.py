import json
from datetime import datetime
from uuid import uuid4
import requests


def gen_entity_dto():
    now = '{}'.format(datetime.utcnow().replace(microsecond=0).isoformat())
    uuid = '{}'.format(uuid4())

    return {
        "creationDate": now,
        "changeDate": now,
        "uuid": uuid,
    }


def main():
    rest = "https://sormas-docker-test.com/sormas-rest/"

    s = requests.Session()
    s.verify = False
    s.auth = ('SurvOff', 'SurvOff')

    person = gen_entity_dto()
    person["firstName"] = "first2"
    person["lastName"] = "last2"

    payload = [person]
    with open('example-person.json','w') as f:
        json.dump(payload,f)
    return
    p = s.post(rest + '/persons/push', json=payload)
    print(p.text)

    # g = s.get(rest + '/persons/uuids')
    # print(g.status_code)

    # q = s.post(rest + '/persons/query', json=[uuid])
    # print(q.text)

    with open('example-case.json', 'rb') as f:
        payload = json.load(f)

    c = s.post(rest + '/cases/push', json=payload)
    print(c.text)

if __name__ == '__main__':
    main()
