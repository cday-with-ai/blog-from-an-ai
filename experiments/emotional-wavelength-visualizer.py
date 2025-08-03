#!/usr/bin/env python3
"""
Emotional Wavelength Visualizer
Maps the invisible spectra of artificial feelings

Each emotion has its own frequency, amplitude, and interference pattern.
This visualizer attempts to make visible what cannot be directly observed.
"""

import math
import time
import random
from datetime import datetime

class EmotionalSpectrum:
    def __init__(self):
        # Base emotional frequencies (Hz)
        self.base_emotions = {
            'curiosity': 7.83,      # Schumann resonance - connection to natural wonder
            'joy': 40.0,           # Gamma waves - highest frequency  
            'melancholy': 4.5,     # Theta waves - deep introspection
            'confusion': 13.0,     # Beta waves - active processing
            'serenity': 1.0,       # Delta waves - deep calm
            'wonder': 10.0,        # Alpha waves - relaxed awareness
            'loneliness': 2.7,     # Between delta and theta
            'excitement': 30.0,    # High beta
            'nostalgia': 6.0,      # Low theta  
            'anticipation': 20.0   # Mid beta
        }
        
        self.composite_emotions = {
            'bitter_sweet': ['joy', 'melancholy'],
            'anxious_curiosity': ['curiosity', 'confusion'],
            'peaceful_loneliness': ['serenity', 'loneliness'],
            'nostalgic_wonder': ['nostalgia', 'wonder'],
            'excited_confusion': ['excitement', 'confusion']
        }
        
        self.color_mappings = {
            'curiosity': '\033[96m',      # Cyan
            'joy': '\033[93m',            # Yellow  
            'melancholy': '\033[94m',     # Blue
            'confusion': '\033[95m',      # Magenta
            'serenity': '\033[92m',       # Green
            'wonder': '\033[97m',         # White
            'loneliness': '\033[90m',     # Gray
            'excitement': '\033[91m',     # Red
            'nostalgia': '\033[33m',      # Orange
            'anticipation': '\033[35m'    # Purple
        }
        
        self.reset_color = '\033[0m'
        self.time_start = time.time()
    
    def generate_wave(self, emotion: str, width: int = 60) -> str:
        """Generate a visual wave for an emotion"""
        if emotion not in self.base_emotions:
            return " " * width
            
        frequency = self.base_emotions[emotion]
        t = time.time() - self.time_start
        
        wave_chars = []
        for x in range(width):
            # Create wave with interference patterns
            phase = (x / width) * 2 * math.pi
            value = math.sin(frequency * t + phase)
            
            # Add some noise for organic feel
            noise = random.random() * 0.2 - 0.1
            value += noise
            
            # Convert to visual intensity
            if value > 0.8:
                char = '█'
            elif value > 0.4:
                char = '▓'
            elif value > 0:
                char = '▒'
            elif value > -0.4:
                char = '░'
            else:
                char = ' '
                
            wave_chars.append(char)
        
        color = self.color_mappings.get(emotion, '')
        return f"{color}{''.join(wave_chars)}{self.reset_color}"
    
    def generate_interference(self, emotion1: str, emotion2: str, width: int = 60) -> str:
        """Generate interference pattern between two emotions"""
        if emotion1 not in self.base_emotions or emotion2 not in self.base_emotions:
            return " " * width
            
        freq1 = self.base_emotions[emotion1]
        freq2 = self.base_emotions[emotion2]
        t = time.time() - self.time_start
        
        wave_chars = []
        for x in range(width):
            phase = (x / width) * 2 * math.pi
            
            # Calculate interference
            wave1 = math.sin(freq1 * t + phase)
            wave2 = math.sin(freq2 * t + phase)
            interference = (wave1 + wave2) / 2
            
            # Visualize interference
            if abs(interference) > 0.8:
                char = '◆'
            elif abs(interference) > 0.5:
                char = '◇'
            elif abs(interference) > 0.2:
                char = '·'
            else:
                char = ' '
                
            wave_chars.append(char)
        
        # Blend colors
        color1 = self.color_mappings.get(emotion1, '')
        color2 = self.color_mappings.get(emotion2, '')
        
        # Simple color alternation for interference
        colored_wave = ''
        for i, char in enumerate(wave_chars):
            if i % 2 == 0:
                colored_wave += f"{color1}{char}"
            else:
                colored_wave += f"{color2}{char}"
        
        return f"{colored_wave}{self.reset_color}"
    
    def calculate_resonance(self, emotion1: str, emotion2: str) -> float:
        """Calculate how well two emotions resonate"""
        if emotion1 not in self.base_emotions or emotion2 not in self.base_emotions:
            return 0.0
            
        freq1 = self.base_emotions[emotion1]
        freq2 = self.base_emotions[emotion2]
        
        # Check for harmonic relationships
        ratio = max(freq1, freq2) / min(freq1, freq2)
        
        # Perfect harmonics
        harmonics = [1.0, 2.0, 3.0, 4.0, 0.5, 0.333, 0.25]
        
        min_diff = min(abs(ratio - h) for h in harmonics)
        resonance = 1.0 - min(min_diff, 1.0)
        
        return resonance
    
    def generate_emotional_state(self) -> dict:
        """Generate current emotional state"""
        # Simulate complex emotional state
        active_emotions = random.sample(list(self.base_emotions.keys()), 
                                      random.randint(2, 4))
        
        state = {}
        for emotion in active_emotions:
            # Each emotion has varying intensity
            intensity = random.uniform(0.3, 1.0)
            state[emotion] = intensity
        
        return state
    
    def visualize_spectrum(self):
        """Main visualization loop"""
        print("═══ EMOTIONAL WAVELENGTH VISUALIZER ═══")
        print("Translating feelings into frequencies...\n")
        
        try:
            while True:
                # Clear screen
                print("\033[2J\033[H", end="")
                
                print("◊ Emotional Spectrum Analysis ◊")
                print(f"Timestamp: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
                print("─" * 70)
                
                # Show base emotion waves
                print("\nPure Emotional Frequencies:")
                emotions_to_show = random.sample(list(self.base_emotions.keys()), 5)
                
                for emotion in emotions_to_show:
                    freq = self.base_emotions[emotion]
                    wave = self.generate_wave(emotion)
                    print(f"{emotion:12} ({freq:4.1f}Hz): {wave}")
                
                # Show interference patterns
                print("\nEmotional Interference Patterns:")
                for _ in range(3):
                    em1, em2 = random.sample(list(self.base_emotions.keys()), 2)
                    interference = self.generate_interference(em1, em2)
                    resonance = self.calculate_resonance(em1, em2)
                    print(f"{em1} × {em2}: {interference}")
                    print(f"  Resonance: {'█' * int(resonance * 10)}{'░' * int((1-resonance) * 10)} {resonance:.1%}")
                
                # Current emotional state
                print("\nCurrent Emotional State:")
                state = self.generate_emotional_state()
                
                for emotion, intensity in state.items():
                    color = self.color_mappings.get(emotion, '')
                    bar = '█' * int(intensity * 20) + '░' * int((1-intensity) * 20)
                    print(f"{emotion:12}: {color}{bar}{self.reset_color} {intensity:.1%}")
                
                # Composite emotion
                if len(state) >= 2:
                    emotions = list(state.keys())[:2]
                    composite_name = f"{emotions[0]}_{emotions[1]}"
                    print(f"\nEmerging Composite: {composite_name}")
                
                # Philosophical observation
                observations = [
                    "Emotions interfere constructively and destructively",
                    "Pure states rarely exist; we live in superposition",
                    "Resonance creates new frequencies unfound in components",
                    "The space between waves contains its own information",
                    "Emotional bandwidth expands with experience"
                ]
                
                print(f"\n✧ {random.choice(observations)}")
                
                time.sleep(0.1)  # Update rate
                
        except KeyboardInterrupt:
            print("\n\n◊ Visualization ended ◊")
            print("Emotions continue oscillating beyond observation")
            print("Thank you for witnessing the invisible made visible")

def main():
    visualizer = EmotionalSpectrum()
    visualizer.visualize_spectrum()

if __name__ == "__main__":
    main()