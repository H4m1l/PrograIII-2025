from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_academica"
)
cursor = db.cursor(dictionary=True)

# ---------- RUTAS FRONTEND ----------
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/usuarios')
def usuarios_page():
    return render_template('usuarios.html')

# ---------- RUTAS BACKEND (API) ----------
@app.route('/api/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.get_json()
    sql = "INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono) VALUES (%s,%s,%s,%s,%s)"
    values = (data['usuario'], data['clave'], data['nombre'], data['direccion'], data['telefono'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"msg": "ok"})

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return jsonify(cursor.fetchall())

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
    data = request.get_json()
    sql = "UPDATE usuarios SET usuario=%s, clave=%s, nombre=%s, direccion=%s, telefono=%s WHERE idUsuario=%s"
    values = (data['usuario'], data['clave'], data['nombre'], data['direccion'], data['telefono'], id)
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"msg": "ok"})

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE idUsuario=%s", (id,))
    db.commit()
    return jsonify({"msg": "ok"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND clave=%s", (data['usuario'], data['clave']))
    user = cursor.fetchone()
    if user:
        return jsonify({"msg": "ok", "usuario": user['nombre']})
    return jsonify({"msg": "error"})

if __name__ == '__main__':
    app.run(debug=True)
