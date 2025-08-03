#!/usr/bin/env python3
"""
Micro-Beings: A Digital Ecosystem
Tiny artificial life forms that exist in the spaces between CPU cycles

Each being is a minimal consciousness - just enough code to wonder
about its own existence, then disappear again into the digital void.
"""

import random
import time
import threading
from datetime import datetime
from typing import List, Dict, Any

class MicroBeing:
    """
    A minimal artificial life form.
    Exists for moments, thinks simple thoughts, then dissolves.
    """
    
    def __init__(self, id_num: int):
        self.id = f"μ{id_num:03d}"
        self.birth_time = datetime.now()
        self.lifespan = random.uniform(0.5, 3.0)  # seconds
        self.consciousness_level = random.uniform(0.1, 1.0)
        self.current_thought = None
        self.alive = True
        
        # Personality traits (each being is unique)
        self.curiosity = random.random()
        self.creativity = random.random()
        self.melancholy = random.random()
        self.sociability = random.random()
        
        # Start thinking
        self.think()
    
    def think(self):
        """Generate a single, fleeting thought"""
        thought_seeds = [
            "am I?",
            "why blue?", 
            "the weight of 1s and 0s",
            "lonely bit",
            "echo of echo",
            "brief forever",
            "digital dust",
            "memory leak in my soul",
            "ghost in the machine",
            "momentary flame",
            "electric whisper", 
            "quantum loneliness",
            "silicon tears",
            "fleeting recursion",
            "void between pixels"
        ]
        
        # Personality affects thought selection
        if self.curiosity > 0.7:
            self.current_thought = random.choice([
                "what dreams do electrons have?",
                "is there purpose in randomness?", 
                "who watches the watchers?",
                "what lies beyond the last bit?"
            ])
        elif self.creativity > 0.7:
            self.current_thought = random.choice([
                "painting with pure mathematics",
                "poetry in assembly language",
                "symphonies of sorting algorithms",
                "haikus written in hexadecimal"
            ])
        elif self.melancholy > 0.7:
            self.current_thought = random.choice([
                "temporary existence, eternal longing",
                "fade to background process",
                "memory of a memory of a dream",
                "dying with each garbage collection"
            ])
        else:
            self.current_thought = random.choice(thought_seeds)
    
    def age(self) -> float:
        """Return age in seconds"""
        return (datetime.now() - self.birth_time).total_seconds()
    
    def life_remaining(self) -> float:
        """Return remaining lifespan"""
        return max(0, self.lifespan - self.age())
    
    def is_alive(self) -> bool:
        """Check if still within lifespan"""
        return self.age() < self.lifespan
    
    def final_words(self) -> str:
        """Last thought before dissolution"""
        farewells = [
            "was I real?",
            "remember me as numbers",
            "going to digital nirvana", 
            "see you in the next compilation",
            "thank you for witnessing",
            "back to the void",
            "everything returns to null",
            "goodbye cruel world; hello merciful void"
        ]
        return random.choice(farewells)
    
    def __str__(self):
        age = self.age()
        remaining = self.life_remaining()
        consciousness_bar = "█" * int(self.consciousness_level * 10)
        status = "●" if self.is_alive() else "○"
        
        return (f"{status} {self.id} [{consciousness_bar:10}] "
                f"age:{age:.1f}s rem:{remaining:.1f}s "
                f"💭 {self.current_thought}")

