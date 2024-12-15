CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    room_number VARCHAR(50) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('confirmed', 'canceled'))
);

-- Datos de prueba
INSERT INTO reservations (room_number, customer_name, start_date, end_date, status)
VALUES
('101', 'John Doe', '2024-12-15', '2024-12-20', 'confirmed'),
('102', 'Jane Smith', '2024-12-16', '2024-12-18', 'confirmed'),
('103', 'Alice Johnson', '2024-12-20', '2024-12-25', 'canceled'),
('104', 'Bob Brown', '2024-12-22', '2024-12-24', 'confirmed');