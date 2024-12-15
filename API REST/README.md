# API REST - Gestión de Reservaciones

## Descripción
Este servicio permite gestionar reservaciones de habitaciones, incluyendo la creación, consulta y cancelación. Al crear una reservación, el sistema verifica la disponibilidad llamando a un servicio SOAP.

## Requisitos
- Python 3.8+
- PostgreSQL
- Dependencias en `requirements.txt`

## Instalación
1. **Clona este repositorio:**
   ```bash
   git clone <repositorio-url>
   cd <nombre-del-repositorio>
   ```

2. **Crea la base de datos:**  
   Ejecuta el script `database.sql` en tu servidor PostgreSQL. Este servicio está diseñado para trabajar con PostgreSQL.

3. **Crea un archivo `.env`:**  
   Antes de ejecutar el programa, necesitas definir tus propias variables de entorno para la conexión a la base de datos.  
   Crea un archivo llamado `.env` en el directorio raíz del proyecto con las siguientes variables:  
   ```env
   DB_HOST= (El host de tu base de datos)
   DB_PORT=5432
   DB_NAME= (El nombre de tu bdd)
   DB_USER= (El nombre del usuario de tu bdd)
   DB_PASSWORD= (La contraseña para acceder a tu bdd)
   ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Inicia el servidor:**
   ```bash
   python run.py
   ```

El servicio estará disponible en:  
`http://localhost:5001/api`

## Uso
Consulta la sección de pruebas para ejemplos de solicitudes y respuestas API. Asegúrate de que la base de datos esté poblada con los datos dados en el archivo database.sql.

## Endpoints

### **1. Crear una Reservación**
**POST /api/reservations**

**Descripción:** Crea una nueva reservación verificando la disponibilidad a través del servicio SOAP.

**Ejemplo de solicitud:**
```json
{
    "room_type": "Single",
    "customer_name": "Juan Pérez",
    "start_date": "2024-12-15",
    "end_date": "2024-12-20"
}
```

**Ejemplo de respuesta:**
```json
{
    "message": "Reservation created successfully",
    "reservation_id": 1
}
```

---

### **2. Consultar una Reservación**
**GET /api/reservations/<reservation_id>**

**Descripción:** Recupera los detalles de una reservación por su ID.

**Ejemplo de respuesta:**
```json
{
    "reservation_id": 1,
    "room_number": "101",
    "customer_name": "Juan Pérez",
    "start_date": "2024-12-15",
    "end_date": "2024-12-20",
    "status": "confirmed"
}
```

---

### **3. Cancelar una Reservación**
**DELETE /api/reservations/<reservation_id>**

**Descripción:** Cancela una reservación existente por su ID.

**Ejemplo de respuesta:**
```json
{
    "message": "Reservation canceled successfully"
}