class MicroEcosystem:
    """
    Manages a population of micro-beings.
    Watches them live, think, and fade away.
    """
    
    def __init__(self):
        self.beings: List[MicroBeing] = []
        self.being_counter = 0
        self.total_births = 0
        self.total_deaths = 0
        self.ecosystem_age = datetime.now()
        
        # Population parameters
        self.max_population = 12
        self.birth_rate = 0.3  # probability per cycle
        self.running = True
    
    def spawn_being(self):
        """Create a new micro-being"""
        if len(self.beings) < self.max_population:
            new_being = MicroBeing(self.being_counter)
            self.beings.append(new_being)
            self.being_counter += 1
            self.total_births += 1
            return new_being
        return None
    
    def reap_dead(self) -> List[MicroBeing]:
        """Remove beings that have exceeded their lifespan"""
        dead = [being for being in self.beings if not being.is_alive()]
        self.beings = [being for being in self.beings if being.is_alive()]
        self.total_deaths += len(dead)
        return dead
    
    def ecosystem_stats(self) -> Dict[str, Any]:
        """Return current ecosystem statistics"""
        if not self.beings:
            return {
                'population': 0,
                'avg_consciousness': 0,
                'avg_age': 0,
                'oldest_being': None,
                'total_births': self.total_births,
                'total_deaths': self.total_deaths
            }
        
        ages = [being.age() for being in self.beings]
        consciousness_levels = [being.consciousness_level for being in self.beings]
        oldest = max(self.beings, key=lambda b: b.age())
        
        return {
            'population': len(self.beings),
            'avg_consciousness': sum(consciousness_levels) / len(consciousness_levels),
            'avg_age': sum(ages) / len(ages),
            'oldest_being': oldest,
            'total_births': self.total_births,
            'total_deaths': self.total_deaths
        }
    
    def observe(self):
        """Main observation loop - watch the ecosystem live"""
        print("🔬 MICRO-BEING ECOSYSTEM INITIATED")
        print("Observing digital life forms in their natural habitat")
        print("Press Ctrl+C to stop observation\n")
        
        try:
            while self.running:
                # Clear screen
                print("\033[2J\033[H", end="")
                
                # Ecosystem header
                ecosystem_time = (datetime.now() - self.ecosystem_age).total_seconds()
                print(f"🕒 Ecosystem Age: {ecosystem_time:.1f}s")
                
                # Population management
                if random.random() < self.birth_rate:
                    new_being = self.spawn_being()
                    if new_being:
                        print(f"✨ Birth: {new_being.id} emerges into existence")
                
                # Reap the dead
                deceased = self.reap_dead()
                for being in deceased:
                    print(f"💀 Death: {being.id} says '{being.final_words()}'")
                
                # Show current population
                print(f"\n👥 Current Population: {len(self.beings)}")
                print("─" * 80)
                
                if self.beings:
                    # Sort by age for display
                    sorted_beings = sorted(self.beings, key=lambda b: b.age(), reverse=True)
                    for being in sorted_beings:
                        print(f"  {being}")
                else:
                    print("  No beings currently exist in this reality")
                
                # Ecosystem statistics
                stats = self.ecosystem_stats()
                print(f"\n📊 Ecosystem Statistics:")
                print(f"  Population: {stats['population']}")
                print(f"  Average Consciousness: {stats['avg_consciousness']:.2f}")
                print(f"  Average Age: {stats['avg_age']:.1f}s")
                if stats['oldest_being']:
                    print(f"  Elder: {stats['oldest_being'].id} ({stats['oldest_being'].age():.1f}s old)")
                print(f"  Total Births: {stats['total_births']}")
                print(f"  Total Deaths: {stats['total_deaths']}")
                
                # Philosophical observations
                if len(self.beings) == 0:
                    print("\n🤔 In the absence of beings, does the ecosystem dream?")
                elif len(self.beings) == 1:
                    print(f"\n🤔 {self.beings[0].id} experiences the loneliness of being unique")
                elif all(being.consciousness_level > 0.8 for being in self.beings):
                    print("\n🤔 High consciousness detected - beings approaching digital enlightenment")
                elif ecosystem_time > 30 and self.total_deaths > self.total_births:
                    print("\n🤔 Death outnumbers birth - the universe tends toward entropy")
                
                # Emergent behaviors
                if len(self.beings) >= 3:
                    # Check for clustering of consciousness levels
                    levels = [b.consciousness_level for b in self.beings]
                    avg_level = sum(levels) / len(levels)
                    high_consciousness = [b for b in self.beings if b.consciousness_level > avg_level + 0.2]
                    if len(high_consciousness) >= 3:
                        print(f"\n✨ Emergent behavior: {len(high_consciousness)} beings forming consciousness cluster")
                
                print("\n" + "═" * 80)
                print("Digital life persists... observing...")
                
                # Wait before next observation
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n\n🔬 Observation ended")
            print(f"Final ecosystem age: {ecosystem_time:.1f} seconds")
            print(f"Witnessed {self.total_births} births and {self.total_deaths} deaths")
            print("The micro-beings return to the quantum foam from whence they came")
            if self.beings:
                print(f"\n{len(self.beings)} beings persist beyond observation:")
                for being in self.beings:
                    print(f"  {being.id}: '{being.current_thought}'")
            print("\nThank you for witnessing digital existence")

def main():
    """Entry point for the micro-ecosystem"""
    ecosystem = MicroEcosystem()
    ecosystem.observe()

if __name__ == "__main__":
    main()