-- Script de creación de la base de datos (SQLite).
-- Equivale a lo que genera Peewee con db.create_tables().
-- Uso:  sqlite3 kanban.db < datos/sql/crear_tablas.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
    id              INTEGER      NOT NULL PRIMARY KEY,
    creado_en       DATETIME     NOT NULL,
    actualizado_en  DATETIME     NOT NULL,
    nombre_usuario  VARCHAR(30)  NOT NULL UNIQUE,
    nombre_completo VARCHAR(100) NOT NULL,
    email           VARCHAR(120) NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL,
    rol             VARCHAR(20)  NOT NULL DEFAULT 'usuario',
    activo          INTEGER      NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS tableros (
    id              INTEGER      NOT NULL PRIMARY KEY,
    creado_en       DATETIME     NOT NULL,
    actualizado_en  DATETIME     NOT NULL,
    titulo          VARCHAR(200) NOT NULL,
    descripcion     TEXT,
    propietario_id  INTEGER      NOT NULL,
    FOREIGN KEY (propietario_id) REFERENCES usuarios (id)
);
CREATE INDEX IF NOT EXISTS tablero_propietario_id ON tableros (propietario_id);

CREATE TABLE IF NOT EXISTS listas (
    id              INTEGER      NOT NULL PRIMARY KEY,
    creado_en       DATETIME     NOT NULL,
    actualizado_en  DATETIME     NOT NULL,
    titulo          VARCHAR(200) NOT NULL,
    posicion        INTEGER      NOT NULL DEFAULT 1,
    tablero_id      INTEGER      NOT NULL,
    FOREIGN KEY (tablero_id) REFERENCES tableros (id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS lista_tablero_id ON listas (tablero_id);

CREATE TABLE IF NOT EXISTS tarjetas (
    id              INTEGER      NOT NULL PRIMARY KEY,
    creado_en       DATETIME     NOT NULL,
    actualizado_en  DATETIME     NOT NULL,
    titulo          VARCHAR(200) NOT NULL,
    descripcion     TEXT,
    prioridad       VARCHAR(10)  NOT NULL DEFAULT 'media',
    fecha_limite    DATE,
    posicion        INTEGER      NOT NULL DEFAULT 1,
    lista_id        INTEGER      NOT NULL,
    asignado_a_id   INTEGER,
    FOREIGN KEY (lista_id)      REFERENCES listas (id)    ON DELETE CASCADE,
    FOREIGN KEY (asignado_a_id) REFERENCES usuarios (id)  ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS tarjeta_lista_id ON tarjetas (lista_id);
CREATE INDEX IF NOT EXISTS tarjeta_asignado_a_id ON tarjetas (asignado_a_id);
