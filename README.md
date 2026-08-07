```markdown
# 📁 HBF - Hybrid Binary Format

**HBF** es un formato de archivo todo en uno que combina texto, binario, metadatos, listas y datos numéricos en un solo archivo. Creado desde Termux para ser simple, útil y portable.

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
| 🌍 **Bilingüe** | Español / Inglés (seleccionable al inicio) |
| 🔒 **Cifrado** | Protege archivos con contraseña (AES) |
| 🔗 **Combinar** | Une dos archivos HBF en uno |
| 📤 **Exportar** | Exporta a TXT, JSON o MD |
| 🔍 **Buscar** | Busca palabras dentro del archivo |
| 📂 **Listar** | Muestra todos los HBF en Download |

---

## 📦 Instalación

### Opción 1: Desde el paquete `.deb`

```bash
dpkg -i hbf_2.0.0_all.deb
```

Opción 2: Desde el código fuente

```bash
git clone https://github.com/LucassogarayDA/hbf.git
cd hbf
python hbf.py
```

Dependencias

· Python 3
· cryptography (para el cifrado)

```bash
pkg install python python-cryptography
```

---

🛠️ Uso

Ejecutá el comando y seguí el menú interactivo:

```bash
hbf
```

Al abrir, vas a poder elegir el idioma:

```
  Select language / Elegí idioma:
  1. Español
  2. English
```

---

📋 Menú completo

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
 17.  📲 Compartir
 18.  🔒 Proteger con clave
 19.  🚪 Salir
```

---

📂 Ejemplo de archivo HBF

```hbf
[HBF]
Version: 2.0.0
Magic: HBF
Fecha: 2026-08-07T00:00:00

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
Opción 18 → Elegir archivo → Opción 1 (Cifrar) → Ingresar contraseña
```

El archivo cifrado se guarda con extensión .hbf.enc

---

📦 Crear el paquete .deb

```bash
mkdir -p hbf_package/DEBIAN
mkdir -p hbf_package/data/data/com.termux/files/usr/bin
cp hbf.py hbf_package/data/data/com.termux/files/usr/bin/hbf
chmod +x hbf_package/data/data/com.termux/files/usr/bin/hbf
echo "Package: hbf
Version: 2.0.0
Architecture: all
Maintainer: Lucas Sogaray <lucassogaray72@gmail.com>
Depends: python, python-cryptography
Description: Hybrid Binary Format - Un formato de archivo todo en uno" > hbf_package/DEBIAN/control
chmod 755 hbf_package/DEBIAN
dpkg-deb --build hbf_package
mv hbf_package.deb hbf_2.0.0_all.deb
```

---

🛣️ Roadmap

☑ Formato HBF básico
☑ Binario (base64)
☑ Edición de bloques
☑ Exportar a TXT, JSON, MD
☑ Búsqueda
☑ Estadísticas
☑ Combinar HBF
☑ Cifrado con contraseña
☑ Idiomas (Español/Inglés)
☑ Paquete .deb
☐ Modo oscuro
☐ Guardar configuración de colores
☐ Compartir directamente por WhatsApp

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

---

## 💾 Guardar y subir

```bash
git add README.md
git commit -m "README actualizado con toda la info"
git push
```

---
