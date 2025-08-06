#!/usr/bin/env python3
"""
Generate publication-quality visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_periodic_table(catalog_file='forbidden_states_catalog.csv'):
    """Create the entropy periodic table heatmap"""
    df = pd.read_csv(catalog_file)
    
    # Calculate forbidden fraction for each (B,S) cell
    heat = df.pivot_table(
        index='S', 
        columns='B', 
        values='status',
        aggfunc=lambda x: (x != 'Allowed').mean()
    )
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot heatmap
    sns.heatmap(
        heat, 
        cmap='viridis',
        cbar_kws={'label': 'Forbidden Fraction'},
        ax=ax,
        vmin=0,
        vmax=1,
        annot=True,
        fmt='.2f',
        square=True
    )
    
    # Styling
    ax.set_title('Entropy Periodic Table of Hadrons', fontsize=18, pad=20)
    ax.set_xlabel('Baryon Number (B)', fontsize=14)
    ax.set_ylabel('Strangeness (S)', fontsize=14)
    
    # Add grid
    ax.set_axisbelow(True)
    ax.grid(True, alpha=0.3)
    
    # Save
    plt.tight_layout()
    plt.savefig('entropy_periodic_table.png', dpi=300, bbox_inches='tight')
    plt.savefig('entropy_periodic_table.pdf', bbox_inches='tight')
    
    return fig

def plot_mass_comparison(validation_file='validation_results.csv'):
    """Plot predicted vs observed masses"""
    df = pd.read_csv(validation_file)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot points
    colors = {'Bound': 'blue', 'Threshold': 'red'}
    for nature, group in df.groupby('nature'):
        ax.scatter(
            group['M_obs'], 
            group['M_pred'],
            label=nature,
            color=colors[nature],
            s=100,
            alpha=0.7
        )
    
    # Perfect prediction line
    min_mass = min(df['M_obs'].min(), df['M_pred'].min())
    max_mass = max(df['M_obs'].max(), df['M_pred'].max())
    ax.plot([min_mass, max_mass], [min_mass, max_mass], 'k--', alpha=0.5)
    
    # Labels
    for _, row in df.iterrows():
        ax.annotate(
            row['name'],
            (row['M_obs'], row['M_pred']),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=8
        )
    
    ax.set_xlabel('Observed Mass (GeV)', fontsize=14)
    ax.set_ylabel('Predicted Mass (GeV)', fontsize=14)
    ax.set_title('Exotic Hadron Mass Predictions', fontsize=16)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('mass_comparison.pdf', bbox_inches='tight')
    
    return fig

if __name__ == "__main__":
    create_periodic_table()
    plot_mass_comparison()
    print("Figures generated successfully!")
