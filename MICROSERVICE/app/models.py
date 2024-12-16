from . import db

class Room(db.Model):
    __tablename__ = 'rooms'

    room_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False, unique=True)
    room_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='disponible')
