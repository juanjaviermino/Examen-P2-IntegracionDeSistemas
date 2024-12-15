from flask import Blueprint, request, jsonify
from .models import Reservation
from . import db
import requests

SOAP_SERVICE_URL = "http://localhost:5000/availability"

api = Blueprint('api', __name__)

@api.route('/reservations', methods=['POST'])
def create_reservation():
    try:
        data = request.get_json()

        # Call the SOAP service to check availability
        soap_request = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
           <soapenv:Body>
              <AvailabilityRequest>
                 <startDate>{data['start_date']}</startDate>
                 <endDate>{data['end_date']}</endDate>
                 <roomType>{data['room_type']}</roomType>
              </AvailabilityRequest>
           </soapenv:Body>
        </soapenv:Envelope>
        """
        headers = {'Content-Type': 'text/xml'}
        soap_response = requests.post(SOAP_SERVICE_URL, data=soap_request, headers=headers)

        if "<Room>" not in soap_response.text:
            return jsonify({"error": "No available rooms for the specified criteria"}), 400

        # Extract RoomID from SOAP response
        room_id_start = soap_response.text.find("<RoomID>") + len("<RoomID>")
        room_id_end = soap_response.text.find("</RoomID>")
        room_number = soap_response.text[room_id_start:room_id_end]

        # Create a new reservation
        new_reservation = Reservation(
            room_number=room_number,
            customer_name=data['customer_name'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            status='confirmed'
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({"message": "Reservation created successfully", "reservation_id": new_reservation.reservation_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    try:
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404
        return jsonify({
            "reservation_id": reservation.reservation_id,
            "room_number": reservation.room_number,
            "customer_name": reservation.customer_name,
            "start_date": reservation.start_date,
            "end_date": reservation.end_date,
            "status": reservation.status
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    try:
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({"message": "Reservation canceled successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
