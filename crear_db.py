from conexion import obtener_conexion



# CONEXIÓN A LA BASE DE DATOS


conexion = obtener_conexion()
cursor = conexion.cursor()



# ACTIVAR CLAVES FORÁNEAS


cursor.execute("PRAGMA foreign_keys = ON")



# TABLA: USUARIO


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (
        rol IN ('Admin', 'Operador', 'Conductor')
    )
)
""")



# TABLA: CLIENTE


cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    direccion TEXT
)
""")



# TABLA: CONDUCTOR


cursor.execute("""
CREATE TABLE IF NOT EXISTS conductor (
    id_conductor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    estado TEXT NOT NULL DEFAULT 'Disponible'
)
""")



# TABLA: LLAMADA


cursor.execute("""
CREATE TABLE IF NOT EXISTS llamada (
    id_llamada INTEGER PRIMARY KEY AUTOINCREMENT,
    telefono TEXT NOT NULL,
    motivo TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")



# TABLA: SOLICITUD


cursor.execute("""
CREATE TABLE IF NOT EXISTS solicitud (
    id_solicitud INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    direccion_recogida TEXT NOT NULL,
    destino TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'Pendiente',

    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
        ON DELETE CASCADE
)
""")



# TABLA: SERVICIO


cursor.execute("""
CREATE TABLE IF NOT EXISTS servicio (
    id_servicio INTEGER PRIMARY KEY AUTOINCREMENT,
    id_solicitud INTEGER NOT NULL,
    id_conductor INTEGER NOT NULL,
    estado TEXT NOT NULL DEFAULT 'Activo',
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_solicitud)
        REFERENCES solicitud(id_solicitud)
        ON DELETE CASCADE,

    FOREIGN KEY (id_conductor)
        REFERENCES conductor(id_conductor)
        ON DELETE CASCADE
)
""")



# TABLA: ALERTA


cursor.execute("""
CREATE TABLE IF NOT EXISTS alerta (
    id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_conductor INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    nivel TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_conductor)
        REFERENCES conductor(id_conductor)
        ON DELETE CASCADE
)
""")



# TABLA: ANÁLISIS DE FATIGA


cursor.execute("""
CREATE TABLE IF NOT EXISTS analisis_fatiga (
    id_analisis INTEGER PRIMARY KEY AUTOINCREMENT,
    id_conductor INTEGER NOT NULL,
    parpadeos INTEGER DEFAULT 0,
    bostezos INTEGER DEFAULT 0,
    ojos_cerrados_segundos REAL DEFAULT 0,
    estado_ojos TEXT DEFAULT 'Normal',
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_conductor)
        REFERENCES conductor(id_conductor)
        ON DELETE CASCADE
)
""")



# TABLA: CONFIGURACIÓN DE ALERTAS


cursor.execute("""
CREATE TABLE IF NOT EXISTS configuracion_alerta (
    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_conductor INTEGER NOT NULL,
    tipo_sonido TEXT DEFAULT 'Alarma fuerte',
    volumen INTEGER DEFAULT 50,
    limite_alertas INTEGER DEFAULT 3,

    FOREIGN KEY (id_conductor)
        REFERENCES conductor(id_conductor)
        ON DELETE CASCADE
)
""")



# USUARIOS INICIALES


cursor.execute("""
INSERT OR IGNORE INTO usuario
(usuario, contraseña, rol)
VALUES (?, ?, ?)
""", (
    "admin",
    "admin123",
    "Admin"
))


cursor.execute("""
INSERT OR IGNORE INTO usuario
(usuario, contraseña, rol)
VALUES (?, ?, ?)
""", (
    "operador1",
    "1234",
    "Operador"
))


cursor.execute("""
INSERT OR IGNORE INTO usuario
(usuario, contraseña, rol)
VALUES (?, ?, ?)
""", (
    "conductor1",
    "1234",
    "Conductor"
))



# CONDUCTORES INICIALES


cursor.execute("""
INSERT OR IGNORE INTO conductor
(id_conductor, nombre, telefono, estado)
VALUES (?, ?, ?, ?)
""", (
    1,
    "Juan Pérez",
    "70000001",
    "Disponible"
))


cursor.execute("""
INSERT OR IGNORE INTO conductor
(id_conductor, nombre, telefono, estado)
VALUES (?, ?, ?, ?)
""", (
    2,
    "Carlos López",
    "70000002",
    "Disponible"
))



# CONFIGURACIÓN INICIAL DE ALERTAS


cursor.execute("""
INSERT OR IGNORE INTO configuracion_alerta
(id_conductor, tipo_sonido, volumen, limite_alertas)
VALUES (?, ?, ?, ?)
""", (
    1,
    "Alarma fuerte",
    50,
    3
))


cursor.execute("""
INSERT OR IGNORE INTO configuracion_alerta
(id_conductor, tipo_sonido, volumen, limite_alertas)
VALUES (?, ?, ?, ?)
""", (
    2,
    "Alarma fuerte",
    50,
    3
))



# GUARDAR CAMBIOS


conexion.commit()



# CERRAR CONEXIÓN


conexion.close()



# MENSAJE FINAL


print()
print("==========================================")
print(" BASE DE DATOS CREADA CORRECTAMENTE")
print("==========================================")
print()
print("USUARIOS PARA INICIAR SESIÓN")
print("------------------------------------------")
print()
print("ADMIN")
print("Usuario: admin")
print("Contraseña: admin123")
print()
print("OPERADOR")
print("Usuario: operador1")
print("Contraseña: 1234")
print()
print("CONDUCTOR")
print("Usuario: conductor1")
print("Contraseña: 1234")
print()
print("------------------------------------------")
print("TABLAS CREADAS")
print("------------------------------------------")
print("1. usuario")
print("2. cliente")
print("3. conductor")
print("4. llamada")
print("5. solicitud")
print("6. servicio")
print("7. alerta")
print("8. analisis_fatiga")
print("9. configuracion_alerta")

print("Base de datos lista para utilizar.")
