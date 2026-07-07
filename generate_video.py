# =====================================================================
# Infinite Point Theory Framework v1.0.0
# Copyright (c) 2026 Winson See. All Rights Reserved.
# Licensed under the MIT License. See LICENSE file in project root.
# =====================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# =====================================================================
# 1. SYSTEM PARAMETERS DEFINITION (WEB-OPTIMIZED)
# =====================================================================
N = 100            # Optimized node grid width for web delivery
Total_Steps = 600  # Streamlined evolution window
r = 3.985         
alpha = 0.5      

FPS = 24           # Standard cinematically smooth web framerate
Iter_Per_Frame = 6 # Weave faster per frame to dramatically reduce GIF file weight
Total_Frames = Total_Steps // Iter_Per_Frame

# =====================================================================
# 2. SYSTEM INITIALIZATION & STATE SETUP
# =====================================================================
# State: Initialize with microscopic fluctuations (Transition from 0 to 1)
State_Psi = np.random.rand(N)

# History Matrix: Pre-allocate space to store the entire spacetime (Time x Space)
Spacetime_History = np.zeros((Total_Steps, N))
Spacetime_History[0, :] = State_Psi

# Color Mapping: Define a custom 'Twilight Nebula' colormap
colors_list = ['#050811', '#191A36', '#4E2D77', '#C44E72', '#E1A29D'] # Deep space palette
cmap_dotdynamics = LinearSegmentedColormap.from_list("dot_dynamics_cmap", colors_list)

# =====================================================================
# 3. ANIMATION RENDERING FUNCTION (FRAME UPDATER)
# =====================================================================
def update_spacetime_animation(frame, im_handle, total_steps_text, current_time_text):
    global State_Psi, Spacetime_History
    
    # Calculate the steps for the current frame window
    current_time_step = frame * Iter_Per_Frame
    
    # Perform core equation iterations optimized by vectorization
    for _ in range(Iter_Per_Frame):
        if current_time_step + Iter_Per_Frame < Total_Steps:
            
            # Step A: Execute the Chaotic Kernel (Diversity Engine)
            f_current = r * State_Psi * (1.0 - State_Psi)
            
            # Step B: Execute Network Coupling (Periodic Boundary Ring Topology)
            f_left = np.roll(f_current, 1)
            f_right = np.roll(f_current, -1)
            network_coupling_term = 0.5 * (f_left + f_right)
            
            # Step C: State Vector Update for current Time step (n)
            State_Psi = (1 - alpha) * f_current + alpha * network_coupling_term
            
            # Store data into the history matrix for image rendering
            current_time_step += 1
            Spacetime_History[current_time_step, :] = State_Psi
    
    # Update the visual data for the 'imshow' handle (optimizes rendering)
    im_handle.set_data(Spacetime_History)
    
    # Update text overlays to show simulation progress
    current_time_text.set_text(f'Current Step (n): {current_time_step:04d}')
    
    # Return the updated artists required for the animation
    return [im_handle, current_time_text]

# =====================================================================
# 4. FIGURE & VISUALIZATION INTERFACE SETUP
# =====================================================================
# FIXED: Using plt.subplots() to correctly unpack fig and ax handles
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.subplots_adjust(left=0, right=1, bottom=0.1, top=0.95) # Full bleed visualization
ax.axis('off') # Hide axes for maximum visual impact

# Initial blank image setup: Crucial for animation handle creation
Initial_View = np.zeros((Total_Steps, N))
im_plot = ax.imshow(Initial_View, cmap=cmap_dotdynamics, aspect='auto', origin='lower', animated=True, vmin=0, vmax=1)

# FIXED: Added raw string prefix 'r' to prevent LaTeX escape sequence syntax warnings
fig.suptitle(r'Dot-Dynamics Paradigm: Spacetime Weaving ($0 \rightarrow 10 \rightarrow \infty$)', color='white', fontsize=22, fontweight='bold', y=0.98)
total_steps_text = ax.text(N-10, Total_Steps - 30, f'Total Steps: {Total_Steps}', color='white', fontsize=12, fontweight='bold', ha='right')
current_time_text = ax.text(N-10, Total_Steps - 60, '', color='#E1A29D', fontsize=12, ha='right') # Highlights current step in nebula color

# =====================================================================
# 5. GENERATE & SAVE ANIMATION (COMPATIBILITY OPTIMIZED)
# =====================================================================
anim_instance = animation.FuncAnimation(fig, update_spacetime_animation, frames=Total_Frames,
                                        fargs=(im_plot, total_steps_text, current_time_text),
                                        interval=1000/FPS, blit=True)

mp4_filename = 'DotDynamics_Spacetime_Weave.mp4'
gif_filename = 'DotDynamics_Spacetime_Weave.gif'

# Save as MP4 with simplified configuration
try:
    print(f"Start rendering: {mp4_filename}...")
    # Removed extra_args to ensure clean fallback if environment configurations vary
    anim_instance.save(mp4_filename, fps=FPS, writer='ffmpeg')
    print(f"Rendering complete: {mp4_filename}")
except Exception as e:
    print(f"MP4 encoding bypassed. Attempting GIF generation instead. Error: {e}")
    
    # Automatic fallback to high-quality GIF banner
    print(f"Start rendering: {gif_filename} (Compiling frames via Pillow)...")
    anim_instance.save(gif_filename, writer='pillow', fps=FPS)
    print(f"Rendering complete: {gif_filename}")

plt.close(fig)
print("Initialization finished. Animation handles closed.")