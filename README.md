# Quantum-Flux

**Cables get cut. We don't.**

## El Talón de Aquiles de Internet

Los cables submarinos son la columna vertebral de las comunicaciones globales. También son su punto más débil.

En los últimos 18 meses, decenas de cables críticos fueron cortados en el Báltico, el Mar Rojo y Taiwán — muchos en circunstancias sospechosas. Cuando un cable se corta, países enteros pueden quedar incomunicados, las transacciones financieras se detienen y la infraestructura crítica se paraliza.

Quantum-Flux es una alternativa.

## Qué hace

Imagina que envías un mensaje urgente por 10 caminos distintos. Si 2 o 3 de esos caminos se bloquean (por niebla, sabotaje o fallo técnico), el mensaje igual llega completo.

Quantum-Flux hace eso con tus datos, pero sobre satélites.

- Toma tu flujo de datos y lo **fragmenta en 10 flujos paralelos**.
- Los envía por satélites comerciales que ya existen (Starlink, Hispasat, Intelsat, etc.).
- Si hasta 3 flujos fallan, el sistema **reconstruye los datos sin pérdida** usando corrección de errores (FEC).
- Una IA **balancea la carga** en tiempo real: si un flujo está más despejado, le manda más datos; si otro se degrada, lo alivia.

El software corre en los puntos de entrada/salida de los operadores satelitales. **No necesita infraestructura nueva**.

## Por qué es diferente

| Solución común | Quantum-Flux |
|----------------|--------------|
| Un solo satélite. Si falla, caes. | 10 flujos sobre múltiples satélites y operadores. Si fallan 2-3, sigues. |
| Depende de cables submarinos. | Independiente. Usa satélites ya en órbita. |
| Reacciona cuando ya hay problemas. | La IA aprende patrones climáticos y anticipa fallos. |

## Para quién es

Cualquier organización que no pueda permitirse perder conectividad:

- **Gobiernos y defensa** — comunicaciones soberanas
- **Bancos e instituciones financieras** — transacciones de alto valor
- **Infraestructura crítica** — energía, minería, data centers, salud

## Modelo de negocio

Vendemos **ancho de banda resiliente garantizado** como servicio mensual. El cliente no invierte en infraestructura; solo paga por un enlace que no se cae.

## Estado actual

 Concepto definido  
 Arquitectura documentada  
 Algoritmos especificados  
 Prototipo en desarrollo  
 Simulación de fallos  
 Prueba piloto con operador satelital

## Proyecto hermano

**Goliat-Orbital** — captura y reciclaje de basura espacial.  
Convierte fragmentos orbitales en lingotes reutilizables.  
[Repositorio](https://github.com/enriqueherbertag-lgtm/Goliat-Orbital)

## Licencia

Apache 2.0 con restricción de uso comercial.  
*Este es un framework base open-source. Funciona con los algoritmos probados. El que quiera más precisión, menor latencia o features avanzadas… que lo modifique y contribuya.*

## Autor

Enrique Aguayo H. — eaguayo@migst.cl  
Investigador independiente, Mackiber Labs
