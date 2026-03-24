# Inicio Rápido - Quantum-Flux

**10 minutos para entender cómo funciona**

## Requisitos Previos

- Go 1.21+ (para compilar)
- Python 3.10+ (para prototipos)
- Acceso a terminales satelitales (Starlink, etc.) para pruebas reales

## Instalación

### Desde código fuente

```bash
git clone https://github.com/enriqueherbertag-lgtm/quantum-flux.git
cd quantum-flux

# Compilar núcleo en Go
make build

# Ejecutar prototipo Python
python examples/simple-bonding.py --help
