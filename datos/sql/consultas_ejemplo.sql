-- Consultas de referencia equivalentes a las de los repositorios.

-- Tableros con su propietario
SELECT t.id, t.titulo, u.nombre_usuario AS propietario
FROM tableros t JOIN usuarios u ON u.id = t.propietario_id
ORDER BY t.id;

-- Vista Kanban de un tablero (reemplazar 1 por el id del tablero)
SELECT l.posicion AS pos_lista, l.titulo AS lista, c.posicion AS pos_tarjeta,
       c.titulo AS tarjeta, c.prioridad, c.fecha_limite, u.nombre_usuario AS asignado_a
FROM listas l
LEFT JOIN tarjetas c ON c.lista_id = l.id
LEFT JOIN usuarios u ON u.id = c.asignado_a_id
WHERE l.tablero_id = 1
ORDER BY l.posicion, c.posicion;

-- Cantidad de tarjetas por lista
SELECT l.titulo, COUNT(c.id) AS total
FROM listas l LEFT JOIN tarjetas c ON c.lista_id = l.id
GROUP BY l.id ORDER BY l.id;

-- Tarjetas con fecha límite vencida
SELECT id, titulo, fecha_limite FROM tarjetas
WHERE fecha_limite IS NOT NULL AND fecha_limite < DATE('now');
