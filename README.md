# Kanban Consola (estilo Trello)

## Integrantes

Gabriel Benjamin Bravo Manriquez
Constanza Ilonka Monserrat Sanchez Badilla

> Reemplazar por los integrantes reales del equipo.

## Descripción general

Aplicación de **consola** multicapa para gestionar proyectos con tableros Kanban, al estilo Trello:

- **Tableros** que contienen **listas** (columnas, p. ej. *Por hacer / En curso / Hecho*).
- **Listas** que contienen **tarjetas** (tareas con descripción, prioridad, fecha límite y usuario asignado).
- **Usuarios** con roles (`admin` y `usuario`) y autenticación obligatoria.

## Usuario inicial

Si la tabla de usuarios está vacía, se crea automáticamente un administrador:

| Usuario | Contraseña |
| `admin` | `Admin123*` |

### Reglas de negocio destacadas

- Contraseñas: mínimo 8 caracteres, con al menos una letra y un número.
- Nombre de usuario y email únicos.
- Los usuarios **se deshabilitan** (no se borran); un usuario deshabilitado no puede iniciar sesión.
- No se puede deshabilitar el propio usuario ni dejar el sistema sin administradores activos.
- Eliminar un tablero elimina sus listas y tarjetas; eliminar una lista elimina sus tarjetas.
- Las tarjetas solo pueden moverse entre listas del mismo tablero.
