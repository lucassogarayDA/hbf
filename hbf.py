#!/usr/bin/env python3
# hbf.py - Hybrid Binary Format v2.1.1
# Creado por Lucas Sogaray
# Compatibilidad extrema: Android (Termux) | Windows | Linux

import json
import re
import base64
import os
import sys
import platform
import locale
from datetime import datetime

VERSION = "2.1.1"

# ====================
# DETECCIÓN DE SISTEMA OPERATIVO
# ====================

SO = platform.system()

if SO == "Android":
    RUTA_DESCARGAS = os.path.expanduser("~/storage/downloads/")
elif SO == "Windows":
    RUTA_DESCARGAS = os.path.expanduser("~/Downloads/")
else:
    RUTA_DESCARGAS = os.path.expanduser("~/Downloads/")

# ====================
# CONFIGURACIÓN
# ====================

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".hbf_config.json")

def cargar_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"color": "azul", "ruta_base": ""}

def guardar_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

config = cargar_config()

# ====================
# COLORES (diccionario corregido)
# ====================

COLORES = {
    "azul": {"titulo": "\033[1;36m", "menu": "\033[1;32m", "error": "\033[1;31m", "exito": "\033[1;32m", "info": "\033[1;34m"},
    "verde": {"titulo": "\033[1;32m", "menu": "\033[1;36m", "error": "\033[1;31m", "exito": "\033[1;33m", "info": "\033[1;34m"},
    "rojo": {"titulo": "\033[1;31m", "menu": "\033[1;33m", "error": "\033[1;31m", "exito": "\033[1;32m", "info": "\033[1;34m"},
    "amarillo": {"titulo": "\033[1;33m", "menu": "\033[1;32m", "error": "\033[1;31m", "exito": "\033[1;36m", "info": "\033[1;34m"},
    "morado": {"titulo": "\033[1;35m", "menu": "\033[1;36m", "error": "\033[1;31m", "exito": "\033[1;32m", "info": "\033[1;34m"},
}

if SO == "Windows":
    C = {"titulo":"","menu":"","error":"","exito":"","info":"","reset":""}
else:
    c = COLORES.get(config.get("color", "azul"), COLORES["azul"])
    C = {**c, "reset": "\033[0m"}

# ====================
# IDIOMAS
# ====================

