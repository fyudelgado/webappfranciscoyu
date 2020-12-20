from . import BaseTestClass


class TestSeed(BaseTestClass):
    def test_create_user(self):
        user = BaseTestClass.create_user(1, 'fyudelgado', 'https://avatars2.githubusercontent.com/u/2074400?s=400&u=2f8eec2f447f22e71c09052c82f72211c87ba461&v=4', 'User', 'https://github.com/fyudelgado')
        user.save()
        self.assertIsNotNone(user)
        self.assertEqual('fyudelgado', user.username)

