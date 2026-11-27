"""Mensajes reutilizables de la aplicación."""

# --- Generales ---
OPCION_INVALIDA = "Opción no válida. Intente nuevamente."
PRESIONE_ENTER = "\nPresione ENTER para continuar..."
ERROR_INESPERADO = "Ocurrió un error inesperado"
HASTA_LUEGO = "Gracias por usar la aplicación. ¡Hasta luego!"
SIN_RESULTADOS = "No se encontraron registros."
OPERACION_CANCELADA = "Operación cancelada."
SELECCIONE_OPCION = "Seleccione una opción: "

# --- Validaciones ---
CAMPO_OBLIGATORIO = "El campo '{campo}' es obligatorio."
CAMPO_MUY_LARGO = "El campo '{campo}' no puede superar {maximo} caracteres."
NOMBRE_USUARIO_INVALIDO = (
    "El nombre de usuario debe tener entre 3 y 30 caracteres: "
    "letras minúsculas, números, punto o guion bajo."
)
EMAIL_INVALIDO = "El email ingresado no es válido."
PASSWORD_CORTA = "La contraseña debe tener al menos {minimo} caracteres."
PASSWORD_DEBIL = "La contraseña debe incluir al menos una letra y un número."
PASSWORD_MUY_LARGA = "La contraseña es demasiado larga (máximo {maximo} bytes)."
ROL_INVALIDO = "Rol no válido. Opciones: {opciones}."
PRIORIDAD_INVALIDA = "Prioridad no válida. Opciones: {opciones}."
FECHA_INVALIDA = "Fecha no válida. Use el formato AAAA-MM-DD."
ENTERO_INVALIDO = "Debe ingresar un número entero válido."
NUMERO_MINIMO = "El valor debe ser mayor o igual a {minimo}."

# --- Autenticación ---
CREDENCIALES_INVALIDAS = "Usuario o contraseña incorrectos."
USUARIO_DESHABILITADO = "El usuario se encuentra deshabilitado."
NO_AUTENTICADO = "Debe iniciar sesión para realizar esta operación."
SOLO_ADMIN = "Esta operación solo está disponible para administradores."
SIN_PERMISO = "No tiene permisos para acceder a este recurso."
LOGIN_BIENVENIDA = "Bienvenido/a, {nombre}."
LOGIN_BLOQUEADO = "Se superó el número máximo de intentos."
LOGIN_INSTRUCCION = "Ingrese 'salir' como usuario para cerrar la aplicación."
SESION_CERRADA = "Sesión cerrada correctamente."
ADMIN_INICIAL_CREADO = (
    "Se creó el usuario inicial '{usuario}' con la contraseña '{password}'. "
    "Cámbiela desde 'Mi cuenta' después de ingresar."
)

# --- Usuarios ---
USUARIO_NO_ENCONTRADO = "Usuario no encontrado."
USUARIO_DUPLICADO = "Ya existe un usuario con el nombre '{valor}'."
EMAIL_DUPLICADO = "Ya existe un usuario con el email '{valor}'."
USUARIO_CREADO = "Usuario '{valor}' creado correctamente."
USUARIO_MODIFICADO = "Usuario modificado correctamente."
USUARIO_DESHABILITADO_OK = "Usuario deshabilitado correctamente."
USUARIO_HABILITADO_OK = "Usuario habilitado correctamente."
USUARIO_YA_DESHABILITADO = "El usuario ya está deshabilitado."
USUARIO_YA_HABILITADO = "El usuario ya está habilitado."
NO_DESHABILITAR_SELF = "No puede deshabilitar su propio usuario."
ULTIMO_ADMIN = "Debe existir al menos un administrador activo en el sistema."
PASSWORD_ACTUAL_INCORRECTA = "La contraseña actual es incorrecta."
PASSWORD_CAMBIADA = "Contraseña actualizada correctamente."
PASSWORDS_NO_COINCIDEN = "Las contraseñas no coinciden."

# --- Tableros ---
TABLERO_NO_ENCONTRADO = "Tablero no encontrado."
TABLERO_CREADO = "Tablero creado correctamente."
TABLERO_MODIFICADO = "Tablero modificado correctamente."
TABLERO_ELIMINADO = "Tablero eliminado correctamente (incluye sus listas y tarjetas)."

# --- Listas ---
LISTA_NO_ENCONTRADA = "Lista no encontrada."
LISTA_CREADA = "Lista creada correctamente."
LISTA_MODIFICADA = "Lista modificada correctamente."
LISTA_ELIMINADA = "Lista eliminada correctamente (incluye sus tarjetas)."

# --- Tarjetas ---
TARJETA_NO_ENCONTRADA = "Tarjeta no encontrada."
TARJETA_CREADA = "Tarjeta creada correctamente."
TARJETA_MODIFICADA = "Tarjeta modificada correctamente."
TARJETA_ELIMINADA = "Tarjeta eliminada correctamente."
TARJETA_MOVIDA = "Tarjeta movida correctamente."
LISTA_OTRO_TABLERO = "La lista destino pertenece a otro tablero."
ASIGNADO_INVALIDO = "El usuario asignado no existe o está deshabilitado."
