from . import BaseTestClass

from run import db
from seed import seed
import math
from models import User

class TestSeed(BaseTestClass):
    def test_quantity_records_downloaded_and_saved_are_the_same(self):
        max_records = 100
        pages = math.ceil(max_records / 100)
        extra_registers = max_records % 100
        max_registers_per_page = 100
        start_from_id = 1

        for p in range(pages):
            if p + 1 == pages:
                start_from_id = seed(extra_registers, start_from_id)
            else:
                start_from_id = seed(max_registers_per_page, start_from_id)

        self.assertGreater(start_from_id, 1)


