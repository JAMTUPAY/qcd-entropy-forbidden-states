# QCD Entropy Forbidden States

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16752674.svg)](https://doi.org/10.5281/zenodo.16752674)

Universal entropy-mass relation applied to exotic hadrons - constraining QCD bound states through information flow.

## Key Discovery
The universal entropy budget |ΔS_RG| = 9.81 kB fundamentally constrains which exotic hadrons can exist in nature.

## Main Results
- ✅ **28,721** hadron configurations systematically analyzed
- ✅ **25,831** allowed states identified (90.0%)
- ✅ **2,730** energy-forbidden states (9.5%)
- ✅ **160** Pauli-suppressed states (0.5%)
- ✅ All **23 known exotic hadrons** correctly validated
- ✅ **X(6900)** identified as threshold enhancement (ΔE = +0.615 GeV)
- ✅ **X(6900)** mass predicted at 6.809 GeV (observed: 6.900 GeV)

## Repository Structure├── paper/           # LaTeX manuscript and PDF
├── code/            # Python analysis pipeline
├── data/            # CSV datasets (28,721 configurations)
├── paper/figures/   # Publication figures
├── web/             # Interactive visualization
└── LICENSE          # MIT License

## Quick Start
```bashcd code/
python3 entropy_forbidden_states.py     # Test X(6900) prediction
python3 validate_known_exotics.py       # Validate all 23 known exotics
python3 visualize_periodic_table.py     # Generate figures

## Five Falsifiable Predictions
1. No hidden-beauty pentaquark above M = 2Υ + 1 GeV (19.9 GeV)
2. No color-singlet hadron with n < 3|B| quarks
3. All-identical multiquarks (n>3) appear >0.3 GeV above entropy-core mass
4. Light pentaquarks unobservable in heavy-ion collisions
5. Compact tetraquarks within 50 MeV of S-wave thresholds

## Citation
```bibtex@software{tupay2025entropy,
author       = {Tupay, Johann Anton Michael},
title        = {Entropy-Forbidden Exotic Hadrons: Universal Constraints from QCD Information Flow},
year         = {2025},
month        = aug,
publisher    = {Zenodo},
version      = {v1.0.0},
doi          = {10.5281/zenodo.16752674},
url          = {https://doi.org/10.5281/zenodo.16752674}
}

## Original Work
Based on: [Universal Entropy-Mass Relation in QCD](https://zenodo.org/records/16747096)

## Interactive Explorer
View the [Interactive Hadron Explorer](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)

## Author
Johann Anton Michael Tupay (jamtupay@icloud.com)

## License
MIT License - See LICENSE file
