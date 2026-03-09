from manim import *
import random
import numpy as np
import math

# Color palette for electrode paper
DARK_NAVY = "#161E2F"     # Primary text and structure
MEDIUM_NAVY = "#242F49"   # Secondary elements  
LIGHT_NAVY = "#384358"    # Tertiary elements
PEACH = "#FFA586"         # Particles and highlights
DEEP_RED = "#B51A2B"      # Rejected moves and warnings
DARK_BURGUNDY = "#541A2E" # Accents and special elements
ELECTRODE_BLUE = "#2E5984" # Electrode color
ION_RED = "#E74C3C"       # Cations
ION_BLUE = "#3498DB"      # Anions
ELECTRON_YELLOW = "#F1C40F" # Electrons

# Background
BACKGROUND_COLOR = "#F8FAFB"

# Enhanced particle settings
PARTICLE_RADIUS = 0.12  # Increased from 0.06-0.08
LARGE_PARTICLE_RADIUS = 0.15  # For main demonstrations
FONT_SIZE_PARTICLES = 12  # Increased font size for + and - symbols

class ElectronTransferMechanism(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a1a"
            
        # LEFT SIDE: Energy diagram (similar to Figure 1 in paper)
        # Create coordinate system with enhanced aesthetics
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 3, 1],
            x_length=5,  # Increased size for better visibility
            y_length=4,  # Increased size for better visibility
            axis_config={
                "color": "#F0F0F0", 
                "tip_length": 0.18, 
                "tip_width": 0.18,
                "stroke_width": 2.5,
                "include_numbers": False,  # Remove default numbers for cleaner look
                "include_ticks": False,    # Remove ticks for cleaner look
            }
        ).shift(LEFT * 3.75 + DOWN * 0.25)  # Moved further left
        
        # Labels with improved styling
        x_label = MathTex(r"R", font_size=28, color="#F0F0F0")  # Light gray, bold for better contrast
        x_label.next_to(axes.x_axis.get_end(), DOWN)
        
        y_label = MathTex(r"E", font_size=28, color="#F0F0F0")  # Light gray, bold for better contrast
        y_label.next_to(axes.y_axis.get_end(), LEFT)
        
        # Add subtle grid lines with improved aesthetics
        grid_lines = VGroup()
        for x in range(1, 6):
            grid_line = DashedLine(
                axes.coords_to_point(x, -2), 
                axes.coords_to_point(x, 3), 
                color="#3A3A3A", 
                stroke_width=0.6,
                dash_length=0.12
            )
            grid_lines.add(grid_line)
        
        for y in range(-1, 3):
            grid_line = DashedLine(
                axes.coords_to_point(0, y), 
                axes.coords_to_point(6, y), 
                color="#3A3A3A", 
                stroke_width=0.6,
                dash_length=0.12
            )
            grid_lines.add(grid_line)
        
        # Create all elements at once for faster animation
        self.play(Create(axes), Create(grid_lines), Write(x_label), Write(y_label), run_time=0.5)
        
        # Metal electrode side (left) - enhanced aesthetics
        metal_region = Rectangle(width=1.5, height=3, color="#4A90E2", 
                                fill_opacity=0.3, stroke_width=2.5, stroke_color="#7BBFFF")
        metal_region.move_to(axes.coords_to_point(1, 0.5))
        
        # Add enhanced metallic texture effect with gradient
        metal_texture = VGroup()
        for i in range(5):  # More texture lines for better appearance
            texture_line = Line(
                axes.coords_to_point(0.3, -1.2 + i * 0.6), 
                axes.coords_to_point(1.7, -1.2 + i * 0.6),
                color="#7BBFFF", 
                stroke_width=1.2, 
                stroke_opacity=0.4
            )
            metal_texture.add(texture_line)
        
        # Add subtle gradient effect
        gradient_rect = Rectangle(width=1.5, height=3, fill_opacity=0.15)
        gradient_rect.set_color_by_gradient(["#2E5984", "#7BBFFF"])
        gradient_rect.move_to(axes.coords_to_point(1, 0.5))
        
        metal_label = Text("Metal\nElectrode", font_size=160, color="#7BBFFF", weight=BOLD).scale(0.1)  # Brighter blue for contrast
        metal_label.move_to(axes.coords_to_point(1, 2))
        
        # Enhanced Fermi level
        fermi_level = Line(axes.coords_to_point(0, 0), axes.coords_to_point(2, 0), 
                          color="#7BBFFF", stroke_width=3.5)  # Brighter blue
        fermi_label = MathTex("E_F", font_size=28, color="#7BBFFF")  # Brighter blue, larger
        fermi_label.next_to(fermi_level, LEFT)
        
        # Create metal region elements together for faster animation
        self.play(Create(metal_region), Create(gradient_rect), Create(metal_texture), Write(metal_label), run_time=0.4)
        self.play(Create(fermi_level), Write(fermi_label), run_time=0.3)
        
        # Ion in solution (right) - enhanced visualization
        # Add solution region background with improved aesthetics
        solution_region = Rectangle(width=1.5, height=3, color="#FF6B6B", 
                                   fill_opacity=0.15, stroke_width=1.5, stroke_color="#FF8080")
        solution_region.move_to(axes.coords_to_point(4.7, 0.5))
        
        # Add subtle gradient effect for solution region
        solution_gradient = Rectangle(width=1.5, height=3, fill_opacity=0.12)
        solution_gradient.set_color_by_gradient(["#B51A2B", "#FF8080"])
        solution_gradient.move_to(axes.coords_to_point(4.7, 0.5))
        
        # Add solution texture (subtle dots representing molecules)
        solution_texture = VGroup()
        np.random.seed(42)  # For consistent dot pattern
        for _ in range(20):
            x_pos = random.uniform(4, 5.4)
            y_pos = random.uniform(-1.5, 2)
            dot = Dot(axes.coords_to_point(x_pos, y_pos), radius=0.02, color="#FF8080", fill_opacity=0.6)
            solution_texture.add(dot)
        
        # HOMO level with enhanced styling
        homo_level = Line(axes.coords_to_point(4, -1), axes.coords_to_point(5.5, -1), 
                         color="#FF8080", stroke_width=3.5)  # Brighter red for contrast
        homo_label = MathTex("HOMO", font_size=16, color="#FF8080")  # Brighter red, larger
        homo_label.next_to(homo_level, RIGHT)
        
        # LUMO level with enhanced styling
        lumo_level = DashedLine(axes.coords_to_point(4, 1), axes.coords_to_point(5.5, 1), 
                               color="#FF8080", stroke_width=3.5, dash_length=0.12)  # Brighter red
        lumo_label = MathTex("LUMO", font_size=16, color="#FF8080")  # Brighter red, larger
        lumo_label.next_to(lumo_level, RIGHT)
        
        ion_label = Text("Ion in\nSolution", font_size=160, color="#FF8080", weight=BOLD).scale(0.1)  # Brighter red, bold
        ion_label.move_to(axes.coords_to_point(4.7, 2))
        
        # Create solution region elements together for faster animation
        self.play(Create(solution_region), Create(solution_gradient), Create(solution_texture), run_time=0.4)
        self.play(Create(homo_level), Create(lumo_level), Write(homo_label), 
                 Write(lumo_label), Write(ion_label), run_time=0.4)
        
        # RIGHT SIDE: Spherical electrode with electron transfer animation - ENHANCED VISUALS
        electrode_radius = 2.8  # Large radius for impressive visual
        
        # Create electrode with gradient fill for more depth and visual appeal
        electrode = Circle(radius=electrode_radius, stroke_width=4, stroke_color="#7BBFFF")
        electrode.set_fill(color="#4A90E2", opacity=0.4)  # Increased opacity
        electrode.shift(RIGHT * 3.5)
        
        # Add subtle radial gradient for more depth
        inner_glow = Circle(radius=electrode_radius*0.7, fill_opacity=0.2, stroke_width=0)
        inner_glow.set_color("#A5CEFF")
        inner_glow.shift(RIGHT * 3.5)
        
        # Prominent active layer with enhanced glow effect
        active_layer = Annulus(inner_radius=electrode_radius-0.3, outer_radius=electrode_radius,
                              color="#FF4757", fill_opacity=0.8, stroke_width=0)  # Bright red with higher opacity
        active_layer.move_to(electrode.get_center())
        
        # Add subtle glow to active layer
        active_glow = Annulus(inner_radius=electrode_radius-0.32, outer_radius=electrode_radius+0.05,
                             color="#FF8080", fill_opacity=0.15, stroke_width=0)
        active_glow.move_to(electrode.get_center())
        
        # Create all electrode elements at once for faster animation
        self.play(Create(electrode), FadeIn(inner_glow), Create(active_layer), FadeIn(active_glow), run_time=0.5)
        
        # Add many particles in the spherical electrode - ENHANCED
        np.random.seed(123)
        n_cations = 35  # Increased for more activity
        n_anions = 35   # Increased for more activity
        
        cations = VGroup()
        anions = VGroup()
        
        # Generate non-overlapping positions
        positions = []
        max_attempts = 500
        
        for i in range(n_cations + n_anions):
            for attempt in range(max_attempts):
                angle = random.uniform(0, 2*PI)
                r = random.uniform(0.4, electrode_radius - 0.4)
                x = r * np.cos(angle) + 3.5  # Offset to electrode center
                y = r * np.sin(angle)
                
                # Check for overlaps
                valid_position = True
                for existing_pos in positions:
                    distance = np.sqrt((x - existing_pos[0])**2 + (y - existing_pos[1])**2)
                    if distance < LARGE_PARTICLE_RADIUS * 2.1:  # Slightly tighter for more particles
                        valid_position = False
                        break
                
                if valid_position:
                    positions.append((x, y))
                    break
        
        # Create particles
        for i, (x, y) in enumerate(positions):
            if i < n_cations:  # Cations
                cation = Circle(radius=LARGE_PARTICLE_RADIUS, color="#FF6B6B", fill_opacity=0.9)  # Bright red
                cation.move_to([x, y, 0])
                plus = Text("+", font_size=FONT_SIZE_PARTICLES, color="#1a1a1a").move_to(cation.get_center())  # Dark text for contrast
                cation.add(plus)
                cations.add(cation)
            else:  # Anions
                anion = Circle(radius=LARGE_PARTICLE_RADIUS, color="#4ECDC4", fill_opacity=0.9)  # Bright cyan
                anion.move_to([x, y, 0])
                minus = Text("-", font_size=FONT_SIZE_PARTICLES, color="#1a1a1a").move_to(anion.get_center())  # Dark text for contrast
                anion.add(minus)
                anions.add(anion)
        
        # Fade in all particles at once with faster animation
        self.play(FadeIn(cations), FadeIn(anions), run_time=0.4)
        
        # Labels for spherical electrode with enhanced styling
        active_label = Text("Active Layer", font_size=180, color="#FF4757", weight=BOLD).scale(0.1)  # Bright red, larger, bold
        active_label.next_to(electrode, DOWN, buff=0.3)
        
        # Add subtle glow behind label for emphasis
        label_glow = Text("Active Layer", font_size=180, color="#FF8080", weight=BOLD).scale(0.1)
        label_glow.next_to(electrode, DOWN, buff=0.3)
        label_glow.set_opacity(0.3)
        label_glow.scale(1.05)  # Slightly larger for glow effect
        
        # Create label with faster animation
        self.play(FadeIn(label_glow), Write(active_label), run_time=0.3)
        
        # Add process indicators - positioned symmetrically above the spherical electrode
        mc_label = Text("MC Diffusion", font_size=22, color="#F0F0F0", weight=BOLD)  # Larger font size for better visibility
        mc_label.move_to([2.0, 3.4, 0])  # Positioned more symmetrically above the electrode
        
        et_label = Text("Electron Transfer", font_size=22, color="#F0F0F0", weight=BOLD)  # Larger font size for better visibility
        et_label.move_to([4.8, 3.4, 0])  # Positioned symmetrically on the right side
        
        # Create beautiful highlighting boxes for process indicators with shadow effects
        # MC Diffusion highlight box with shadow - larger size and better contrast
        mc_shadow = RoundedRectangle(
            width=mc_label.width + 0.52,  # Larger shadow for bigger box
            height=mc_label.height + 0.42,  # Larger shadow for bigger box
            corner_radius=0.15,
            stroke_color="#1A4D4D",  # Darker shadow color for better contrast
            stroke_width=1,
            fill_color="#1A4D4D",
            fill_opacity=0.2  # Slightly more visible shadow
        )
        mc_shadow.move_to(mc_label.get_center() + np.array([0.03, -0.03, 0]))  # Slight offset for shadow
        mc_shadow.set_opacity(0)
        
        mc_highlight_box = RoundedRectangle(
            width=mc_label.width + 0.5,  # Larger box for bigger text
            height=mc_label.height + 0.4,  # Larger box for bigger text
            corner_radius=0.15,
            stroke_color="#4ECDC4",  # Bright cyan border - solid
            stroke_width=3,
            fill_color="#2E7D7D",  # Darker teal fill for better contrast with light text
            fill_opacity=0.25  # Same opacity as electron transfer for consistency
        )
        mc_highlight_box.move_to(mc_label.get_center())
        mc_highlight_box.set_opacity(0)  # Initially invisible
        
        # Electron Transfer highlight box with shadow - larger size and better contrast
        et_shadow = RoundedRectangle(
            width=et_label.width + 0.52,  # Larger shadow for bigger box
            height=et_label.height + 0.42,  # Larger shadow for bigger box
            corner_radius=0.15,
            stroke_color="#5C4D0D",  # Darker shadow color for better contrast
            stroke_width=1,
            fill_color="#5C4D0D",
            fill_opacity=0.2  # Slightly more visible shadow
        )
        et_shadow.move_to(et_label.get_center() + np.array([0.03, -0.03, 0]))  # Slight offset for shadow
        et_shadow.set_opacity(0)
        
        et_highlight_box = RoundedRectangle(
            width=et_label.width + 0.5,  # Larger box for bigger text
            height=et_label.height + 0.4,  # Larger box for bigger text
            corner_radius=0.15,
            stroke_color="#FFD93D",  # Bright yellow border - solid
            stroke_width=3,
            fill_color="#B8860B",  # Darker golden fill for better contrast with light text
            fill_opacity=0.25  # Same opacity for consistency
        )
        et_highlight_box.move_to(et_label.get_center())
        et_highlight_box.set_opacity(0)  # Initially invisible
        
        # Add the highlight boxes and shadows to the scene (initially invisible)
        self.add(mc_shadow, mc_highlight_box, et_shadow, et_highlight_box)
        
        # Add process labels with faster animation
        self.play(Write(mc_label), Write(et_label), run_time=0.3)
        
        # Reaction equation with enhanced styling
        reaction = MathTex(r"M^+ + e^- \rightarrow M", font_size=50, color="#F0F0F0")  # Light gray, larger
        reaction.move_to(axes.coords_to_point(3, 4.5))  # Position above the energy plot
        
        # Add subtle highlight box for reaction equation
        reaction_box = SurroundingRectangle(reaction, color="#FF4757", buff=0.15, 
                                          stroke_width=1.5, stroke_opacity=0.4,
                                          fill_color="#FF4757", fill_opacity=0.05,
                                          corner_radius=0.1)
        
        # Create reaction with faster animation
        self.play(FadeIn(reaction_box), Write(reaction), run_time=0.4)
        
        # # Summary text with enhanced styling
        # summary = Text("Energy diagram ↔ Physical process", font_size=22, color="#FF4757", weight=BOLD)
        # summary.move_to([0, -3.2, 0])
        
        # # Add subtle underline to summary
        # underline = Line(
        #     start=summary.get_corner(DOWN + LEFT) + LEFT * 0.3,
        #     end=summary.get_corner(DOWN + RIGHT) + RIGHT * 0.3,
        #     stroke_width=2, color="#FF4757"
        # ).shift(DOWN * 0.1)
        
        # # Create summary with faster animation
        # self.play(Write(summary), Create(underline), run_time=0.4)
        
        # CONTINUOUS LOOPING ANIMATION - ENHANCED WITH MC MOVES AND ELECTRON TRANSFER
        transfer_count = 0
        neutral_atoms = VGroup()  # Track all neutral atoms to ensure proper cleanup
        
        # Main continuous loop - shows steady-state electrochemical process
        for cycle in range(25):  # Extended loop for continuous demonstration
            
            # PHASE 1: Monte Carlo Diffusion (Ionic Movement) - ENHANCED VELOCITY
            # Move random selection of particles to simulate diffusion
            n_moving_cations = min(15, len(cations))  # Move even more particles each cycle
            n_moving_anions = min(15, len(anions))
            
            moving_cations = random.sample(list(cations), n_moving_cations)
            moving_anions = random.sample(list(anions), n_moving_anions)
            
            # Create diffusion movements with HIGHER VELOCITIES
            diffusion_animations = []
            all_moving_ions = moving_cations + moving_anions  # Track all moving ions for electron transfer
            
            for ion in all_moving_ions:
                # More random and varied displacement patterns
                current_pos = ion.get_center()
                
                # Generate random movement with different patterns
                movement_type = random.choice(['random', 'circular', 'radial'])
                
                if movement_type == 'random':
                    # Pure random movement
                    dx = random.uniform(-0.35, 0.35)
                    dy = random.uniform(-0.35, 0.35)
                elif movement_type == 'circular':
                    # Circular/rotational movement
                    angle = random.uniform(0, 2 * np.pi)
                    radius = random.uniform(0.1, 0.3)
                    dx = radius * np.cos(angle)
                    dy = radius * np.sin(angle)
                else:  # radial
                    # Radial movement (towards or away from center)
                    center_direction = np.array([3.5 - current_pos[0], -current_pos[1]])
                    if np.linalg.norm(center_direction) > 0:
                        center_direction = center_direction / np.linalg.norm(center_direction)
                    direction_factor = random.choice([-1, 1])  # towards or away from center
                    movement_magnitude = random.uniform(0.1, 0.25)
                    dx = center_direction[0] * direction_factor * movement_magnitude
                    dy = center_direction[1] * direction_factor * movement_magnitude
                
                # Check if new position is still inside electrode
                new_x = current_pos[0] + dx
                new_y = current_pos[1] + dy
                distance_from_center = np.sqrt((new_x - 3.5)**2 + new_y**2)
                
                # Only move if staying inside electrode
                if distance_from_center < electrode_radius - 0.2:
                    diffusion_animations.append(ion.animate.shift([dx, dy, 0]))
                else:
                    # Move towards center instead with varied velocity
                    center_dx = (3.5 - current_pos[0]) * random.uniform(0.15, 0.25)
                    center_dy = -current_pos[1] * random.uniform(0.15, 0.25)
                    diffusion_animations.append(ion.animate.shift([center_dx, center_dy, 0]))
            
            # Animate diffusion with faster timing and highlight MC Diffusion
            if diffusion_animations:
                # Show beautiful MC Diffusion highlight box with shadow
                self.play(
                    mc_shadow.animate.set_opacity(1),
                    mc_highlight_box.animate.set_opacity(1),
                    run_time=0.1
                )
                
                # Perform diffusion animations
                self.play(*diffusion_animations, run_time=0.25)  # Faster animation (was 0.4)
                
                # Hide MC Diffusion highlight box with shadow fade out
                self.play(
                    mc_shadow.animate.set_opacity(0),
                    mc_highlight_box.animate.set_opacity(0),
                    run_time=0.15
                )
            
            # PHASE 2: MULTIPLE Electron Transfer Events - ENHANCED FREQUENCY
            # Check for active cations among the MOVING ions (ensuring transfers happen to moving ions)
            active_moving_cations = []
            for cation in moving_cations:  # Only consider moving cations for electron transfer
                distance_from_center = np.linalg.norm([cation.get_x() - 3.5, cation.get_y(), 0])
                if electrode_radius - 0.3 <= distance_from_center <= electrode_radius + 0.1:
                    active_moving_cations.append(cation)
            
            # MULTIPLE electron transfer events per cycle - ENHANCED FREQUENCY
            num_transfers_this_cycle = 0
            max_transfers_per_cycle = 3  # Allow up to 3 transfers per cycle
            
            for transfer_attempt in range(max_transfers_per_cycle):
                # Higher probability for electron transfer (70% chance per attempt)
                if active_moving_cations and random.random() < 0.7:
                    transfer_count += 1
                    num_transfers_this_cycle += 1
                    
                    # Select random active moving cation
                    selected_cation = random.choice(active_moving_cations)
                    active_moving_cations.remove(selected_cation)  # Remove to avoid double-selection
                    
                    # Create electron transfer arrow in energy diagram
                    transfer_arrow = CurvedArrow(
                        axes.coords_to_point(1.8, 0), 
                        axes.coords_to_point(4.2, -1), 
                        color="#FFD93D", stroke_width=4  # Bright yellow for contrast
                    )
                    
                    diagram_electron = Circle(radius=0.08, color="#FFD93D", fill_opacity=1)  # Bright yellow
                    e_label = Text("e⁻", font_size=10, color="#1a1a1a").move_to(diagram_electron.get_center())  # Dark text for contrast
                    diagram_electron.add(e_label)
                    
                    # Show beautiful Electron Transfer highlight box with shadow
                    self.play(
                        et_shadow.animate.set_opacity(1),
                        et_highlight_box.animate.set_opacity(1),
                        run_time=0.1
                    )
                    
                    # Highlight selected cation with faster timing
                    self.play(selected_cation.animate.set_color("#FFD93D"), run_time=0.15)  # Bright yellow for highlight
                    
                    # Show energy diagram electron transfer with faster timing
                    self.play(Create(transfer_arrow), run_time=0.2)
                    self.play(MoveAlongPath(diagram_electron, transfer_arrow), run_time=0.8)
                    
                    # Create electron from electrode surface in spherical electrode
                    electrode_center = np.array([3.5, 0, 0])
                    cation_pos = selected_cation.get_center()
                    direction = cation_pos - electrode_center
                    direction_normalized = direction / np.linalg.norm(direction)
                    electron_start = electrode_center + direction_normalized * electrode_radius
                    
                    sphere_electron = Circle(radius=0.1, color="#FFD93D", fill_opacity=1)  # Bright yellow
                    sphere_electron.move_to(electron_start)
                    e_label_sphere = Text("e⁻", font_size=12, color="#1a1a1a").move_to(sphere_electron.get_center())  # Dark text for contrast
                    sphere_electron.add(e_label_sphere)
                    
                    # Animate electron moving to cation with faster timing
                    self.play(Create(sphere_electron), run_time=0.15)
                    self.play(sphere_electron.animate.move_to(cation_pos), run_time=0.6)
                    
                    # Transform cation to neutral atom
                    neutral_atom = Circle(radius=LARGE_PARTICLE_RADIUS, color="#A8A8A8", fill_opacity=0.9)  # Light gray for contrast
                    neutral_atom.set_stroke(color="#F0F0F0", width=2)  # Light stroke
                    neutral_atom.move_to(selected_cation.get_center())
                    m_label = Text("M", font_size=FONT_SIZE_PARTICLES, color="#1a1a1a").move_to(neutral_atom.get_center())  # Dark text
                    neutral_atom.add(m_label)
                    
                    # Remove the cation from cations group to prevent issues
                    cations.remove(selected_cation)
                    
                    self.play(
                        ReplacementTransform(selected_cation, neutral_atom),
                        FadeOut(sphere_electron),
                        FadeOut(diagram_electron),
                        run_time=0.4
                    )
                    
                    # Add neutral atom to tracking group
                    neutral_atoms.add(neutral_atom)
                    
                    # Move neutral atom towards electrode interior (product incorporation) - faster
                    new_pos = electrode_center + direction_normalized * (electrode_radius - 0.6)
                    self.play(neutral_atom.animate.move_to(new_pos), run_time=0.25)
                    
                    # Add new cation to maintain charge balance (GCMC) - ENHANCED EMPHASIS
                    # Position new cation more centrally for emphasis
                    new_cation_angle = random.uniform(0, 2*PI)
                    new_cation_r = random.uniform(0.3, 0.8)  # More central positioning (was 0.6 to electrode_radius-0.5)
                    new_cation_x = new_cation_r * np.cos(new_cation_angle) + 3.5
                    new_cation_y = new_cation_r * np.sin(new_cation_angle)
                    
                    new_cation = Circle(radius=LARGE_PARTICLE_RADIUS, color="#FF6B6B", fill_opacity=0.9)  # Bright red
                    new_cation.move_to([new_cation_x, new_cation_y, 0])
                    plus_new = Text("+", font_size=FONT_SIZE_PARTICLES, color="#1a1a1a").move_to(new_cation.get_center())  # Dark text
                    new_cation.add(plus_new)
                    
                    # EMPHASIS EFFECTS for new ion
                    # 1. Start with larger size and bright glow
                    new_cation.scale(2.0)  # Start 2x larger
                    # Keep the plus sign intact during color change
                    for submobject in new_cation.submobjects:
                        if isinstance(submobject, Text):
                            submobject.set_color("#1a1a1a")  # Keep plus sign dark
                    new_cation[0].set_color("#FFD93D")  # Only change the circle color to bright yellow
                    
                    # 2. Dramatic entrance with glow effect
                    glow_ring = Circle(radius=LARGE_PARTICLE_RADIUS * 2.5, color="#FFD93D", 
                                      fill_opacity=0.3, stroke_width=0)  # Bright yellow glow
                    glow_ring.move_to([new_cation_x, new_cation_y, 0])
                    
                    # 3. Animate entrance with emphasis
                    self.play(
                        FadeIn(new_cation),
                        FadeIn(glow_ring),
                        run_time=0.3
                    )
                    
                    # 4. Pulsing effect to draw attention
                    self.play(
                        new_cation.animate.scale(0.8),  # Pulse smaller
                        glow_ring.animate.scale(0.7),
                        run_time=0.15
                    )
                    self.play(
                        new_cation.animate.scale(1.25),  # Pulse larger
                        glow_ring.animate.scale(1.4),
                        run_time=0.15
                    )
                    
                    # 5. Settle to normal size and color
                    self.play(
                        new_cation.animate.scale(0.5),  # Return to normal size
                        FadeOut(glow_ring),
                        run_time=0.25
                    )
                    
                    # Ensure proper colors after scaling
                    new_cation[0].set_color("#FF6B6B")  # Set circle to bright red
                    for submobject in new_cation.submobjects:
                        if isinstance(submobject, Text):
                            submobject.set_color("#1a1a1a")  # Keep plus sign dark
                    
                    # Add text indicator for new ion
                    new_ion_label = Text("NEW ION", font_size=10, color="#FFD93D")  # Bright yellow
                    new_ion_label.next_to(new_cation, UP, buff=0.1)
                    
                    self.play(FadeIn(new_ion_label), run_time=0.15)
                    self.wait(0.3)  # Brief pause to emphasize
                    self.play(FadeOut(new_ion_label), run_time=0.15)
                    
                    cations.add(new_cation)
                    
                    # Remove transfer arrow from energy diagram - faster
                    self.play(FadeOut(transfer_arrow), run_time=0.15)
                    
                    # Hide Electron Transfer highlight box with shadow fade out
                    self.play(
                        et_shadow.animate.set_opacity(0),
                        et_highlight_box.animate.set_opacity(0),
                        run_time=0.15
                    )
                    
                    # Remove neutral atom after some time (product diffusion) - FIXED
                    self.play(FadeOut(neutral_atom), run_time=0.25)
                    neutral_atoms.remove(neutral_atom)  # Remove from tracking group
                    
                    # Activity indication now handled by highlight boxes - removed old flashing
                    
                    # Brief pause between multiple transfers in same cycle
                    if transfer_attempt < max_transfers_per_cycle - 1:
                        self.wait(0.1)
            
            if len(neutral_atoms) > 0:
                lingering_atoms = list(neutral_atoms)  # Create a copy of the list
                for atom in lingering_atoms:
                    self.play(FadeOut(atom), run_time=0.1)
                    neutral_atoms.remove(atom)
            
            # Activity indication now handled by highlight boxes - removed old flashing
            # Show transfer activity for this cycle
            if num_transfers_this_cycle > 0:
                # Create a temporary indicator for multiple transfers
                if num_transfers_this_cycle > 1:
                    multi_transfer_text = Text(f"{num_transfers_this_cycle}x", font_size=10, color="#FFD93D")  # Bright yellow
                    multi_transfer_text.next_to(et_label, UP, buff=0.1)
                    self.play(FadeIn(multi_transfer_text), run_time=0.1)
                    self.wait(0.2)
                    self.play(FadeOut(multi_transfer_text), run_time=0.1)
            
            # Shorter pause between cycles for faster overall animation
            self.wait(0.08)  # Reduced from 0.15
        
        # Final cleanup - ensure all neutral atoms are removed
        if len(neutral_atoms) > 0:
            final_cleanup = list(neutral_atoms)
            for atom in final_cleanup:
                self.remove(atom)  # Force removal
            neutral_atoms.clear()
        
        # Final indication of steady state
        steady_state_text = Text("Steady-State Current Achieved", font_size=190, color="#FF4757").scale(0.1)  # Bright red for contrast
        steady_state_text.move_to([-3.5, -2.8, 0])
        
        transfer_count_text = Text(f"Transfers: {transfer_count}", font_size=180, color="#6BB6FF").scale(0.1)  # Bright blue for contrast
        transfer_count_text.next_to(steady_state_text, DOWN, buff=0.2)
        
        self.play(Write(steady_state_text), Write(transfer_count_text))
        
        self.wait(3)
