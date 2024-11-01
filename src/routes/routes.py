# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
import os
import requests
from flask import Flask, request, redirect, session, url_for, jsonify
from dotenv import load_dotenv
load_dotenv(override=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------

# LIBRERIAS (INTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
from ..models import Scopes, AuthClient
# -------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos la app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Instanciamos la autenticacion sobre el cliente (OAuth0)
auth_client = AuthClient(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    redirect_uri = os.getenv('REDIRECT_URI')
)

@app.route('/')
def home():
    if 'access_token' in session:
        return 'Ya estás autenticado. <a href="/logout">Cerrar sesión</a>'
    else:
        return redirect(url_for('authenticate'))
    

@app.route('/authenticate')
def authenticate():
    lst_scopes = [
        Scopes.DATA_READ.value,
        Scopes.DATA_WRITE.value,
        Scopes.DATA_CREATE.value,
        Scopes.BUCKET_CREATE.value,
        Scopes.BUCKET_READ.value
    ]
    auth_url = auth_client.get_authorization_url(lst_scopes)
    return redirect(auth_url)

@app.route('/api/auth/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return jsonify({'mensaje': 'No se proporcionó el código de autorización'}), 400
    
    try:
        tokens = auth_client.exchange_code_for_token(code)
        session['access_token'] = tokens.get('access_token')
        session['refresh_token'] = tokens.get('refresh_token')
        return redirect(url_for('protected'))
    except requests.HTTPError as httpe:
        return jsonify({'mensaje': f'Error al obtener el token: {httpe.response.text}'}), 400


@app.route('/api/auth/refresh')
def refresh():
    if 'refresh_token' not in session:
        return redirect(url_for('authenticate'))

    auth_client.refresh_token = session['refresh_token']

    try:
        tokens = auth_client.refresh_access_token()
        session['access_token'] = tokens.get('access_token')
        session['refresh_token'] = tokens.get('refresh_token')
        return redirect(url_for('protected'))
    except ValueError as ve:
        return str(ve), 400
    except requests.HTTPError as httpe:
        return jsonify({'mensaje': f'Error al refrescar el token: {httpe.response.text}'}), 400


@app.route('/protected')
def protected():
    if 'access_token' in session:
        auth_client.access_token = session['access_token']
        return f"Acceso permitido. Tu token de acceso es: {session['access_token']}<br><a href='/logout'>Cerrar sesión</a>"
    else:
        return redirect(url_for('authenticate'))


@app.route('/logout')
def logout():
    session.clear()
    auth_client.access_token = None
    auth_client.refresh_token = None
    return 'Sesión cerrada. <a href="/">Iniciar sesión de nuevo</a>'

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------