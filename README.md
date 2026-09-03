# 📁 HBF - Hybrid Binary Format

**HBF** es un formato de archivo todo en uno que combina texto, binario, metadatos, listas y datos numéricos en un solo archivo. Creado desde Termux, diseñado para ser simple, útil y portable.

---

## 🚀 Características

| Característica | Descripción |
|----------------|-------------|
| 📝 **Texto** | Contenido principal del archivo |
| 📊 **Metadatos** | Título, autor y fecha |
| 🖼️ **Binario** | Guarda imágenes, archivos, etc. en base64 |
| 📋 **Listas** | Listas jerárquicas |
| 🔢 **Numérico** | Datos numéricos estructurados |
| 📌 **Notas** | Notas personales o técnicas |
| 🌍 **12 idiomas** | Español, Inglés, Portugués, Francés, Alemán, Italiano, Japonés, Chino, Ruso, Coreano, Árabe e Hindi |
| 🔒 **Cifrado** | Protege archivos con contraseña (AES) |
| 🔗 **Combinar** | Une dos archivos HBF en uno |
| 📤 **Exportar** | Exporta a TXT, JSON, MD, XML, CSV, YAML, HTML, INI o TOML |
| 📥 **Importar** | Importa desde TXT, JSON, XML, YAML, TOML, INI, CSV, MD o HTML |
| 🔍 **Buscar** | Busca palabras dentro del archivo |
| 📂 **Listar** | Muestra todos los HBF en la carpeta |
| 💾 **Configurable** | Guarda colores, ruta base e idioma en un archivo de configuración |
| 🖥️ **Multiplataforma** | Funciona en Termux (Android), Linux y Windows |
| 🗄️ **Bloque SQL** | Edita y exporta a SQLite |

---

## 📦 Instalación

### Opción 1: Desde PyPI (recomendado)

pip install hbf-hyper
hbf

Opción 2: Desde el código fuente

git clone https://github.com/lucassogarayDA/hbf.git
cd hbf
python hbf.py


Opción 3: Desde el paquete .deb (Termux/Linux)

dpkg -i hbf_3.0.1_all.deb
hbf

---

🛠️ Uso

Ejecutá el comando y seguí el menú interactivo:

hbf

Al abrir, podés elegir idioma o usar la detección automática entre 12 idiomas disponibles.

---

📋 Menú completo (36 opciones)

```
  1.  📝 Crear HBF
  2.  📖 Leer HBF
  3.  📥 Importar a HBF
  4.  ✏️ Editar TEXTO
  5.  📋 Editar LISTAS
  6.  💬 Editar NOTAS
  7.  🔢 Editar NUMERICO
  8.  🏷️ Editar TITULOS
  9.  📝 Editar METADATOS
 10.  💻 Editar CODE
 11.  🌐 Editar API
 12.  🗄️ Editar SQL
 13.  📦 Editar DEPLOY
 14.  🧪 Editar TEST
 15.  📊 Editar SCHEMA
 16.  🔐 Editar ENV
 17.  ⚙️ Editar CONFIG
 18.  📖 Editar DOCS
 19.  ⚡ Editar COMANDOS
 20.  🐍 Editar SCRIPTS
 21.  📦 Editar DEPENDENCIAS
 22.  🖼️ Gestionar imágenes
 23.  🖼️ Guardar binario
 24.  📤 Extraer binario
 25.  📤 Exportar
 26.  🔍 Buscar
 27.  📂 Listar HBF
 28.  📊 Estadísticas
 29.  📜 Historial
 30.  🔗 Combinar HBF
 31.  🔒 Proteger con clave
 32.  📦 Generar desde HBF
 33.  📁 Cambiar ruta base
 34.  🎨 Colores
 35.  🌍 Cambiar idioma
 36.  📦 Activar/desactivar compresión
 37.  🚪 Salir
```

---

📂 Ejemplo de archivo HBF

```
[HBF]
Version: 3.0.1
Magic: HBF
Fecha: 2026-09-03T00:00:00

[METADATOS]
{
  "titulo": "Mi proyecto",
  "autor": "Lucas Sogaray"
}

[TEXTO]
Este es el contenido principal del archivo.

[LISTAS]
- Tarea 1
- Tarea 2
  - Subtarea A

[FIN]
```

---

🔒 Proteger con contraseña

hbf
Opción 31 → Elegir archivo → Opción 1 (Cifrar) → Ingresar contraseña


El archivo cifrado se guarda con extensión .hbf.enc

---

🛣️ Roadmap

☑ Formato HBF básico
☑ Binario (base64)
☑ Edición de bloques
☑ Exportar a 9 formatos
☑ Importar desde 9 formatos
☑ Búsqueda
☑ Estadísticas
☑ Combinar HBF
☑ Cifrado con contraseña
☑ 12 idiomas completos
☑ Paquete .deb
☑ Multiplataforma (Android, Linux, Windows)
☑ Ruta base configurable
☑ Gestión de imágenes
☑ Historial de cambios
☑ Generación desde HBF
☑ Compresión activable desde TUI

---

📄 Licencia

MIT — Podés usarlo, modificarlo y distribuirlo libremente.

---

👤 Autor

Lucas Sogaray

· GitHub: @LucassogarayDA
· Email: lucassogaray72@gmail.com

---

⭐ ¿Te gusta HBF?

Si te gusta el proyecto, dejale una estrella en GitHub ⭐ y compartilo con otros.

