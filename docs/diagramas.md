# Diagramas del proyecto

Los diagramas están en formato [Mermaid](https://mermaid.js.org/), que GitHub renderiza automáticamente.

## 1. Diagrama de clases UML (modelos ORM)

```mermaid
classDiagram
    class ModelBase {
        <<abstract>>
        +DateTime creado_en
        +DateTime actualizado_en
        +save()
    }
    class Usuario {
        +int id
        +str nombre_usuario [único]
        +str nombre_completo
        +str email [único]
        +str password_hash [BCrypt]
        +str rol
        +bool activo
    }
    class Tablero {
        +int id
        +str titulo
        +str descripcion
        +Usuario propietario
    }
    class Lista {
        +int id
        +str titulo
        +int posicion
        +Tablero tablero
    }
    class Tarjeta {
        +int id
        +str titulo
        +str descripcion
        +str prioridad
        +date fecha_limite
        +int posicion
        +Lista lista
        +Usuario asignado_a
    }
    ModelBase <|-- Usuario
    ModelBase <|-- Tablero
    ModelBase <|-- Lista
    ModelBase <|-- Tarjeta
    Usuario "1" --> "0..*" Tablero : es propietario
    Tablero "1" *-- "0..*" Lista : contiene
    Lista "1" *-- "0..*" Tarjeta : contiene
    Usuario "0..1" <-- "0..*" Tarjeta : asignado a
```

## 2. Modelo entidad-relación

```mermaid
erDiagram
    USUARIOS ||--o{ TABLEROS : "es propietario"
    TABLEROS ||--o{ LISTAS : contiene
    LISTAS ||--o{ TARJETAS : contiene
    USUARIOS |o--o{ TARJETAS : "asignado a"

    USUARIOS {
        int id PK
        varchar nombre_usuario UK
        varchar nombre_completo
        varchar email UK
        varchar password_hash
        varchar rol
        bool activo
    }
    TABLEROS {
        int id PK
        varchar titulo
        text descripcion
        int propietario_id FK
    }
    LISTAS {
        int id PK
        varchar titulo
        int posicion
        int tablero_id FK
    }
    TARJETAS {
        int id PK
        varchar titulo
        text descripcion
        varchar prioridad
        date fecha_limite
        int posicion
        int lista_id FK
        int asignado_a_id FK
    }
```

## 3. Arquitectura por capas

```mermaid
flowchart TB
    subgraph PRES[presentacion]
        P1[login_vista]
        P2[menu_principal]
        P3[usuarios / tableros / listas / tarjetas / cuenta _vista]
    end
    subgraph NEG[negocio]
        N1[auth_servicio]
        N2[usuario / tablero / lista / tarjeta _servicio]
        N3[seguridad - BCrypt]
        N4[sesion]
    end
    subgraph DAT[datos]
        D1[repositorio - funciones]
        D2[modelos - Peewee]
        D3[model_base + conexion]
        D4[(SQLite)]
    end
    AUX[auxiliares: constantes, mensajes, validaciones, utilidades, configuracion]

    PRES --> NEG --> DAT
    D1 --> D2 --> D3 --> D4
    PRES -.usa.-> AUX
    NEG -.usa.-> AUX
    DAT -.usa.-> AUX
```

## 4. Flujo de autenticación

```mermaid
flowchart TD
    A([Inicio de la aplicación]) --> B[Crear tablas y usuario inicial si corresponde]
    B --> C[Pantalla de login]
    C --> D[Ingresar usuario y contraseña con maskpass]
    D --> E{BCrypt: ¿credenciales válidas?}
    E -- No --> F{¿Intentos < 3?}
    F -- Sí --> D
    F -- No --> Z([Fin])
    E -- Sí --> G{¿Usuario activo?}
    G -- No --> F
    G -- Sí --> H[Sesión iniciada]
    H --> I[Menú principal]
    I -- Cerrar sesión --> C
    I -- Salir --> Z
```
