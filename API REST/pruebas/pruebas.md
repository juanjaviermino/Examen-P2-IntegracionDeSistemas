# Pruebas de la API REST - Gestión de Reservas

Este archivo contiene ejemplos de pruebas que pueden ser utilizadas para validar la funcionalidad de la API Rest. Cada prueba incluye una solicitud en formato JSON para cada endpoint y su respuesta esperada en base a los datos de prueba.

## Introducción
El servicio permite consultar la disponibilidad de habitaciones en un rango de fechas específico y para un tipo de habitación particular. A continuación, se presentan tres casos de prueba representativos.

---

## Prueba 1: Crear una reserva - Método POST

**Solicitud de Éxito:**
```json
{
    "room_type": "Single",
    "customer_name": "Juan Pérez",
    "start_date": "2024-12-15",
    "end_date": "2024-12-20"
}
```

**Respuesta esperada: (201)**
```json
{
    "message": "Reservation created successfully",
    "reservation_id": 5
}
```

**Solicitud de Error:**
```json
{
    "room_type": "Double",
    "customer_name": "Juan Pérez",
    "start_date": "2020-12-15",
    "end_date": "2020-12-20"
}
```

**Respuesta esperada: (400)**
```json
{
    "error": "No available rooms for the specified criteria"
}
```

---

## Prueba 2: Consultar una reserva - Método GET

**Solicitud de Éxito: (id = 1)**
```
`http://127.0.0.1:5001/reservations/1`

```

**Respuesta esperada: (200)**
```json
{
    "customer_name": "John Doe",
    "end_date": "Fri, 20 Dec 2024 00:00:00 GMT",
    "reservation_id": 1,
    "room_number": "101",
    "start_date": "Sun, 15 Dec 2024 00:00:00 GMT",
    "status": "confirmed"
}
```

**Solicitud de Error: (id = 99)**
```
`http://127.0.0.1:5001/reservations/99`

```

**Respuesta esperada: (404)**
```json
{
    "error": "Reservation not found"
}
```

---

## Prueba 3: Eliminar una reserva - Método DELETE

**Solicitud de Éxito: (id = 1)**
```
`http://127.0.0.1:5001/reservations/1`

```

**Respuesta esperada: (200)**
```json
{
    "message": "Reservation canceled successfully"
}
```

**Solicitud de Error: (id = 99)**
```
`http://127.0.0.1:5001/reservations/99`

```

**Respuesta esperada: (404)**
```json
{
    "error": "Reservation not found"
}
```