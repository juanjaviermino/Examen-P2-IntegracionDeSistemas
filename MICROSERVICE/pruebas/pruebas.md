# Pruebas del Microservicio - Gestión de Habitaciones

Este archivo contiene ejemplos de pruebas que pueden ser utilizadas para validar la funcionalidad del microservicio de gestión de habitaciones. Cada prueba incluye una solicitud en formato JSON para cada endpoint y su respuesta esperada en base a los datos de prueba.

## Introducción
El servicio permite gestionar las habitaciones de un sistema hotelero mediante el registro de nuevas habitaciones y la actualización de su estado. A continuación, se presentan ejemplos representativos para validar la funcionalidad.

---

## Prueba 1: Registrar una habitación - Método POST

**Solicitud de Éxito:**
```json
{
    "room_number": "201",
    "room_type": "Suite",
    "status": "disponible"
}
```

**Respuesta esperada: (201)**
```json
{
    "message": "Room registered successfully",
    "room_id": 5
}
```

**Solicitud de Error (Room duplicada):**
```json
{
    "room_number": "101",
    "room_type": "Single",
    "status": "disponible"
}
```

**Respuesta esperada: (400)**
```json
{
    "error": "UNIQUE constraint failed: rooms.room_number"
}
```

---

## Prueba 2: Actualizar el estado de una habitación - Método PATCH

**Solicitud de Éxito:**
```
`http://127.0.0.1:5003/rooms/1`
```

**Body:**
```json
{
    "status": "mantenimiento"
}
```

**Respuesta esperada: (200)**
```json
{
    "message": "Room status updated successfully"
}
```

**Solicitud de Error (Room no encontrada):**
```
`http://127.0.0.1:5003/rooms/99`
```

**Body:**
```json
{
    "status": "mantenimiento"
}
```

**Respuesta esperada: (404)**
```json
{
    "error": "Room not found"
}
```

**Solicitud de Error (Status faltante):**
```
`http://127.0.0.1:5003/rooms/1`
```

**Body:**
```json
{
}
```

**Respuesta esperada: (400)**
```json
{
    "error": "'status' field is required"
}
```

---
