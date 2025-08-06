#!/usr/bin/env python3
"""
Entropy Forbidden States in QCD
Universal entropy-mass relation applied to exotic hadrons
Author: Johann Anton Michael Tupay
"""

import pandas as pd
import numpy as np
import itertools

# ===== CONSTANTS =====
# Quark types
QUARKS = ['u', 'd', 's', 'c', 'b']
ANTIQUARKS = [q + '_bar' for q in QUARKS]
ALL_TYPES = QUARKS + ANTIQUARKS

# Entropy coefficients (MeV/kB) from original paper
ENTROPY_COEFF = {
    'c0': 83.5,
    'aB': 15.0,
    'alphaS': 11.4,
    'betaJ': 25.3
}
DELTA_S_RG = 9.81  # kB

# Heavy quark masses (GeV)
HEAVY_MASS = {'c': 1.28, 'c_bar': 1.28, 'b': 4.18, 'b_bar': 4.18}

# Calibrated parameters for exotics
BIND_CC = 0.08  # GeV per cc diquark
BIND_BB = 0.16  # GeV per bb diquark
REPULSION = 0.95  # GeV for 4+ heavy quarks

def baryon_number(cfg):
    """Calculate baryon number B = (n_quarks - n_antiquarks)/3"""
    n_q = sum(cfg.get(q, 0) for q in QUARKS)
    n_qbar = sum(cfg.get(q, 0) for q in ANTIQUARKS)
    return (n_q - n_qbar) / 3

def strangeness(cfg):
    """Calculate strangeness S = -(n_s - n_sbar)"""
    return -(cfg.get('s', 0) - cfg.get('s_bar', 0))

def total_mass(cfg, J):
    """Calculate total mass using entropy formula"""
    # Entropy contribution
    B = baryon_number(cfg)
    S = strangeness(cfg)
    F = ENTROPY_COEFF['c0'] + ENTROPY_COEFF['aB']*B + \
        ENTROPY_COEFF['alphaS']*abs(S) + ENTROPY_COEFF['betaJ']*J
    m_entropy = DELTA_S_RG * F / 1000  # Convert to GeV
    
    # Heavy quark masses
    m_heavy = sum(cfg.get(q, 0) * HEAVY_MASS.get(q, 0) for q in ALL_TYPES)
    
    # Count heavy quarks for repulsion
    n_heavy = sum(cfg.get(q, 0) for q in ['c', 'c_bar', 'b', 'b_bar'])
    repulsion = REPULSION if n_heavy >= 4 else 0
    
    # Diquark binding
    n_cc = min(cfg.get('c', 0), cfg.get('c', 0)) // 2
    n_bb = min(cfg.get('b', 0), cfg.get('b', 0)) // 2
    binding = n_cc * BIND_CC + n_bb * BIND_BB
    
    return m_entropy + m_heavy + repulsion - binding

def evaluate_status(cfg, J):
    """Simple status evaluation"""
    B = baryon_number(cfg)
    n = sum(cfg.values())
    
    # Gauge check
    if n < 3 * abs(B):
        return 'Gauge', False, False, False, False, 0
    
    # Calculate mass
    mass = total_mass(cfg, J)
    
    # Simple threshold check (simplified for this version)
    threshold = 3.73 if cfg.get('c', 0) > 0 else 0.28  # D-Dbar or pi-pi
    dE = mass - threshold
    
    if dE > 0 and n >= 4:
        return 'Energy', True, False, False, False, dE
    
    return 'Allowed', True, True, True, True, dE

# Simple test
if __name__ == "__main__":
    print("Entropy Forbidden States Framework")
    print(f"Universal entropy budget: {DELTA_S_RG} kB")
    
    # Test X(6900): cccc̄c̄
    test_cfg = {'c': 2, 'c_bar': 2}
    test_cfg['n'] = 4
    mass = total_mass(test_cfg, J=0)
    print(f"\nX(6900) test: predicted mass = {mass:.3f} GeV")
    print(f"Observed: 6.900 GeV")
