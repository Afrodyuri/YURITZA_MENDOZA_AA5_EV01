from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    document = request.form.get('document')
    
    if len(password) < 6:
        flash('La contraseña debe tener al menos 6 caracteres', 'error')
        return redirect(url_for('home'))

    flash('Registro exitoso')
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if password == "123456":  # Cambia esto a tu lógica real de autenticación
            flash('¡Bienvenido!')
            return redirect(url_for('welcome'))
        else:
            flash('Contraseña incorrecta. Inténtalo de nuevo.', 'error')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
