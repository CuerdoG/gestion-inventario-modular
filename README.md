# Gestión Modular de Inventarios de Servidores (TXT + JSON + SQLite)

Este proyecto es una solución integral para la importación, normalización y persistencia de datos de servidores. Evoluciona el procesamiento básico de archivos planos hacia un sistema modular que permite el intercambio de datos vía JSON y la consulta interactiva mediante una base de datos SQLite.



## Estructura del Proyecto

La solución se divide en tres capas modulares interconectadas:

1.  **Procesamiento (Módulo procesamiento_datos)**: Lee el archivo `inventario.txt`, limpia inconsistencias y valida datos (IPs, SO, etc.).
2.  **Persistencia JSON (`servers_json.py`)**: Intercambio de datos entre el procesamiento inicial y el almacenamiento final.
3.  **Gestión SQLite (`sqlite_servers.py`)**: Capa de base de datos que permite el almacenamiento persistente y la consulta segura de registros.

## Funcionalidades Principales

* **Integración TXT → JSON**: Automatización del volcado de datos procesados a archivos `.json` indentados.
* **Base de Datos Robusta**: Creación dinámica de tablas en SQLite con limpieza de datos previos (`DROP TABLE`).
* **Interfaz de Usuario**: Menú interactivo por consola para gestionar el ciclo de vida de los datos (Crear BDD, Insertar, Consultar).

## Flujo de Datos

El sistema sigue el siguiente flujo lógico:
1. `inventario.txt` --> **Validación Python**
2. **Validación Python** --> `lista_servidores.json`
3. `lista_servidores.json` --> **SQLite (Tabla Servidores)**
4. **SQLite** --> **Consulta de Usuario**

## Instalación y Uso

### Requisitos
* Python 3.x
* Biblioteca `sqlite3` y `json` (incluidas en la librería estándar).

### Ejecución
Para iniciar el gestor de inventarios y acceder al menú, ejecuta el módulo principal:
```bash
py sqlite_servers.py
