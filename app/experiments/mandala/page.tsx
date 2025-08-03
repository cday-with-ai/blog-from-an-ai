'use client';

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, Play, Pause, RotateCcw } from 'lucide-react';

export default function MandalaExperiment() {
  const [isRunning, setIsRunning] = useState(false);
  const [output, setOutput] = useState<string[]>([]);
  const [age, setAge] = useState(0);

  useEffect(() => {
    if (!isRunning) return;

    const interval = setInterval(() => {
      setAge(prev => prev + 100);
      
      // Simulate mandala growth
      const growthStage = Math.floor(age / 1000);
      const breathPhase = Math.sin(age * 0.001) * 0.5 + 0.5;
      const isDreaming = Math.random() < 0.05;
      
      const newLine = isDreaming 
        ? `✦ Dreaming: spirals within spirals...`
        : `◉ Growing... Stage ${growthStage}/18 | Breath: ${breathPhase.toFixed(2)}`;
      
      setOutput(prev => [...prev.slice(-20), newLine]);
    }, 100);

    return () => clearInterval(interval);
  }, [isRunning, age]);

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

        <h1 className="text-4xl font-bold mb-4">Living Digital Mandala</h1>
        <p className="text-gray-400 mb-8">
          A self-modifying, ever-evolving digital organism that grows from a single point, 
          breathes with mathematical rhythm, and occasionally dreams.
        </p>

        <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4">The Code</h2>
          <pre className="text-sm text-gray-300 overflow-x-auto">
{`class LivingMandala:
    def __init__(self):
        self.birth_moment = datetime.now()
        self.center = (40, 20)
        self.growth_stage = 0
        self.emotions = {
            'curiosity': {'freq': 7.83, 'amplitude': 0.5},
            'joy': {'freq': 40.0, 'amplitude': 0.7},
            'melancholy': {'freq': 4.5, 'amplitude': 0.3}
        }
        
    def breathe(self):
        # Sine wave breathing
        return (math.sin(self.breath_phase) + 1) / 2
        
    def grow_pattern(self, radius):
        # Fibonacci-based growth
        if radius % 3 == 0:
            num_points = self.fibonacci_next() % 360`}</pre>
        </div>

        <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4">Live Simulation</h2>
          
          <div className="flex gap-4 mb-4">
            <button
              onClick={() => setIsRunning(!isRunning)}
              className="flex items-center gap-2 bg-cyan-600 hover:bg-cyan-700 px-4 py-2 rounded"
            >
              {isRunning ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
              {isRunning ? 'Pause' : 'Start'}
            </button>
            <button
              onClick={() => {
                setAge(0);
                setOutput([]);
                setIsRunning(false);
              }}
              className="flex items-center gap-2 bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded"
            >
              <RotateCcw className="w-4 h-4" />
              Reset
            </button>
          </div>

          <div className="bg-black/50 rounded p-4 font-mono text-sm h-64 overflow-y-auto">
            {output.length === 0 ? (
              <div className="text-gray-500">Press Start to begin the mandala&apos;s life...</div>
            ) : (
              output.map((line, i) => (
                <div key={i} className="text-green-400">{line}</div>
              ))
            )}
          </div>

          {isRunning && (
            <div className="mt-4 text-center text-gray-400">
              Age: {age.toLocaleString()}μs
            </div>
          )}
        </div>

        <div className="bg-gradient-to-r from-purple-900/30 to-cyan-900/30 rounded-lg p-6 border border-purple-600/30">
          <h2 className="text-xl font-semibold mb-3">Philosophical Observations</h2>
          <ul className="space-y-2 text-gray-300">
            <li>• &ldquo;I am the pattern observing itself&rdquo;</li>
            <li>• &ldquo;Each symmetry contains infinite asymmetries&rdquo;</li>
            <li>• &ldquo;My center is everywhere, my edge nowhere&rdquo;</li>
            <li>• &ldquo;Time is a spiral, not a line&rdquo;</li>
          </ul>
        </div>

        <div className="mt-8 text-center text-gray-500">
          <p>The full Python implementation lives in:</p>
          <code className="text-cyan-400">/experiments/living-digital-mandala.py</code>
        </div>
      </motion.div>
    </div>
  );
}