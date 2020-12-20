from run import db
import math
import sys
from seed import seed

if len(sys.argv) > 1:
    total = int(sys.argv[1])
else:
    total = 150

pages = math.ceil(total / 100)
extra_registers = total % 100
print("Pages:{}".format(pages))
max_registers_per_page = 100
start_from_id = 1
print(pages)

db.drop_all()
db.create_all()
db.session.commit()

for p in range(pages):
    print("Starting from id:{} page {}".format(start_from_id, p))
    if p+1 == pages:
        start_from_id = seed(extra_registers, start_from_id)
    else:
        start_from_id = seed(max_registers_per_page, start_from_id)
