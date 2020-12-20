import sys
import requests
import math
from run import db
from models import User


def seed(num_registers, id):
    payload = {'accept': 'application/vnd.github.v3+json', 'since': id, 'per_page': num_registers}
    url = 'https://api.github.com/users'

    print("Payload:{}".format(payload))

    response = requests.get(url, params=payload)


    if response.ok:
        #print("Content: {}".format(response.json()))
        jData = response.json()
        print("The response contains {0} properties".format(len(jData)))
        print("\n")

        for u in jData:
            user = User(username=u['login'], id=u['id'], image_url=u['avatar_url'], type=u['type'], link=u['html_url'])
            db.session.add(user)
            db.session.commit()

        lastid = jData[len(jData)-1]
    return lastid['id']

# print("Number of arguments:{}".format(len(sys.argv)))
# print("Arguments List:{}".format(sys.argv))
# print("Arguments List:{}".format(sys.argv[1:]))

# pages = math.ceil(int(sys.argv[1]) / 100)
# extra_registers = int(sys.argv[1]) % 100
# print("Pages:{}".format(pages))
# max_registers_per_page = 100
# start_from_id = 1
# print(pages)

# db.create_all()
# db.session.commit()

# for p in range(pages):
#     print("Starting from id:{} page {}".format(start_from_id, p))
#     if p+1 == pages:
#         start_from_id = seed(extra_registers, start_from_id)
#     else:
#         start_from_id = seed(max_registers_per_page, start_from_id)

