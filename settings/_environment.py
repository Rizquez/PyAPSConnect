# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
import os
import binascii
# -------------------------------------------------------------------------------------------------------------------------------------------------

# LIBRERIAS (INTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
from .keys import Keys
# -------------------------------------------------------------------------------------------------------------------------------------------------

class _SettingGlobal(object):
    """
    ACTUA COMO UNA PLANTILLA PARA TODAS LAS DEMAS CLASES SE DEFINEN LAS CONFIGURACIONES SEGUN CADA ENTORNO DE EJECUCION ENTORNOS DE LA APP.
    """
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = binascii.hexlify(os.urandom(48)).decode()

class Development(_SettingGlobal):
    """
    DEFINE LA CONFIGURACION DEL ENTORNO DE DESARROLLO.
    """
    ENV = Keys.DEV
    HOST = '127.0.0.1'
    PORT = '8080'
    DEBUG = True
    TESTING = True

class Production(_SettingGlobal):
    """
    DEFINE LA CONFIGURACION DEL ENTORNO DE PRODUCCION.
    """
    ENV = Keys.PRO
    HOST = '0.0.0.0'
    PORT = '8080'
    DEBUG = False
    TESTING = False

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------