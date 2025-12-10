CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    prioridad VARCHAR(20),
    estado VARCHAR(20),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);