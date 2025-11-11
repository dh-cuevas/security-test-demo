from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Security Test Demo - Vulnerable Application"

@app.route('/hello')
def hello():
    # VULNERABLE: Sin sanitización de entrada
    name = request.args.get('name', 'World')
    return f"Hello, {name}!"

@app.route('/command')
def command():
    # VULNERABLE: Inyección de comandos OS
    cmd = request.args.get('cmd', 'echo hello')
    result = os.system(cmd)
    return f"Command executed with result: {result}"

@app.route('/eval')
def eval_code():
    # VULNERABLE: Ejecución de código arbitrario
    code = request.args.get('code', '1+1')
    try:
        result = eval(code)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # VULNERABLE: Debug mode en producción
    app.run(host='0.0.0.0', port=5000, debug=True)
