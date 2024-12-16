# Proyecto de Integración de Sistemas - Sistema de Gestión Hotelera

## **Descripción General**
Este proyecto implementa un sistema de gestión hotelera distribuido utilizando arquitectura basada en microservicios. Cada servicio está diseñado para manejar una funcionalidad específica del sistema, asegurando modularidad, escalabilidad y facilidad de mantenimiento.

## **Objetivo**
Desarrollar un sistema que permita la gestión integral de las operaciones de un hotel, incluyendo:
1. **Consulta de disponibilidad de habitaciones**.
2. **Gestión de reservas**.
3. **Gestión del inventario de habitaciones**.

El sistema se basa en buenas prácticas de diseño de software, utilizando microservicios independientes que se comunican de manera eficiente y segura.

## **Problemática**
Los sistemas de gestión hotelera suelen estar centralizados y acoplados, lo que dificulta su mantenimiento y escalabilidad. Este proyecto aborda esta problemática mediante la implementación de:
- **Desacoplamiento de funcionalidades** en servicios específicos.
- **Comunicación eficiente** entre servicios utilizando estándares como SOAP y REST.
- **Independencia tecnológica**, permitiendo el despliegue y escalabilidad individual de cada servicio.

## **Servicios Implementados**

### **1. Servicio SOAP - Consulta de Disponibilidad**
**Descripción:** Este servicio permite consultar la disponibilidad de habitaciones en base a tipo, fechas y estado.
- **Tecnología:** SOAP basado en Python (Flask y Zeep).
- **Base de datos:** PostgreSQL.
- **Endpoints:**
  - `POST /availability`: Verifica disponibilidad para un rango de fechas y tipo de habitación.

[Consulta el README del Servicio SOAP para más detalles.](./soap_service/README.md)

---

### **2. API REST - Gestión de Reservas**
**Descripción:** Este servicio gestiona las reservas del sistema. Verifica la disponibilidad utilizando el servicio SOAP antes de confirmar una reserva.
- **Tecnología:** REST API basada en Python (Flask).
- **Base de datos:** PostgreSQL.
- **Endpoints:**
  - `POST /reservations`: Crea una nueva reserva.
  - `GET /reservations/<reservation_id>`: Consulta una reserva específica.
  - `DELETE /reservations/<reservation_id>`: Cancela una reserva existente.

[Consulta el README de la API REST para más detalles.](./api_rest/README.md)

---

### **3. Microservicio - Gestión de Habitaciones**
**Descripción:** Este servicio gestiona el inventario de habitaciones, incluyendo el registro de nuevas habitaciones y la actualización de su estado.
- **Tecnología:** REST API basada en Python (Flask).
- **Base de datos:** PostgreSQL.
- **Endpoints:**
  - `POST /rooms`: Registra una nueva habitación.
  - `PATCH /rooms/<room_id>`: Actualiza el estado de una habitación existente.

[Consulta el README del Microservicio para más detalles.](./microservice/README.md)

---

## **Estructura del Proyecto**
```
.
├── soap_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── database.sql
│   └── README.md
├── api_rest/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── database.sql
│   └── README.md
├── microservice/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── database.sql
│   └── README.md
└── docker-compose.yml
```

## **Instalación y Despliegue**

### **Requisitos Previos**
- Docker y Docker Compose instalados.
- PostgreSQL configurado para cada servicio.

### **Pasos para la Instalación**
1. **Clona este repositorio:**
   ```bash
   git clone <repositorio-url>
   cd <nombre-del-repositorio>
   ```

2. **Configura las bases de datos:**
   Ejecuta los scripts `database.sql` dentro de cada directorio de servicio para configurar las bases de datos necesarias.

3. **Configura los archivos `.env`:**
   Crea archivos `.env` en cada servicio con las variables de entorno requeridas para la conexión a las bases de datos. Ejemplo:
   ```env
   DB_HOST=<host_de_la_bdd>
   DB_PORT=5432
   DB_NAME=<nombre_de_la_bdd>
   DB_USER=<usuario_de_la_bdd>
   DB_PASSWORD=<contraseña_de_la_bdd>
   ```

4. **Construye y ejecuta los contenedores:**
   ```bash
   docker-compose up --build
   ```

### **Acceso a los Servicios**
- **Servicio SOAP:** `http://localhost:5000`
- **API REST:** `http://localhost:5001`
- **Microservicio:** `http://localhost:5003`

## **Pruebas**
Consulta los archivos de pruebas correspondientes en cada directorio de servicio:
- [Pruebas del Servicio SOAP](./soap_service/pruebas.md)
- [Pruebas de la API REST](./api_rest/pruebas.md)
- [Pruebas del Microservicio](./microservice/pruebas.md)

## **Conclusión**
Este proyecto demuestra cómo implementar un sistema distribuido basado en microservicios para la gestión hotelera, resolviendo problemas comunes de escalabilidad y mantenimiento. Si tienes preguntas o necesitas soporte, no dudes en contactarme.
