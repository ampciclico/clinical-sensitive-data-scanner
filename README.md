# Clinical Sensitive Data Scanner
`Clinical Sensitive Data Scanner` es una herramienta en Python diseñada para el reconocimiento y auditoría de archivos de texto plano (`.txt`) en entornos clínicos. Su objetivo principal es detectar fugas potenciales de información sensible (DLP - *Data Loss Prevention*), identificando patrones críticos de datos de pacientes o personal de salud.

Este proyecto nació como una herramienta práctica de automatización para fortalecer habilidades en el análisis de expresiones regulares, manejo de estructuras de datos eficientes y desarrollo seguro en entornos Linux.

## Características Principales
*   **Detección de Identificadores Nacionales:** Escaneo y extracción automática de RUTs mediante expresiones regulares.
*   **Identificación de Canales de Contacto:** Parseo de direcciones de correo electrónico.
*   **Filtro por Palabras Clave:** Búsqueda dirigida basada en un diccionario de `SENSITIVE_KEYWORDS` (por ejemplo: diagnósticos, términos clínicos específicos, etc.).
*   **Asociación Estructurada:** Vinculación estricta de cada hallazgo con su respectivo archivo de origen.
*   **Deduplicación Inteligente:** Uso de conjuntos (`sets`) para garantizar que los datos repetidos dentro de un mismo archivo se reporten una sola vez, optimizando la lectura del reporte.
*   **Resiliencia Básica:** Manejo de excepciones (`try/except`) para evitar que el script colapse ante archivos corruptos, inexistentes o sin permisos de lectura.

## Tecnologías y Conceptos Aplicados
*   **Python 3:** Lenguaje base para la lógica del script.
*   **Expresiones Regulares (`re`):** Implementación de patrones complejos para la captura precisa de strings (RUTs y Emails).
*   **Estructuras de Datos:** Uso de diccionarios anidados para el mapeo de metadatos y *Sets* para la optimización y limpieza de duplicados.
*   **Modularidad:** División limpia del código (Mapeo de archivos, Diccionario de patrones y Motor principal de escaneo).

## Estructura del Proyecto
```text
├── clinical_scanner.py   # Motor principal y flujo de la aplicación (CLI)
├── patterns.py           # Definición de Regex y Keywords sensibles
├── file_handler.py       # Lógica de lectura y filtrado de archivos del sistema
└── README.md             # Documentación del proyecto
