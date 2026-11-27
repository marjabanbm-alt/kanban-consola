"""Constantes globales de la aplicación."""

# Roles
ROL_ADMIN = "admin"
ROL_USUARIO = "usuario"
ROLES = (ROL_ADMIN, ROL_USUARIO)

# Prioridades de tarjetas
PRIORIDADES = ("baja", "media", "alta")
PRIORIDAD_POR_DEFECTO = "media"

# Seguridad
MAX_INTENTOS_LOGIN = 3
PASSWORD_MIN_LARGO = 8
PASSWORD_MAX_BYTES = 72  # límite real de BCrypt

# Usuario inicial (se crea solo si la tabla de usuarios está vacía)
ADMIN_INICIAL_USUARIO = "admin"
ADMIN_INICIAL_PASSWORD = "Admin123*"
ADMIN_INICIAL_NOMBRE = "Administrador"
ADMIN_INICIAL_EMAIL = "admin@kanban.local"

# Formatos
FORMATO_FECHA = "%Y-%m-%d"
ANCHO_PANTALLA = 64
MAX_CELDA_TABLA = 40
