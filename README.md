# PyForgeConnect (En desarrollo)

## Descripcion
PyForgeConnect es una herramienta desarrollada en `Python` para facilitar la conectividad e integración con `Autodesk Forge`, un conjunto de APIs en la nube que permiten a los desarrolladores crear aplicaciones para visualizar, manipular y gestionar datos de diseño en 3D. Este proyecto está en desarrollo y se enfoca en simplificar la interacción con `Autodesk Forge` a través de una interfaz `Python`.

## Caracteristicas
- Conectividad rápida y segura con `Autodesk Forge`.
- Funciones de manipulación y visualización de modelos `3D en la nube`.
- Configuración sencilla y flexible para integrarse en otros proyectos `Python`.
- Enfoque modular para facilitar la extensión y personalización.

## 🛠️ Tecnologias utilizadas
- __Flask__: Framework de desarrollo web de alto nivel que promueve un desarrollo rápido y un diseño limpio y pragmático.

## 📂 Estructura del proyecto
```
├── settings
│   ├── _environment.py 
│   ├── constants.py 
│   └── settings.py 
├── src
│   ├── models /...
│   └── routes /...
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requierments.txt
```

## 🧾 Dependencias
- Python 3.6 o superior.
- Librerías especificadas en `requirements.txt`.
Para instalar las dependencias, ejecuta:
```
pip install -r requirements.txt
```
> [!NOTE]
> Asegúrate de tener las credenciales de Autodesk Forge. Configura tus credenciales en el archivo de configuración o utiliza variables de entorno.

## 📚 Recursos adicionales
Para mas informacion visite el sitio web oficial de [Autodesk Platform Services](https://aps.autodesk.com/developer/documentation)

## 📝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor:
- Haz un fork del proyecto.
- Crea una rama con tu funcionalidad o corrección (git checkout -b feature/nueva-funcion).
- Realiza un pull request con una descripción clara de tus cambios.

## 📄 Licencia
Este proyecto está licenciado bajo la licencia `GNU GENERAL PUBLIC LICENSE`. Consulta el archivo `LICENSE` para más detalles.
