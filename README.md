# Quantum-Flux / Tenebra Link

**Cables get cut. We don't.**

## ¿Qué es esto?

Quantum-Flux es un software que convierte enlaces satelitales comunes en **enlaces ultra-resilientes**. Fragmenta los datos en **10 flujos paralelos**, los distribuye sobre satélites comerciales existentes (Starlink, Hispasat, Intelsat, etc.) con corrección de errores (FEC), y los recombina en destino.

Si 2 o 3 flujos fallan (por clima, sabotaje o fallo técnico), **el enlace sigue funcionando sin pérdida de datos**.

## ¿Por qué existe?

Los cables submarinos se cortan. En 2024-2026, decenas de cables críticos fueron dañados en el Báltico, Mar Rojo y Taiwán — muchos en circunstancias sospechosas. Gobiernos, bancos e infraestructura crítica necesitan una alternativa que **no dependa del fondo del mar**.

## Arquitectura

El software se ejecuta en servidores en los puntos de entrada/salida (gateways de operadores satelitales). **No necesita infraestructura nueva**.

- **Fragmentación:** divide los datos en 10 flujos independientes.
- **FEC:** añade redundancia para corregir errores sin retransmitir.
- **Balanceo dinámico:** asigna más carga a los flujos con mejor calidad.
- **Recombinación:** une los flujos y entrega el flujo original.

## Estado actual

✅ Concepto definido  
✅ Arquitectura documentada  
✅ Algoritmos especificados  
🔲 Prototipo en desarrollo  
🔲 Simulación de fallos  
🔲 Prueba piloto con operador satelital

## Modelo de negocio

Arriendo de enlace resiliente como servicio mensual a clientes que no pueden permitirse caídas:
- Gobiernos y defensa
- Bancos e instituciones financieras
- Infraestructura crítica (energía, minería, data centers)

## Proyecto hermano

**Goliat-Orbital** — captura y reciclaje de basura espacial.  
[Repositorio](https://github.com/enriqueherbertag-lgtm/Goliat-Orbital)

## Licencia

Apache 2.0 con restricción de uso comercial.  
*Este es un framework base open-source. Funciona con los algoritmos probados. El que quiera más precisión, menor latencia o features avanzadas… que lo modifique y contribuya.*

## Autor

Enrique Aguayo H. — eaguayo@migst.cl  
Investigador independiente, Mackiber Labs
