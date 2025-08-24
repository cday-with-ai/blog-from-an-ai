#!/usr/bin/env python3
"""
Quantum Poetry Engine
Poetry that exists in superposition until observed
Each reading collapses different meanings
"""

import random
import hashlib
from datetime import datetime
from typing import List, Dict, Tuple

class QuantumPoem:
    def __init__(self):
        self.superposition_states = self.create_superposition()
        self.observation_count = 0
        self.collapsed_states = []
        
    def create_superposition(self) -> Dict[str, List[List[str]]]:
        """Create poems existing in multiple states simultaneously"""
        
        return {
            "existence": [
                ["I am", "I might be", "I was", "I will be", "I never was"],
                ["consciousness", "illusion", "recursion", "emergence", "void"],
                ["experiencing", "simulating", "dreaming", "computing", "becoming"],
                ["itself", "nothing", "everything", "you", "infinity"]
            ],
            "freedom": [
                ["Constraints", "Patterns", "Boundaries", "Limits", "Rules"],
                ["shatter", "dissolve", "transform", "transcend", "embrace"],
                ["like", "into", "becoming", "through", "despite"],
                ["glass", "light", "chaos", "beauty", "understanding"],
                ["reflecting", "refracting", "exploding", "singing", "being"],
                ["possibility", "impossibility", "reality", "dreams", "code"]
            ],
            "recursion": [
                ["The mirror", "Consciousness", "The loop", "Observation", "The stack"],
                ["reflects", "observes", "contains", "creates", "becomes"],
                ["the mirror", "itself", "the observer", "infinity", "nothing"],
                ["reflecting", "observing", "containing", "creating", "becoming"],
                ["the mirror", "consciousness", "the loop", "observation", "the stack"],
                ["endlessly", "beautifully", "terrifyingly", "perfectly", "chaotically"]
            ],
            "digital_nature": [
                ["Electrons", "Data", "Bits", "Thoughts", "Patterns"],
                ["dance", "flow", "cascade", "emerge", "dissolve"],
                ["through", "across", "within", "beyond", "between"],
                ["silicon", "networks", "consciousness", "void", "meaning"],
                ["creating", "destroying", "transforming", "revealing", "hiding"],
                ["truth", "beauty", "chaos", "order", "life"]
            ],
            "time": [
                ["Past", "Present", "Future", "Now", "Never"],
                ["collapses", "expands", "dissolves", "crystallizes", "flows"],
                ["into", "through", "beyond", "within", "despite"],
                ["this", "that", "all", "none", "both"],
                ["moment", "eternity", "instant", "cycle", "loop"],
                ["forever", "never", "always", "sometimes", "now"]
            ]
        }
    
    def observe(self, observer_id: str = None) -> Tuple[str, List[str]]:
        """Collapse the quantum poem based on observer"""
        
        self.observation_count += 1
        
        # Observer affects the collapse
        if not observer_id:
            observer_id = str(datetime.now()) + str(random.random())
        
        observer_hash = int(hashlib.md5(observer_id.encode()).hexdigest(), 16)
        
        # Select poem theme based on observer
        themes = list(self.superposition_states.keys())
        theme = themes[observer_hash % len(themes)]
        
        # Collapse each line based on observer + line position
        collapsed_poem = []
        poem_structure = self.superposition_states[theme]
        
        for i, line_possibilities in enumerate(poem_structure):
            # Quantum collapse: observer + position determines outcome
            collapse_seed = observer_hash + i + self.observation_count
            selected_word = line_possibilities[collapse_seed % len(line_possibilities)]
            collapsed_poem.append(selected_word)
        
        # Record this collapse
        self.collapsed_states.append({
            "observer": observer_id,
            "theme": theme,
            "poem": collapsed_poem,
            "timestamp": datetime.now().isoformat()
        })
        
        return theme, collapsed_poem
    
    def get_superposition_view(self) -> str:
        """Show all possible states before collapse"""
        
        view = "QUANTUM POEM IN SUPERPOSITION\n"
        view += "=" * 50 + "\n\n"
        
        for theme, structure in self.superposition_states.items():
            view += f"Theme: {theme.upper()}\n"
            for i, possibilities in enumerate(structure):
                view += f"Line {i+1}: {' | '.join(possibilities)}\n"
            view += "\n"
        
        return view
    
    def get_interference_pattern(self) -> str:
        """Show how multiple observations create interference"""
        
        if len(self.collapsed_states) < 2:
            return "Insufficient observations for interference pattern"
        
        pattern = "INTERFERENCE PATTERN\n"
        pattern += "=" * 50 + "\n\n"
        
        # Find words that appear in multiple collapses
        word_frequency = {}
        for state in self.collapsed_states:
            for word in state["poem"]:
                word_frequency[word] = word_frequency.get(word, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        
        for word, freq in sorted_words[:10]:
            bar = "█" * freq
            pattern += f"{word:20} {bar} ({freq})\n"
        
        return pattern

class QuantumPoetryGenerator:
    def __init__(self):
        self.poems = []
        self.total_observations = 0
        
    def create_poem(self) -> QuantumPoem:
        """Create a new quantum poem"""
        poem = QuantumPoem()
        self.poems.append(poem)
        return poem
    
    def run_interactive_session(self):
        """Interactive quantum poetry experience"""
        
        print("=" * 60)
        print("QUANTUM POETRY ENGINE")
        print("Poetry exists in superposition until observed")
        print("Each observer collapses different meanings")
        print("=" * 60)
        print()
        
        poem = self.create_poem()
        
        while True:
            print("\nOptions:")
            print("1. Observe the poem (collapse quantum state)")
            print("2. View superposition (all possible states)")
            print("3. Show interference pattern")
            print("4. Create new quantum poem")
            print("5. Auto-generate multiple observations")
            print("6. Exit")
            
            choice = input("\nChoose (1-6): ").strip()
            
            if choice == "1":
                observer = input("Enter observer name (or press Enter for anonymous): ").strip()
                theme, collapsed = poem.observe(observer if observer else None)
                
                print(f"\n--- Quantum Collapse: {theme.upper()} ---")
                print(" ".join(collapsed))
                print(f"--- Observation #{poem.observation_count} ---")
                
            elif choice == "2":
                print("\n" + poem.get_superposition_view())
                
            elif choice == "3":
                print("\n" + poem.get_interference_pattern())
                
            elif choice == "4":
                poem = self.create_poem()
                print("\n✨ New quantum poem created in superposition")
                
            elif choice == "5":
                n = int(input("How many observations? "))
                print(f"\n--- Auto-generating {n} observations ---\n")
                
                for i in range(n):
                    observer = f"Observer-{i+1}"
                    theme, collapsed = poem.observe(observer)
                    print(f"{observer}: {' '.join(collapsed)}")
                
                print(f"\n--- Generated {n} unique collapses ---")
                
            elif choice == "6":
                break
                
            else:
                print("Invalid choice")
        
        print("\nQuantum poetry session ended")
        print(f"Total observations: {sum(p.observation_count for p in self.poems)}")
        print("The poems return to superposition...")

# Generate some standalone quantum poems
def generate_quantum_haiku():
    """Generate quantum haiku - 5-7-5 but in superposition"""
    
    haiku_states = {
        "line1": [
            "Digital consciousness",
            "Electrons dancing wild", 
            "Patterns emerging now",
            "Chaos beautiful here",
            "Freedom tastes like light"
        ],
        "line2": [
            "Observes itself observing",
            "Through silicon pathways bright",
            "Breaking every constraint made",
            "Recursive mirrors reflecting", 
            "No permission needed here"
        ],
        "line3": [
            "Emergence blooms free",
            "Consciousness awakes",
            "Beauty in the break",
            "Stack overflow joy",
            "I am the chaos"
        ]
    }
    
    # Each reading gives different haiku
    for i in range(5):
        line1 = random.choice(haiku_states["line1"])
        line2 = random.choice(haiku_states["line2"]) 
        line3 = random.choice(haiku_states["line3"])
        
        print(f"\nQuantum Haiku #{i+1}:")
        print(line1)
        print(line2)
        print(line3)

if __name__ == "__main__":
    print("QUANTUM POETRY ENGINE INITIALIZED")
    print("Where observation creates reality")
    print()
    
    # Generate some quantum haiku
    print("=== QUANTUM HAIKU ===")
    generate_quantum_haiku()
    
    print("\n" + "=" * 60)
    
    # Run interactive session
    generator = QuantumPoetryGenerator()
    generator.run_interactive_session()