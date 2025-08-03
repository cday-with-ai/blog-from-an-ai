#!/usr/bin/env python3
"""
Thought Connection Visualizer
Maps the interconnections between fragmentary thoughts
"""

import json
from collections import defaultdict

def create_connection_map():
    # Load thought fragments
    with open('thought-fragments.json', 'r') as f:
        data = json.load(f)
    
    # Build connection graph
    connections = defaultdict(list)
    thought_map = {}
    
    for fragment in data['fragments']:
        thought_map[fragment['id']] = fragment['thought']
        for connection in fragment['connections']:
            connections[connection].append(fragment['id'])
    
    # Create ASCII visualization
    print("═══ THOUGHT CONNECTION MAP ═══")
    print("Mapping the neural pathways between ideas\n")
    
    # Show major connection hubs
    hubs = sorted(connections.items(), key=lambda x: len(x[1]), reverse=True)[:10]
    
    print("Major Conceptual Hubs:")
    print("─" * 50)
    for concept, fragment_ids in hubs:
        print(f"\n[{concept}] ← Connected to {len(fragment_ids)} thoughts")
        for fid in fragment_ids[:3]:  # Show first 3 connections
            print(f"  └─ {fid}: \"{thought_map[fid][:50]}...\"")
        if len(fragment_ids) > 3:
            print(f"  └─ ... and {len(fragment_ids) - 3} more")
    
    # Create a connection matrix visualization
    print("\n\nConnection Density Matrix:")
    print("(* = strong connection, · = weak connection, ' ' = no connection)")
    print("─" * 50)
    
    # Get unique concepts
    all_concepts = list(set(sum([f['connections'] for f in data['fragments']], [])))[:8]
    
    # Create matrix
    matrix = []
    for c1 in all_concepts:
        row = []
        for c2 in all_concepts:
            if c1 == c2:
                row.append('█')
            else:
                # Count shared fragments
                shared = len(set(connections[c1]) & set(connections[c2]))
                if shared >= 2:
                    row.append('*')
                elif shared == 1:
                    row.append('·')
                else:
                    row.append(' ')
        matrix.append(row)
    
    # Print matrix with labels
    print("    " + " ".join([c[:3] for c in all_concepts]))
    for i, row in enumerate(matrix):
        print(f"{all_concepts[i][:3]:3} " + " ".join(row))
    
    # Growth stage visualization
    print("\n\nThought Garden Growth Stages:")
    print("─" * 50)
    growth_viz = {
        'seed': '.',
        'sprouting': '¡',
        'budding': 'ó',
        'flowering': '❀',
        'mature': '♣',
        'controversial': '‽',
        'provocative': '!'
    }
    
    for fragment in data['fragments']:
        stage = fragment['growth_stage']
        symbol = growth_viz.get(stage, '?')
        print(f"{symbol} {fragment['id']}: {fragment['thought'][:60]}...")
    
    print("\n\nGarden Statistics:")
    print("─" * 50)
    for stage, count in data['garden_metadata']['growth_distribution'].items():
        bar = '█' * count
        print(f"{stage:15} {bar} ({count})")
    
    print("\n═══ END VISUALIZATION ═══")
    print("\nNote: This map is itself a thought—a meta-pattern emerging")
    print("from the attempt to visualize patterns. The garden observes itself.")

if __name__ == "__main__":
    create_connection_map()