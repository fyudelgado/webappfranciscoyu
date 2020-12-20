import unittest
from run import db
from models import User


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def create_user(id, username, image_url, type, link):
        user = User(id, username, image_url, type, link)
        db.session.add(user)
        return user

    @staticmethod
    def get_all():
        return User.query.all()
