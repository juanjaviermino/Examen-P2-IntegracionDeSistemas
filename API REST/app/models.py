from . import db

class Reservation(db.Model):
    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
