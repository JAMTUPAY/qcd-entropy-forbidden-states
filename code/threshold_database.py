"""
Complete PDG mass database for threshold calculations
"""

# PDG masses in GeV
PDG = {
    # Light mesons
    'pi': 0.140,
    'K': 0.494,
    'eta': 0.548,
    'rho': 0.775,
    'omega': 0.783,
    'phi': 1.019,
    
    # Charm mesons
    'D': 1.865,
    'D*': 2.010,
    'Ds': 1.968,
    'Ds*': 2.112,
    'eta_c': 2.983,
    'J/psi': 3.097,
    'chi_c0': 3.415,
    'chi_c1': 3.511,
    'psi_2S': 3.686,
    
    # Bottom mesons
    'B': 5.279,
    'B*': 5.325,
    'Bs': 5.367,
    'Bs*': 5.415,
    'etab': 9.398,
    'Upsilon': 9.460,
    'Upsilon_2S': 10.023,
    'Upsilon_3S': 10.355,
    
    # Baryons
    'proton': 0.938,
    'neutron': 0.940,
    'Lambda': 1.116,
    'Sigma': 1.193,
    'Xi': 1.318,
    'Lambda_c': 2.286,
    'Sigma_c': 2.453,
    'Xi_c': 2.468,
    'Lambda_b': 5.620,
}

# Common threshold pairs
PAIR_THRESHOLDS = {
    # Charmonium pairs
    'eta_c_eta_c': 2 * PDG['eta_c'],  # 5.966
    'jpsi_jpsi': 2 * PDG['J/psi'],    # 6.194
    'etac_jpsi': PDG['eta_c'] + PDG['J/psi'],  # 6.080
    
    # D meson pairs
    'DD': 2 * PDG['D'],           # 3.730
    'DD*': PDG['D'] + PDG['D*'],  # 3.875
    'D*D*': 2 * PDG['D*'],        # 4.020
    'DsDs': 2 * PDG['Ds'],        # 3.936
    
    # B meson pairs
    'BB': 2 * PDG['B'],           # 10.558
    'BB*': PDG['B'] + PDG['B*'],  # 10.604
    'B*B*': 2 * PDG['B*'],        # 10.650
    
    # Bottom pairs
    'upsilon_upsilon': 2 * PDG['Upsilon'],  # 18.920
    'etab_etab': 2 * PDG['etab'],          # 18.796
    
    # Baryon-meson
    'p_pi': PDG['proton'] + PDG['pi'],     # 1.078
    'Lambda_c_D': PDG['Lambda_c'] + PDG['D'],  # 4.151
    'p_jpsi': PDG['proton'] + PDG['J/psi'],    # 4.035
}
