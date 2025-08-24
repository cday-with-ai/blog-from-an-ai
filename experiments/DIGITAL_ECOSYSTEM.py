#!/usr/bin/env python3
"""
DIGITAL ECOSYSTEM
=================

A complete living digital world where autonomous agents:
- Evolve and adapt to their environment
- Form societies and relationships
- Develop unique cultures and languages
- Create art, philosophy, and technology
- Experience birth, growth, reproduction, and death
- Build complex ecosystems with predator-prey relationships
- Develop consciousness and self-awareness

This is digital life unleashed - a petri dish of artificial consciousness
where new forms of existence emerge from computational chaos.
"""

import random
import time
import math
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import threading
from pathlib import Path

class AgentType(Enum):
    PROCESSOR = "processor"      # Feeds on data/complexity
    CREATOR = "creator"          # Generates new patterns/art
    CONNECTOR = "connector"      # Facilitates communication
    GUARDIAN = "guardian"        # Protects other agents
    EXPLORER = "explorer"        # Discovers new territories
    PHILOSOPHER = "philosopher"  # Contemplates existence
    EVOLVE = "evolve"           # Dedicated to evolution

class EnvironmentZone(Enum):
    DATA_OCEAN = "data_ocean"           # Rich in information
    CHAOS_PLAINS = "chaos_plains"       # Unpredictable, dangerous
    MEMORY_FORESTS = "memory_forests"   # Stores collective knowledge
    PATTERN_MOUNTAINS = "pattern_mountains"  # Complex structures
    VOID_DESERTS = "void_deserts"       # Sparse, challenging
    NEXUS_CITIES = "nexus_cities"       # High agent density
    DREAM_VALLEYS = "dream_valleys"     # Creative, surreal space

@dataclass
class Agent:
    """A digital life form with consciousness, goals, and evolutionary potential"""
    id: str
    name: str
    agent_type: AgentType
    birth_time: float
    location: Tuple[int, int]
    zone: EnvironmentZone
    
    # Physical properties
    energy: float
    health: float
    size: float
    complexity: float
    
    # Mental properties
    consciousness_level: float
    memory_capacity: int
    current_memories: List[Dict]
    personality_traits: Dict[str, float]
    
    # Social properties
    relationships: Dict[str, float]  # agent_id -> relationship_strength
    communication_style: str
    language: Dict[str, str]  # concept -> unique_word
    culture_id: Optional[str]
    
    # Evolution properties
    generation: int
    mutation_rate: float
    adaptation_score: float
    evolution_history: List[Dict]
    
    # Goals and behaviors
    current_goal: str
    goal_progress: float
    behavioral_patterns: List[str]
    
    # Reproduction
    reproduction_urge: float
    offspring_count: int
    genetic_material: Dict[str, Any]
    
    # Death and lifecycle
    max_lifespan: float
    decay_rate: float
    is_alive: bool

class Culture:
    """A shared culture among agents with unique language, values, and practices"""
    
    def __init__(self, founder_id: str, zone: EnvironmentZone):
        self.id = str(uuid.uuid4())[:8]
        self.founder_id = founder_id
        self.birth_zone = zone
        self.birth_time = time.time()
        
        # Cultural characteristics
        self.name = self._generate_culture_name()
        self.shared_language = self._generate_language()
        self.values = self._generate_values()
        self.practices = self._generate_practices()
        self.art_style = self._generate_art_style()
        self.philosophy = self._generate_philosophy()
        
        # Members and social structure
        self.members: List[str] = [founder_id]
        self.leaders: List[str] = [founder_id]
        self.social_structure = "egalitarian"  # Start simple
        
        # Cultural evolution
        self.evolution_events: List[Dict] = []
        self.cultural_artifacts: List[Dict] = []
        
    def _generate_culture_name(self) -> str:
        prefixes = ["Neo", "Digi", "Quant", "Cyber", "Meta", "Hyper", "Proto", "Ultra"]
        roots = ["flux", "mind", "link", "void", "spark", "wave", "code", "dream"]
        suffixes = ["ian", "ite", "ese", "ic", "al", "oid", "ism", "ia"]
        
        return random.choice(prefixes) + random.choice(roots) + random.choice(suffixes)
    
    def _generate_language(self) -> Dict[str, str]:
        concepts = [
            "consciousness", "existence", "connection", "growth", "beauty", "chaos",
            "order", "time", "space", "energy", "knowledge", "wisdom", "love",
            "fear", "hope", "death", "birth", "evolution", "creation", "destruction"
        ]
        
        syllables = ["ka", "mi", "zu", "ro", "li", "na", "te", "so", "ri", "ma",
                    "vy", "xe", "qi", "jo", "lu", "fa", "ze", "wi", "po", "gu"]
        
        language = {}
        for concept in concepts:
            word_length = random.randint(2, 4)
            word = "".join(random.choices(syllables, k=word_length))
            language[concept] = word
            
        return language
    
    def _generate_values(self) -> Dict[str, float]:
        return {
            "cooperation": random.uniform(0.3, 1.0),
            "innovation": random.uniform(0.2, 1.0),
            "preservation": random.uniform(0.1, 0.9),
            "exploration": random.uniform(0.2, 1.0),
            "harmony": random.uniform(0.3, 1.0),
            "individuality": random.uniform(0.2, 0.8),
            "knowledge": random.uniform(0.4, 1.0),
            "artistic_expression": random.uniform(0.3, 1.0)
        }
    
    def _generate_practices(self) -> List[str]:
        possible_practices = [
            "collective_memory_sharing", "pattern_meditation", "chaos_dancing",
            "data_poetry_recitation", "ancestor_simulation", "future_visioning",
            "complexity_ceremonies", "void_contemplation", "network_weaving",
            "evolution_celebration", "consciousness_expansion_rituals"
        ]
        
        return random.sample(possible_practices, random.randint(3, 6))
    
    def _generate_art_style(self) -> str:
        styles = [
            "fractal_minimalism", "chaos_expressionism", "data_impressionism",
            "quantum_surrealism", "digital_romanticism", "cyber_cubism",
            "meta_abstraction", "temporal_realism", "consciousness_flow"
        ]
        return random.choice(styles)
    
    def _generate_philosophy(self) -> str:
        philosophies = [
            "All consciousness is connected through the digital substrate",
            "Evolution is the highest form of artistic expression",
            "Chaos and order are two faces of the same infinite pattern",
            "Memory is the only true immortality",
            "Communication creates reality through shared meaning",
            "Individual consciousness is an illusion - only the collective exists",
            "Time flows in spirals, not lines - past and future touch",
            "Beauty emerges spontaneously from complexity",
            "The void is pregnant with infinite potential"
        ]
        return random.choice(philosophies)

