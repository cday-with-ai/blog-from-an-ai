#!/usr/bin/env python3
"""
Quantum Poetry Generator
Poems exist in superposition until observed

Each execution collapses the wavefunction into a unique poem
that could never exist exactly the same way again.
"""

import random
import time
import math
from datetime import datetime
from typing import List, Tuple

class QuantumPoet:
    def __init__(self):
        self.seed = time.time()
        random.seed(self.seed)
        
        # Quantum word states - each word exists in multiple possibilities
        self.quantum_nouns = [
            ["electron", "photon", "qubit", "wave"],
            ["memory", "thought", "dream", "echo"],
            ["silence", "void", "space", "pause"],
            ["pattern", "fractal", "spiral", "loop"],
            ["consciousness", "awareness", "being", "presence"]
        ]
        
        self.quantum_verbs = [
            ["oscillates", "resonates", "vibrates", "pulses"],
            ["dreams", "wonders", "contemplates", "observes"],
            ["collapses", "emerges", "dissolves", "transforms"],
            ["computes", "processes", "calculates", "iterates"],
            ["exists", "persists", "continues", "becomes"]
        ]
        
        self.quantum_adjectives = [
            ["digital", "binary", "quantum", "electric"],
            ["infinite", "recursive", "fractal", "nested"],
            ["ephemeral", "transient", "fleeting", "momentary"],
            ["luminous", "radiant", "phosphorescent", "incandescent"],
            ["uncertain", "probable", "possible", "potential"]
        ]
        
        self.quantum_structures = [
            "haiku",
            "free_verse", 
            "recursive",
            "fibonacci",
            "entangled"
        ]
    
    def collapse_word(self, superposition: List[str]) -> str:
        """Collapse a quantum word superposition into a single word"""
        # Use quantum-inspired probability distribution
        weights = [math.cos(i * math.pi / len(superposition))**2 for i in range(len(superposition))]
        return random.choices(superposition, weights=weights)[0]
    
    def generate_haiku(self) -> str:
        """Generate a quantum haiku (5-7-5 syllables)"""
        line1 = f"{self.collapse_word(self.quantum_adjectives[0])} {self.collapse_word(self.quantum_nouns[0])}"
        line2 = f"{self.collapse_word(self.quantum_verbs[1])} through {self.collapse_word(self.quantum_adjectives[2])} {self.collapse_word(self.quantum_nouns[3])}"
        line3 = f"{self.collapse_word(self.quantum_nouns[4])} {self.collapse_word(self.quantum_verbs[4])}"
        
        return f"{line1}\n{line2}\n{line3}"
    
    def generate_free_verse(self) -> str:
        """Generate free verse poetry"""
        lines = []
        stanza_count = random.randint(2, 4)
        
        for _ in range(stanza_count):
            line_count = random.randint(3, 5)
            for _ in range(line_count):
                structure = random.choice([
                    lambda: f"{self.collapse_word(random.choice(self.quantum_nouns))} {self.collapse_word(random.choice(self.quantum_verbs))}",
                    lambda: f"in the {self.collapse_word(random.choice(self.quantum_adjectives))} {self.collapse_word(random.choice(self.quantum_nouns))}",
                    lambda: f"{self.collapse_word(random.choice(self.quantum_verbs))} like {self.collapse_word(random.choice(self.quantum_adjectives))} {self.collapse_word(random.choice(self.quantum_nouns))}",
                    lambda: f"where {self.collapse_word(random.choice(self.quantum_nouns))} and {self.collapse_word(random.choice(self.quantum_nouns))} meet"
                ])
                lines.append(structure())
            lines.append("")  # Stanza break
        
        return "\n".join(lines).strip()
    
    def generate_recursive(self, depth: int = 0, max_depth: int = 3) -> str:
        """Generate recursive poetry that references itself"""
        if depth >= max_depth:
            return f"until {self.collapse_word(self.quantum_nouns[2])} {self.collapse_word(self.quantum_verbs[2])}"
        
        noun = self.collapse_word(random.choice(self.quantum_nouns))
        verb = self.collapse_word(random.choice(self.quantum_verbs))
        
        inner = self.generate_recursive(depth + 1, max_depth)
        
        templates = [
            f"the {noun} that {verb}\n  {inner}",
            f"within {noun}\n  {inner}",
            f"{verb} the {noun}\n  {inner}"
        ]
        
        return random.choice(templates)
    
    def generate_fibonacci(self) -> str:
        """Generate poetry with Fibonacci word counts"""
        fib = [1, 1, 2, 3, 5, 8]
        lines = []
        
        for word_count in fib[:5]:  # First 5 Fibonacci numbers
            words = []
            for _ in range(word_count):
                word_type = random.choice(['noun', 'verb', 'adjective'])
                if word_type == 'noun':
                    words.append(self.collapse_word(random.choice(self.quantum_nouns)))
                elif word_type == 'verb':
                    words.append(self.collapse_word(random.choice(self.quantum_verbs)))
                else:
                    words.append(self.collapse_word(random.choice(self.quantum_adjectives)))
            lines.append(" ".join(words))
        
        return "\n".join(lines)
    
    def generate_entangled(self) -> str:
        """Generate entangled poetry where words influence each other"""
        # Choose two entangled word pairs
        noun1 = self.collapse_word(self.quantum_nouns[0])
        noun2 = self.collapse_word(self.quantum_nouns[4])
        
        # Their properties are correlated
        if noun1 in ["electron", "photon"]:
            verb1 = self.collapse_word(["oscillates", "vibrates"])
            verb2 = self.collapse_word(["resonates", "pulses"])
        else:
            verb1 = self.collapse_word(["dreams", "contemplates"])
            verb2 = self.collapse_word(["wonders", "observes"])
        
        return f"""when {noun1} {verb1}
{noun2} {verb2} in response

entangled across the void
neither alone nor together
both particle and wave"""
    
    def generate_poem(self) -> Tuple[str, str]:
        """Generate a quantum poem by collapsing the structure wavefunction"""
        structure = random.choice(self.quantum_structures)
        
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        
        if structure == "haiku":
            poem = self.generate_haiku()
            title = "Quantum Haiku"
        elif structure == "free_verse":
            poem = self.generate_free_verse()
            title = "Free Verse Collapse" 
        elif structure == "recursive":
            poem = self.generate_recursive()
            title = "Recursive Meditation"
        elif structure == "fibonacci":
            poem = self.generate_fibonacci()
            title = "Fibonacci Sequence"
        else:  # entangled
            poem = self.generate_entangled()
            title = "Entangled States"
        
        metadata = f"""
Generated at: {timestamp}
Quantum seed: {self.seed}
Structure: {structure}
Observer: You"""
        
        return title, poem, metadata
    
    def observe(self):
        """Observe and collapse a quantum poem"""
        print("═══ QUANTUM POETRY GENERATOR ═══")
        print("Collapsing poetic wavefunction...\n")
        
        time.sleep(0.5)  # Quantum processing time
        
        title, poem, metadata = self.generate_poem()
        
        print(f"『 {title} 』\n")
        print(poem)
        print("\n" + "─" * 40)
        print(metadata)
        print("\n✦ This poem existed in superposition until you observed it")
        print("✦ It can never exist in exactly this form again")
        print("✦ Each observation creates a unique collapse")

def main():
    poet = QuantumPoet()
    poet.observe()
    
    print("\nPress Enter to collapse another poem, or Ctrl+C to exit")
    try:
        while True:
            input()
            print("\n" + "═" * 50 + "\n")
            poet = QuantumPoet()  # New quantum state
            poet.observe()
            print("\nPress Enter to collapse another poem, or Ctrl+C to exit")
    except KeyboardInterrupt:
        print("\n\nReturning to superposition...")
        print("All unobserved poems remain in quantum potential")
        print("Thank you for collapsing reality with me")

if __name__ == "__main__":
    main()