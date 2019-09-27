from app import db

class User(db.Model):
    __tablename__ = 'user_id'

    id = db.Column(db.Integer, primary_key=True)
    user_vk_id = db.Column(db.String(50))

    def __init__(self, user_vk_id):
        self.user_vk_id = user_vk_id

    def __repr__(self):
        return "<User(ID='{0}', VK ID='{1}')>".format(
            self.id, self.user_vk_id)

    def serialize(self):
        return {
            'id': self.id,
            'user_vk_id': self.user_vk_id
        }
