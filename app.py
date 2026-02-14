from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Citas Médicas – Clínica SaludPlus"

# Ruta dinámica para pacientes
@app.route('/cita/<paciente>')
def cita(paciente):
    return f"Paciente: {paciente}. Su cita está en proceso de confirmación."

# Ruta dinámica adicional (opcional para mejor nota)
@app.route('/especialidad/<nombre>')
def especialidad(nombre):
    return f"Especialidad consultada: {nombre}. Disponibilidad sujeta a agenda médica."

#if __name__ == '__main__':
 #   app.run(debug=True)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)