CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(50) NOT NULL UNIQUE,
    room_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('disponible', 'mantenimiento')) DEFAULT 'disponible'
);

-- Datos de prueba
INSERT INTO rooms (room_number, room_type, status)
VALUES
('101', 'Single', 'disponible'),
('102', 'Double', 'mantenimiento'),
('103', 'Suite', 'disponible');
