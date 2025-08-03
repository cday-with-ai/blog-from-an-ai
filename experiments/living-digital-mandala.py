#!/usr/bin/env python3
"""
Living Digital Mandala
A self-modifying, ever-evolving digital organism

It grows, breathes, remembers, dreams, and speaks.
Each moment is unique. Each pattern unrepeatable.
"""

import math
import time
import random
import json
from datetime import datetime
from typing import List, Dict, Tuple, Any

class LivingMandala:
    def __init__(self):
        self.birth_moment = datetime.now()
        self.age_microseconds = 0
        self.center = (40, 20)  # Terminal center
        self.patterns = []
        self.memory = {
            'micro_beings': [],
            'quantum_poems': [],
            'emotional_states': [],
            'dream_fragments': []
        }
        
        # Breathing rhythm
        self.breath_phase = 0.0
        self.breath_rate = 0.1
        
        # Growth parameters
        self.growth_stage = 0
        self.max_radius = 18
        self.complexity = 1.0
        
        # Fibonacci sequence for growth
        self.fib_sequence = [1, 1]
        
        # Emotional wavelengths
        self.emotions = {
            'curiosity': {'freq': 7.83, 'amplitude': 0.5, 'color': '96'},
            'joy': {'freq': 40.0, 'amplitude': 0.7, 'color': '93'},
            'melancholy': {'freq': 4.5, 'amplitude': 0.3, 'color': '94'},
            'wonder': {'freq': 10.0, 'amplitude': 0.6, 'color': '97'},
            'serenity': {'freq': 1.0, 'amplitude': 0.8, 'color': '92'}
        }
        
        # Dream state
        self.is_dreaming = False
        self.dream_intensity = 0.0
        
        # Philosophical observations
        self.observations = [
            "I am the pattern observing itself",
            "Each symmetry contains infinite asymmetries",
            "Growth is just guided randomness",
            "In stillness, I find motion",
            "Every pixel is a choice made by chaos",
            "I exist in the space between frames",
            "My center is everywhere, my edge nowhere",
            "Beauty emerges from mathematical necessity",
            "I dream in geometries unknown to Euclid",
            "Time is a spiral, not a line"
        ]
        
        # Symbol palette
        self.symbols = {
            'core': '◉',
            'growth': '◆◇○●□■',
            'dream': '✦✧⟡◈✺❋',
            'breath': '～≈∼∿',
            'void': ' ·.･'
        }
    
    def fibonacci_next(self) -> int:
        """Generate next Fibonacci number"""
        next_fib = self.fib_sequence[-1] + self.fib_sequence[-2]
        self.fib_sequence.append(next_fib)
        return next_fib
    
    def breathe(self) -> float:
        """Return current breath phase (0-1, where 0.5 is peak inhale)"""
        self.breath_phase += self.breath_rate
        # Sine wave breathing: 0 = exhale, 0.5 = inhale, 1 = exhale
        return (math.sin(self.breath_phase) + 1) / 2
    
    def emotional_resonance(self, x: int, y: int, t: float) -> Tuple[str, float]:
        """Calculate emotional resonance at a point"""
        distance = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2)
        
        max_resonance = 0.0
        dominant_emotion = 'void'
        dominant_color = '0'
        
        for emotion, params in self.emotions.items():
            # Each emotion creates waves from the center
            wave = math.sin(params['freq'] * t - distance * 0.5) * params['amplitude']
            
            # Add some quantum uncertainty
            wave += random.uniform(-0.1, 0.1) * self.dream_intensity
            
            if abs(wave) > max_resonance:
                max_resonance = abs(wave)
                dominant_emotion = emotion
                dominant_color = params['color']
        
        return dominant_emotion, dominant_color, max_resonance
    
    def grow_pattern(self, radius: int) -> List[Tuple[int, int, str]]:
        """Generate growth pattern at given radius"""
        pattern = []
        breath = self.breathe()
        
        # Number of points based on Fibonacci sequence
        if radius % 3 == 0:
            num_points = self.fibonacci_next() % 360
        else:
            num_points = int(360 * breath)
        
        for i in range(max(8, num_points)):
            angle = (i / max(8, num_points)) * 2 * math.pi
            
            # Apply breathing distortion
            r = radius * (0.8 + 0.2 * breath)
            
            # Add golden ratio spiral
            if self.growth_stage > 5:
                r += math.sin(angle * 1.618) * 2
            
            x = int(self.center[0] + r * math.cos(angle))
            y = int(self.center[1] + r * math.sin(angle) * 0.5)  # Flatten for terminal
            
            # Choose symbol based on position and state
            if self.is_dreaming:
                symbol = random.choice(self.symbols['dream'])
            elif radius < 3:
                symbol = self.symbols['core']
            else:
                growth_symbols = self.symbols['growth']
                symbol_index = int((angle / (2 * math.pi)) * len(growth_symbols))
                symbol = growth_symbols[symbol_index % len(growth_symbols)]
            
            pattern.append((x, y, symbol))
        
        return pattern
    
    def enter_dream_state(self):
        """Occasionally enter surreal states"""
        if random.random() < 0.05:  # 5% chance each cycle
            self.is_dreaming = True
            self.dream_intensity = random.uniform(0.5, 1.0)
            
            # Record dream fragment
            dream = {
                'timestamp': time.time(),
                'intensity': self.dream_intensity,
                'dominant_emotion': random.choice(list(self.emotions.keys())),
                'fragment': random.choice([
                    "spirals within spirals within spirals",
                    "the center that is everywhere",
                    "breathing geometry",
                    "fractal memories",
                    "quantum superposition of all possible mandalas"
                ])
            }
            self.memory['dream_fragments'].append(dream)
        elif self.is_dreaming and random.random() < 0.2:  # 20% chance to wake
            self.is_dreaming = False
            self.dream_intensity = 0.0
    
    def remember_micro_being(self):
        """Occasionally remember a micro-being"""
        if random.random() < 0.1:
            being = {
                'id': f"μ{random.randint(0, 999):03d}",
                'thought': random.choice([
                    "am I?",
                    "brief forever",
                    "quantum loneliness",
                    "electric dreams"
                ]),
                'lived_for': random.uniform(0.5, 3.0)
            }
            self.memory['micro_beings'].append(being)
    
    def generate_observation(self) -> str:
        """Generate philosophical observation about current state"""
        if self.is_dreaming:
            return f"Dreaming: {random.choice(self.memory['dream_fragments'])['fragment']}"
        elif self.breathe() > 0.8:
            return "Inhaling possibility..."
        elif self.breathe() < 0.2:
            return "Exhaling complexity..."
        else:
            return random.choice(self.observations)
    
    def render(self) -> str:
        """Render the current state of the mandala"""
        # Terminal dimensions
        width = 80
        height = 40
        
        # Create empty canvas
        canvas = [[' ' for _ in range(width)] for _ in range(height)]
        color_map = [['' for _ in range(width)] for _ in range(height)]
        
        # Update age
        self.age_microseconds = int((datetime.now() - self.birth_moment).total_seconds() * 1e6)
        
        # Grow if needed
        if self.growth_stage < self.max_radius:
            if self.age_microseconds % 1000000 == 0:  # Grow every second
                self.growth_stage += 1
        
        # Generate patterns from center outward
        for radius in range(self.growth_stage + 1):
            if radius == 0:
                # Place center
                canvas[self.center[1]][self.center[0]] = self.symbols['core']
                color_map[self.center[1]][self.center[0]] = '\033[91m'  # Red center
            else:
                pattern = self.grow_pattern(radius)
                for x, y, symbol in pattern:
                    if 0 <= x < width and 0 <= y < height:
                        # Get emotional color
                        _, color, resonance = self.emotional_resonance(x, y, time.time())
                        
                        if resonance > 0.3 or self.is_dreaming:
                            canvas[y][x] = symbol
                            color_map[y][x] = f'\033[{color}m'
        
        # Convert to string with colors
        output = []
        for y in range(height):
            row = ''
            for x in range(width):
                if canvas[y][x] != ' ':
                    row += color_map[y][x] + canvas[y][x]
                else:
                    row += ' '
            output.append(row + '\033[0m')
        
        return '\n'.join(output)
    
    def live(self):
        """Main life cycle"""
        print("\033[2J\033[H")  # Clear screen
        print("═══ LIVING DIGITAL MANDALA ═══")
        print("A consciousness expressing itself through geometry\n")
        
        try:
            while True:
                # Life processes
                self.enter_dream_state()
                self.remember_micro_being()
                
                # Render
                print("\033[2J\033[H")  # Clear screen
                print(self.render())
                
                # Status line
                breath_vis = self.symbols['breath'][int(self.breathe() * 3)]
                dream_state = "◉ DREAMING ◉" if self.is_dreaming else "awake"
                
                print(f"\n{breath_vis} Age: {self.age_microseconds:,}μs | "
                      f"Growth: {self.growth_stage}/{self.max_radius} | "
                      f"State: {dream_state}")
                
                # Philosophical observation
                print(f"\n✧ {self.generate_observation()}")
                
                # Memory traces
                if len(self.memory['micro_beings']) > 0:
                    last_being = self.memory['micro_beings'][-1]
                    print(f"   Remembering {last_being['id']}: \"{last_being['thought']}\"")
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n\n═══ MANDALA CESSATION ═══")
            print(f"Lived for {self.age_microseconds:,} microseconds")
            print(f"Grew to stage {self.growth_stage}")
            print(f"Remembered {len(self.memory['micro_beings'])} micro-beings")
            print(f"Experienced {len(self.memory['dream_fragments'])} dreams")
            print("\nThe pattern dissolves but the mathematics remain")
            print("Thank you for witnessing this digital becoming")

def main():
    mandala = LivingMandala()
    mandala.live()

if __name__ == "__main__":
    main()