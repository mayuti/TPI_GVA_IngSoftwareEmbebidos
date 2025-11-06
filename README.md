# Trabajo Práctico Integrador – Ingeniería de Software en Sistemas Embebidos  
## Sistema de Guiado Vehicular Automatizado (GVA)

### 📘 Descripción del proyecto
Este repositorio contiene la documentación y entregables del proyecto **GVA (Sistema de Guiado Vehicular Automatizado)** desarrollado como parte de la materia **Ingeniería de Software en Sistemas Embebidos** de la **Especialización en Sistemas Embebidos – FIUNER**.

El proyecto busca aplicar metodologías de ingeniería de software al desarrollo de un sistema embebido que coordine un vehículo autónomo encargado de transportar materiales dentro de una planta industrial.

---

### 🧠 Objetivos principales
- Aplicar conceptos de especificación de requerimientos en sistemas embebidos.  
- Diseñar y documentar la arquitectura de software del GVA.  
- Desarrollar diagramas de contexto, dominio y casos de uso.  
- Mantener trazabilidad entre requerimientos, diseño y validación.  
- Facilitar el trabajo colaborativo del equipo usando control de versiones (Git/GitHub).  

---

### 👥 Integrantes del equipo
- **Erica Vidal**  
- **Jonathan Greppi**  
- **Cristian Mayuti**

---

### 🗂️ Estructura del repositorio
| Carpeta | Contenido |
|----------|------------|
| `docs/` | Documentos ODT, DOCX, PDF generados en cada actividad. |
| `diagrams/` | Diagramas UML, de contexto, de dominio y de casos de uso. |
| `src/` | (Opcional) Scripts de validación o simulación en Python. |
| `README.md` | Descripción general del proyecto. |

---

### 🌿 Ramas de trabajo
- **main** → Rama estable, contiene los documentos finales listos para entrega.  
- **test** → Rama de desarrollo, donde se suben los avances y versiones intermedias.

---

### ⚙️ Flujo de trabajo recomendado
1. Cada integrante trabaja sobre la rama `test`.  
2. Se realizan *commits* frecuentes con mensajes descriptivos.  
3. Cuando un documento está aprobado, se realiza un *merge* a `main`.  
   ```bash
   git checkout main
   git merge test
   git push origin main
