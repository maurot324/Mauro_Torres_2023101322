from flask import Flask, render_template, request, redirect, url_for
from db_connection import get_db_connection

app = Flask(__name__)
app.secret_key = 'mi_secreto'

@app.route('/')
def home(): 
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username='Usuario')

# Rutas de categorías de ganado
@app.route('/ternero')
def ternero():
    return render_template('ternero.html', username='Usuario')

@app.route('/Novillito')
def novillito():
    return render_template('Novillito.html', username='Usuario')

@app.route('/Novillo')
def novillo():
    return render_template('Novillo.html', username='Usuario')

@app.route('/Vaquillona')
def vaquillona():
    return render_template('Vaquillona.html', username='Usuario')

@app.route('/vaca')
def vaca():
    return render_template('vaca.html', username='Usuario')

@app.route('/Toro')
def toro():
    return render_template('Toro.html', username='Usuario')

# Rutas antiguas (puedes mantenerlas o eliminarlas)
@app.route('/productos')
def productos():
    return render_template('productos.html', username='Usuario')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html', username='Usuario')
    
@app.route('/Oferta')
def ignite():
    return render_template('Oferta.html', username='Usuario')

@app.route('/waka')
def waka():
    return render_template('waka.html', username='Usuario')

@app.route('/herramientas')
def herramientas():
    return render_template('herramientas.html', username='Usuario')

# Ruta de registro actualizada con todos los campos
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        nombre = request.form['nombre']
        apellido = request.form.get('apellido', '')  # Opcional
        correo = request.form.get('email', '')  # Opcional
        celular = request.form['celular']
        horario_llamar = request.form['horario_llamar']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (username, nombre, apellido, correo, celular, horario_llamar) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (username, nombre, apellido, correo, celular, horario_llamar))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('dashboard'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)