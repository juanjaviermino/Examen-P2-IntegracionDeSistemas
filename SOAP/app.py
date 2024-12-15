from flask import Flask, request, Response
from zeep import CachingClient
from lxml import etree
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Conexión a la base de datos
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/availability', methods=['POST'])
def check_availability():
    try:
        # Parse SOAP request
        envelope = etree.fromstring(request.data)
        ns = {'soap': 'http://schemas.xmlsoap.org/soap/envelope/'}
        body = envelope.find('.//soap:Body', ns)

        # Extract parameters
        start_date = body.find('.//startDate').text
        end_date = body.find('.//endDate').text
        room_type = body.find('.//roomType').text

        # Query the database
        conn = connect_db()
        cursor = conn.cursor()
        query = """
            SELECT room_id, room_type, available_date, status 
            FROM availability 
            WHERE available_date BETWEEN %s AND %s 
            AND room_type = %s AND status = 'available'
        """
        cursor.execute(query, (start_date, end_date, room_type))
        rooms = cursor.fetchall()
        conn.close()

        # Build SOAP response
        response_body = etree.Element('AvailabilityResponse')
        for room in rooms:
            room_element = etree.SubElement(response_body, 'Room')
            etree.SubElement(room_element, 'RoomID').text = str(room[0])
            etree.SubElement(room_element, 'RoomType').text = room[1]
            etree.SubElement(room_element, 'AvailableDate').text = room[2].strftime('%Y-%m-%d')
            etree.SubElement(room_element, 'Status').text = room[3]

        # Wrap response in SOAP Envelope
        envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
        body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
        body.append(response_body)
        response_xml = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')

        return Response(response_xml, content_type='text/xml; charset=utf-8')
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
