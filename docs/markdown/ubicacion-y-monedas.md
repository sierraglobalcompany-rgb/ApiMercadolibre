---
id: "ubicacion-y-monedas"
title: "Ubicación y Monedas"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas"
source_updated_at: "27/03/2025"
captured_at: "2026-10-08T22:54:01.179Z"
sha256: "63f07e5e64b80596edfe0c84e35a7551ec044b9f8761e97093b85260ff6a6061"
---

# Ubicación y Monedas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 27/03/2025  
**Captura:** 2026-10-08T22:54:01.179Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas](https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas)

## Resumen

Agrupa consultas de países, estados, ciudades, códigos postales y monedas disponibles en Mercado Libre.

## Contenido y conceptos documentados

- Los recursos classified_locations permiten recorrer país, estado y ciudad; el ejemplo de país incluye locale, currency_id, separadores y zona horaria.
- La conversión usa from y to y devuelve rate, inv_rate y creation_date; el ejemplo usa el header x-format-new=true.
- La fuente advierte que Chile, Ecuador y Perú no tienen códigos postales locales disponibles por esta API. Para México indica mantener la guía actual de carga de MXN, aunque en ciertos flujos se muestre el símbolo MXN.

## Operaciones de API
## Operaciones de API

### Consultar ciudad

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/{city_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene datos de una ciudad y sus referencias geográficas.

**Parámetros**

- `city_id` (path, obligatorio): ID de ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, state, country y geo_information.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/cities/TUxVQ0NBQjY1MmQ1.

### Listar países de ubicaciones clasificadas

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los países y sus configuraciones regionales y monedas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de id, name, locale y currency_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye CO con es_CO y COP.

### Consultar país

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/{country_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene datos de un país, separadores, zona horaria y estados.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, locale, currency_id, decimal_separator, thousands_separator, time_zone, geo_information y states.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/countries/UY.

### Consultar estado/provincia

**Método:** `GET`  
**Ruta:** `/classified_locations/states/{state_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene un estado y las ciudades asociadas.

**Parámetros**

- `state_id` (path, obligatorio): ID de estado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, country, geo_information y cities.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/states/UY-RO.

### Consultar ubicación por código postal

**Método:** `GET`  
**Ruta:** `/countries/{country_id}/zip_codes/{zip_code}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca ubicación asociada a un código postal de país.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.
- `zip_code` (path, obligatorio): Código postal.

**Solicitud**

No documentado en la fuente.

**Respuesta**

zip_code, city, state y country.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /countries/AR/zip_codes/5000.

### Buscar intervalo de códigos postales

**Método:** `GET`  
**Ruta:** `/country/{country_id}/zip_codes/search_between`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información postal entre dos códigos para un país.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.
- `zip_code_from` (query, obligatorio): Código postal inicial.
- `zip_code_to` (query, obligatorio): Código postal final.

**Solicitud**

No documentado en la fuente.

**Respuesta**

zip_code, city, state, country y extended_attributes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /country/AR/zip_codes/search_between?zip_code_from=5000&zip_code_to=5100.

### Listar monedas

**Método:** `GET`  
**Ruta:** `/currencies/`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista monedas disponibles con descripción, símbolo y decimales.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de id, description, symbol y decimal_places.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currencies/.

### Consultar moneda

**Método:** `GET`  
**Ruta:** `/currencies/{currency_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una moneda.

**Parámetros**

- `currency_id` (path, obligatorio): Código de moneda.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, description, symbol y decimal_places.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currencies/CLP.

### Consultar conversión de monedas

**Método:** `GET`  
**Ruta:** `/currency_conversions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene tasa de cambio y fecha para el par solicitado.

**Parámetros**

- `from` (query, obligatorio): Código de moneda de origen.
- `to` (query, obligatorio): Código de moneda destino.
- `x-format-new` (header): El ejemplo usa true para el formato nuevo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

currency_base, currency_quote, rate, inv_rate y creation_date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currency_conversions/search?from=ARS&to=CLP con x-format-new:true.

### Referencia HTTP GET /classified_locations/states/UY-RO

**Método:** `GET`  
**Ruta:** `/classified_locations/states/UY-RO`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/states/UY-RO. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /currencies/CLP

**Método:** `GET`  
**Ruta:** `/currencies/CLP`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /currencies/CLP. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /classified_locations/countries/UY

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/UY`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/countries/UY. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /countries/AR/zip_codes/5000

**Método:** `GET`  
**Ruta:** `/countries/AR/zip_codes/5000`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /countries/AR/zip_codes/5000. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /country/AR/zip_codes/search_between

**Método:** `GET`  
**Ruta:** `/country/AR/zip_codes/search_between`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /country/AR/zip_codes/search_between. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `zip_code_from` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `zip_code_to` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas](https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas)  
**Captura:** 2026-10-08T22:54:01.179Z
