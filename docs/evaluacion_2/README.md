# Evaluación N°2 – Evaluación Formativa Unidad 2

Documento de referencia: [`TI3021_U2_EF01_GUIA.docx`](TI3021_U2_EF01_GUIA.docx)
(*Guía de Aprendizaje – Evaluación Formativa – Unidad 2*).

## Datos de la asignatura

| | |
|---|---|
| Asignatura | Programación Orientada a Objeto Seguro (TI3021) |
| Carrera | Analista Programador |
| Unidad | 2 – Implementación de Software Orientado a Objetos en Python |
| Problema (ABP) | *Optimización del Sistema de Gestión Interna en EcoTech Solutions mediante Modelado Orientado a Objetos* |
| Modalidad | Grupal (2 a 3 estudiantes), con rol rotativo de Líder de Proyecto |
| Entrega | Semana 8, vía plataforma AAI (hasta las 23:00 hrs; no se reciben entregas por correo) |

## Criterios de evaluación

- **2.1.1** Implementa la estructura de clases y métodos en Python a partir de un diagrama UML validado.
- **2.1.2** Aplica principios de POO coherentes con el modelo diseñado y sin automatización del código.
- **2.1.3** Emplea librerías oficiales de Python para la conexión a bases de datos según el gestor seleccionado.

## Actividades solicitadas y dónde se evidencian en el repositorio

| Paso | Qué pide la guía | Evidencia en el repositorio |
|---|---|---|
| 1 (2.1.1) | Implementar en Python la totalidad de las clases del UML, respetando asociaciones y herencia | Diagrama de clases en [`../diagramas.md`](../diagramas.md) y clases en `datos/modelos/` (herencia desde `ModelBase`, asociaciones por claves foráneas) |
| 2 (2.1.2) | Encapsulamiento y reutilización de código (evitar duplicación) | `ModelBase` como clase base común y repositorios/servicios reutilizables en `datos/` y `negocio/` |
| 3 (2.1.3) | Conexión a base de datos con librería oficial y prueba de conexión exitosa | `datos/conexion.py` y `python main.py --init-db` |

## Entregables propios de la Evaluación 2

> **Pendiente del equipo:** agregar en esta carpeta el diagrama UML validado en la Unidad 1 (imagen o PDF)
> y cualquier otro material entregado en la Evaluación 2, y verificar que `docs/diagramas.md`
> sea coherente con él.

Esta evaluación es la base de la Evaluación 3: el proyecto actual continúa el mismo modelo,
incorporando ORM Peewee, arquitectura por capas, gestión de usuarios y login.
