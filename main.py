"""Punto de entrada: Aplicación -> Login -> Validación -> Menú principal."""
import sys

from auxiliares import configuracion as cfg
from auxiliares import constantes as c
from auxiliares import mensajes as m
from datos import conexion
from negocio import usuario_servicio
from presentacion import consola, login_vista, menu_principal


def inicializar_base_datos() -> None:
    """Crea las tablas (si no existen) y el usuario inicial (si no hay usuarios)."""
    conexion.conectar()
    conexion.crear_tablas()
    if usuario_servicio.crear_usuario_inicial():
        consola.info(
            m.ADMIN_INICIAL_CREADO.format(
                usuario=c.ADMIN_INICIAL_USUARIO, password=c.ADMIN_INICIAL_PASSWORD
            )
        )


def main() -> None:
    try:
        inicializar_base_datos()
        if "--init-db" in sys.argv:
            consola.ok(f"Base de datos lista en: {cfg.RUTA_BD}")
            return

        # Sin login exitoso no se llega al menú principal
        while login_vista.pantalla_login():
            if not menu_principal.ejecutar():
                break
        print(m.HASTA_LUEGO)
    except (KeyboardInterrupt, EOFError):
        print(f"\n{m.HASTA_LUEGO}")
    finally:
        conexion.cerrar()


if __name__ == "__main__":
    main()
