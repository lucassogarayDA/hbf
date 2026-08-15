```markdown
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
| 🌍 **Multilingüe** | Español / Inglés / Portugués (detección automática) |
| 🔒 **Cifrado** | Protege archivos con contraseña (AES) |
| 🔗 **Combinar** | Une dos archivos HBF en uno |
| 📤 **Exportar** | Exporta a TXT, JSON, MD, XML, CSV o YAML |
| 🔍 **Buscar** | Busca palabras dentro del archivo |
| 📂 **Listar** | Muestra todos los HBF en Download |
| 💾 **Configurable** | Guarda colores y ruta base en un archivo de configuración |
| 🖥️ **Multiplataforma** | Funciona en Termux (Android), Linux y Windows |

---

## 📦 Instalación

### Opción 1: Desde PyPI (recomendado)

```bash
pip install hbf-hyper
hbf
```

Opción 2: Desde el código fuente

```bash
git clone https://github.com/lucassogarayDA/hbf.git
cd hbf
python hbf.py
```

Opción 3: Desde el paquete .deb (Termux/Linux)

```bash
dpkg -i hbf_2.1.1_all.deb
hbf
```

Dependencias

· Python 3.7+
· cryptography (para el cifrado) — se instala automáticamente con pip

---

🛠️ Uso

Ejecutá el comando y seguí el menú interactivo:

```bash
hbf
```

Al abrir, podés elegir idioma o usar la detección automática:

```
  Select language / Elegí idioma:
  1. Español
  2. English
  3. Português
```

---

📋 Menú completo (19 opciones)

```
  1.  📝 Crear HBF
  2.  📖 Leer HBF
  3.  🖼️ Guardar binario
  4.  📤 Extraer binario
  5.  ✏️ Editar TEXTO
  6.  📋 Editar LISTAS
  7.  💬 Editar NOTAS
  8.  🔢 Editar NUMERICO
  9.  🏷️ Editar TITULOS
 10.  📝 Editar METADATOS
 11.  📤 Exportar
 12.  🔍 Buscar
 13.  📂 Listar HBF
 14.  📊 Estadísticas
 15.  🎨 Colores
 16.  🔗 Combinar HBF
 17.  🔒 Proteger con clave
 18.  📁 Cambiar ruta base
 19.  🚪 Salir
```

---

📂 Ejemplo de archivo HBF

```hbf
[HBF]
Version: 2.1.1
Magic: HBF
Fecha: 2026-08-15T00:00:00

[METADATOS]
{
  "titulo": "Mi proyecto",
  "autor": "Lucas Sogaray"
}

[TEXTO]
Este es el contenido principal del archivo.
Puede tener múltiples líneas.

[LISTAS]
- Tarea 1
- Tarea 2
  - Subtarea A
  - Subtarea B

[NOTAS]
Recordatorio: Subir a GitHub.

[FIN]
```

---

🧪 Probar HBF

Crear un archivo

```bash
hbf
Opción 1 → Nombre del archivo: prueba
```

Leer un archivo

```bash
hbf
Opción 2 → Nombre del archivo: prueba.hbf
```

Exportar a TXT

```bash
hbf
Opción 11 → Seleccionar archivo → Formato 1 (TXT)
```

---

🔒 Proteger con contraseña

```bash
hbf
Opción 17 → Elegir archivo → Opción 1 (Cifrar) → Ingresar contraseña
```

El archivo cifrado se guarda con extensión .hbf.enc

---

📁 Cambiar ruta base

Podés configurar una carpeta por defecto para importar archivos:

```bash
hbf
Opción 18 → Ingresar una ruta (ej: ~/Imagenes/)
```

---

📦 Crear el paquete .deb

```bash
mkdir -p hbf_package/DEBIAN
mkdir -p hbf_package/data/data/com.termux/files/usr/bin
cp hbf.py hbf_package/data/data/com.termux/files/usr/bin/hbf
chmod +x hbf_package/data/data/com.termux/files/usr/bin/hbf
echo "Package: hbf
Version: 2.1.1
Architecture: all
Maintainer: Lucas Sogaray <lucassogaray72@gmail.com>
Depends: python, python-cryptography
Description: Hybrid Binary Format - Un formato de archivo todo en uno" > hbf_package/DEBIAN/control
chmod 755 hbf_package/DEBIAN
dpkg-deb --build hbf_package
mv hbf_package.deb hbf_2.1.1_all.deb
```

---

🛣️ Roadmap

☑ Formato HBF básico
☑ Binario (base64)
☑ Edición de bloques
☑ Exportar a TXT, JSON, MD, XML, CSV y YAML
☑ Búsqueda
☑ Estadísticas
☑ Combinar HBF
☑ Cifrado con contraseña
☑ Idiomas (Español/Inglés/Portugués)
☑ Paquete .deb
☑ Multiplataforma (Android, Linux, Windows)
☑ Ruta base configurable
☐ Guardar configuración de colores
☐ Botón visible para salir de opciones

---

📄 Licencia

Este proyecto está bajo la licencia MIT. Podés usarlo, modificarlo y distribuirlo libremente.

---

👤 Autor

Lucas Sogaray

· GitHub: @LucassogarayDA
· Email: lucassogaray72@gmail.com

---

⭐ ¿Te gusta HBF?

Si te gusta el proyecto, dejale una estrella en GitHub ⭐ y compartilo con otros.

---

📬 Contacto

Si tenés preguntas, sugerencias o encontrás un error, podés abrir un Issue en GitHub o contactarme por email.

---

Hecho con 💻 y ☕ desde Termux

```