IDIOMAS = {
    "es": {
        "titulo": "📁 HBF - Hybrid Binary Format",
        "creado_por": "Creado por Lucas Sogaray",
        "guardado_en": "Todos los archivos se guardan en:",
        "menu": "¿Qué querés hacer?",
        "opciones": [
            "📝 Crear HBF", "📖 Leer HBF", "🖼️ Guardar binario",
            "📤 Extraer binario", "✏️ Editar TEXTO", "📋 Editar LISTAS",
            "💬 Editar NOTAS", "🔢 Editar NUMERICO", "🏷️ Editar TITULOS",
            "📝 Editar METADATOS", "📤 Exportar", "🔍 Buscar",
            "📂 Listar HBF", "📊 Estadísticas", "🎨 Colores",
            "🔗 Combinar HBF", "🔒 Proteger con clave", "📁 Cambiar ruta base",
            "🚪 Salir"
        ],
        "recordatorio": "💡 Escribí el número de la opción (ej: 1, 2, 3...)",
        "salir": "👋 ¡Chau! Gracias por usar HBF",
        "archivos_en": "Tus archivos están en:",
        "error": "❌ Opción no válida",
        "cancelar": "✖️ Operación cancelada",
        "ruta_actual": "📁 Ruta base actual:",
        "nueva_ruta": "📁 Nueva ruta base (dejá vacío para usar Descargas):"
    },
    "en": {
        "titulo": "📁 HBF - Hybrid Binary Format",
        "creado_por": "Created by Lucas Sogaray",
        "guardado_en": "All files are saved in:",
        "menu": "What do you want to do?",
        "opciones": [
            "📝 Create HBF", "📖 Read HBF", "🖼️ Save binary",
            "📤 Extract binary", "✏️ Edit TEXT", "📋 Edit LISTS",
            "💬 Edit NOTES", "🔢 Edit NUMERIC", "🏷️ Edit TITLES",
            "📝 Edit METADATA", "📤 Export", "🔍 Search",
            "📂 List HBF", "📊 Statistics", "🎨 Colors",
            "🔗 Combine HBF", "🔒 Protect with key", "📁 Change base path",
            "🚪 Exit"
        ],
        "recordatorio": "💡 Type the option number (e.g. 1, 2, 3...)",
        "salir": "👋 Bye! Thanks for using HBF",
        "archivos_en": "Your files are in:",
        "error": "❌ Invalid option",
        "cancelar": "✖️ Operation cancelled",
        "ruta_actual": "📁 Current base path:",
        "nueva_ruta": "📁 New base path (leave empty to use Downloads):"
    },
    "pt": {
        "titulo": "📁 HBF - Hybrid Binary Format",
        "creado_por": "Criado por Lucas Sogaray",
        "guardado_en": "Todos os arquivos são salvos em:",
        "menu": "O que você quer fazer?",
        "opciones": [
            "📝 Criar HBF", "📖 Ler HBF", "🖼️ Salvar binário",
            "📤 Extrair binário", "✏️ Editar TEXTO", "📋 Editar LISTAS",
            "💬 Editar NOTAS", "🔢 Editar NUMÉRICO", "🏷️ Editar TÍTULOS",
            "📝 Editar METADADOS", "📤 Exportar", "🔍 Buscar",
            "📂 Listar HBF", "📊 Estatísticas", "🎨 Cores",
            "🔗 Combinar HBF", "🔒 Proteger com chave", "📁 Alterar caminho base",
            "🚪 Sair"
        ],
        "recordatorio": "💡 Digite o número da opção (ex: 1, 2, 3...)",
        "salir": "👋 Tchau! Obrigado por usar HBF",
        "archivos_en": "Seus arquivos estão em:",
        "error": "❌ Opção inválida",
        "cancelar": "✖️ Operação cancelada",
        "ruta_actual": "📁 Caminho base atual:",
        "nueva_ruta": "📁 Novo caminho base (deixe vazio para usar Downloads):"
    }
}

def detectar_idioma():
    try:
        idioma = locale.getlocale()[0]
        if idioma:
            if idioma.startswith("es"):
                return "es"
            elif idioma.startswith("pt"):
                return "pt"
            elif idioma.startswith("en"):
                return "en"
        return "en"
    except:
        return "en"

def elegir_idioma():
    idioma_detectado = detectar_idioma()
    print("\n" + "=" * 48)
    if idioma_detectado == "es":
        print("  🌎 Idioma detectado: Español")
    elif idioma_detectado == "pt":
        print("  🌎 Idioma detectado: Português")
    else:
        print("  🌎 Detected language: English")
    
    print("  1. Español")
    print("  2. English")
    print("  3. Português")
    print("=" * 48)
    opcion = input("  👉 Opción / Option / Opção: ")
    
    if opcion == "1":
        return "es"
    elif opcion == "2":
        return "en"
    elif opcion == "3":
        return "pt"
    else:
        return idioma_detectado

T = IDIOMAS[elegir_idioma()]

# ====================
# FUNCIONES BÁSICAS
# ====================

def limpiar():
    os.system('cls' if SO == "Windows" else 'clear')

def esperar():
    input(f"\n{C['info']}   ⏎ Enter para continuar...{C['reset']}")

def error(mensaje):
    print(f"\n{C['error']}   ❌  {mensaje}{C['reset']}")

def exito(mensaje):
    print(f"\n{C['exito']}   ✅  {mensaje}{C['reset']}")

