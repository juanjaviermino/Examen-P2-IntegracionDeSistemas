CREATE TABLE availability (
    room_id SERIAL PRIMARY KEY,
    room_type VARCHAR(50) NOT NULL,
    available_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'unavailable'))
);

-- Datos de prueba
INSERT INTO availability (room_type, available_date, status)
VALUES
('Single', '2024-12-15', 'available'),
('Single', '2024-12-16', 'unavailable'),
('Double', '2024-12-15', 'available');
