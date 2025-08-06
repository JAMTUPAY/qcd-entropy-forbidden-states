#!/usr/bin/env python3
"""
Validate entropy-forbidden framework against known exotic hadrons
"""

from entropy_forbidden_states import *
import pandas as pd

# Known exotic hadrons
KNOWN_EXOTICS = {
    # Original 6 test cases
    'X(3872)': {'quarks': 'ccUD', 'mass': 3.872, 'J': 1},
    'Zc(3900)': {'quarks': 'ccUD', 'mass': 3.900, 'J': 1},
    'X(6900)': {'quarks': 'ccCC', 'mass': 6.900, 'J': 0},
    'Pc(4312)': {'quarks': 'ccuud', 'mass': 4.312, 'J': 0.5},
    'Pc(4440)': {'quarks': 'ccuud', 'mass': 4.440, 'J': 0.5},
    'Pc(4457)': {'quarks': 'ccuud', 'mass': 4.457, 'J': 0.5},
    
    # Add remaining 17 exotic hadrons here...
    # Tetraquarks
    'Zc(4430)': {'quarks': 'ccUD', 'mass': 4.430, 'J': 1},
    'X(4140)': {'quarks': 'ccSS', 'mass': 4.140, 'J': 1},
    'X(4274)': {'quarks': 'ccSS', 'mass': 4.274, 'J': 1},
    # etc...
}

def validate_all():
    results = []
    for name, data in KNOWN_EXOTICS.items():
        # Parse quark content
        cfg = dict.fromkeys(ALL_TYPES, 0)
        for ch in data['quarks']:
            if ch.islower():
                cfg[ch] += 1
            else:
                cfg[ch.lower() + '_bar'] += 1
        
        # Set quantum numbers
        cfg['n'] = sum(cfg.values())
        cfg['B'] = baryon_number(cfg)
        cfg['S'] = strangeness(cfg)
        
        # Evaluate
        J = data['J']
        status, g, e, w, p, dE = evaluate_status(cfg, J)
        M_pred = total_mass(cfg, J)
        
        results.append({
            'name': name,
            'quarks': data['quarks'],
            'status': status,
            'M_pred': round(M_pred, 3),
            'M_obs': data['mass'],
            'delta_M': round(M_pred - data['mass'], 3),
            'dE': round(dE, 3),
            'nature': 'Threshold' if dE > 0 else 'Bound'
        })
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    print("Validating known exotic hadrons...")
    df = validate_all()
    print(df)
    
    # Save results
    df.to_csv('validation_results.csv', index=False)
    
    # Summary
    print(f"\nPassed: {len(df[df['status'] == 'Allowed'])}")
    print(f"Failed: {len(df[df['status'] != 'Allowed'])}")
    print(f"Threshold states: {len(df[df['dE'] > 0])}")
    print(f"Bound states: {len(df[df['dE'] <= 0])}")
