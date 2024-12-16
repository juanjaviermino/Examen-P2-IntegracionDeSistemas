from flask import Blueprint, request, jsonify
from .models import Room
from . import db

inventory = Blueprint('inventory', __name__)

@inventory.route('/rooms', methods=['POST'])
def register_room():
    try:
        data = request.get_json()

        # Set default status if not provided
        status = data.get('status', 'disponible')

        new_room = Room(
            room_number=data['room_number'],
            room_type=data['room_type'],
            status=status
        )
        db.session.add(new_room)
        db.session.commit()
        return jsonify({"message": "Room registered successfully", "room_id": new_room.room_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@inventory.route('/rooms/<int:room_id>', methods=['PATCH'])
def update_room_status(room_id):
    try:
        data = request.get_json()
        room = Room.query.get(room_id)
        if not room:
            return jsonify({"error": "Room not found"}), 404
        room.status = data['status']
        db.session.commit()
        return jsonify({"message": "Room status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
