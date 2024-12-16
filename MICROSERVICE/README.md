# Microservicio - Gestión de Habitaciones

## Descripción
Este servicio permite gestionar las habitaciones de un sistema hotelero, incluyendo el registro de nuevas habitaciones y la actualización de su estado. Es un microservicio independiente que interactúa exclusivamente con la base de datos de inventario.

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
`http://localhost:5003`

## Uso
Consulta la sección de pruebas para ejemplos de solicitudes y respuestas API. Asegúrate de que la base de datos esté poblada con los datos dados en el archivo database.sql.

## Endpoints

### **1. Registrar una Habitación**
**POST /rooms**

**Descripción:** Registra una nueva habitación en el sistema.

**Ejemplo de solicitud:**
```json
{
    "room_number": "201",
    "room_type": "Suite",
    "status": "disponible"
}
```

**Ejemplo de respuesta:**
```json
{
    "message": "Room registered successfully",
    "room_id": 1
}
```

---

### **2. Actualizar el Estado de una Habitación**
**PATCH /rooms/<room_id>**

**Descripción:** Actualiza el estado de una habitación específica por su ID.

**Ejemplo de solicitud:**
```json
{
    "status": "mantenimiento"
}
```

**Ejemplo de respuesta:**
```json
{
    "message": "Room status updated successfully"
}
```

---
