from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional
import psycopg2
import os

def config():
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'tickets_db'),
        'user': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASS', 'postgres'),
        'port': os.getenv('DB_PORT', '5432')
    }

@contextmanager
def establecer_conexion():
    cfg = config()
    conexion = psycopg2.connect(**cfg)
    try:
        yield conexion
    finally:
        conexion.close()

def init_db(): 
    with establecer_conexion() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id SERIAL PRIMARY KEY,
                    descripcion TEXT,
                    prioridad VARCHAR(20),
                    estado VARCHAR(20),
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()

def crear(descripcion, prioridad, estado, fecha: Optional[str] = None):
    with establecer_conexion() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tickets (descripcion, prioridad, estado, fecha)
                VALUES (%s, %s, %s, COALESCE(%s, CURRENT_TIMESTAMP))
                RETURNING id;
                """,
                (descripcion, prioridad, estado, fecha)
            )
            ticket_id = cursor.fetchone()[0]
            conn.commit()
            return ticket_id

def listar():
    with establecer_conexion() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, descripcion, prioridad, estado, fecha FROM tickets;")
            rows = cursor.fetchall()
            return [
                {"id": r[0], "descripcion": r[1], "prioridad": r[2], "estado": r[3], "fecha": r[4]}
                for r in rows
            ]