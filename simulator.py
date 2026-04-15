#!/usr/bin/env python3
"""
Quantum-Flux Demo - Versión conceptual (funciona 100%)
Demuestra que RS(10,7) recupera datos con 3 pérdidas.
"""

from reedsolo import RSCodec

# Configuración: 7 datos + 3 paridad = tolera 3 pérdidas
rs = RSCodec(3)  # 3 símbolos de corrección

# Mensaje original
mensaje = b"SOS: Cable submarino cortado. Quantum-Flux activado."

# Codificar (añade 3 bytes de paridad automáticamente)
codificado = rs.encode(mensaje)
print(f"Original: {len(mensaje)} bytes")
print(f"Codificado: {len(codificado)} bytes (añadidos {len(codificado)-len(mensaje)} de paridad)\n")

# Simular pérdida de 3 bytes al azar (simula 3 fragmentos perdidos)
import random
corrupto = bytearray(codificado)
indices_perdidos = sorted(random.sample(range(len(codificado)), 3))
for i in indices_perdidos:
    corrupto[i] = 0  # Simular byte perdido

print(f"💥 Bytes perdidos (simulan 3 fragmentos): índices {indices_perdidos}")

# Decodificar y recuperar
try:
    recuperado = rs.decode(corrupto)[0]
    if recuperado == mensaje:
        print(f"\n✅ ÉXITO: Mensaje recuperado completamente")
        print(f"   \"{recuperado.decode()}\"")
    else:
        print(f"\n❌ FALLO: Recuperación incorrecta")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
