#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 17:36:26 2025

@author: carlosar
"""

import numpy as np
import matplotlib.pyplot as plt

# Grid definition
x = np.linspace(-0.5, 0.5, 10)
y = np.linspace(-0.5, 0.5, 10)
X, Y = np.meshgrid(x, y)

# --- First Field: Circular Flow ---
def velocity_field_1(X, Y):
    R2 = X**2 + Y**2
    # Avoid division by zero
    R2[R2 == 0] = np.nan
    u = Y / R2
    v = -X / R2
    return u, v

# --- Second Field: Hyperbolic Flow ---
def velocity_field_2(X, Y):
    u = X
    v = -Y
    return u, v

# Create figure for vector fields
fig1, axs1 = plt.subplots(1, 2, figsize=(6, 3), dpi=300)

# --- Plot 1: Vector field for circular flow ---
u1, v1 = velocity_field_1(X, Y)
axs1[0].quiver(X, Y, u1, v1, color='blue')#, scale=1, width=0.005, headwidth=4, headlength=6)
axs1[0].set_title('Vector Field: Example 1')
axs1[0].set_aspect('equal')
axs1[0].set_xlim(-0.5, 0.5)
axs1[0].set_ylim(-0.5, 0.5)

# --- Plot 2: Vector field for hyperbolic flow ---
u2, v2 = velocity_field_2(X, Y)
axs1[1].quiver(X, Y, u2, v2, color='darkred')#, scale=1, width=0.005, headwidth=4, headlength=6)
axs1[1].set_title('Vector Field: Example 2')
axs1[1].set_aspect('equal')
axs1[1].set_xlim(-0.5, 0.5)
axs1[1].set_ylim(-0.5, 0.5)

plt.tight_layout()
plt.show()


# --- Now the streamline plots ---

# Create figure for streamlines
fig2, axs2 = plt.subplots(1, 2, figsize=(6, 3), dpi=300)

# --- Plot 3: Streamlines for circular flow ---
axs2[0].streamplot(X, Y, u1, v1, color='blue', density=0.5)
axs2[0].set_title('Streamlines: Example 1')
axs2[0].set_aspect('equal')
axs2[0].set_xlim(-0.5, 0.5)
axs2[0].set_ylim(-0.5, 0.5)

# --- Plot 4: Streamlines for hyperbolic flow ---
axs2[1].streamplot(X, Y, u2, v2, color='darkred', density=0.5)
axs2[1].set_title('Streamlines: Example 2')
axs2[1].set_aspect('equal')
axs2[1].set_xlim(-0.5, 0.5)
axs2[1].set_ylim(-0.5, 0.5)

plt.tight_layout()
plt.show()
