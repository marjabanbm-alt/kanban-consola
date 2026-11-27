# Kanban Consola (estilo Trello)

## Integrantes

| Nombre | Rol |
|---|---|
| _Nombre Apellido_ | _Rol_ |
| _Nombre Apellido_ | _Rol_ |
| _Nombre Apellido_ | _Rol_ |

> Reemplazar por los integrantes reales del equipo.

## Descripción general

Aplicación de **consola** multicapa para gestionar proyectos con tableros Kanban, al estilo Trello:

- **Tableros** que contienen **listas** (columnas, p. ej. *Por hacer / En curso / Hecho*).
- **Listas** que contienen **tarjetas** (tareas con descripción, prioridad, fecha límite y usuario asignado).
- **Usuarios** con roles (`admin` y `usuario`) y autenticación obligatoria.

Cada usuario ve y gestiona sus propios tableros; el administrador ve todos y además gestiona los usuarios.

### Cumplimiento de la pauta

| Requisito | Implementación |
|---|---|
| ORM Peewee | `datos/modelos/` (todos heredan de `ModelBase`) |
| Conexión y modelo base | `datos/conexion.py`, `datos/model_base.py` |
| Repositorios con funciones | `datos/repositorio/*_repositorio.py` (`guardar` usa `save()`, listados y búsquedas) |
| CRUD completo desde la interfaz | Usuarios, Tableros, Listas y Tarjetas (`presentacion/*_vista.py`) |
| Gestión de usuarios | Crear, consultar, modificar, deshabilitar/habilitar y restablecer contraseña |
| BCrypt | `negocio/seguridad.py` (solo se guarda el hash) |
| Maskpass | `presentacion/consola.py` → `pedir_password()` |
| Login y restricción de acceso | `presentacion/login_vista.py`, `negocio/auth_servicio.py`, `negocio/sesion.py` |
| Arquitectura por capas | `datos/`, `negocio/`, `presentacion/`, `auxiliares/` |

## Estructura del proyecto

```
.
├── main.py                     # Punto de entrada (Login -> Menú principal)
├── requirements.txt
├── README.md
├── docs/
│   ├── diagramas.md            # UML de clases, ER, capas y flujo de login (Mermaid)
│   └── evaluacion_2/           # Entregables de la Evaluación N°2
├── datos/
│   ├── conexion.py             # Configuración de la base de datos
│   ├── model_base.py           # ModelBase (config compartida)
│   ├── modelos/                # Usuario, Tablero, Lista, Tarjeta
│   ├── repositorio/            # Funciones de acceso a datos por entidad
│   └── sql/                    # crear_tablas.sql, eliminar_tablas.sql, consultas_ejemplo.sql
├── negocio/                    # Reglas de negocio, seguridad (BCrypt) y sesión
├── presentacion/               # Menús, login y captura/presentación de datos
└── auxiliares/                 # Constantes, mensajes, validaciones, configuración, utilidades
```

Flujo de dependencias: `presentacion → negocio → datos`. La capa `auxiliares` es transversal.

## Dependencias

- Python 3.10 o superior
- [peewee](https://docs.peewee-orm.com/) – ORM
- [bcrypt](https://pypi.org/project/bcrypt/) – hash de contraseñas
- [maskpass](https://pypi.org/project/maskpass/) – ocultar la contraseña al escribir

La base de datos es **SQLite** (incluida en Python), por lo que no requiere instalar ningún servidor.

## Instalación

```bash
git clone <URL-DEL-REPOSITORIO>
cd <carpeta-del-repositorio>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Creación de la base de datos

La base de datos (`kanban.db`) se crea **automáticamente** al ejecutar la aplicación por primera vez.
También se puede crear sin abrir la aplicación:

```bash
python main.py --init-db
```

Alternativa con SQL puro (requiere el cliente `sqlite3`):

```bash
sqlite3 kanban.db < datos/sql/crear_tablas.sql
```

Para usar otra ubicación, defina la variable de entorno `KANBAN_DB` (por ejemplo `KANBAN_DB=/ruta/mi.db`).
Los scripts de `datos/sql/` también permiten eliminar las tablas (`eliminar_tablas.sql`) y ver consultas de ejemplo (`consultas_ejemplo.sql`).

## Usuario inicial

Si la tabla de usuarios está vacía, se crea automáticamente un administrador:

| Usuario | Contraseña |
|---|---|
| `admin` | `Admin123*` |

Se recomienda cambiar la contraseña desde **Menú principal → Mi cuenta → Cambiar mi contraseña**.
La contraseña se almacena únicamente como hash BCrypt.

## Ejecución

```bash
python main.py
```

> Ejecute la aplicación en una **terminal real** (cmd, PowerShell, Terminal, bash). `maskpass` puede no funcionar dentro de la consola integrada de algunos IDE.

Flujo de la aplicación:

```
Aplicación → Login → Validación (BCrypt) → Menú principal
```

- En el login se permiten 3 intentos; escribir `salir` como usuario cierra la aplicación.
- No es posible acceder al menú principal sin autenticarse.

### Menú principal

| Opción | Descripción |
|---|---|
| Tableros | Ver vista Kanban, listar, buscar, crear, modificar y eliminar |
| Listas | Listar, buscar, crear, modificar y eliminar listas de un tablero |
| Tarjetas | Listar, ver detalle, buscar, crear, modificar, mover entre listas, eliminar y ver "mis tarjetas" |
| Usuarios *(solo admin)* | Listar, buscar, crear, modificar, deshabilitar/habilitar y restablecer contraseña |
| Mi cuenta | Ver y modificar mis datos, cambiar mi contraseña |
| Cerrar sesión / Salir | Volver al login o terminar |

### Reglas de negocio destacadas

- Contraseñas: mínimo 8 caracteres, con al menos una letra y un número.
- Nombre de usuario y email únicos.
- Los usuarios **se deshabilitan** (no se borran); un usuario deshabilitado no puede iniciar sesión.
- No se puede deshabilitar el propio usuario ni dejar el sistema sin administradores activos.
- Eliminar un tablero elimina sus listas y tarjetas; eliminar una lista elimina sus tarjetas.
- Las tarjetas solo pueden moverse entre listas del mismo tablero.

## Diagramas

Ver [`docs/diagramas.md`](docs/diagramas.md): diagrama de clases UML, modelo entidad-relación, arquitectura por capas y flujo de autenticación.

## Evaluación N°2

La guía de la Evaluación Formativa de la Unidad 2 y su resumen están en [`docs/evaluacion_2/`](docs/evaluacion_2/README.md).
