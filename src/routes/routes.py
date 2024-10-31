# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
import os
import requests
from flask import Flask, request, redirect, session, url_for
from dotenv import load_dotenv
load_dotenv(override=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
URL_CALLBACK = os.getenv('URL_CALLBACK')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

@app.route('/')
def home():
    if 'access_token' in session:
        return 'Ya estás autenticado. <a href="/logout">Cerrar sesión</a>'
    else:
        return redirect(url_for('authenticate'))

@app.route('/authenticate')
def authenticate():
    scopes = 'data:read data:write data:create bucket:create bucket:read'
    return redirect(f"https://developer.api.autodesk.com/authentication/v2/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={URL_CALLBACK}&scope={scopes}")

@app.route('/api/auth/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Error: No se proporcionó el código de autorización.', 400

    token_url = "https://developer.api.autodesk.com/authentication/v2/token"
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': URL_CALLBACK
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    resp = requests.post(token_url, data=payload, headers=headers)
    if resp.status_code == 200:
        resp_json = resp.json()
        session['access_token'] = resp_json['access_token']
        session['refresh_token'] = resp_json.get('refresh_token')
        return redirect(url_for('protected'))
    else:
        return f"Error al obtener el token: {resp.text}", 400

@app.route('/protected')
def protected():
    if 'access_token' in session:
        return f"Acceso permitido. Tu token de acceso es: {session['access_token']}<br><a href='/logout'>Cerrar sesión</a>"
    else:
        return redirect(url_for('authenticate'))

@app.route('/logout')
def logout():
    session.clear()
    return 'Sesión cerrada. <a href="/">Iniciar sesión de nuevo</a>'

@app.route('/api/auth/refresh')
def refresh():
    if 'refresh_token' not in session:
        return redirect(url_for('authenticate'))

    refresh_token = session['refresh_token']
    token_url = "https://developer.api.autodesk.com/authentication/v2/token"
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    resp = requests.post(token_url, data=payload, headers=headers)
    if resp.status_code == 200:
        resp_json = resp.json()
        session['access_token'] = resp_json['access_token']
        session['refresh_token'] = resp_json.get('refresh_token')
        return redirect(url_for('protected'))
    else:
        return f"Error al refrescar el token: {resp.text}", 400

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------