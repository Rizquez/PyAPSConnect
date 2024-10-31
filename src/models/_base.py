# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
import requests
from typing import Dict
# -------------------------------------------------------------------------------------------------------------------------------------------------

class BaseClient:
    """
    Base para un cliente `HTTP` que simplifica la construccion y el manejo de solicitudes a una `API` o servidor dada una `URL` base.

    Atributos:
        base_url: URL base para construir las rutas de las solicitudes.
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def __resolve_url(self, url: str) -> str:
        """
        Construye la URL completa combinando la URL base y la URL relativa proporcionada.

        Argumentos:
            url: Ruta relativa para la solicitud.

        Retorna:
            str: URL completa.
        """
        if url.startswith("/"):
            url = self.base_url + url
        return url

    def _head(self, url: str, **kwargs) -> requests.Response:
        """
        Realiza una solicitud `HTTP HEAD` a la URL especificada.

        Argumentos:
            url: Ruta relativa o URL completa.
            kwargs: Argumentos adicionales para pasar a `requests.head`.

        Retorna:
            Response: Objeto de respuesta de la solicitud HEAD.

        Errores:
            HTTPError: Si la respuesta contiene un error HTTP.
        """
        url = self.__resolve_url(url)
        response = requests.head(url, **kwargs)
        response.raise_for_status()
        return response

    def _get(self, url: str, **kwargs) -> requests.Response:
        """
        Realiza una solicitud `HTTP GET` a la URL especificada.

        Argumentos:
            url: Ruta relativa o URL completa.
            kwargs: Argumentos adicionales para pasar a `requests.get`.

        Retorna:
            Response: Objeto de respuesta de la solicitud GET.

        Errores:
            HTTPError: Si la respuesta contiene un error HTTP.
        """
        url = self.__resolve_url(url)
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return response

    def _post(self, url: str, form: Dict=None, json: Dict=None, buff=None, **kwargs) -> requests.Response:
        """
        Realiza una solicitud `HTTP POST` a la URL especificada, permitiendo varios tipos de datos.

        Argumentos:
            url: Ruta relativa o URL completa.
            form: Datos en formato de formulario para enviar como `data`.
            json: Datos en formato JSON para enviar como `json`.
            buff: Datos en formato de bytes para enviar como `data`.
            kwargs: Argumentos adicionales para pasar a `requests.post`.

        Retorna:
            Response: Objeto de respuesta de la solicitud POST.

        Errores:
            HTTPError: Si la respuesta contiene un error HTTP.
        """
        url = self.__resolve_url(url)
        response = None
        if form:
            response = requests.post(url, data=form, **kwargs)
        elif buff:
            response = requests.post(url, data=buff, **kwargs)
        elif json:
            response = requests.post(url, json=json, **kwargs)
        else:
            response = requests.post(url, **kwargs)
        response.raise_for_status()
        return response

    def _put(self, url: str, form: Dict=None, json: Dict=None, buff=None, **kwargs) -> requests.Response:
        """
        Realiza una solicitud `HTTP PUT` a la URL especificada, permitiendo varios tipos de datos.

        Argumentos:
            url: Ruta relativa o URL completa.
            form: Datos en formato de formulario para enviar como `data`.
            json: Datos en formato JSON para enviar como `json`.
            buff: Datos en formato de bytes para enviar como `data`.
            kwargs: Argumentos adicionales para pasar a `requests.put`.

        Retorna:
            Response: Objeto de respuesta de la solicitud PUT.

        Errores:
            HTTPError: Si la respuesta contiene un error HTTP.
        """
        url = self.__resolve_url(url)
        response = None
        if form:
            response = requests.put(url, data=form, **kwargs)
        elif buff:
            response = requests.put(url, data=buff, **kwargs)
        elif json:
            response = requests.put(url, json=json, **kwargs)
        else:
            response = requests.put(url, **kwargs)
        response.raise_for_status()
        return response

    def _delete(self, url: str, **kwargs) -> requests.Response:
        """
        Realiza una solicitud `HTTP DELETE` a la URL especificada.

        Argumentos:
            url: Ruta relativa o URL completa.
            kwargs: Argumentos adicionales para pasar a `requests.delete`.

        Retorna:
            Response: Objeto de respuesta de la solicitud DELETE.

        Errores:
            HTTPError: Si la respuesta contiene un error HTTP.
        """
        url = self.__resolve_url(url)
        response = requests.delete(url, **kwargs)
        response.raise_for_status()
        return response

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------