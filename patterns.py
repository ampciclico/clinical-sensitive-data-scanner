#!/usr/bin/env python3

import re

RUT_PATTERN = r'\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b'

EMAIL_PATTERN = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

SENSITIVE_KEYWORDS = [
    "vih",
    "oncologia",
    "biopsia",
    "paciente",
    "urgencia"
]


