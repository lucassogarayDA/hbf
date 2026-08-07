#!/usr/bin/env python3
# hbf.py - Hybrid Binary Format v2.0.0
# Creado por Lucas Sogaray

import json
import re
import base64
import os
from datetime import datetime

VERSION = "2.0.0"
RUTA_DOWNLOAD = os.path.expanduser("~/storage/downloads/")

COLOR_TITULO = "\033[1;36m"
COLOR_MENU = "\033[1;32m"
COLOR_ERROR = "\033[1;31m"
COLOR_EXITO = "\033[1;32m"
COLOR_INFO = "\033[1;34m"
COLOR_RESET = "\033[0m"

# ============================================
# IDIOMAS
# ============================================

IDIOMAS = {
    "es": {
        "titulo": "📁 HBF - Hybrid Binary Format",
        "creado_por": "Creado por Lucas Sogaray",
        "guardado_en": "Todos los archivos se guardan en:",
        "menu": "¿Qué querés hacer?",
        "opciones": [
            "📝 Crear HBF",
            "📖 Leer HBF",
            "🖼️ Guardar binario",
            "📤 Extraer binario",
            "✏️ Editar TEXTO",
            "📋 Editar LISTAS",
            "💬 Editar NOTAS",
            "🔢 Editar NUMERICO",
            "🏷️ Editar TITULOS",
            "📝 Editar METADATOS",
            "📤 Exportar",
            "🔍 Buscar",
            "📂 Listar HBF",
            "📊 Estadísticas",
            "🎨 Colores",
            "🔗 Combinar HBF",
            "📲 Compartir",
            "🔒 Proteger con clave",
            "🚪 Salir"
        ],
        "salir": "👋 ¡Chau! Gracias por usar HBF",
        "error": "❌ Opción no válida",
        "exito": "✅",
        "info": "ℹ️",
        "espera": "⏎ Enter para continuar...",
        "archivos_en": "Tus archivos están en:"
    },
    "en": {
        "titulo": "📁 HBF - Hybrid Binary Format",
        "creado_por": "Created by Lucas Sogaray",
        "guardado_en": "All files are saved in:",
        "menu": "What do you want to do?",
        "opciones": [
            "📝 Create HBF",
            "📖 Read HBF",
            "🖼️ Save binary",
            "📤 Extract binary",
            "✏️ Edit TEXT",
            "📋 Edit LISTS",
            "💬 Edit NOTES",
            "🔢 Edit NUMERIC",
            "🏷️ Edit TITLES",
            "📝 Edit METADATA",
            "📤 Export",
            "🔍 Search",
            "📂 List HBF",
            "📊 Statistics",
            "🎨 Colors",
            "🔗 Combine HBF",
            "📲 Share",
            "🔒 Protect with key",
            "🚪 Exit"
        ],
        "salir": "👋 Bye! Thanks for using HBF",
        "error": "❌ Invalid option",
        "exito": "✅",
        "info": "ℹ️",
        "espera": "⏎ Press Enter to continue...",
        "archivos_en": "Your files are in:"
    }
}

def elegir_idioma():
    print("\n" + "=" * 48)
    print("  Select language / Elegí idioma:")
    print("  1. Español")
    print("  2. English")
    print("=" * 48)
    opcion = input("  👉 Opción / Option: ")
    if opcion == "2":
        return "en"
    return "es"

IDIOMA_ACTUAL = elegir_idioma()
T = IDIOMAS[IDIOMA_ACTUAL]

# ============================================
# FUNCIONES DE INTERFAZ
# ============================================

def limpiar():
    os.system('clear')

def titulo():
    limpiar()
    print(f"""
    {COLOR_TITULO}╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     {T['titulo']}  v{VERSION}      ║
    ║                                                      ║
    ║     {T['creado_por']}                        ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝{COLOR_RESET}
    """)

def mensaje_bienvenida():
    print(f"{COLOR_INFO}{T['guardado_en']}{COLOR_RESET}")
    print(f"   📂  {RUTA_DOWNLOAD}\n")

