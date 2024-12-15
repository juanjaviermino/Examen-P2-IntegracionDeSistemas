# Pruebas del Servicio Web SOAP - Consulta de Disponibilidad

Este archivo contiene ejemplos de pruebas que pueden ser utilizadas para validar la funcionalidad del servicio web SOAP. Cada prueba incluye una solicitud SOAP y su respuesta esperada.

## Introducción
El servicio permite consultar la disponibilidad de habitaciones en un rango de fechas específico y para un tipo de habitación particular. A continuación, se presentan tres casos de prueba representativos.

---

## Prueba 1: Disponibilidad de habitación tipo "Single"

**Solicitud:**
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <AvailabilityRequest>
         <startDate>2024-12-15</startDate>
         <endDate>2024-12-16</endDate>
         <roomType>Single</roomType>
      </AvailabilityRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

**Respuesta esperada:**
```xml
<?xml version='1.0' encoding='UTF-8'?>
<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/">
    <ns0:Body>
        <AvailabilityResponse>
            <Room>
                <RoomID>1</RoomID>
                <RoomType>Single</RoomType>
                <AvailableDate>2024-12-15</AvailableDate>
                <Status>available</Status>
            </Room>
        </AvailabilityResponse>
    </ns0:Body>
</ns0:Envelope>
```

---

## Prueba 2: Disponibilidad de habitación tipo "Double"

**Solicitud:**
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <AvailabilityRequest>
         <startDate>2024-12-15</startDate>
         <endDate>2024-12-16</endDate>
         <roomType>Double</roomType>
      </AvailabilityRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

**Respuesta esperada:**
```xml
<?xml version='1.0' encoding='UTF-8'?>
<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/">
    <ns0:Body>
        <AvailabilityResponse>
            <Room>
                <RoomID>3</RoomID>
                <RoomType>Double</RoomType>
                <AvailableDate>2024-12-15</AvailableDate>
                <Status>available</Status>
            </Room>
        </AvailabilityResponse>
    </ns0:Body>
</ns0:Envelope>
```

---

## Prueba 3: Fechas sin disponibilidad

**Solicitud:**
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <AvailabilityRequest>
         <startDate>2024-12-20</startDate>
         <endDate>2024-12-21</endDate>
         <roomType>Single</roomType>
      </AvailabilityRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

**Respuesta esperada:**
```xml
<?xml version='1.0' encoding='UTF-8'?>
<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/">
    <ns0:Body>
        <AvailabilityResponse/>
    </ns0:Body>
</ns0:Envelope>
```