def info(mensaje):
    print(f"\n{C['info']}   ℹ️  {mensaje}{C['reset']}")

def input_con_salida(mensaje):
    valor = input(mensaje)
    if valor.lower() in ["salir", "exit", "sair"]:
        info(T['cancelar'])
        return None
    return valor

def obtener_ruta(archivo):
    archivo = os.path.expanduser(archivo)
    if not "/" in archivo and not "\\" in archivo:
        if config.get("ruta_base") and os.path.exists(config["ruta_base"]):
            ruta_base = config["ruta_base"]
            if not ruta_base.endswith("/") and not ruta_base.endswith("\\"):
                ruta_base += "/"
            archivo = ruta_base + archivo
        else:
            archivo = RUTA_DESCARGAS + archivo
    return archivo

def obtener_ruta_busqueda():
    """Retorna la ruta donde se buscan/guardan archivos (configurable o descargas)"""
    if config.get("ruta_base") and os.path.exists(config["ruta_base"]):
        return config["ruta_base"]
    return RUTA_DESCARGAS

def listar_hbf():
    ruta = obtener_ruta_busqueda()
    try:
        archivos = [f for f in os.listdir(ruta) if f.endswith(".hbf")]
    except:
        archivos = []
    if not archivos:
        info(f"No hay archivos .hbf en {ruta}")
        return []
    print(f"\n   📂  Archivos .hbf en {ruta} ({len(archivos)}):")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    return archivos

def mostrar_menu():
    limpiar()
    print(f"""
    {C['titulo']}╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     {T['titulo']}  v{VERSION}      ║
    ║                                                      ║
    ║     {T['creado_por']}                        ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝{C['reset']}
    """)
    print(f"{C['info']}{T['guardado_en']}{C['reset']}")
    print(f"   📂  {RUTA_DESCARGAS}\n")
    if config.get("ruta_base"):
        print(f"{C['info']}{T['ruta_actual']}{C['reset']}")
        print(f"   📂  {config['ruta_base']}\n")
    print(f"{C['menu']}    {T['menu']}{C['reset']}\n")
    print("    ┌────────────────────────────────────────────┐")
    for i, opcion in enumerate(T['opciones'], 1):
        print(f"    │  {i:2d}.  {opcion:<28}│")
    print("    └────────────────────────────────────────────┘")
    print(f"\n{C['info']}   {T['recordatorio']}{C['reset']}")

def crear_hbf():
    print("\n   📝  CREAR HBF\n")
    nombre = input_con_salida("   📄  Nombre del archivo: ")
    if nombre is None:
        return
    if not nombre.endswith(".hbf"):
        nombre += ".hbf"
    archivo = obtener_ruta(nombre)
    titulo = input_con_salida("   🏷️  Título: ") or "Sin título"
    if titulo is None:
        return
    autor = input_con_salida("   👤  Autor: ") or "Anónimo"
    if autor is None:
        return
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
    nombre = input_con_salida("   📄  Nombre del archivo: ")
    if nombre is None:
        return
    archivo = obtener_ruta(nombre)
    
    # Si no existe con .hbf, probar con .enc
    if not os.path.exists(archivo) and not archivo.endswith(".enc"):
        if os.path.exists(archivo + ".enc"):
            archivo = archivo + ".enc"
    
    if not os.path.exists(archivo):
        error("El archivo no existe.")
        return
    
    if archivo.endswith(".enc"):
        clave = input_con_salida("   🔑  Contraseña: ")
        if clave is None:
            return
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            import base64 as b64
            with open(archivo, 'rb') as f:
                salt = f.read(16)
                datos_cifrados = f.read()
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
            key = b64.urlsafe_b64encode(kdf.derive(clave.encode()))
            fernet = Fernet(key)
            contenido = fernet.decrypt(datos_cifrados).decode('utf-8')
            print("\n   📖  CONTENIDO DESCIFRADO:")
            print("   " + "=" * 48)
            print(contenido)
            print("   " + "=" * 48)
        except ImportError:
            error("Se requiere cryptography. Instalá: pip install cryptography")
        except Exception as e:
            error(f"No se pudo descifrar: {e}")
        return
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    print("\n   📖  CONTENIDO:")
    print("   " + "=" * 48)
    print(contenido)
    print("   " + "=" * 48)