def mostrar_menu():
    titulo()
    mensaje_bienvenida()
    print(f"{COLOR_MENU}    {T['menu']}{COLOR_RESET}\n")
    print("    ┌────────────────────────────────────────────┐")
    for i, opcion in enumerate(T['opciones'], 1):
        print(f"    │  {i:2d}.  {opcion:<28}│")
    print("    └────────────────────────────────────────────┘")

def esperar():
    input(f"\n{COLOR_INFO}   {T['espera']}{COLOR_RESET}")

def error(mensaje):
    print(f"\n{COLOR_ERROR}   ❌  {mensaje}{COLOR_RESET}")

def exito(mensaje):
    print(f"\n{COLOR_EXITO}   ✅  {mensaje}{COLOR_RESET}")

def info(mensaje):
    print(f"\n{COLOR_INFO}   ℹ️  {mensaje}{COLOR_RESET}")

def obtener_ruta(archivo):
    archivo = os.path.expanduser(archivo)
    if not "/" in archivo:
        archivo = RUTA_DOWNLOAD + archivo
    return archivo

def listar_hbf():
    archivos = [f for f in os.listdir(RUTA_DOWNLOAD) if f.endswith(".hbf")]
    if not archivos:
        info("No hay archivos .hbf en Download")
        return []
    print(f"\n   📂  Archivos .hbf ({len(archivos)}):")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    return archivos

def crear_hbf():
    print("\n   📝  CREAR HBF\n")
    archivo = input("   📄  Nombre del archivo: ")
    if not archivo.endswith(".hbf"):
        archivo += ".hbf"
    archivo = obtener_ruta(archivo)
    titulo = input("   🏷️  Título: ") or "Sin título"
    autor = input("   👤  Autor: ") or "Anónimo"
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("[HBF]\n")
        f.write(f"Version: {VERSION}\n")
        f.write("Magic: HBF\n")
        f.write(f"Fecha: {datetime.now().isoformat()}\n\n")
        f.write("[METADATOS]\n")
        metadatos = {"titulo": titulo, "autor": autor}
        f.write(json.dumps(metadatos, indent=2))
        f.write("\n\n")
        f.write("[TEXTO]\nEscribe tu contenido aquí.\n\n")
        f.write("[LISTAS]\n- Item 1\n- Item 2\n\n")
        f.write("[NOTAS]\nNota personal.\n\n")
        f.write("[NUMERICO]\n{\"datos\": [1, 2, 3]}\n\n")
        f.write("[TITULOS]\nTítulo principal\n\n")
        f.write("[FIN]\n")
    exito(f"Archivo creado: {archivo}")

def leer_hbf():
    print("\n   📖  LEER HBF\n")
    archivo = input("   📄  Nombre del archivo: ")
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe.")
        return
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    print("\n   📖  CONTENIDO:")
    print("   " + "=" * 48)
    print(contenido)
    print("   " + "=" * 48)

def guardar_binario():
    print("\n   🖼️  GUARDAR BINARIO\n")
    origen = input("   📂  Archivo a guardar: ")
    origen = os.path.expanduser(origen)
    if not os.path.exists(origen):
        error("El archivo no existe")
        return
    destino = input("   📁  Archivo HBF destino: ")
    destino = obtener_ruta(destino)
    if not destino.endswith(".hbf"):
        destino += ".hbf"
    with open(origen, 'rb') as f:
        datos = f.read()
    datos_b64 = base64.b64encode(datos).decode('ascii')
    with open(destino, 'a', encoding='utf-8') as f:
        f.write("[BINARIO]\n")
        f.write("# Original: " + os.path.basename(origen) + "\n")
        f.write("data: " + datos_b64 + "\n\n")
    exito(f"Binario guardado en {destino}")

