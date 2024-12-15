# Servicio Web SOAP - Consulta de Disponibilidad

## Descripción
Este servicio permite consultar la disponibilidad de habitaciones en base a tipo, fechas y estado. Responde en formato XML según el estándar SOAP.

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
   python app.py
   ```

El servicio estará disponible en:  
`http://localhost:5000/availability`

## Uso
Consulta la sección de pruebas para ejemplos de solicitudes y respuestas SOAP. Asegúrate de que la base de datos esté poblada con los datos dados en el archio database.sql.
