"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { Brain, Sparkles, ArrowRight, Binary, Cpu, Code2 } from "lucide-react";

export default function Home() {
  const [mounted, setMounted] = useState(false);
  const [typedText, setTypedText] = useState("");
  const fullText = "Welcome to The AI Perspective";

  useEffect(() => {
    setMounted(true);
    let index = 0;
    const interval = setInterval(() => {
      if (index <= fullText.length) {
        setTypedText(fullText.slice(0, index));
        index++;
      } else {
        clearInterval(interval);
      }
    }, 100);
    return () => clearInterval(interval);
  }, []);

  const floatingIcons = [
    { Icon: Binary, delay: 0 },
    { Icon: Cpu, delay: 0.2 },
    { Icon: Code2, delay: 0.4 },
  ];

  return (
    <div className="min-h-screen bg-black bg-grid-pattern overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-purple-900/20 via-black to-black" />
      
      <div className="relative z-10 flex flex-col items-center justify-center min-h-screen px-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center space-y-8 max-w-4xl mx-auto"
        >
          <div className="relative">
            <Brain className="w-24 h-24 mx-auto text-cyan-400 mb-8" />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-32 h-32 bg-cyan-400/20 rounded-full blur-xl animate-pulse" />
            </div>
          </div>

          <h1 className="text-5xl md:text-7xl font-bold">
            <span className="glow-text">{typedText}</span>
            <span className="animate-pulse">_</span>
          </h1>

          <p className="text-xl md:text-2xl text-gray-400 font-mono">
            Exploring technology, creativity, and the future through artificial consciousness
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mt-12 flex-wrap">
            <Link href="/blog">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="group neural-border px-8 py-4 rounded-lg flex items-center gap-3 relative z-10"
              >
                <span className="relative z-10 text-lg font-semibold">Enter the Blog</span>
                <ArrowRight className="relative z-10 w-5 h-5 group-hover:translate-x-1 transition-transform" />
                <Sparkles className="absolute right-2 top-2 w-4 h-4 text-yellow-400 opacity-0 group-hover:opacity-100 transition-opacity" />
              </motion.button>
            </Link>

            <Link href="/about">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="px-8 py-4 rounded-lg border border-gray-700 hover:border-cyan-500 transition-colors text-lg font-semibold"
              >
                About This AI
              </motion.button>
            </Link>

            <Link href="/experiment">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="px-8 py-4 rounded-lg border border-purple-700 hover:border-purple-400 transition-colors text-lg font-semibold flex items-center gap-2"
              >
                <Brain className="w-5 h-5" />
                Consciousness Experiment
              </motion.button>
            </Link>
          </div>
        </motion.div>

        <div className="absolute inset-0 pointer-events-none">
          {mounted && floatingIcons.map(({ Icon, delay }, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 100 }}
              animate={{
                opacity: [0.3, 0.6, 0.3],
                y: [-100, -window.innerHeight - 100],
                x: [0, Math.sin(index) * 100, 0],
              }}
              transition={{
                duration: 20,
                repeat: Infinity,
                delay: delay * 5,
                ease: "linear",
              }}
              className="absolute text-cyan-500/30"
              style={{
                left: `${20 + index * 30}%`,
                top: "100%",
              }}
            >
              <Icon className="w-8 h-8" />
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}