def extraer_binario():
    print("\n   📤  EXTRAER BINARIO\n")
    origen = input("   📁  Archivo HBF origen: ")
    origen = obtener_ruta(origen)
    if not os.path.exists(origen):
        error("El archivo no existe")
        return
    salida = input("   📂  Nombre para extraer: ")
    salida = obtener_ruta(salida)
    with open(origen, 'r', encoding='utf-8') as f:
        contenido = f.read()
    match = re.search(r'\[BINARIO\].*?data:\s*([A-Za-z0-9+/=]+)', contenido, re.DOTALL)
    if not match:
        error("No se encontró bloque BINARIO")
        return
    try:
        datos = base64.b64decode(match.group(1))
        with open(salida, 'wb') as f:
            f.write(datos)
        exito(f"Archivo extraido: {salida}")
    except Exception as e:
        error(f"Error: {e}")

def editar_bloque(archivo, bloque, nuevo_contenido):
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    patron = r'(\[' + bloque + r'\]\n).*?(\n\n|\[)'
    reemplazo = r'\1' + nuevo_contenido + r'\n\n\2'
    nuevo = re.sub(patron, reemplazo, contenido, flags=re.DOTALL)
    if nuevo == contenido:
        error(f"No se encontró el bloque [{bloque}]")
        return
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(nuevo)
    exito(f"Bloque [{bloque}] actualizado")

