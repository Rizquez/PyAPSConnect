# PyAPSConnect

## Contexto
__PyAPSConnect__ nace como una solución para desarrolladores que buscan integrar aplicaciones `Python` con `Autodesk Platform Services (APS)`, antiguamente `Forge`.
`APS` es una plataforma de servicios en la nube que ofrece `APIs` para visualizar, manipular y gestionar datos de diseño en 3D. 
Debido a la falta de herramientas en `Python` que faciliten esta integración, este proyecto pretende llenar ese vacío, proporcionando una manera sencilla, robusta y escalable de conectar aplicaciones con `APS`.

## Descripcion del proyecto
__PyAPSConnect__ es una herramienta desarrollada en `Python` para facilitar la conectividad e integración con `APS`. Su objetivo es simplificar la interacción con esta plataforma a través de una interfaz `Python`, permitiendo que los desarrolladores puedan acceder a funciones clave de `APS` como la visualización y manipulación de modelos 3D, la gestión de datos y más. 

> [!NOTE]
> Este proyecto está en desarrollo activo, por lo que algunas funcionalidades aún están en construcción. El `README` se actualizará continuamente para indicar estas nuevas funcionalidades.

## Funcionalidades
- Autenticación rápida y segura con `APS`.
<!-- Estas funcionalidades están planificadas:
- Conexión simplificada a las APIs de `APS`, permitiendo integrarse sin fricciones en otros proyectos de `Python`.
- Configuración flexible para una integración modular y fácil de personalizar.
- Funciones de manipulación y visualización de modelos 3D alojados en la nube.
- Opciones avanzadas para gestionar y almacenar datos de diseño y simulación.
- Soporte para tareas específicas en proyectos de ingeniería, arquitectura y manufactura.
-->

## Tecnologías utilizadas
- __Flask__: Framework de desarrollo web ligero y flexible para la construcción de endpoints y gestión de autenticación.
- __Render__: Plataforma de despliegue de aplicaciones en la nube.

> [!NOTE]
> Proyecto desarrollado con Python `3.11.2`.

## Estructura del proyecto
La estructura del proyecto sigue un esquema modular para facilitar el crecimiento y la incorporación de nuevas funcionalidades:
```
├── settings
│   ├── _base.py 
│   ├── constants.py 
│   └── settings.py 
├── src
│   ├── models /...
│   ├── routes /...
│   ├── static /...
│   └── templates /...
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requierments.txt
```

## Instalación y dependencias
Para comenzar a usar `PyAPSConnect`, sigue los siguientes pasos:

1. Clona el repositorio (ssh):
```
git clone git@github.com:Rizquez/PyAPSConnect.git
```

2. Librerías especificadas en `requirements.txt`, para instalar las dependencias, ejecuta:
```
pip install -r requirements.txt
```

3. Asegúrate de tener configuradas las credenciales de `APS` en el archivo `.env` de la siguiente manera:
```
CLIENT_ID = your_client_id
REDIRECT_URI = your_redirect_uri
CLIENT_SECRET = your_client_secret
```

> [!TIP]
> Dentro del archivo `.env` se recomienda añadir la siguiente variable `FLASK_ENV = development`, esta define el entorno de ejecucion en local para el programa.

> [!IMPORTANT]
> Para evitar problemas de autenticación, asegura tener configuradas correctamente tus credenciales en el archivo de variables de entorno.

## Recursos adicionales
Para obtener más información sobre `APS`, consulta el sitio web oficial de [Autodesk Platform Services](https://aps.autodesk.com/developer/documentation)

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:
- Realiza un `fork` del proyecto.
- Crea una nueva rama con tu funcionalidad o corrección.
```
git checkout -b feature/funcion
```
- Realiza un `pull request` describiendo claramente tus cambios.

> [!NOTE]
> Por favor, asegúrate de seguir las normas de estilo y de añadir pruebas si aplican.

## Licencia
Este proyecto está licenciado bajo la licencia `GNU GENERAL PUBLIC LICENSE`. Consulta el archivo `LICENSE` para más detalles.
