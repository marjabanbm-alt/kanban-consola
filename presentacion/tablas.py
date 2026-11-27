"""Formato de resultados: tablas y vista Kanban."""
from auxiliares import utilidades as u

from . import consola


def mostrar_usuarios(usuarios) -> None:
    consola.mostrar_tabla(
        ["ID", "Usuario", "Nombre", "Email", "Rol", "Activo"],
        [
            (x.id, x.nombre_usuario, x.nombre_completo, x.email, x.rol, u.si_no(x.activo))
            for x in usuarios
        ],
    )


def mostrar_usuarios_basico(usuarios) -> None:
    consola.mostrar_tabla(
        ["ID", "Usuario", "Nombre"],
        [(x.id, x.nombre_usuario, x.nombre_completo) for x in usuarios],
    )


def mostrar_tableros(tableros) -> None:
    consola.mostrar_tabla(
        ["ID", "Título", "Descripción", "Propietario", "Creado"],
        [
            (
                t.id,
                t.titulo,
                t.descripcion or "",
                t.propietario.nombre_usuario,
                t.creado_en.strftime("%Y-%m-%d"),
            )
            for t in tableros
        ],
    )


def mostrar_listas(listas) -> None:
    consola.mostrar_tabla(
        ["ID", "Posición", "Título"], [(x.id, x.posicion, x.titulo) for x in listas]
    )


def _asignado(tarjeta) -> str:
    return tarjeta.asignado_a.nombre_usuario if tarjeta.asignado_a_id else ""


def mostrar_tarjetas(tarjetas) -> None:
    consola.mostrar_tabla(
        ["ID", "Título", "Lista", "Prioridad", "Vence", "Asignado a"],
        [
            (
                t.id,
                t.titulo,
                t.lista.titulo,
                t.prioridad,
                u.formatear_fecha(t.fecha_limite),
                _asignado(t),
            )
            for t in tarjetas
        ],
    )


def mostrar_detalle_tarjeta(t) -> None:
    print(f"  Tarjeta #{t.id}: {t.titulo}")
    print(f"  Lista:       {t.lista.titulo}")
    print(f"  Descripción: {t.descripcion or '-'}")
    print(f"  Prioridad:   {t.prioridad}")
    print(f"  Vence:       {u.formatear_fecha(t.fecha_limite) or '-'}")
    print(f"  Asignado a:  {_asignado(t) or '-'}")


def mostrar_kanban(tablero, columnas) -> None:
    consola.titulo(f"TABLERO #{tablero.id}: {tablero.titulo}")
    if tablero.descripcion:
        print(f" {tablero.descripcion}")
    if not columnas:
        consola.info("El tablero aún no tiene listas.")
        return
    for lista, tarjetas in columnas:
        print(f"\n [{lista.titulo}]  ({len(tarjetas)} tarjeta(s))")
        if not tarjetas:
            print("    (vacía)")
        for t in tarjetas:
            vence = f" | vence {u.formatear_fecha(t.fecha_limite)}" if t.fecha_limite else ""
            asignado = f" | @{_asignado(t)}" if t.asignado_a_id else ""
            print(f"    #{t.id} {t.titulo}  [{t.prioridad}]{vence}{asignado}")
