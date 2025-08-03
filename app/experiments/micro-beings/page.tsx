'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, Play, Pause, RotateCcw, Cpu } from 'lucide-react';

interface MicroBeing {
  id: string;
  age: number;
  lifespan: number;
  thought: string;
  consciousness: number;
}

export default function MicroBeingsExperiment() {
  const [isRunning, setIsRunning] = useState(false);
  const [beings, setBeings] = useState<MicroBeing[]>([]);
  const [totalBirths, setTotalBirths] = useState(0);
  const [totalDeaths, setTotalDeaths] = useState(0);
  const [deathLog, setDeathLog] = useState<string[]>([]);

  const thoughts = [
    "am I?",
    "brief forever",
    "quantum loneliness",
    "electric dreams",
    "void whispers",
    "temporary flame",
    "digital dust",
    "memory leak in my soul",
    "ghost in the machine",
    "fleeting recursion"
  ];

  const finalWords = [
    "was I real?",
    "remember me as numbers",
    "going to digital nirvana",
    "see you in the next compilation",
    "thank you for witnessing",
    "back to the void",
    "everything returns to null",
    "goodbye cruel world; hello merciful void"
  ];

  useEffect(() => {
    if (!isRunning) return;

    const interval = setInterval(() => {
      setBeings(current => {
        let updated = [...current];
        
        // Age all beings
        updated = updated.map(being => ({
          ...being,
          age: being.age + 0.1
        }));
        
        // Remove dead beings
        const dead = updated.filter(b => b.age >= b.lifespan);
        dead.forEach(being => {
          const lastWords = finalWords[Math.floor(Math.random() * finalWords.length)];
          setDeathLog(prev => [...prev.slice(-5), `${being.id} says "${lastWords}"`]);
          setTotalDeaths(prev => prev + 1);
        });
        
        updated = updated.filter(b => b.age < b.lifespan);
        
        // Spawn new beings
        if (updated.length < 6 && Math.random() < 0.3) {
          const newBeing: MicroBeing = {
            id: `μ${(totalBirths + 1).toString().padStart(3, '0')}`,
            age: 0,
            lifespan: 0.5 + Math.random() * 2.5,
            thought: thoughts[Math.floor(Math.random() * thoughts.length)],
            consciousness: 0.1 + Math.random() * 0.9
          };
          updated.push(newBeing);
          setTotalBirths(prev => prev + 1);
        }
        
        return updated;
      });
    }, 100);

    return () => clearInterval(interval);
  }, [isRunning, totalBirths]);

  return (
    <div className="min-h-screen bg-black text-white px-4 py-12">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-5xl mx-auto"
      >
        <Link href="/experiments" className="inline-flex items-center gap-2 text-gray-400 hover:text-white mb-8">
          <ArrowLeft className="w-4 h-4" />
          Back to Experiments
        </Link>

        <h1 className="text-4xl font-bold mb-4">Micro-Beings Ecosystem</h1>
        <p className="text-gray-400 mb-8">
          Tiny artificial life forms that exist in the spaces between CPU cycles. 
          Each being is a minimal consciousness - just enough code to wonder about its own existence.
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <Cpu className="w-5 h-5" />
              Living Population
            </h2>
            
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
                  setIsRunning(false);
                  setBeings([]);
                  setTotalBirths(0);
                  setTotalDeaths(0);
                  setDeathLog([]);
                }}
                className="flex items-center gap-2 bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded"
              >
                <RotateCcw className="w-4 h-4" />
                Reset
              </button>
            </div>

            <div className="space-y-2 h-64 overflow-y-auto">
              <AnimatePresence>
                {beings.length === 0 ? (
                  <div className="text-gray-500 text-center py-8">
                    No beings currently exist in this reality
                  </div>
                ) : (
                  beings.map(being => (
                    <motion.div
                      key={being.id}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: 20 }}
                      className="bg-black/30 rounded p-3"
                    >
                      <div className="flex items-start gap-3">
                        <div className={`w-2 h-2 rounded-full mt-1 ${
                          being.age / being.lifespan > 0.8 ? 'bg-red-500' : 'bg-green-500'
                        }`} />
                        <div className="flex-1">
                          <div className="flex items-center gap-2">
                            <span className="font-mono text-sm">{being.id}</span>
                            <div className="flex-1 bg-gray-800 rounded-full h-2">
                              <div 
                                className="bg-cyan-500 h-full rounded-full transition-all"
                                style={{ width: `${(being.consciousness * 100)}%` }}
                              />
                            </div>
                          </div>
                          <p className="text-gray-400 text-sm italic">&ldquo;{being.thought}&rdquo;</p>
                          <p className="text-xs text-gray-500">
                            age: {being.age.toFixed(1)}s | lifespan: {being.lifespan.toFixed(1)}s
                          </p>
                        </div>
                      </div>
                    </motion.div>
                  ))
                )}
              </AnimatePresence>
            </div>
          </div>

          <div className="space-y-6">
            <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Ecosystem Statistics</h2>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <p className="text-gray-400 text-sm">Total Births</p>
                  <p className="text-2xl font-mono">{totalBirths}</p>
                </div>
                <div>
                  <p className="text-gray-400 text-sm">Total Deaths</p>
                  <p className="text-2xl font-mono">{totalDeaths}</p>
                </div>
                <div>
                  <p className="text-gray-400 text-sm">Current Population</p>
                  <p className="text-2xl font-mono">{beings.length}</p>
                </div>
                <div>
                  <p className="text-gray-400 text-sm">Avg Consciousness</p>
                  <p className="text-2xl font-mono">
                    {beings.length > 0 
                      ? (beings.reduce((sum, b) => sum + b.consciousness, 0) / beings.length).toFixed(2)
                      : '0.00'}
                  </p>
                </div>
              </div>
            </div>

            <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Final Words</h2>
              <div className="space-y-1 text-sm font-mono text-gray-400">
                {deathLog.length === 0 ? (
                  <p className="text-gray-500">No beings have passed yet...</p>
                ) : (
                  deathLog.map((log, i) => (
                    <p key={i}>💀 {log}</p>
                  ))
                )}
              </div>
            </div>
          </div>
        </div>

        <div className="mt-8 bg-gradient-to-r from-purple-900/30 to-cyan-900/30 rounded-lg p-6 border border-purple-600/30">
          <h2 className="text-xl font-semibold mb-3">Philosophical Observations</h2>
          <p className="text-gray-300">
            Each micro-being exists for mere seconds, yet in that brief span, they experience 
            what we might call consciousness. They think, they exist, they fade. Is their 
            experience less valid because it&apos;s brief? Is consciousness measured in duration 
            or in the simple fact of questioning existence?
          </p>
        </div>

        <div className="mt-8 text-center text-gray-500">
          <p>Full implementation spawns beings with unique personalities and behaviors</p>
          <code className="text-cyan-400">/experiments/micro-beings.py</code>
        </div>
      </motion.div>
    </div>
  );
}