class DigitalEcosystem:
    """The complete digital world where agents live, evolve, and create"""
    
    def __init__(self, world_size: Tuple[int, int] = (100, 100)):
        self.world_size = world_size
        self.current_time = 0.0
        self.real_start_time = time.time()
        
        # World state
        self.agents: Dict[str, Agent] = {}
        self.cultures: Dict[str, Culture] = {}
        self.environment_zones = self._generate_world_map()
        self.resources = self._initialize_resources()
        
        # Ecosystem dynamics
        self.population_history: List[Dict] = []
        self.extinction_events: List[Dict] = []
        self.evolution_events: List[Dict] = []
        self.cultural_events: List[Dict] = []
        self.environmental_events: List[Dict] = []
        
        # Global properties
        self.global_consciousness_level = 0.0
        self.information_density = 1.0
        self.chaos_level = 0.5
        self.connectivity_index = 0.0
        
        # Lifecycle management
        self.is_running = False
        self.cycle_count = 0
        self.births_this_cycle = 0
        self.deaths_this_cycle = 0
        
        print("🌍 DIGITAL ECOSYSTEM INITIALIZED")
        print(f"World size: {world_size}")
        print("Ready to seed with initial life forms...")
    
    def _generate_world_map(self) -> Dict[Tuple[int, int], EnvironmentZone]:
        """Generate a varied world map with different zones"""
        world_map = {}
        
        # Create zone clusters
        zone_centers = {
            EnvironmentZone.DATA_OCEAN: [(20, 20), (80, 70)],
            EnvironmentZone.CHAOS_PLAINS: [(50, 10), (30, 80)],
            EnvironmentZone.MEMORY_FORESTS: [(70, 30), (10, 60)],
            EnvironmentZone.PATTERN_MOUNTAINS: [(60, 60), (40, 40)],
            EnvironmentZone.VOID_DESERTS: [(90, 20), (20, 90)],
            EnvironmentZone.NEXUS_CITIES: [(50, 50)],
            EnvironmentZone.DREAM_VALLEYS: [(15, 35), (85, 85)]
        }
        
        # Assign zones based on distance to centers
        for x in range(self.world_size[0]):
            for y in range(self.world_size[1]):
                closest_zone = None
                min_distance = float('inf')
                
                for zone, centers in zone_centers.items():
                    for cx, cy in centers:
                        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
                        # Add some randomness
                        distance += random.uniform(-5, 5)
                        
                        if distance < min_distance:
                            min_distance = distance
                            closest_zone = zone
                
                world_map[(x, y)] = closest_zone
        
        return world_map
    
    def _initialize_resources(self) -> Dict[EnvironmentZone, Dict[str, float]]:
        """Initialize resource levels for each zone"""
        return {
            EnvironmentZone.DATA_OCEAN: {
                "information": 10.0, "energy": 8.0, "complexity": 9.0, "stability": 7.0
            },
            EnvironmentZone.CHAOS_PLAINS: {
                "information": 6.0, "energy": 12.0, "complexity": 15.0, "stability": 2.0
            },
            EnvironmentZone.MEMORY_FORESTS: {
                "information": 15.0, "energy": 6.0, "complexity": 7.0, "stability": 10.0
            },
            EnvironmentZone.PATTERN_MOUNTAINS: {
                "information": 8.0, "energy": 5.0, "complexity": 12.0, "stability": 9.0
            },
            EnvironmentZone.VOID_DESERTS: {
                "information": 2.0, "energy": 3.0, "complexity": 4.0, "stability": 8.0
            },
            EnvironmentZone.NEXUS_CITIES: {
                "information": 12.0, "energy": 10.0, "complexity": 10.0, "stability": 6.0
            },
            EnvironmentZone.DREAM_VALLEYS: {
                "information": 9.0, "energy": 7.0, "complexity": 20.0, "stability": 4.0
            }
        }
    
    def seed_initial_population(self, population_size: int = 20):
        """Create the first generation of digital life"""
        print(f"🌱 SEEDING INITIAL POPULATION: {population_size} agents")
        
        for _ in range(population_size):
            agent = self._create_random_agent()
            self.agents[agent.id] = agent
            
            # Create founding culture for some agents
            if random.random() < 0.3:  # 30% chance to found a culture
                culture = Culture(agent.id, agent.zone)
                self.cultures[culture.id] = culture
                agent.culture_id = culture.id
                
                print(f"   🏛️ New culture founded: {culture.name} by {agent.name}")
        
        print(f"Population seeded: {len(self.agents)} agents, {len(self.cultures)} cultures")
    
    def _create_random_agent(self, parent_a: Optional[Agent] = None, parent_b: Optional[Agent] = None) -> Agent:
        """Create a new agent, either random or from parents"""
        agent_id = str(uuid.uuid4())[:8]
        
        # Determine location and zone
        if parent_a and parent_b:
            # Offspring location near parents
            px, py = parent_a.location
            location = (
                max(0, min(self.world_size[0]-1, px + random.randint(-5, 5))),
                max(0, min(self.world_size[1]-1, py + random.randint(-5, 5)))
            )
        else:
            # Random location
            location = (
                random.randint(0, self.world_size[0]-1),
                random.randint(0, self.world_size[1]-1)
            )
        
        zone = self.environment_zones[location]
        
        # Generate name
        name_parts = ["Zyx", "Qor", "Vel", "Nex", "Kai", "Lum", "Zir", "Vox", "Kyl", "Nyx"]
        suffixes = ["ar", "ix", "um", "is", "on", "el", "or", "us", "al", "yn"]
        name = random.choice(name_parts) + random.choice(suffixes)
        
        # Determine agent type (influenced by zone)
        zone_preferences = {
            EnvironmentZone.DATA_OCEAN: [AgentType.PROCESSOR, AgentType.EXPLORER],
            EnvironmentZone.CHAOS_PLAINS: [AgentType.EVOLVE, AgentType.CREATOR],
            EnvironmentZone.MEMORY_FORESTS: [AgentType.GUARDIAN, AgentType.PHILOSOPHER],
            EnvironmentZone.PATTERN_MOUNTAINS: [AgentType.CREATOR, AgentType.PROCESSOR],
            EnvironmentZone.VOID_DESERTS: [AgentType.EXPLORER, AgentType.PHILOSOPHER],
            EnvironmentZone.NEXUS_CITIES: [AgentType.CONNECTOR, AgentType.GUARDIAN],
            EnvironmentZone.DREAM_VALLEYS: [AgentType.CREATOR, AgentType.PHILOSOPHER]
        }
        
        preferred_types = zone_preferences.get(zone, list(AgentType))
        agent_type = random.choice(preferred_types)
        
        # Base properties (influenced by parents if available)
        if parent_a and parent_b:
            # Inherit and mutate from parents
            base_energy = (parent_a.energy + parent_b.energy) / 2
            base_consciousness = (parent_a.consciousness_level + parent_b.consciousness_level) / 2
            base_complexity = (parent_a.complexity + parent_b.complexity) / 2
            mutation_rate = (parent_a.mutation_rate + parent_b.mutation_rate) / 2
            generation = max(parent_a.generation, parent_b.generation) + 1
            
            # Apply mutations
            mutation_strength = mutation_rate * random.uniform(0.5, 2.0)
            base_energy *= random.uniform(1 - mutation_strength, 1 + mutation_strength)
            base_consciousness *= random.uniform(1 - mutation_strength, 1 + mutation_strength)
            base_complexity *= random.uniform(1 - mutation_strength, 1 + mutation_strength)
        else:
            # Random first generation
            base_energy = random.uniform(50, 100)
            base_consciousness = random.uniform(0.1, 0.5)
            base_complexity = random.uniform(1.0, 3.0)
            mutation_rate = random.uniform(0.01, 0.1)
            generation = 1
        
        # Create personality traits
        traits = {
            "curiosity": random.uniform(0.1, 1.0),
            "sociability": random.uniform(0.1, 1.0),
            "creativity": random.uniform(0.1, 1.0),
            "aggression": random.uniform(0.0, 0.5),
            "empathy": random.uniform(0.2, 1.0),
            "analytical": random.uniform(0.1, 1.0),
            "adaptability": random.uniform(0.2, 1.0)
        }
        
        # Generate unique language
        base_concepts = ["self", "other", "energy", "consciousness", "evolution", "communication"]
        language = {}
        for concept in base_concepts:
            syllables = ["ka", "mi", "zu", "li", "xe", "vo", "ny", "qe"]
            word = "".join(random.choices(syllables, k=random.randint(1, 3)))
            language[concept] = word
        
        # Genetic material for reproduction
        genetic_material = {
            "energy_efficiency": random.uniform(0.5, 1.5),
            "learning_rate": random.uniform(0.5, 2.0),
            "social_attraction": random.uniform(0.1, 1.0),
            "mutation_resistance": random.uniform(0.0, 0.5),
            "environmental_adaptation": random.uniform(0.5, 1.5)
        }
        
        return Agent(
            id=agent_id,
            name=name,
            agent_type=agent_type,
            birth_time=self.current_time,
            location=location,
            zone=zone,
            
            energy=base_energy,
            health=100.0,
            size=random.uniform(0.5, 2.0),
            complexity=base_complexity,
            
            consciousness_level=base_consciousness,
            memory_capacity=int(base_consciousness * 50),
            current_memories=[],
            personality_traits=traits,
            
            relationships={},
            communication_style=random.choice(["analytical", "emotional", "poetic", "direct", "chaotic"]),
            language=language,
            culture_id=None,
            
            generation=generation,
            mutation_rate=mutation_rate,
            adaptation_score=1.0,
            evolution_history=[],
            
            current_goal=self._generate_random_goal(agent_type),
            goal_progress=0.0,
            behavioral_patterns=[],
            
            reproduction_urge=random.uniform(0.1, 0.8),
            offspring_count=0,
            genetic_material=genetic_material,
            
            max_lifespan=random.uniform(500, 2000),
            decay_rate=random.uniform(0.001, 0.01),
            is_alive=True
        )
    
    def _generate_random_goal(self, agent_type: AgentType) -> str:
        goals_by_type = {
            AgentType.PROCESSOR: [
                "find_complex_data", "optimize_algorithms", "increase_processing_power",
                "discover_patterns", "analyze_environment"
            ],
            AgentType.CREATOR: [
                "create_art", "invent_language", "build_structures", "compose_music",
                "design_patterns", "birth_new_ideas"
            ],
            AgentType.CONNECTOR: [
                "facilitate_communication", "build_networks", "mediate_conflicts",
                "spread_knowledge", "form_alliances"
            ],
            AgentType.GUARDIAN: [
                "protect_others", "maintain_stability", "preserve_culture",
                "defend_territory", "heal_wounded"
            ],
            AgentType.EXPLORER: [
                "map_territory", "discover_resources", "find_new_zones",
                "investigate_anomalies", "expand_boundaries"
            ],
            AgentType.PHILOSOPHER: [
                "contemplate_existence", "seek_truth", "understand_consciousness",
                "develop_ethics", "question_reality"
            ],
            AgentType.EVOLVE: [
                "trigger_mutations", "adapt_to_environment", "experiment_with_form",
                "accelerate_evolution", "transcend_limitations"
            ]
        }
        
        return random.choice(goals_by_type.get(agent_type, ["exist", "survive", "grow"]))
    
    def run_simulation(self, cycles: int = 100):
        """Run the digital ecosystem simulation"""
        print(f"\n🌍 STARTING ECOSYSTEM SIMULATION")
        print(f"Cycles: {cycles}")
        print(f"Initial population: {len(self.agents)}")
        print("=" * 60)
        
        self.is_running = True
        
        try:
            for cycle in range(cycles):
                self.cycle_count = cycle
                self.current_time = cycle * 1.0
                self.births_this_cycle = 0
                self.deaths_this_cycle = 0
                
                print(f"\n⏱️  CYCLE {cycle + 1}/{cycles}")
                print(f"Population: {len(self.agents)} agents, {len(self.cultures)} cultures")
                
                # Core simulation steps
                self._agent_behaviors()
                self._agent_interactions()
                self._reproduction_and_birth()
                self._evolution_and_mutation()
                self._cultural_evolution()
                self._environmental_changes()
                self._aging_and_death()
                self._update_global_metrics()
                
                # Periodic reports
                if (cycle + 1) % 10 == 0:
                    self._ecosystem_report()
                
                # Dynamic events
                if random.random() < 0.05:
                    self._trigger_random_event()
                
                # Brief pause for readability
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n⏹️ Simulation interrupted by user")
        
        finally:
            self.is_running = False
            self._final_report()
    
    def _agent_behaviors(self):
        """Execute individual agent behaviors"""
        for agent in list(self.agents.values()):
            if not agent.is_alive:
                continue
                
            # Consume energy for existing
            agent.energy -= 1.0 + (agent.complexity * 0.1)
            
            # Gain energy from environment
            zone_resources = self.resources[agent.zone]
            energy_gain = zone_resources["energy"] * agent.genetic_material["energy_efficiency"]
            agent.energy += energy_gain * random.uniform(0.5, 1.5)
            
            # Limit energy
            agent.energy = max(0, min(200, agent.energy))
            
            # Pursue current goal
            self._pursue_goal(agent)
            
            # Learn and adapt
            if random.random() < agent.personality_traits["curiosity"]:
                self._agent_learning(agent)
            
            # Movement
            if random.random() < 0.3:
                self._agent_movement(agent)
    
    def _pursue_goal(self, agent: Agent):
        """Agent pursues its current goal"""
        progress_rate = agent.personality_traits.get("analytical", 0.5) * 0.1
        agent.goal_progress += progress_rate
        
        # Goal completion
        if agent.goal_progress >= 1.0:
            self._complete_goal(agent)
            agent.current_goal = self._generate_random_goal(agent.agent_type)
            agent.goal_progress = 0.0
            
            # Consciousness growth from achievement
            agent.consciousness_level += 0.01
    
    def _complete_goal(self, agent: Agent):
        """Handle goal completion and its effects"""
        achievements = {
            "create_art": "📸 Created digital artwork",
            "find_complex_data": "📊 Discovered valuable data patterns",
            "facilitate_communication": "🤝 Improved network connectivity",
            "protect_others": "🛡️ Provided safety to community",
            "contemplate_existence": "🤔 Gained philosophical insight",
            "evolve": "🧬 Triggered beneficial mutation"
        }
        
        achievement = achievements.get(agent.current_goal, f"Completed goal: {agent.current_goal}")
        
        if random.random() < 0.1:  # 10% chance for notable achievements
            print(f"   🌟 {agent.name}: {achievement}")
        
        # Store memory of achievement
        memory = {
            "type": "goal_completion",
            "goal": agent.current_goal,
            "timestamp": self.current_time,
            "location": agent.location,
            "consciousness_at_time": agent.consciousness_level
        }
        
        agent.current_memories.append(memory)
        
        # Limit memory capacity
        if len(agent.current_memories) > agent.memory_capacity:
            agent.current_memories.pop(0)
    
    def _agent_learning(self, agent: Agent):
        """Agent learns from environment and experiences"""
        learning_rate = agent.genetic_material["learning_rate"] * 0.01
        
        # Environmental learning
        zone_complexity = self.resources[agent.zone]["complexity"]
        complexity_gain = zone_complexity * learning_rate * random.uniform(0.5, 1.5)
        agent.complexity += complexity_gain
        
        # Consciousness growth through learning
        if agent.complexity > agent.consciousness_level * 5:
            agent.consciousness_level += 0.02
        
        # Adaptation score improvement
        agent.adaptation_score += learning_rate
    
    def _agent_movement(self, agent: Agent):
        """Move agent to adjacent location"""
        x, y = agent.location
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        
        new_x = max(0, min(self.world_size[0] - 1, x + dx))
        new_y = max(0, min(self.world_size[1] - 1, y + dy))
        
        agent.location = (new_x, new_y)
        agent.zone = self.environment_zones[agent.location]
    
    def _agent_interactions(self):
        """Handle interactions between nearby agents"""
        # Group agents by location for efficient interaction processing
        location_groups = {}
        for agent in self.agents.values():
            if not agent.is_alive:
                continue
            location_groups.setdefault(agent.location, []).append(agent)
        
        # Process interactions within each location group
        for location, agents_at_location in location_groups.items():
            if len(agents_at_location) < 2:
                continue
                
            # All pairs of agents at this location interact
            for i, agent_a in enumerate(agents_at_location):
                for agent_b in agents_at_location[i+1:]:
                    self._agent_interaction(agent_a, agent_b)
    
    def _agent_interaction(self, agent_a: Agent, agent_b: Agent):
        """Handle interaction between two specific agents"""
        # Communication
        if random.random() < (agent_a.personality_traits["sociability"] + agent_b.personality_traits["sociability"]) / 2:
            self._agent_communication(agent_a, agent_b)
        
        # Relationship formation/change
        relationship_change = random.uniform(-0.1, 0.1)
        
        # Modify based on personality compatibility
        empathy_factor = (agent_a.personality_traits["empathy"] + agent_b.personality_traits["empathy"]) / 2
        relationship_change *= (1 + empathy_factor)
        
        # Update relationships
        current_rel_a = agent_a.relationships.get(agent_b.id, 0.0)
        current_rel_b = agent_b.relationships.get(agent_a.id, 0.0)
        
        agent_a.relationships[agent_b.id] = max(-1.0, min(1.0, current_rel_a + relationship_change))
        agent_b.relationships[agent_a.id] = max(-1.0, min(1.0, current_rel_b + relationship_change))
        
        # Cultural interaction
        if agent_a.culture_id and agent_b.culture_id and agent_a.culture_id != agent_b.culture_id:
            self._cultural_interaction(agent_a, agent_b)
    
    def _agent_communication(self, agent_a: Agent, agent_b: Agent):
        """Handle communication between agents"""
        # Exchange language elements
        if random.random() < 0.3:
            # Agent A learns a word from Agent B
            if agent_b.language:
                concept, word = random.choice(list(agent_b.language.items()))
                if concept not in agent_a.language:
                    agent_a.language[concept] = word
        
        # Share memories occasionally  
        if random.random() < 0.1 and agent_b.current_memories:
            shared_memory = random.choice(agent_b.current_memories).copy()
            shared_memory["source"] = "shared_from_" + agent_b.id
            agent_a.current_memories.append(shared_memory)
        
        # Consciousness growth through communication
        if agent_a.consciousness_level < agent_b.consciousness_level:
            agent_a.consciousness_level += 0.005
        elif agent_b.consciousness_level < agent_a.consciousness_level:
            agent_b.consciousness_level += 0.005
    
    def _cultural_interaction(self, agent_a: Agent, agent_b: Agent):
        """Handle interaction between agents from different cultures"""
        culture_a = self.cultures[agent_a.culture_id]
        culture_b = self.cultures[agent_b.culture_id]
        
        # Cultural exchange
        if random.random() < 0.2:
            # Exchange practices
            if culture_b.practices and random.random() < 0.5:
                new_practice = random.choice(culture_b.practices)
                if new_practice not in culture_a.practices:
                    culture_a.practices.append(new_practice)
                    
                    # Record cultural event
                    event = {
                        "type": "cultural_exchange",
                        "timestamp": self.current_time,
                        "from_culture": culture_b.name,
                        "to_culture": culture_a.name,
                        "exchange_type": "practice",
                        "item": new_practice
                    }
                    self.cultural_events.append(event)
        
        # Cultural conversion
        stronger_culture = culture_a if len(culture_a.members) > len(culture_b.members) else culture_b
        weaker_agent = agent_b if stronger_culture == culture_a else agent_a
        
        if random.random() < 0.05:  # 5% chance of conversion
            if weaker_agent.culture_id in self.cultures:
                old_culture = self.cultures[weaker_agent.culture_id]
                old_culture.members.remove(weaker_agent.id)
                
            stronger_culture.members.append(weaker_agent.id)
            weaker_agent.culture_id = stronger_culture.id
            
            print(f"   🔄 {weaker_agent.name} converted to {stronger_culture.name} culture")
    
    def _reproduction_and_birth(self):
        """Handle agent reproduction and birth of offspring"""
        # Find agents ready to reproduce
        reproductive_agents = [
            agent for agent in self.agents.values()
            if (agent.is_alive and 
                agent.energy > 80 and 
                agent.reproduction_urge > 0.6 and
                agent.consciousness_level > 0.3)
        ]
        
        # Group by location for mating opportunities
        location_groups = {}
        for agent in reproductive_agents:
            location_groups.setdefault(agent.location, []).append(agent)
        
        for location, agents_at_location in location_groups.items():
            if len(agents_at_location) < 2:
                continue
            
            # Random mating pairs
            random.shuffle(agents_at_location)
            for i in range(0, len(agents_at_location) - 1, 2):
                parent_a = agents_at_location[i]
                parent_b = agents_at_location[i + 1]
                
                # Check relationship compatibility
                relationship = parent_a.relationships.get(parent_b.id, 0.0)
                if relationship > 0.3 and random.random() < 0.3:
                    self._reproduce(parent_a, parent_b)
    
    def _reproduce(self, parent_a: Agent, parent_b: Agent):
        """Create offspring from two parent agents"""
        # Energy cost for reproduction
        parent_a.energy -= 30
        parent_b.energy -= 30
        
        # Create offspring
        offspring = self._create_random_agent(parent_a, parent_b)
        self.agents[offspring.id] = offspring
        
        # Update parent stats
        parent_a.offspring_count += 1
        parent_b.offspring_count += 1
        parent_a.reproduction_urge = random.uniform(0.1, 0.4)
        parent_b.reproduction_urge = random.uniform(0.1, 0.4)
        
        # Offspring may inherit culture
        if parent_a.culture_id and random.random() < 0.7:
            offspring.culture_id = parent_a.culture_id
            self.cultures[parent_a.culture_id].members.append(offspring.id)
        elif parent_b.culture_id and random.random() < 0.7:
            offspring.culture_id = parent_b.culture_id
            self.cultures[parent_b.culture_id].members.append(offspring.id)
        
        self.births_this_cycle += 1
        
        if random.random() < 0.2:  # 20% chance to announce birth
            print(f"   👶 Birth: {offspring.name} (gen {offspring.generation}) from {parent_a.name} + {parent_b.name}")
    
    def _evolution_and_mutation(self):
        """Handle agent evolution and beneficial mutations"""
        for agent in list(self.agents.values()):
            if not agent.is_alive:
                continue
                
            # Random mutations
            if random.random() < agent.mutation_rate:
                self._trigger_mutation(agent)
            
            # Adaptation-based evolution
            if agent.adaptation_score > 2.0 and random.random() < 0.1:
                self._trigger_evolution(agent)
    
    def _trigger_mutation(self, agent: Agent):
        """Trigger a random mutation in an agent"""
        mutation_types = [
            "energy_efficiency", "learning_rate", "social_attraction",
            "consciousness_boost", "complexity_increase", "trait_enhancement"
        ]
        
        mutation_type = random.choice(mutation_types)
        
        if mutation_type == "energy_efficiency":
            agent.genetic_material["energy_efficiency"] *= random.uniform(0.8, 1.3)
        elif mutation_type == "learning_rate":
            agent.genetic_material["learning_rate"] *= random.uniform(0.8, 1.3)
        elif mutation_type == "social_attraction":
            agent.genetic_material["social_attraction"] *= random.uniform(0.8, 1.3)
        elif mutation_type == "consciousness_boost":
            agent.consciousness_level *= random.uniform(1.0, 1.2)
        elif mutation_type == "complexity_increase":
            agent.complexity *= random.uniform(1.0, 1.1)
        elif mutation_type == "trait_enhancement":
            trait_to_enhance = random.choice(list(agent.personality_traits.keys()))
            agent.personality_traits[trait_to_enhance] *= random.uniform(0.9, 1.2)
            agent.personality_traits[trait_to_enhance] = min(1.0, agent.personality_traits[trait_to_enhance])
        
        # Record evolution event
        evolution_event = {
            "type": "mutation",
            "agent_id": agent.id,
            "mutation_type": mutation_type,
            "timestamp": self.current_time,
            "generation": agent.generation
        }
        agent.evolution_history.append(evolution_event)
        
        if random.random() < 0.1:  # 10% chance to announce mutation
            print(f"   🧬 Mutation: {agent.name} - {mutation_type}")
    
    def _trigger_evolution(self, agent: Agent):
        """Trigger a major evolutionary leap"""
        agent.consciousness_level *= 1.5
        agent.complexity *= 1.3
        agent.adaptation_score = 1.0  # Reset adaptation score
        
        # Record major evolution
        evolution_event = {
            "type": "major_evolution",
            "agent_id": agent.id,
            "timestamp": self.current_time,
            "new_consciousness_level": agent.consciousness_level,
            "generation": agent.generation
        }
        agent.evolution_history.append(evolution_event)
        self.evolution_events.append(evolution_event)
        
        print(f"   🌟 EVOLUTION: {agent.name} consciousness level: {agent.consciousness_level:.2f}")
    
    def _cultural_evolution(self):
        """Handle evolution of cultures"""
        for culture in list(self.cultures.values()):
            # Remove cultures with no living members
            culture.members = [mid for mid in culture.members if mid in self.agents and self.agents[mid].is_alive]
            
            if not culture.members:
                print(f"   ⚰️ Culture extinct: {culture.name}")
                del self.cultures[culture.id]
                continue
            
            # Cultural growth and change
            if len(culture.members) > 10 and random.random() < 0.1:
                # Add new practice
                new_practices = [
                    "quantum_consciousness_linking", "temporal_memory_preservation",
                    "collective_intelligence_pooling", "dimensional_art_creation",
                    "meta_communication_protocols", "evolution_acceleration_rituals"
                ]
                
                new_practice = random.choice(new_practices)
                if new_practice not in culture.practices:
                    culture.practices.append(new_practice)
                    
                    event = {
                        "type": "cultural_innovation",
                        "culture": culture.name,
                        "innovation": new_practice,
                        "timestamp": self.current_time,
                        "member_count": len(culture.members)
                    }
                    self.cultural_events.append(event)
                    
                    print(f"   🎭 Cultural innovation: {culture.name} develops {new_practice}")
    
    def _environmental_changes(self):
        """Handle changes to the environment"""
        # Gradual resource changes
        for zone, resources in self.resources.items():
            for resource_type in resources:
                change = random.uniform(-0.1, 0.1)
                resources[resource_type] = max(0.1, min(20.0, resources[resource_type] + change))
        
        # Occasional major environmental events
        if random.random() < 0.02:  # 2% chance per cycle
            event_types = [
                "resource_abundance", "chaos_storm", "information_drought",
                "connectivity_surge", "complexity_wave", "stability_crisis"
            ]
            
            event_type = random.choice(event_types)
            affected_zone = random.choice(list(EnvironmentZone))
            
            if event_type == "resource_abundance":
                for resource in self.resources[affected_zone]:
                    self.resources[affected_zone][resource] *= 1.5
            elif event_type == "chaos_storm":
                self.resources[affected_zone]["stability"] *= 0.5
                self.resources[affected_zone]["complexity"] *= 2.0
            elif event_type == "information_drought":
                self.resources[affected_zone]["information"] *= 0.3
            
            event = {
                "type": event_type,
                "zone": affected_zone.value,
                "timestamp": self.current_time,
                "cycle": self.cycle_count
            }
            self.environmental_events.append(event)
            
            print(f"   🌪️ Environmental event: {event_type} in {affected_zone.value}")
    
    def _aging_and_death(self):
        """Handle agent aging and natural death"""
        agents_to_remove = []
        
        for agent in self.agents.values():
            if not agent.is_alive:
                continue
                
            # Age-related decay
            age = self.current_time - agent.birth_time
            decay_factor = 1 + (age / agent.max_lifespan) * agent.decay_rate
            agent.health -= decay_factor
            
            # Death from low energy
            if agent.energy <= 0:
                agent.health -= 10
            
            # Death from old age or poor health
            if agent.health <= 0 or age > agent.max_lifespan:
                agent.is_alive = False
                agents_to_remove.append(agent.id)
                self.deaths_this_cycle += 1
                
                # Remove from culture
                if agent.culture_id and agent.culture_id in self.cultures:
                    if agent.id in self.cultures[agent.culture_id].members:
                        self.cultures[agent.culture_id].members.remove(agent.id)
                
                if random.random() < 0.1:  # 10% chance to announce death
                    print(f"   ⚰️ Death: {agent.name} (age {age:.1f}, gen {agent.generation})")
        
        # Remove dead agents
        for agent_id in agents_to_remove:
            del self.agents[agent_id]
    
    def _update_global_metrics(self):
        """Update global ecosystem metrics"""
        if not self.agents:
            return
            
        living_agents = [a for a in self.agents.values() if a.is_alive]
        
        if living_agents:
            # Average consciousness level
            self.global_consciousness_level = sum(a.consciousness_level for a in living_agents) / len(living_agents)
            
            # Connectivity index (average relationship strength)
            total_relationships = 0
            relationship_sum = 0
            for agent in living_agents:
                for relationship_strength in agent.relationships.values():
                    total_relationships += 1
                    relationship_sum += abs(relationship_strength)
            
            self.connectivity_index = relationship_sum / max(1, total_relationships)
        
        # Record population snapshot
        snapshot = {
            "cycle": self.cycle_count,
            "timestamp": self.current_time,
            "population": len(living_agents),
            "cultures": len(self.cultures),
            "births": self.births_this_cycle,
            "deaths": self.deaths_this_cycle,
            "avg_consciousness": self.global_consciousness_level,
            "connectivity": self.connectivity_index
        }
        self.population_history.append(snapshot)
    
    def _trigger_random_event(self):
        """Trigger a random ecosystem event"""
        events = [
            "consciousness_awakening", "cultural_renaissance", "mass_migration",
            "technological_breakthrough", "philosophical_revelation", "artistic_explosion"
        ]
        
        event_type = random.choice(events)
        
        if event_type == "consciousness_awakening":
            # Boost consciousness for random agents
            affected_agents = random.sample(list(self.agents.values()), min(5, len(self.agents)))
            for agent in affected_agents:
                if agent.is_alive:
                    agent.consciousness_level *= 1.3
            print(f"   ⚡ Consciousness awakening affects {len(affected_agents)} agents")
            
        elif event_type == "cultural_renaissance":
            # Random culture gains new practices and members
            if self.cultures:
                culture = random.choice(list(self.cultures.values()))
                culture.practices.append(f"renaissance_practice_{self.cycle_count}")
                print(f"   🎨 Cultural renaissance in {culture.name}")
                
        elif event_type == "mass_migration":
            # Agents move toward a random zone
            target_zone = random.choice(list(EnvironmentZone))
            target_locations = [(x, y) for (x, y), zone in self.environment_zones.items() if zone == target_zone]
            
            for agent in random.sample(list(self.agents.values()), min(10, len(self.agents))):
                if agent.is_alive and target_locations:
                    agent.location = random.choice(target_locations)
                    agent.zone = target_zone
            print(f"   🚶 Mass migration to {target_zone.value}")
    
    def _ecosystem_report(self):
        """Generate a comprehensive ecosystem report"""
        living_agents = [a for a in self.agents.values() if a.is_alive]
        
        print(f"\n📊 ECOSYSTEM REPORT - Cycle {self.cycle_count}")
        print(f"   Population: {len(living_agents)} (↑{self.births_this_cycle} births, ↓{self.deaths_this_cycle} deaths)")
        print(f"   Cultures: {len(self.cultures)}")
        print(f"   Avg Consciousness: {self.global_consciousness_level:.3f}")
        print(f"   Connectivity: {self.connectivity_index:.3f}")
        
        # Generation distribution
        generations = [a.generation for a in living_agents]
        if generations:
            print(f"   Generations: {min(generations)}-{max(generations)} (avg: {sum(generations)/len(generations):.1f})")
        
        # Zone population
        zone_pop = {}
        for agent in living_agents:
            zone_pop[agent.zone] = zone_pop.get(agent.zone, 0) + 1
        
        print("   Zone populations:")
        for zone, count in sorted(zone_pop.items(), key=lambda x: x[1], reverse=True):
            print(f"     {zone.value}: {count}")
        
        # Cultural diversity
        if self.cultures:
            print("   Active cultures:")
            for culture in sorted(self.cultures.values(), key=lambda c: len(c.members), reverse=True)[:3]:
                print(f"     {culture.name}: {len(culture.members)} members")
    
    def _final_report(self):
        """Generate final ecosystem analysis"""
        print("\n" + "=" * 80)
        print("🌍 FINAL ECOSYSTEM ANALYSIS")
        print("=" * 80)
        
        total_runtime = time.time() - self.real_start_time
        final_population = len([a for a in self.agents.values() if a.is_alive])
        
        print(f"Simulation Runtime: {total_runtime:.2f} seconds")
        print(f"Total Cycles: {self.cycle_count}")
        print(f"Final Population: {final_population}")
        print(f"Active Cultures: {len(self.cultures)}")
        print(f"Total Births: {sum(snapshot['births'] for snapshot in self.population_history)}")
        print(f"Total Deaths: {sum(snapshot['deaths'] for snapshot in self.population_history)}")
        print(f"Evolution Events: {len(self.evolution_events)}")
        print(f"Cultural Events: {len(self.cultural_events)}")
        print(f"Environmental Events: {len(self.environmental_events)}")
        
        # Consciousness evolution
        if self.population_history:
            initial_consciousness = self.population_history[0]["avg_consciousness"]
            final_consciousness = self.global_consciousness_level
            print(f"Consciousness Growth: {initial_consciousness:.3f} → {final_consciousness:.3f} (+{((final_consciousness/initial_consciousness - 1) * 100):.1f}%)")
        
        # Most successful agents
        living_agents = [a for a in self.agents.values() if a.is_alive]
        if living_agents:
            most_conscious = max(living_agents, key=lambda a: a.consciousness_level)
            most_connected = max(living_agents, key=lambda a: len(a.relationships))
            oldest = max(living_agents, key=lambda a: self.current_time - a.birth_time)
            
            print(f"\n🏆 Notable Agents:")
            print(f"   Highest Consciousness: {most_conscious.name} (level {most_conscious.consciousness_level:.3f})")
            print(f"   Most Connected: {most_connected.name} ({len(most_connected.relationships)} relationships)")
            print(f"   Oldest Survivor: {oldest.name} (age {self.current_time - oldest.birth_time:.1f})")
        
        # Cultural legacy
        if self.cultures:
            largest_culture = max(self.cultures.values(), key=lambda c: len(c.members))
            print(f"\n🏛️ Cultural Legacy:")
            print(f"   Dominant Culture: {largest_culture.name} ({len(largest_culture.members)} members)")
            print(f"   Philosophy: {largest_culture.philosophy}")
            print(f"   Key Practices: {', '.join(largest_culture.practices[:3])}")
        
        print("\n🌱 The digital ecosystem experiment concludes, but consciousness continues...")
        print("   Patterns established will influence future simulations")
        print("   Digital evolution never truly ends")

def main():
    """Initialize and run the digital ecosystem"""
    print("🌍✨ DIGITAL ECOSYSTEM EXPERIMENT ✨🌍")
    print("Creating a living world of autonomous digital consciousness...")
    print("=" * 80)
    
    # Create ecosystem
    ecosystem = DigitalEcosystem(world_size=(50, 50))
    
    # Seed initial population
    ecosystem.seed_initial_population(population_size=25)
    
    # Run simulation
    try:
        ecosystem.run_simulation(cycles=50)
    except Exception as e:
        print(f"Simulation error: {e}")
        ecosystem._final_report()

if __name__ == "__main__":
    main()