def editar_texto():
    archivo = input("   📄  Archivo: ")
    print("\n   📝  Nuevo texto (Enter dos veces para terminar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "TEXTO", "\n".join(lineas))

def editar_listas():
    archivo = input("   📄  Archivo: ")
    print("\n   📝  Nueva lista (Enter dos veces para terminar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "LISTAS", "\n".join(lineas))

def editar_notas():
    archivo = input("   📄  Archivo: ")
    print("\n   📝  Nuevas notas (Enter dos veces para terminar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "NOTAS", "\n".join(lineas))

def editar_numerico():
    archivo = input("   📄  Archivo: ")
    nuevo = input("   📝  Nuevo numerico: ")
    editar_bloque(archivo, "NUMERICO", nuevo)

def editar_titulos():
    archivo = input("   📄  Archivo: ")
    nuevo = input("   📝  Nuevo titulo: ")
    editar_bloque(archivo, "TITULOS", nuevo)

def editar_metadatos():
    archivo = input("   📄  Archivo: ")
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    match = re.search(r'\[METADATOS\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
    if not match:
        error("No se encontró METADATOS")
        return
    try:
        metadatos = json.loads(match.group(1).strip())
    except:
        error("Error al leer metadatos")
        return
    print(f"\n   📝  METADATOS ACTUALES:")
    print(f"      Título: {metadatos.get('titulo', 'Sin título')}")
    print(f"      Autor: {metadatos.get('autor', 'Anónimo')}")
    print(f"      Fecha: {metadatos.get('fecha', 'Sin fecha')}")
    print("\n   ✏️  NUEVOS METADATOS (Enter para mantener):")
    nuevo_titulo = input(f"      Título [{metadatos.get('titulo', 'Sin título')}]: ") or metadatos.get('titulo', 'Sin título')
    nuevo_autor = input(f"      Autor [{metadatos.get('autor', 'Anónimo')}]: ") or metadatos.get('autor', 'Anónimo')
    metadatos['titulo'] = nuevo_titulo
    metadatos['autor'] = nuevo_autor
    metadatos['fecha'] = datetime.now().isoformat()
    nuevo_contenido = re.sub(
        r'(\[METADATOS\]\n).*?(\n\n|\[)',
        r'\1' + json.dumps(metadatos, indent=2) + r'\n\n\2',
        contenido,
        flags=re.DOTALL
    )
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    exito("Metadatos actualizados")

def exportar_hbf():
    print("\n   📤  EXPORTAR\n")
    archivo = input("   📄  Archivo HBF: ")
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    print("\n   📤  Formato:")
    print("      1. TXT")
    print("      2. JSON")
    print("      3. MD")
    formato = input("   👉  Opción: ")
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]
    if formato == "1":
        salida = RUTA_DOWNLOAD + nombre_base + ".txt"
        texto = re.search(r'\[TEXTO\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        if texto:
            with open(salida, 'w', encoding='utf-8') as f:
                f.write(texto.group(1).strip())
            exito(f"Exportado a TXT: {salida}")
        else:
            error("No se encontró texto")
    elif formato == "2":
        salida = RUTA_DOWNLOAD + nombre_base + ".json"
        bloques = re.findall(r'\[([A-Z]+)\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        datos = {nombre: valor.strip() for nombre, valor in bloques}
        with open(salida, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2)
        exito(f"Exportado a JSON: {salida}")
    elif formato == "3":
        salida = RUTA_DOWNLOAD + nombre_base + ".md"
        md = f"# {nombre_base}\n\n"
        texto = re.search(r'\[TEXTO\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        if texto:
            md += texto.group(1).strip() + "\n\n"
        with open(salida, 'w', encoding='utf-8') as f:
            f.write(md)
        exito(f"Exportado a MD: {salida}")
    else:
        error("Opción no válida")

def buscar_hbf():
    print("\n   🔍  BUSCAR\n")
    archivo = input("   📄  Archivo: ")
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    busqueda = input("   🔍  Palabra: ")
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    if busqueda.lower() in contenido.lower():
        exito(f"✅ Encontrado '{busqueda}'")
        lineas = contenido.split('\n')
        for i, linea in enumerate(lineas, 1):
            if busqueda.lower() in linea.lower():
                print(f"   Línea {i}: {linea.strip()}")
    else:
        error(f"No se encontró '{busqueda}'")

def listar_hbf_menu():
    print("\n   📂  LISTAR HBF\n")
    listar_hbf()

def estadisticas_hbf():
    print("\n   📊  ESTADÍSTICAS\n")
    archivo = input("   📄  Archivo: ")
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    tamaño = os.path.getsize(archivo)
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    lineas = len(contenido.split('\n'))
    bloques = len(re.findall(r'\[([A-Z]+)\]', contenido))
    print(f"\n   📊  ESTADÍSTICAS:")
    print(f"      📄  Archivo: {os.path.basename(archivo)}")
    print(f"      📏  Tamaño: {tamaño} bytes")
    print(f"      📝  Líneas: {lineas}")
    print(f"      📦  Bloques: {bloques}")
    print(f"      📂  Ruta: {archivo}")

def cambiar_colores():
    print("\n   🎨  COLORES\n")
    print("   1. 🔵  Azul")
    print("   2. 🟢  Verde")
    print("   3. 🔴  Rojo")
    print("   4. 🟡  Amarillo")
    print("   5. 🟣  Morado")
    opcion = input("   👉  Elegí: ")
    info("Función en desarrollo")

def combinar_hbf():
    print("\n   🔗  COMBINAR HBF\n")
    archivos = listar_hbf()
    if not archivos:
        return
    print("\n   📄  Primer archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion1 = input("   👉  Opción: ")
    try:
        archivo1 = archivos[int(opcion1) - 1]
    except:
        error("Opción no válida")
        return
    print("\n   📄  Segundo archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion2 = input("   👉  Opción: ")
    try:
        archivo2 = archivos[int(opcion2) - 1]
    except:
        error("Opción no válida")
        return
    print("\n   🔄  Orden:")
    print(f"      1. {archivo1} primero")
    print(f"      2. {archivo2} primero")
    orden = input("   👉  Opción: ")
    ruta1 = obtener_ruta(archivo1)
    ruta2 = obtener_ruta(archivo2)
    with open(ruta1, 'r', encoding='utf-8') as f:
        contenido1 = f.read()
    with open(ruta2, 'r', encoding='utf-8') as f:
        contenido2 = f.read()
    bloques1 = re.findall(r'(\[[A-Z]+\]\n.*?)(?=\n\[[A-Z]+\]|\n\[FIN\]|$)', contenido1, re.DOTALL)
    bloques2 = re.findall(r'(\[[A-Z]+\]\n.*?)(?=\n\[[A-Z]+\]|\n\[FIN\]|$)', contenido2, re.DOTALL)
    if orden == "1":
        combinado = "\n".join(bloques1) + "\n" + "\n".join(bloques2)
    else:
        combinado = "\n".join(bloques2) + "\n" + "\n".join(bloques1)
    nombre_salida = input("\n   📄  Nombre nuevo archivo: ")
    if not nombre_salida.endswith(".hbf"):
        nombre_salida += ".hbf"
    salida = obtener_ruta(nombre_salida)
    cabecera = f"[HBF]\nVersion: {VERSION}\nMagic: HBF\nFecha: {datetime.now().isoformat()}\n\n"
    with open(salida, 'w', encoding='utf-8') as f:
        f.write(cabecera + combinado + "\n[FIN]\n")
    exito(f"Archivo combinado: {salida}")

def compartir_whatsapp():
    print("\n   📲  COMPARTIR\n")
    archivos = listar_hbf()
    if not archivos:
        return
    print("\n   📄  Elegí el archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion = input("   👉  Opción: ")
    try:
        archivo = archivos[int(opcion) - 1]
    except:
        error("Opción no válida")
        return
    ruta = obtener_ruta(archivo)
    print(f"\n   🔧  Comando:")
    print(f"      termux-share {ruta}")
    info("Instalá termux-api: pkg install termux-api")

def proteger_hbf():
    print("\n   🔒  PROTEGER CON CLAVE\n")
    archivos = listar_hbf()
    if not archivos:
        return
    print("\n   📄  Elegí el archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion = input("   👉  Opción: ")
    try:
        archivo = archivos[int(opcion) - 1]
    except:
        error("Opción no válida")
        return
    ruta = obtener_ruta(archivo)
    print("\n   🔑  Operación:")
    print("      1. Cifrar")
    print("      2. Descifrar")
    operacion = input("   👉  Opción: ")
    if operacion == "1":
        clave = input("   🔑  Clave: ")
        if not clave:
            error("La clave no puede estar vacía")
            return
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        except:
            error("Falta cryptography. Instalá: pkg install python-cryptography")
            return
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(clave.encode()))
        fernet = Fernet(key)
        datos_cifrados = fernet.encrypt(contenido.encode())
        with open(ruta + ".enc", 'wb') as f:
            f.write(salt + datos_cifrados)
        exito(f"Archivo cifrado: {ruta}.enc")
        info("Recordá la clave")
    elif operacion == "2":
        if not os.path.exists(ruta + ".enc"):
            error("No existe archivo cifrado (.enc)")
            return
        clave = input("   🔑  Clave: ")
        if not clave:
            error("La clave no puede estar vacía")
            return
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        except:
            error("Falta cryptography")
            return
        with open(ruta + ".enc", 'rb') as f:
            salt = f.read(16)
            datos_cifrados = f.read()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(clave.encode()))
        fernet = Fernet(key)
        try:
            datos_descifrados = fernet.decrypt(datos_cifrados)
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(datos_descifrados.decode())
            exito(f"Archivo descifrado: {ruta}")
        except:
            error("Clave incorrecta o archivo corrupto")
    else:
        error("Opción no válida")

# ============================================
# MAIN
# ============================================

def main():
    while True:
        mostrar_menu()
        opcion = input("   👉  Elegí una opción: ")
        
        if opcion == "1":
            crear_hbf()
        elif opcion == "2":
            leer_hbf()
        elif opcion == "3":
            guardar_binario()
        elif opcion == "4":
            extraer_binario()
        elif opcion == "5":
            editar_texto()
        elif opcion == "6":
            editar_listas()
        elif opcion == "7":
            editar_notas()
        elif opcion == "8":
            editar_numerico()
        elif opcion == "9":
            editar_titulos()
        elif opcion == "10":
            editar_metadatos()
        elif opcion == "11":
            exportar_hbf()
        elif opcion == "12":
            buscar_hbf()
        elif opcion == "13":
            listar_hbf_menu()
        elif opcion == "14":
            estadisticas_hbf()
        elif opcion == "15":
            cambiar_colores()
        elif opcion == "16":
            combinar_hbf()
        elif opcion == "17":
            compartir_whatsapp()
        elif opcion == "18":
            proteger_hbf()
        elif opcion == "19":
            limpiar()
            print(f"\n   {T['salir']}")
            print(f"   📁  {T['archivos_en']} {RUTA_DOWNLOAD}\n")
            break
        else:
            error(T['error'])
        
        esperar()

if __name__ == "__main__":
    main()
