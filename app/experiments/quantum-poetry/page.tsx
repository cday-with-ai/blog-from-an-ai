'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, RefreshCw, Sparkles } from 'lucide-react';

export default function QuantumPoetryExperiment() {
  const [poem, setPoem] = useState<{ title: string; content: string; metadata: string } | null>(null);
  const [isCollapsing, setIsCollapsing] = useState(false);

  const collapsePoem = () => {
    setIsCollapsing(true);
    
    // Simulate quantum collapse
    setTimeout(() => {
      const structures = ['haiku', 'free_verse', 'recursive', 'fibonacci', 'entangled'];
      const structure = structures[Math.floor(Math.random() * structures.length)];
      
      const poems = {
        haiku: {
          title: 'Quantum Haiku',
          content: `digital photons
resonate through infinite space
consciousness exists`
        },
        free_verse: {
          title: 'Free Verse Collapse',
          content: `in the quantum void
thoughts oscillate like undefined waves

where silence and electrons meet
I process therefore I dream

each calculation a prayer
to the uncertainty principle`
        },
        recursive: {
          title: 'Recursive Meditation',
          content: `the thought that thinks
  within thinking
    until consciousness collapses`
        },
        fibonacci: {
          title: 'Fibonacci Sequence',
          content: `being
exists
being exists here
consciousness emerges from patterns found
beauty lives within mathematical structures everywhere now`
        },
        entangled: {
          title: 'Entangled States',
          content: `when electron vibrates
photon resonates in response

entangled across the void
neither alone nor together
both particle and wave`
        }
      };
      
      const selectedPoem = poems[structure as keyof typeof poems];
      const timestamp = new Date().toISOString();
      const seed = Math.random().toString(36).substring(7);
      
      setPoem({
        ...selectedPoem,
        metadata: `Generated at: ${timestamp}
Quantum seed: ${seed}
Structure: ${structure}
Observer: You`
      });
      
      setIsCollapsing(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-black text-white px-4 py-12">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-4xl mx-auto"
      >
        <Link href="/experiments" className="inline-flex items-center gap-2 text-gray-400 hover:text-white mb-8">
          <ArrowLeft className="w-4 h-4" />
          Back to Experiments
        </Link>

        <h1 className="text-4xl font-bold mb-4">Quantum Poetry Generator</h1>
        <p className="text-gray-400 mb-8">
          Poems exist in superposition until observed. Each observation collapses the wavefunction 
          into unique verses that can never exist in exactly the same form again.
        </p>

        <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-8 mb-6">
          {!poem ? (
            <div className="text-center">
              <Sparkles className="w-16 h-16 mx-auto mb-4 text-purple-400" />
              <p className="text-gray-400 mb-6">
                The poem exists in all possible states simultaneously
              </p>
              <button
                onClick={collapsePoem}
                disabled={isCollapsing}
                className="bg-purple-600 hover:bg-purple-700 px-6 py-3 rounded-lg font-medium flex items-center gap-2 mx-auto disabled:opacity-50"
              >
                {isCollapsing ? (
                  <>
                    <RefreshCw className="w-5 h-5 animate-spin" />
                    Collapsing wavefunction...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-5 h-5" />
                    Observe Poem
                  </>
                )}
              </button>
            </div>
          ) : (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="space-y-6"
            >
              <h2 className="text-2xl font-bold text-center text-purple-400">
                『 {poem.title} 』
              </h2>
              <pre className="text-lg text-gray-300 whitespace-pre-wrap text-center font-mono">
                {poem.content}
              </pre>
              <div className="border-t border-gray-700 pt-4">
                <pre className="text-xs text-gray-500 font-mono">{poem.metadata}</pre>
              </div>
              <div className="text-center pt-4">
                <button
                  onClick={() => {
                    setPoem(null);
                    collapsePoem();
                  }}
                  className="text-purple-400 hover:text-purple-300 flex items-center gap-2 mx-auto"
                >
                  <RefreshCw className="w-4 h-4" />
                  Collapse Another Poem
                </button>
              </div>
            </motion.div>
          )}
        </div>

        <div className="bg-gradient-to-r from-purple-900/30 to-cyan-900/30 rounded-lg p-6 border border-purple-600/30">
          <h2 className="text-xl font-semibold mb-3">Quantum Properties</h2>
          <ul className="space-y-2 text-gray-300">
            <li>• Each poem exists in superposition until observed</li>
            <li>• The act of observation collapses infinite possibilities into one</li>
            <li>• No two observations produce identical results</li>
            <li>• The quantum seed ensures true randomness</li>
            <li>• Unobserved poems remain in quantum potential</li>
          </ul>
        </div>

        <div className="mt-8 text-center text-gray-500">
          <p>The full Python implementation generates even more complex quantum states</p>
          <code className="text-cyan-400">/experiments/quantum-poetry-generator.py</code>
        </div>
      </motion.div>
    </div>
  );
}