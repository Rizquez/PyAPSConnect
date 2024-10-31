# -------------------------------------------------------------------------------------------------------------------------------------------------
# LIBRERIAS (EXTERNAS)
# -------------------------------------------------------------------------------------------------------------------------------------------------
from enum import Enum
# -------------------------------------------------------------------------------------------------------------------------------------------------

class Scopes(Enum):
    """
    Un `scope` es un permiso que se establece sobre un token, un contexto en el que ese token puede actuar. Por ejemplo, un token con el 
    ambito data:read tiene permiso para leer datos dentro del ecosistema APS y puede utilizarse en aquellos puntos finales que requieran 
    ese ambito. A los tokens sin ese ambito se les denegaa el acceso a dichos puntos finales. (Las paginas de referencia de puntos finales 
    individuales enumeran los ambitos requeridos).

    Documentacion: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/scopes/
    """
    USER_PROFILE_READ = 'user-profile:read'
    """
    La aplicacion podra leer los datos del perfil del usuario final 
    (sin incluir los productos y servicios asociados).
    """
    USER_READ = 'user:read'
    """
    La aplicacion podra leer los datos del perfil del usuario final, 
    incluidos los productos y servicios asociados.
    """
    USER_WRITE = 'user:write'
    """
    La aplicacion podra leer los datos del perfil del usuario final, 
    incluidos los productos y servicios asociados.
    """
    VIEWABLES_READ = 'viewables:read'
    """
    La aplicacion solo podra leer los datos visibles del usuario final 
    (por ejemplo, archivos PNG y SVF) dentro del ecosistema de Autodesk.
    """
    DATA_READ = 'data:read'
    """
    La aplicacion podra leer todos los datos del usuario final 
    (visibles y no visibles) dentro del ecosistema de Autodesk.
    """
    DATA_WRITE = 'data:write'
    """
    La aplicacion podra crear, actualizar y eliminar datos en nombre del 
    usuario final dentro del ecosistema de Autodesk.
    """
    DATA_CREATE = 'data:create'
    """
    La aplicacion podra crear datos en nombre del usuario final dentro del 
    ecosistema de Autodesk.
    """
    DATA_SEARCH = 'data:search'
    """
    La aplicacion podra buscar los datos del usuario final dentro del 
    ecosistema de Autodesk.
    """
    BUCKET_CREATE = 'bucket:create'
    """
    La aplicacion podra crear un bucket OSS de su propiedad.
    """
    BUCKET_READ = 'bucket:read'
    """
    La aplicacion podra leer los metadatos y listar los contenidos de 
    los buckets OSS a los que tenga acceso.
    """
    BUCKET_UPDATE = 'bucket:update'
    """
    La aplicacion podra establecer permisos y derechos para los buckets 
    de OSS que tenga permiso para modificar.
    """
    BUCKET_DELETE = 'bucket:delete'
    """
    La aplicacion podra eliminar un cubo para el que tenga permiso.
    """
    CODE_ALL = 'code:all'
    """
    La aplicacion podra crear y ejecutar codigo en nombre del usuario final 
    (por ejemplo, scripts procesados por la API de automatizacion del diseño).
    """
    ACCOUNT_READ = 'account:read'
    """
    En el caso de las API de productos, la aplicacion podra leer los datos de 
    la cuenta a la que tiene derecho el usuario final.
    """
    ACCOUNT_WRITE = 'account:write'
    """
    En el caso de las API de productos, la aplicacion podra actualizar los datos 
    de la cuenta a la que tiene derecho el usuario final.
    """

# -------------------------------------------------------------------------------------------------------------------------------------------------
# FIN DEL FICHERO
# -------------------------------------------------------------------------------------------------------------------------------------------------