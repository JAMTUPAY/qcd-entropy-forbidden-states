# QCD Entropy-Forbidden Exotic Hadrons: Interactive Explorer & Predictive Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16752674.svg)](https://doi.org/10.5281/zenodo.16752674)
[![Interactive Explorer](https://img.shields.io/badge/Interactive-Explorer-blueviolet)](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Interactive Explorer Available!

**[Launch the Interactive QCD Explorer →](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)**

Explore all 23 confirmed exotic hadrons and test your own quark configurations against the universal entropy budget constraint!

## Abstract

Universal entropy-mass relation applied to exotic hadrons - constraining QCD bound states through information flow. The universal entropy budget |ΔS_RG| = 9.81 kB fundamentally constrains which exotic hadrons can exist in nature.

## Key Results

- ✅ **28,721** hadron configurations systematically analyzed
- ✅ **25,831** allowed states identified (90.0%)
- ✅ **2,730** energy-forbidden states (9.5%)
- ✅ **160** Pauli-suppressed states (0.5%)
- ✅ **All 23 known exotic hadrons** correctly validated
- ✅ **X(6900)** identified as threshold enhancement (ΔE = +0.615 GeV)
- ✅ **X(6900) mass** predicted at 6.809 GeV (observed: 6.900 GeV)

## 🔬 Interactive Features

The **[Interactive Explorer](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)** allows you to:

1. **Browse All 23 Confirmed Exotics** - Complete database of LHC discoveries
2. **Search & Filter** - Find specific states by name or quark content
3. **Sort Columns** - Analyze patterns in mass, energy, and status
4. **Check Custom Configurations** - Test ANY quark combination to see if it's:
   - ✅ Allowed by entropy budget
   - ⚡ At threshold (like X(6900))
   - ❌ Forbidden by universal constraint
5. **Predict New States** - Use the entropy framework to predict undiscovered hadrons

### Example Configurations to Try:
- `cccc` - Fully charm tetraquark (like X(6900))
- `bbbbb` - Hypothetical beauty pentaquark
- `cccccc` - Hexaquark (not yet observed!)
- `ccuud` - Standard pentaquark configuration

## Repository Structure

```
qcd-entropy-forbidden-states/
├── code/                    # Python analysis pipeline
│   ├── entropy_forbidden_states.py
│   ├── validate_known_exotics.py
│   └── visualize_periodic_table.py
├── data/                    # CSV datasets (28,721 configurations)
│   ├── allowed_states.csv
│   ├── forbidden_states.csv
│   └── threshold_states.csv
├── paper/                   # LaTeX source and figures
│   ├── main.tex
│   └── figures/
├── web/                     # Interactive visualization
│   └── index.html          # 🌟 Interactive Explorer
├── notebooks/              # Jupyter notebooks
│   └── explore_forbidden_states.ipynb
└── LICENSE                 # MIT License
```

## Quick Start

### Run Analysis Locally
```bash
git clone https://github.com/JAMTUPAY/qcd-entropy-forbidden-states.git
cd qcd-entropy-forbidden-states
python3 code/entropy_forbidden_states.py
```

### Test X(6900) Prediction
```bash
python3 code/validate_known_exotics.py
```

### Use Interactive Explorer
Visit: **[https://jamtupay.github.io/qcd-entropy-forbidden-states/web/](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)**

## Five Falsifiable Predictions

1. **No hidden-beauty pentaquark** above M = 2Υ + 1 GeV (19.9 GeV)
2. **No color-singlet hadron** with n < 3|B| quarks
3. **All-identical multiquarks** (n>3) appear >0.3 GeV above entropy-core mass
4. **Light pentaquarks** unobservable in heavy-ion collisions
5. **Compact tetraquarks** within 50 MeV of S-wave thresholds

## Scientific Impact

This work provides the first application of universal entropy constraints to exotic hadrons, offering:
- A **predictive framework** for undiscovered states
- **Explanation** for why certain configurations exist while others don't
- **Validation** of all 23 known exotic hadrons
- **Quantitative predictions** for future discoveries

## Citation

```bibtex
@software{tupay2025entropy,
  author = {Tupay, Johann Anton Michael},
  title = {Entropy-Forbidden Exotic Hadrons: Universal Constraints from QCD Information Flow},
  year = {2025},
  month = aug,
  publisher = {Zenodo},
  version = {v1.0.0},
  doi = {10.5281/zenodo.16752674},
  url = {https://doi.org/10.5281/zenodo.16752674}
}
```

## Original Work

Based on: [Universal Entropy-Mass Relation in QCD](https://zenodo.org/records/16747096)

## Interactive Explorer

🌟 **[Launch Interactive Explorer](https://jamtupay.github.io/qcd-entropy-forbidden-states/web/)**

Features:
- Real-time configuration checking
- All 23 confirmed exotic hadrons
- Custom quark combination validator
- Predictive mass calculations
- Entropy budget visualization

## Author

**Johann Anton Michael Tupay**  
Contact: jamtupay@icloud.com  
ORCID: [0009-0008-7661-8698](https://orcid.org/0009-0008-7661-8698)

## License

MIT License - See [LICENSE](LICENSE) file

## Acknowledgments

Special thanks to the particle physics community and the LHC collaborations (LHCb, CMS, ATLAS, Belle) for exotic hadron discoveries that validate this framework.

---

<p align="center">
  <a href="https://jamtupay.github.io/qcd-entropy-forbidden-states/web/">
    <img src="https://img.shields.io/badge/Try%20the-Interactive%20Explorer-blueviolet?style=for-the-badge" alt="Interactive Explorer">
  </a>
</p>
