# Quantum-Flux: Communications that survive submarine cable cuts

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19358417.svg)](https://doi.org/10.5281/zenodo.19358417)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

In an increasingly internet-dependent world, the submarine cables that connect entire continents are vulnerable. An intentional cut, an accident, or a natural disaster can leave countries, banks, hospitals, or defense systems without communication for days or weeks.

**Quantum-Flux was created to solve this problem.**

## What it does

Instead of relying on a single link (either a submarine cable or a specific satellite), Quantum-Flux splits your data into 10 parallel streams. These streams are sent simultaneously through different existing commercial satellites (Starlink, Hispasat, Intelsat, and others).

Even if several of these streams fail or are lost, the system can reconstruct the complete information thanks to powerful error correction (FEC). It also uses intelligent real-time load balancing to optimize traffic based on each satellite's availability and speed.

The result is a much more stable and resilient connection, even in scenarios of massive infrastructure disruption.

## Who it is for

Quantum-Flux is designed for organizations that cannot afford to lose connectivity:

- Governments and defense — sovereign communications
- Banks and financial institutions — high-value transactions
- Critical infrastructure — energy, mining, data centers, healthcare
- Emergency teams — disaster coordination

## Main advantages

- High resilience against submarine cable cuts or massive link failures.
- Works with existing commercial satellites — no new infrastructure required.
- Reconstructs data even if up to 3 out of 10 streams are lost.
- Intelligent load balancing that maximizes real-time performance.

## Business model

We sell guaranteed resilient bandwidth as a monthly service. The customer does not invest in infrastructure; they only pay for a connection that does not go down.

## Current status

- Concept defined
- Architecture documented
- Algorithms specified
- Prototype in development (pending)
- Failure simulation (pending)
- Pilot test with satellite operator (pending)


```bash
# Installation
pip install reedsolo

# Execution
python simulator.py
```

## Related projects

- Goliat-Orbital — space debris capture and recycling
- ShieldAir — oxygen production towers
- CORPUS — artificial body systems

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

This project is protected by copyright.

PERMITTED:
- Non-commercial use for educational or research purposes.
- Distribution without modification, as long as this license is maintained and credit is given to the author.

PROHIBITED without express written authorization:
- Commercial use (including, but not limited to: offering it as a service, SaaS, subscription, integration into revenue-generating products, or any use that generates direct or indirect economic benefit).
- Modification for production environments.
- Distribution of modified versions without authorization.

For commercial licenses, technical support, enterprise pilots, or inquiries:
Contact: eaguayo@migst.cl

Any use outside the permitted terms requires prior authorization from the author.

Commercial inquiries are welcome and will be answered within a maximum of 7 business days.

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
