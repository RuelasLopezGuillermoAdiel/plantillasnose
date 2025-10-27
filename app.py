from flask import Flask, render_template, request , redirect ,url_for ,flash

app = flask(__name__)
app.config["SECRET_KEY"]="una_clave_muy_larga_y_dificil_de_adivinar"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/animales")
def index():
    return render_template("animales.html")
@app.route("/veiculos")
def index():
    return render_template("autosviejos.html")
@app.route("/maravillas")
def index():
    return render_template("lasmaravillasdelmundo.html")
@app.route("/acercade")
def index():
    return render_template("acercade.html")
@app.router("/crear", methods=["GET", "POST"])
def crear():
    error = None 
    if request.method == "POST":
        nombreCompleto = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmarPassword = request.form.get("confirmPassword")
        fechaNacimiento = request.form.get("fechaNacimiento")
        genero = request.form.get("genero")
        genero_personalizado = request.form.get("genero_personalizado")
        
        if password != confirmarPassword:
            error = "las contraseñas no coinciden"
        elif not nombreCompleto or not email or not password:
            error = "todos los campos obligatorios deben completarse"
            
        if error:
            flash(error, "error")
            return render_template("inicio.html")
        else:
            flash{f"Registro exitoso, bienvenido/a {nombreCompleto} {apellido}"}
            return redirect(url_for(index))
        return render_template("inicio.html")
    
    @app.route("/inicio")
    def inicio():
        return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True)

