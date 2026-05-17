# Clinical Sensitive Data Scanner

*****Estado actual del proyecto: Beta (v0.8-beta)

Clinical Sensitive Data Scanner es una herramienta desarrollada en Python orientada al reconocimiento y auditoría de archivos de texto plano (.txt) en entornos clínicos. Su objetivo principal es detectar posibles fugas de información sensible (DLP - Data Loss Prevention), identificando patrones críticos asociados a datos de pacientes o personal de salud.

Este proyecto nació como una herramienta práctica para fortalecer mi aprendizaje de Python, ciberseguridad y automatización en entornos Linux, permitiéndome desarrollar conocimientos en expresiones regulares, estructuras de datos eficientes, modularidad y scripting seguro.


## Estado del Proyecto
Actualmente el proyecto se encuentra en fase Beta.

La versión actual incluye funcionalidades centrales de análisis y detección sobre archivos `.txt`, mientras que futuras versiones incorporarán nuevas capacidades como:

- Soporte para PDF, DOCX y XLSX
- Exportación de reportes estructurados
- Clasificación de severidad de hallazgos
- Mejoras en el motor de detección
- Escaneo de archivos comprimidos
- Reportes en PDF/HTML


## Características Principales
### Detección de RUTs
Escaneo y extracción automática de RUTs mediante expresiones regulares.

### Identificación de Emails
Parseo y detección de direcciones de correo electrónico.

### Filtro por Palabras Clave
Búsqueda dirigida utilizando un diccionario de `SENSITIVE_KEYWORDS` orientado a términos clínicos o información potencialmente sensible.

### Asociación Estructurada
Vinculación estricta de cada hallazgo con su respectivo archivo de origen.

### Deduplicación Inteligente
Uso de estructuras `set()` para evitar duplicados y optimizar la lectura de resultados.

### Resiliencia Básica
Implementación de manejo de excepciones (`try/except`) para evitar interrupciones ante:
- archivos corruptos,
- problemas de permisos,
- errores de lectura,
- o archivos inexistentes.

## Tecnologías y Conceptos Aplicados
- **Python 3** — Desarrollo principal del motor de análisis.
- **Expresiones Regulares (`re`)** — Captura precisa de patrones complejos.
- **Estructuras de Datos** — Uso de diccionarios anidados y `sets`.
- **Modularidad** — Separación lógica entre análisis, patrones y manejo de archivos.
- **Scripting en Linux** — Ejecución y pruebas en entornos Linux.

## Estructura del Proyecto
```text
├── clinical_scanner.py   # Motor principal y flujo de la aplicación (CLI)
├── patterns.py           # Definición de Regex y Keywords sensibles
├── file_handler.py       # Lógica de lectura y filtrado de archivos
└── README.md             # Documentación del proyecto
```

## Objetivo del Proyecto
El objetivo de este proyecto es continuar evolucionando una herramienta práctica orientada al análisis automatizado de datos sensibles, fortaleciendo al mismo tiempo habilidades en:

- Python
- Ciberseguridad
- Automatización
- Data Parsing
- DLP (Data Loss Prevention)
- Desarrollo seguro

## Roadmap
### v0.9-beta
- Mejoras de rendimiento
- Exportación JSON/TXT
- Logging básico
- Mejor manejo de errores

### v1.0
- Soporte para múltiples formatos de archivo
- Reportes estructurados
- CLI más robusta
- Mejoras de arquitectura y documentación

### Futuras versiones
- OCR
- Dashboard web
- Clasificación de riesgo
- Soporte para archivos comprimidos
- Detección avanzada de patrones sensibles


## Disclaimer

Este proyecto fue desarrollado con fines educativos, de aprendizaje y automatización defensiva.

No debe utilizarse para acceder, extraer o manipular información sensible sin autorización explícita.

---

## Licencia

MIT License