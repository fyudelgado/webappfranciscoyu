from run import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String)
    image_url = db.Column('image_url', db.String)
    type = db.Column('type', db.String)
    link = db.Column('link', db.String)

    def __init__(self, id, username, image_url, type, link):
        self.id = id
        self.username = username
        self.image_url = image_url
        self.type = type
        self.link = link

    def __repr__(self):
        return 'User({self.username, self.id, self.image_url, self.type, self.link})'

    def __str__(self):
        return self.username

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_headers():
        return User.__table__.columns.keys()
