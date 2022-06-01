# linky

Pasos y definiciones para la creación y ejecución de un archivo empaquetado rpm:

Temas a tratar:
- rmpbuild: programa para el empaquetado de código fuente y/o binarios en formato .rpm
- setuptools: módulo de python para el empaquetamiento de código fuente

Condiciones:
- Estructura de directorios para el empaquetado de archivo .rpm: para la generación de empaquetados .rpm se debe contar con un directorio raíz llamado "rpmbuild", el cual contenga 5 subdirectorios; "BUILD" "RPMS" "SOURCES" "SPECS" "SRPMS".
  Cada uno de los subdirectorios tiene como propósito:
  
- rpmbuild/
├── BUILD: almacena el código fuente que fue empaquetado luego de realizar el proceso de empaquetación.
├── RPMS: almacena el archivo .rpm con arquitectura noarch (noarch.rpm) luego de ejecutar el proceso de empaquetado.
├── SOURCES: almacena el código fuente ANTES de ser empaquetado, es decir, el código de interés a empaquetar.
├── SPECS: contiene el archivo .spec, este es un archivo de especificación o configuración que contiene los parámetros, instrucciones y procedimientos que definen el cómo se construirá el .rpm y el cómo será el archivo .rpm final.
└── SRPMS: almacena el archivo .rpm que trae consigo el código fuente (source.rpm)
  
- Estructura de directorios y ficheros requeridos para el empaquetado de código Python mediante el uso del módulo setuptools: el módulo setuptools requiere que el código fuente se almacene dentro de una estructura específica junto a diversos ficheros de configuración.
  Estructura de directorios requerida:

python-app: carpeta contenedora del proyecto o programa
├── funciones-sourcecode: carpeta contenedora de código fuente (módulos, funciones, main ...)
│   ├── __init__.py: importa, por debajo, el código relacionado o existente
│   └── program.py: código fuente, módulos, funciones ...
├── __init__.py: importa, por debajo, el código relacionado o existente
└── setup.py: contiene todas aquellas definiciones y configuraciones que harán parte del empaquetado mediante setuptools

A grandes rasgos, se puede definir el proceso de empaquetado, al menos para este aplicativo y en esta forma, en los pasos de;
1 - codificación de setup.py, archivo requerido para el empaquetado a través de setuptools
2 - generación de archivo .spec en base al setup.py
3 - construcción de paquete .rpm en base al archivo .spec

Si se cumplieron todas las condiciones necesarias, almacenando el código Python dentro del directorio rpmbuild/SOURCES y respetando la estructura de setuptools y rpmbuild;
Se pueden ejecutar los comandos:

1 - "python3 setup.py bdist_rpm --spec-only" -> generar fichero .spec en base al setup.py alojado en rpmbuild/SOURCES/python-app
2 - "cp rpmbuild/SOURCES/python-app/dist/file.spec rpmbuild/SPECS" -> copiar fichero .spec dentro del directorio rpmbuild/SPECS
3 - "rpmbuild -ba SPECS/file.spec" -> construcción de paquete .rpm final

El paquete noarch.rpm se creará dentro del directorio RPMS/noarch/paquete.noarch.rpm y el paquete src.rpm en el directorio /SRPMS/src.rpm
