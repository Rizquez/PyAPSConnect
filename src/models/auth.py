# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
from typing import List, Dict
from urllib.parse import urlencode
# -------------------------------------------------------------------------------------------------------------------------------------------------

# LIBRERIAS (INTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
from ._base import BaseClient
# -------------------------------------------------------------------------------------------------------------------------------------------------

TOKEN_URL = '/authentication/v2/token'
AUTHORIZE_URL = '/authentication/v2/authorize'
BASE_URL = 'https://developer.api.autodesk.com' 

class AuthClient(BaseClient):
    """
    Clase para gestionar la autenticacion OAuth2 en un cliente que interactua con una API.

    Proporciona metodos para obtener una URL de autorizacion, intercambiar un codigo de autorizacion por un token de acceso, y refrescar el 
    token de acceso usando un refresh token. Esta clase hereda de `BaseClient`.

    Atributos:
        client_id: Identificador del cliente.
        client_secret: Secreto del cliente.
        redirect_uri: URI de redireccion configurada para la aplicacion.
        base_url: URL base de la API de autenticacion. Por defecto es BASE_URL.
        token_url: URL para obtener tokens.
        authorize_url: URL para la autorizacion del usuario.
        access_token: Token de acceso actual (si ha sido asignado).
        refresh_token: Refresh token actual (si ha sido asignado).
    """

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, base_url: str = BASE_URL) -> None:
        super().__init__(base_url)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_url = TOKEN_URL
        self.authorize_url = AUTHORIZE_URL
        self.access_token = None
        self.refresh_token = None

    def get_authorization_url(self, scopes: List[str]) -> str:
        """
        Genera la URL de autorizacion para redirigir al usuario y obtener el codigo de autorizacion.

        Argumentos:
            scopes (List[str]): Lista de permisos requeridos para la aplicacion.

        Retorna:
            str: URL de autorizacion completa.
        """
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': ' '.join(scopes)
        }
        url = self.base_url + self.authorize_url + '?' + urlencode(params)
        return url
    
    def exchange_code_for_token(self, code: str) -> Dict:
        """
        Intercambia el codigo de autorizacion por un token de acceso y refresh token.

        Argumentos:
            code: Codigo de autorizacion obtenido en la redireccion.

        Retorna:
            Dict: Diccionario con el token de acceso y el refresh token.
        """
        form = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self._post(self.token_url, form=form, headers=headers)
        tokens = response.json()
        self.access_token = tokens.get('access_token')
        self.refresh_token = tokens.get('refresh_token')
        return tokens
    
    def refresh_access_token(self) -> Dict:
        """
        Refresca el token de acceso usando el refresh token actual.

        Retorna:
            Dict: Diccionario con el nuevo token de acceso y refresh token.

        Errores:
            ValueError: Si no hay un refresh_token disponible.
        """
        if not self.refresh_token:
            raise ValueError('No hay `refresh_token` disponible para refrescar el token de acceso.')
        form = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self._post(self.token_url, form=form, headers=headers)
        tokens = response.json()
        self.access_token = tokens.get('access_token')
        self.refresh_token = tokens.get('refresh_token')
        return tokens

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------