# CoreDesk — Sitio Web Informativo

Sitio web estático generado con Python, listo para GitHub Pages.

## 🚀 Cómo usar

### 1. Generar el sitio
```bash
python3 build.py
```
Esto crea `index.html` en la misma carpeta.

### 2. Publicar en GitHub Pages

1. Crea un repositorio en GitHub (p. ej. `coredesk-web`)
2. Sube los archivos:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/<tu-usuario>/coredesk-web.git
   git push -u origin main
   ```
3. En GitHub → **Settings** → **Pages**
4. Source: **Deploy from a branch** → `main` → `/ (root)` → Save
5. Tu sitio estará disponible en:
   `https://<tu-usuario>.github.io/coredesk-web/`

## 📁 Estructura del proyecto

```
coredesk/
├── build.py      # Script Python que genera el sitio
├── index.html    # Sitio generado (este es el que sube GitHub Pages)
└── README.md     # Esta guía
```

## ✏️ Personalización

Edita `build.py` — toda la lógica y contenido están en la variable `HTML_TEMPLATE`:

- **Colores**: cambia las variables CSS en `:root { ... }`
- **Textos**: busca las secciones `#hero`, `#servicios`, `#nosotros`, `#contacto`
- **Contacto**: actualiza email, teléfono y ciudad en la sección `#contacto`

Después de editar, vuelve a ejecutar `python3 build.py` y sube los cambios.
