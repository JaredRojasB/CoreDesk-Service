# Documentación Técnica — Sitio Web Vantyx

---

> **AVISO DE PROPIEDAD INTELECTUAL**
>
> Este código fuente, su estructura, diseño y contenido son propiedad exclusiva de
> **Vantyx** (vantyxsupportti@gmail.com · instagram.com/vantyxti).
> Queda estrictamente prohibida su reproducción total o parcial, distribución,
> modificación o uso sin autorización expresa y por escrito de Vantyx.
> © 2025 Vantyx. Todos los derechos reservados.

---

## Índice

1. [Descripción general](#1-descripción-general)
2. [Estructura de archivos](#2-estructura-de-archivos)
3. [Cómo generar y publicar el sitio](#3-cómo-generar-y-publicar-el-sitio)
4. [build.py — Script de construcción](#4-buildpy--script-de-construcción)
5. [template.html — Estructura general](#5-templatehtml--estructura-general)
6. [Sección: Variables CSS y estilos globales](#6-sección-variables-css-y-estilos-globales)
7. [Sección: NAV — Barra de navegación](#7-sección-nav--barra-de-navegación)
8. [Sección: HERO — Portada principal](#8-sección-hero--portada-principal)
9. [Sección: SERVICIOS](#9-sección-servicios)
10. [Sección: PRECIOS](#10-sección-precios)
11. [Sección: BLOG](#11-sección-blog)
12. [Sección: FAQ](#12-sección-faq)
13. [Sección: NOSOTROS — Misión, Visión, Objetivo](#13-sección-nosotros--misión-visión-objetivo)
14. [Sección: CONTACTO](#14-sección-contacto)
15. [Sección: FOOTER](#15-sección-footer)
16. [Componente: Botón flotante de Instagram](#16-componente-botón-flotante-de-instagram)
17. [JavaScript — Interactividad](#17-javascript--interactividad)
18. [Cómo modificar contenido](#18-cómo-modificar-contenido)
19. [Integraciones pendientes](#19-integraciones-pendientes)

---

## 1. Descripción general

El sitio web de Vantyx es un sitio **estático de una sola página** (one-page)
construido con HTML, CSS y JavaScript vanilla (sin frameworks). Un script en
Python genera el archivo `index.html` final a partir de una plantilla.

El sitio está diseñado para publicarse directamente en **GitHub Pages** sin
necesidad de servidor, base de datos ni dependencias externas más allá de
Google Fonts.

**Stack tecnológico:**
- `Python 3` — script de build
- `HTML5 / CSS3 / JavaScript` — sin frameworks
- `Google Fonts` — tipografías Syne y DM Sans
- `GitHub Pages` — hosting gratuito

---

## 2. Estructura de archivos

```
vantyx/
├── build.py          → Script Python que genera el sitio
├── template.html     → Código fuente completo del sitio (editar aquí)
├── index.html        → Archivo generado (NO editar directamente)
├── DOCUMENTACION.md  → Este archivo
└── README.md         → Guía rápida de deploy
```

> ⚠️ **Importante:** Nunca edites `index.html` directamente.
> Todos los cambios van en `template.html`. Luego ejecutas `python3 build.py`
> para regenerar el `index.html`.

---

## 3. Cómo generar y publicar el sitio

### Generar el sitio localmente

```bash
python3 build.py
```

Esto lee `template.html` y escribe el contenido en `index.html`.

### Publicar en GitHub Pages

```bash
# Primera vez
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main

# Actualizaciones posteriores
git add .
git commit -m "Descripción del cambio"
git push
```

Luego en GitHub → **Settings → Pages → Deploy from branch → main / (root)**.

Tu sitio estará disponible en: `https://TU_USUARIO.github.io/TU_REPO/`

### Conectar dominio personalizado (cuando esté listo)

1. En tu registrador de dominio (Cloudflare recomendado), agrega registros tipo A:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
2. En GitHub → Settings → Pages → Custom domain → escribe `vantyx.mx`
3. Activa **Enforce HTTPS**

---

## 4. build.py — Script de construcción

```python
# build.py
HTML_TEMPLATE = open("template.html", encoding="utf-8").read()

def build():
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)

if __name__ == "__main__":
    build()
```

**¿Qué hace?**
- Lee el contenido completo de `template.html`
- Lo escribe tal cual en `index.html`
- El script está pensado para escalar: en el futuro puede inyectar variables
  dinámicas (fecha, versión, contenido de un JSON de servicios, etc.)

---

## 5. template.html — Estructura general

El archivo se divide en las siguientes partes, en este orden:

```
<head>
  - Meta tags SEO
  - Fuentes Google (Syne + DM Sans)
  - <style> con todo el CSS del sitio

<body>
  - <nav>          → Barra de navegación fija
  - #hero          → Sección portada
  - #servicios     → Tarjetas de servicios
  - #precios       → Planes y tarifas
  - #blog          → Artículos del blog
  - #faq           → Preguntas frecuentes (acordeón)
  - #nosotros      → Misión, Visión y Objetivo
  - #contacto      → Formulario + datos de contacto
  - <footer>       → Pie de página
  - .ig-float      → Botón flotante de Instagram
  - <script>       → JavaScript de interactividad
```

---

## 6. Sección: Variables CSS y estilos globales

Ubicación en el archivo: dentro de `<style>`, al inicio.

```css
:root {
  --navy:    #1a2340;   /* Azul marino oscuro — color principal de textos y fondos */
  --navy-2:  #0f1829;   /* Azul marino más oscuro — fondo de secciones oscuras */
  --steel:   #5a6478;   /* Gris azulado — textos secundarios y nav links */
  --accent:  #2d6cdf;   /* Azul acento — botones, highlights, íconos */
  --accent-2:#4a8fff;   /* Azul acento claro — hovers, detalles */
  --light:   #f0f2f5;   /* Fondo gris claro — secciones alternas */
  --white:   #ffffff;
  --card-bg: #f7f8fa;   /* Fondo de tarjetas */
  --border:  #e2e6ed;   /* Color de bordes */
  --text:    #1a2340;   /* Color de texto principal */
  --muted:   #6b7280;   /* Texto apagado / descripciones */
  --radius:  12px;      /* Border radius estándar de tarjetas */
  --transition: 0.3s cubic-bezier(0.4,0,0.2,1); /* Transición suave estándar */
}
```

**Para cambiar los colores del sitio**, solo modifica estas variables.
El cambio se aplica automáticamente en todo el sitio.

**Clases de animación:**
- `.fade-in` — elemento invisible al cargar, aparece al hacer scroll
- `.fade-in.visible` — estado visible (lo agrega JavaScript automáticamente)

---

## 7. Sección: NAV — Barra de navegación

**HTML:** bloque `<nav>` al inicio del `<body>`

**¿Qué hace?**
- Barra fija en la parte superior de la pantalla (`position: fixed`)
- Fondo semitransparente con efecto de cristal (`backdrop-filter: blur`)
- Logo SVG inline a la izquierda (brackets + cilindro de base de datos)
- Links de navegación que hacen scroll suave a cada sección
- Botón "Contacto" destacado en navy a la derecha

**Para agregar un nuevo link al nav:**
```html
<li><a href="#nueva-seccion">Nueva Sección</a></li>
```

**Para cambiar el nombre de la empresa en el nav:**
```html
<span class="nav-brand">Van<span>tyx</span></span>
<!-- "Van" aparece en navy, "tyx" aparece en azul acento -->
```

**Responsive:** en pantallas menores a 768px los links desaparecen
(`.nav-links { display: none }`). Pendiente implementar menú hamburguesa
para mobile en versión futura.

---

## 8. Sección: HERO — Portada principal

**HTML:** `<section id="hero">`

**¿Qué hace?**
- Ocupa el 100% de la pantalla al entrar al sitio (`min-height: 100vh`)
- Fondo degradado claro con una cuadrícula decorativa muy sutil
- Brilla radial azul en la esquina superior derecha (efecto "glow")
- Badge animado con punto pulsante
- Título principal con palabra en acento azul (`<em>`)
- Subtítulo descriptivo
- Dos botones: primario "Ver servicios" y secundario "Ver precios"
- Fila de 3 estadísticas en la parte inferior

**Para cambiar el texto principal:**
```html
<h1 class="hero-title">Tu empresa merece<br/>tecnología de <em>verdad</em></h1>
```

**Para cambiar las estadísticas:**
```html
<div class="stat-item">
  <div class="stat-number">11</div>        <!-- número grande -->
  <div class="stat-label">Servicios disponibles</div>  <!-- texto debajo -->
</div>
```

---

## 9. Sección: SERVICIOS

**HTML:** `<section id="servicios">`

**¿Qué hace?**
- Grid responsivo de tarjetas de servicios (mínimo 255px por columna)
- Cada tarjeta tiene: ícono SVG, título, descripción
- Al hacer hover: sube 4px, aparece línea de color en la parte superior
- Etiqueta "Nuevo" opcional en la esquina superior derecha

**Servicios actuales (11):**
Desarrollo Web, Desarrollo de Software a Medida, Soporte Remoto,
Mantenimiento Preventivo, Mantenimiento Correctivo, Respaldo y Recuperación,
Seguridad Informática, Redes e Infraestructura, Cloud y Migración,
Automatización de Procesos, Capacitación Tecnológica, Consultoría Tecnológica.

**Para agregar un nuevo servicio:**
```html
<div class="service-card fade-in">
  <!-- Opcional: quitar si no es nuevo -->
  <span class="service-new">Nuevo</span>

  <!-- Ícono: reemplaza el SVG interno con cualquier ícono de Lucide Icons -->
  <div class="service-icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="#2d6cdf" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <!-- pega el path del ícono aquí -->
    </svg>
  </div>

  <h3>Nombre del Servicio</h3>
  <p>Descripción breve del servicio, máximo 2 líneas.</p>
</div>
```

> Los íconos usados son de **Lucide Icons** (lucide.dev), todos en estilo
> outline con `stroke="#2d6cdf"` para mantener consistencia visual.

---

## 10. Sección: PRECIOS

**HTML:** `<section id="precios">`

**¿Qué hace?**
- Grid de tarjetas de precios (mínimo 280px por columna)
- Cada tarjeta muestra: categoría, nombre del plan, descripción, precio,
  lista de características y botón de acción
- La tarjeta con clase `.featured` tiene borde azul y badge "Más popular"

**Tarifas actuales (MXN con IVA incluido):**

| Servicio | Precio |
|---|---|
| Visita Preventiva | $350 / equipo |
| Plan Mensual Empresarial | $2,800 / mes |
| Auditoría de Seguridad | $4,500 único |
| Backup Empresarial | $1,200 / mes |
| Sitio Corporativo | desde $12,000 |
| Software a Medida | desde $25,000 |

**Para cambiar un precio:**
```html
<span class="price-amount">2,800</span>
<span class="price-period">/ mes</span>
```

**Para marcar una tarjeta como destacada:**
```html
<div class="pricing-card featured fade-in">
  <div class="pricing-badge">⭐ Más popular</div>
  ...
</div>
```

**Para agregar una característica a un plan:**
```html
<ul class="pricing-features">
  <li>Nueva característica aquí</li>
</ul>
```

---

## 11. Sección: BLOG

**HTML:** `<section id="blog">`

**¿Qué hace?**
- Grid de 4 tarjetas de artículos de muestra
- Cada tarjeta tiene: imagen de fondo degradada con emoji, etiqueta de
  categoría, título, resumen, tiempo de lectura y link "Leer más"
- Los artículos actualmente apuntan a `#contacto` (el blog completo es
  una integración futura)

**Artículos actuales:**
1. 5 señales de que tu equipo necesita mantenimiento urgente
2. Cómo proteger tu empresa del ransomware en 2025
3. ¿Cuándo necesita tu empresa un sistema a medida?
4. Google Workspace vs Microsoft 365

**Para agregar un artículo:**
```html
<div class="blog-card fade-in">
  <!-- Opciones de fondo: blog-thumb-1 (azul), -2 (verde), -3 (rojo), -4 (naranja) -->
  <div class="blog-thumb blog-thumb-1">🖥️</div>
  <div class="blog-body">
    <span class="blog-tag">Categoría</span>
    <h3>Título del artículo</h3>
    <p>Resumen breve en 1-2 líneas.</p>
    <div class="blog-meta">
      <span>5 min lectura</span>
      <a href="#" class="blog-read-more">Leer más →</a>
    </div>
  </div>
</div>
```

---

## 12. Sección: FAQ

**HTML:** `<section id="faq">`

**¿Qué hace?**
- Layout de dos columnas: texto descriptivo a la izquierda, preguntas a la derecha
- Acordeón interactivo: solo una pregunta abierta a la vez
- La animación de apertura/cierre usa `max-height` en CSS para una
  transición suave

**Preguntas actuales (6):**
1. ¿Atienden a empresas de cualquier tamaño?
2. ¿Cuánto tarda desarrollar un sistema a medida?
3. ¿El soporte remoto es seguro?
4. ¿En qué zonas brindan servicio presencial?
5. ¿Ofrecen contratos anuales?
6. ¿Facturan? ¿Trabajan con empresas formales?

**Para agregar una pregunta:**
```html
<div class="faq-item">
  <button class="faq-question" onclick="toggleFaq(this)">
    ¿Tu pregunta aquí?
    <span class="faq-icon">+</span>
  </button>
  <div class="faq-answer">
    Respuesta detallada aquí. Puede ser tan larga como necesites.
  </div>
</div>
```

**Cómo funciona el acordeón (JavaScript):**
```javascript
function toggleFaq(btn) {
  const answer = btn.nextElementSibling; // obtiene el div de respuesta
  const isOpen = answer.classList.contains('open');
  // cierra todos los abiertos
  document.querySelectorAll('.faq-answer.open').forEach(...);
  // si estaba cerrado, lo abre
  if (!isOpen) { answer.classList.add('open'); btn.classList.add('open'); }
}
```

---

## 13. Sección: NOSOTROS — Misión, Visión, Objetivo

**HTML:** `<section id="nosotros">`

**¿Qué hace?**
- Fondo oscuro navy para contraste visual con las secciones anteriores
- Tres tarjetas con la identidad corporativa de Vantyx

**Contenido actual:**

| | |
|---|---|
| **Misión** | Brindar soluciones tecnológicas accesibles, eficientes y de alta calidad |
| **Visión** | Ser el referente tecnológico integral de mayor confianza en México |
| **Objetivo** | Optimizar la operación de los clientes reduciendo costos y mejorando productividad |

**Para modificar:**
```html
<div class="mvv-card fade-in">
  <div class="mvv-label">Misión</div>   <!-- etiqueta superior -->
  <h3>Título corto de la tarjeta</h3>
  <p>Texto descriptivo de la misión.</p>
</div>
```

---

## 14. Sección: CONTACTO

**HTML:** `<section id="contacto">`

**¿Qué hace?**
- Layout de dos columnas: información de contacto a la izquierda,
  formulario a la derecha
- El formulario actualmente no envía datos (es visual). Para activarlo
  se debe conectar a Formspree o EmailJS (ver sección 19)

**Datos de contacto actuales:**
- Email: `vantyxsupportti@gmail.com`
- Instagram: `@vantyxti` → `https://www.instagram.com/vantyxti/`
- Ubicación: Guadalajara, Jalisco, México

**Para actualizar el correo:**
Busca `vantyxsupportti@gmail.com` en `template.html` y reemplázalo.

**Para agregar el teléfono cuando esté disponible:**
```html
<div class="contact-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
       stroke="#2d6cdf" stroke-width="2">
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 ..."/>
  </svg>
  +52 (33) 0000-0000
</div>
```

---

## 15. Sección: FOOTER

**HTML:** bloque `<footer>` al final del `<body>`

**¿Qué hace?**
- Fondo navy oscuro
- Logo SVG + nombre de la empresa a la izquierda
- Texto de copyright al centro
- Links de navegación rápida a la derecha

**Para actualizar el año de copyright:**
```html
<span>© 2025 Vantyx · Guadalajara, México · Todos los derechos reservados.</span>
```

---

## 16. Componente: Botón flotante de Instagram

**HTML:** elemento `.ig-float` justo antes de `</body>`

**¿Qué hace?**
- Botón fijo en la esquina inferior derecha de la pantalla
- Fondo degradado con los colores de Instagram (morado → rojo → naranja)
- Al hacer hover sube 3px con sombra más intensa
- Abre el perfil de Instagram en una pestaña nueva

```html
<a href="https://www.instagram.com/vantyxti/"
   target="_blank"
   rel="noopener"
   class="ig-float"
   aria-label="Síguenos en Instagram">
  <!-- ícono SVG de Instagram -->
  @vantyxti
</a>
```

**Para cambiar el handle o URL:**
Busca `vantyxti` en `template.html` y reemplaza con el nuevo nombre.

**Para ocultar el botón temporalmente:**
Agrega `display: none` al selector `.ig-float` en los estilos CSS.

---

## 17. JavaScript — Interactividad

El JavaScript está al final del `<body>`, dentro de una etiqueta `<script>`.
No depende de ninguna librería externa.

### Función 1: Acordeón del FAQ

```javascript
function toggleFaq(btn) {
  const answer = btn.nextElementSibling;
  const isOpen = answer.classList.contains('open');
  // Cierra todos los elementos abiertos
  document.querySelectorAll('.faq-answer.open').forEach(a => a.classList.remove('open'));
  document.querySelectorAll('.faq-question.open').forEach(b => b.classList.remove('open'));
  // Si el elemento clickeado estaba cerrado, lo abre
  if (!isOpen) {
    answer.classList.add('open');
    btn.classList.add('open');
  }
}
```

### Función 2: Animaciones de scroll (IntersectionObserver)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    // Cuando el elemento entra en la ventana visible...
    if (entry.isIntersecting) {
      // ...agrega la clase 'visible' con un pequeño retraso escalonado
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
    }
  });
}, { threshold: 0.08 }); // Se activa cuando el 8% del elemento es visible

// Observa todos los elementos con clase 'fade-in'
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
```

### Función 3: Highlight de nav activo al hacer scroll

```javascript
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  const y = window.scrollY + 120; // offset para compensar la nav fija
  sections.forEach(s => {
    const link = document.querySelector('.nav-links a[href="#' + s.id + '"]');
    if (!link) return;
    // Determina si la sección actual está en el viewport
    const active = y >= s.offsetTop && y < s.offsetTop + s.offsetHeight;
    link.style.color = active ? 'var(--navy)' : '';
    link.style.fontWeight = active ? '700' : '';
  });
});
```

---

## 18. Cómo modificar contenido

### Cambiar textos
Edita directamente en `template.html`, luego ejecuta `python3 build.py`.

### Cambiar colores del sitio
Modifica las variables CSS en `:root { }` al inicio del bloque `<style>`.

### Agregar una nueva sección completa
1. Agrega el HTML de la sección en `template.html`
2. Agrega los estilos CSS correspondientes en el bloque `<style>`
3. Agrega el link en el `<nav>` y en el `<footer>`
4. Ejecuta `python3 build.py`

### Cambiar tipografía
Modifica el link de Google Fonts en el `<head>` y actualiza las variables
`font-family` en el CSS.

---

## 19. Integraciones pendientes

| Integración | Descripción | Herramienta sugerida |
|---|---|---|
| **Formulario funcional** | Que el formulario de contacto envíe correos reales | Formspree / EmailJS |
| **Dominio propio** | Conectar vantyx.mx o vantyx.com | Cloudflare Registrar |
| **Analytics** | Medir visitas, origen del tráfico y comportamiento | Google Analytics |
| **Número de teléfono** | Agregar cuando esté disponible | — |
| **Menú mobile** | Menú hamburguesa para pantallas pequeñas | JS vanilla |
| **Calendly** | Botón para agendar llamadas directamente | Calendly |

---

*Documentación generada para uso interno de Vantyx.*
*Última actualización: 2025.*
*© 2025 Vantyx. Código protegido. Todos los derechos reservados.*