def guardar_binario():
    print("\n   🖼️  GUARDAR BINARIO\n")
    origen = input_con_salida("   📂  Ruta del archivo a guardar (ej: ~/Imagenes/foto.jpg): ")
    if origen is None:
        return
    origen = os.path.expanduser(origen)
    if not os.path.exists(origen):
        error("El archivo no existe")
        return
    destino = input_con_salida("   📁  Nombre del archivo HBF destino: ")
    if destino is None:
        return
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
    origen = input_con_salida("   📁  Archivo HBF origen: ")
    if origen is None:
        return
    origen = obtener_ruta(origen)
    if not os.path.exists(origen):
        error("El archivo no existe")
        return
    salida = input_con_salida("   📂  Nombre para extraer: ")
    if salida is None:
        return
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
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    print("\n   📝  Nuevo texto (Enter dos veces para terminar; escribí 'salir' para cancelar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea.lower() in ["salir", "exit", "sair"]:
            info(T['cancelar'])
            return
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "TEXTO", "\n".join(lineas))

def editar_listas():
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    print("\n   📝  Nueva lista (Enter dos veces para terminar; escribí 'salir' para cancelar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea.lower() in ["salir", "exit", "sair"]:
            info(T['cancelar'])
            return
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "LISTAS", "\n".join(lineas))

def editar_notas():
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    print("\n   📝  Nuevas notas (Enter dos veces para terminar; escribí 'salir' para cancelar):")
    lineas = []
    while True:
        linea = input("   > ")
        if linea.lower() in ["salir", "exit", "sair"]:
            info(T['cancelar'])
            return
        if linea == "":
            break
        lineas.append(linea)
    editar_bloque(archivo, "NOTAS", "\n".join(lineas))

def editar_numerico():
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    nuevo = input_con_salida("   📝  Nuevo numerico: ")
    if nuevo is None:
        return
    editar_bloque(archivo, "NUMERICO", nuevo)

def editar_titulos():
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    nuevo = input_con_salida("   📝  Nuevo titulo: ")
    if nuevo is None:
        return
    editar_bloque(archivo, "TITULOS", nuevo)

