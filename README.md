# Covid South America Dashboard

Proyecto desarrollado con FastAPI que consume datos desde una API
pública de COVID, guarda la información en PostgreSQL y la muestra en
una tabla HTML usando Tailwind.

## Tecnologías

-   Python 3.11.9
-   FastAPI
-   SQLAlchemy
-   PostgreSQL 17
-   HTML + Tailwind (CDN)

## Requisitos

-   Python instalado (3.11.9 o superior)
-   PostgreSQL instalado y en ejecución

## Setup Local

### 1. Clonar el repositorio

``` bash
git clone https://github.com/paillaleoleonfabian/covid-dashboard-fastapi.git
cd covid-dashboard-fastapi
```

### 2. Crear entorno virtual e instalar dependencias

``` bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Variables de entorno

Crear un archivo `.env` en la raíz del proyecto con el siguiente
contenido:

``` env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
COVID_API_URL=https://disease.sh/v3/covid-19/countries
```

También se puede copiar el archivo `.env.example` y renombrarlo a
`.env`.

### 4. Crear base de datos

Crear una base de datos en PostgreSQL con el nombre definido en el
archivo `.env`.

Ejemplo:

``` sql
CREATE DATABASE covid_db;
```

### 5. Ejecutar la aplicación

``` bash
uvicorn app.main:app --reload
```

## Uso

-   Interfaz web: http://localhost:8000/
-   Documentación Swagger: http://localhost:8000/docs

## Refrescar datos

Desde la interfaz web se puede utilizar el botón "Refrescar datos" para
sincronizar la información desde la API pública y actualizar la base de
datos.

Este proceso llama al endpoint:

-   POST /api/countries/refresh

Luego se recarga la vista con los datos actualizados.

## Seguridad

-   El archivo `.env` no se sube al repositorio.
-   No se incluyen credenciales en el código fuente.

## Autor

Fabian Paillaleo


