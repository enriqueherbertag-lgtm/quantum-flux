# Arquitectura Técnica - Quantum-Flux

## Visión General

Quantum-Flux es un sistema de orquestación de enlaces satelitales que proporciona resiliencia extrema mediante fragmentación de datos y corrección de errores. Opera como un **proxy inteligente** entre el cliente y los operadores satelitales.

## Componentes

### 1. Fragmentador (Fragmentor)
- Divide el flujo de entrada en N flujos independientes (por defecto 10)
- Implementa **Reed-Solomon FEC** para añadir redundancia
- Cada flujo es enviado a través de un enlace satelital distinto (diferente operador, frecuencia, o satélite)

### 2. Balanceador Dinámico (Balancer)
- Monitorea en tiempo real:
  - Pérdida de paquetes
  - Latencia
  - Jitter
  - Capacidad disponible
- Asigna más carga a los flujos con mejor calidad
- Detecta fallos en <100ms y redistribuye

### 3. Recombinador (Recombiner)
- Recibe los N flujos en destino
- Detecta y corrige errores usando FEC
- Reconstruye el flujo original
- Si faltan hasta 2-3 flujos, puede reconstruir sin pérdida

### 4. API de Control
- REST API para administración y monitoreo
- gRPC para comunicación entre componentes
- Métricas en formato Prometheus

## Flujo de Datos