def editar_metadatos():
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
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
    nuevo_titulo = input_con_salida(f"      Título [{metadatos.get('titulo', 'Sin título')}]: ") or metadatos.get('titulo', 'Sin título')
    if nuevo_titulo is None:
        return
    nuevo_autor = input_con_salida(f"      Autor [{metadatos.get('autor', 'Anónimo')}]: ") or metadatos.get('autor', 'Anónimo')
    if nuevo_autor is None:
        return
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
    archivo = input_con_salida("   📄  Archivo HBF: ")
    if archivo is None:
        return
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
    print("      4. XML")
    print("      5. CSV")
    print("      6. YAML")
    formato = input_con_salida("   👉  Opción: ")
    if formato is None:
        return
    ruta_salida = obtener_ruta_busqueda()
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]
    if formato == "1":
        salida = ruta_salida + nombre_base + ".txt"
        texto = re.search(r'\[TEXTO\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        if texto:
            with open(salida, 'w', encoding='utf-8') as f:
                f.write(texto.group(1).strip())
            exito(f"Exportado a TXT: {salida}")
        else:
            error("No se encontró texto")
    elif formato == "2":
        salida = ruta_salida + nombre_base + ".json"
        bloques = re.findall(r'\[([A-Z]+)\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        datos = {nombre: valor.strip() for nombre, valor in bloques}
        with open(salida, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2)
        exito(f"Exportado a JSON: {salida}")
    elif formato == "3":
        salida = ruta_salida + nombre_base + ".md"
        md = f"# {nombre_base}\n\n"
        texto = re.search(r'\[TEXTO\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        if texto:
            md += texto.group(1).strip() + "\n\n"
        with open(salida, 'w', encoding='utf-8') as f:
            f.write(md)
        exito(f"Exportado a MD: {salida}")
    elif formato == "4":
        salida = ruta_salida + nombre_base + ".xml"
        bloques = re.findall(r'\[([A-Z]+)\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        xml = "<hbf>\n"
        for nombre, valor in bloques:
            xml += f"  <{nombre.lower()}>\n"
            xml += f"    {valor.strip()}\n"
            xml += f"  </{nombre.lower()}>\n"
        xml += "</hbf>"
        with open(salida, 'w', encoding='utf-8') as f:
            f.write(xml)
        exito(f"Exportado a XML: {salida}")
    elif formato == "5":
        salida = ruta_salida + nombre_base + ".csv"
        bloques = re.findall(r'\[([A-Z]+)\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        csv = "BLOQUE,CONTENIDO\n"
        for nombre, valor in bloques:
            csv += f"{nombre},{valor.strip()}\n"
        with open(salida, 'w', encoding='utf-8') as f:
            f.write(csv)
        exito(f"Exportado a CSV: {salida}")
    elif formato == "6":
        salida = ruta_salida + nombre_base + ".yaml"
        bloques = re.findall(r'\[([A-Z]+)\]\n(.*?)(?=\n\[|\Z)', contenido, re.DOTALL)
        yaml = ""
        for nombre, valor in bloques:
            yaml += f"{nombre.lower()}:\n"
            for linea in valor.strip().split('\n'):
                yaml += f"  {linea}\n"
        with open(salida, 'w', encoding='utf-8') as f:
            f.write(yaml)
        exito(f"Exportado a YAML: {salida}")
    else:
        error("Opción no válida")

def buscar_hbf():
    print("\n   🔍  BUSCAR\n")
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
    archivo = obtener_ruta(archivo)
    if not os.path.exists(archivo):
        error("El archivo no existe")
        return
    busqueda = input_con_salida("   🔍  Palabra: ")
    if busqueda is None:
        return
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
    archivo = input_con_salida("   📄  Archivo: ")
    if archivo is None:
        return
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

def cambiar_ruta_base():
    print("\n   📁  CAMBIAR RUTA BASE\n")
    ruta_actual = config.get("ruta_base") or RUTA_DESCARGAS
    print(f"   {T['ruta_actual']} {ruta_actual}")
    nueva = input_con_salida(f"   {T['nueva_ruta']} ")
    if nueva is None:
        return
    if nueva.strip() == "":
        config["ruta_base"] = ""
        guardar_config(config)
        exito("Ruta base restablecida a Descargas")
    else:
        nueva = os.path.expanduser(nueva)
        if os.path.exists(nueva):
            config["ruta_base"] = nueva
            guardar_config(config)
            exito(f"Ruta base cambiada a: {nueva}")
        else:
            error("La ruta no existe")

def cambiar_colores():
    print("\n   🎨  COLORES\n")
    print("   1. 🔵  Azul")
    print("   2. 🟢  Verde")
    print("   3. 🔴  Rojo")
    print("   4. 🟡  Amarillo")
    print("   5. 🟣  Morado")
    opcion = input_con_salida("   👉  Elegí: ")
    if opcion is None:
        return
    colores = {"1": "azul", "2": "verde", "3": "rojo", "4": "amarillo", "5": "morado"}
    color_elegido = colores.get(opcion)
    if color_elegido:
        config["color"] = color_elegido
        guardar_config(config)
        exito(f"Color cambiado a {color_elegido}. Reiniciá HBF para ver los cambios.")
    else:
        error("Opción no válida")

def combinar_hbf():
    print("\n   🔗  COMBINAR HBF\n")
    archivos = listar_hbf()
    if not archivos:
        return
    print("\n   📄  Primer archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion1 = input_con_salida("   👉  Opción: ")
    if opcion1 is None:
        return
    try:
        archivo1 = archivos[int(opcion1) - 1]
    except:
        error("Opción no válida")
        return
    print("\n   📄  Segundo archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion2 = input_con_salida("   👉  Opción: ")
    if opcion2 is None:
        return
    try:
        archivo2 = archivos[int(opcion2) - 1]
    except:
        error("Opción no válida")
        return
    print("\n   🔄  Orden:")
    print(f"      1. {archivo1} primero")
    print(f"      2. {archivo2} primero")
    orden = input_con_salida("   👉  Opción: ")
    if orden is None:
        return
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
    nombre_salida = input_con_salida("\n   📄  Nombre nuevo archivo: ")
    if nombre_salida is None:
        return
    if not nombre_salida.endswith(".hbf"):
        nombre_salida += ".hbf"
    salida = obtener_ruta(nombre_salida)
    cabecera = f"[HBF]\nVersion: {VERSION}\nMagic: HBF\nFecha: {datetime.now().isoformat()}\n\n"
    with open(salida, 'w', encoding='utf-8') as f:
        f.write(cabecera + combinado + "\n[FIN]\n")
    exito(f"Archivo combinado: {salida}")

def proteger_hbf():
    print("\n   🔒  PROTEGER CON CLAVE\n")
    archivos = listar_hbf()
    if not archivos:
        return
    print("\n   📄  Elegí el archivo:")
    for i, arch in enumerate(archivos, 1):
        print(f"      {i}. {arch}")
    opcion = input_con_salida("   👉  Opción: ")
    if opcion is None:
        return
    try:
        archivo = archivos[int(opcion) - 1]
    except:
        error("Opción no válida")
        return
    ruta = obtener_ruta(archivo)
    
    # Verificar si existe archivo cifrado
    tiene_cifrado = os.path.exists(ruta + ".enc")
    
    print("\n   🔑  Operación:")
    print("      1. Cifrar")
    if tiene_cifrado:
        print("      2. Descifrar")
    operacion = input_con_salida("   👉  Opción: ")
    if operacion is None:
        return
    
    # Importar cryptography
    try:
        from cryptography.fernet import Fernet
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        import base64 as b64
    except ImportError:
        error("Se requiere cryptography. Instalá: pip install cryptography")
        return
    
    if operacion == "1":
        clave = input_con_salida("   🔑  Clave: ")
        if clave is None:
            return
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
        key = b64.urlsafe_b64encode(kdf.derive(clave.encode()))
        fernet = Fernet(key)
        datos_cifrados = fernet.encrypt(contenido.encode())
        with open(ruta + ".enc", 'wb') as f:
            f.write(salt + datos_cifrados)
        exito(f"Archivo cifrado: {ruta}.enc")
        info("Recordá la clave. El archivo original NO fue eliminado.")
    elif operacion == "2":
        if not tiene_cifrado:
            error("No existe archivo cifrado (.enc)")
            return
        clave = input_con_salida("   🔑  Clave: ")
        if clave is None:
            return
        with open(ruta + ".enc", 'rb') as f:
            salt = f.read(16)
            datos_cifrados = f.read()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
        key = b64.urlsafe_b64encode(kdf.derive(clave.encode()))
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
            proteger_hbf()
        elif opcion == "18":
            cambiar_ruta_base()
        elif opcion == "19":
            limpiar()
            print(f"\n   {T['salir']}")
            print(f"   📁  {T['archivos_en']} {RUTA_DESCARGAS}\n")
            break
        else:
            error(T['error'])
        esperar()

if __name__ == "__main__":
    main()
