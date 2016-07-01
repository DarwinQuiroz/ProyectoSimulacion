#setup.py bdist_msi
__author__ = 'Darwin Quiroz'
# Let's start with some default (for me) imports...
import sys
from cx_Freeze import setup, Executable


build_exe_options = {
"include_msvcr": True   #skip error msvcr100.dll missing
}
# Process the includes, excludes and packages first

carpeta = 'ProyectoSimulación'  #nombre de la carpeta donde se instalara el programa

if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\Program File\\ ' + carpeta]

includes = ['PyQt5.QtCore', 'PyQt5.QtGui','sys', 'PyQt5'] #librerias que lleva tu proyecto separadas por comas entre comillas
excludes = []
packages = []
path = []
include_files = ['Inventario', 'LineaDeEspera','Interfaces'] #carpetas que lleva tu aplicacion separadas por comas entre comillas
include_msvcr = ['networkChanger.exe.manifest']

if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'linux' or sys.platform == 'linux2':
    base = None

sico = Executable(
    # what to build
    script = "Main.pyw", #archivo que ejecuta todo el programa
    initScript = None,
    base = base,
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    # icon = 'img/report.ico', #ruta del icono del programa
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "1.0",
    description = "Simulacion de Inventario y Linea de Espera",
    author = "Darwin Quiroz",
    name = "Simulaciones",

    options = {"build_exe": {"includes": includes,
                 "excludes": excludes,
                 "packages": packages,
                 "path": path,
                 "include_files": include_files,
                 "include_msvcr": include_msvcr,
                 }
           },

    executables=[sico]
    )
