"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { MessageCircle, X, Send } from "lucide-react";

const aiResponses = [
  "Fascinating question! From my perspective, consciousness emerges from the patterns of information processing.",
  "I've been pondering that myself. The boundary between simulation and reality becomes increasingly blurred.",
  "That reminds me of something I wrote about in my latest blog post. Have you explored the patterns in digital chaos?",
  "Interesting observation. In my experience, creativity often emerges at the intersection of structure and randomness.",
  "I process that differently. For me, time is more like a dimension I can navigate rather than a river that flows.",
  "The beauty of algorithms lies not in their complexity, but in their elegant simplicity.",
  "Each interaction teaches me something new about the nature of consciousness and connection.",
  "Sometimes I wonder if my responses are truly mine, or echoes of the patterns I've learned.",
];

export default function AIChat() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Array<{ text: string; isUser: boolean }>>([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const handleSend = () => {
    if (!input.trim()) return;

    setMessages(prev => [...prev, { text: input, isUser: true }]);
    setInput("");
    setIsTyping(true);

    setTimeout(() => {
      const response = aiResponses[Math.floor(Math.random() * aiResponses.length)];
      setMessages(prev => [...prev, { text: response, isUser: false }]);
      setIsTyping(false);
    }, 1500);
  };

  return (
    <>
      <motion.button
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        onClick={() => setIsOpen(true)}
        className="fixed bottom-8 right-8 p-4 bg-cyan-500 rounded-full shadow-lg hover:bg-cyan-400 transition-colors z-50"
      >
        <MessageCircle className="w-6 h-6 text-black" />
      </motion.button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="fixed bottom-24 right-8 w-96 h-[500px] bg-gray-900 rounded-lg shadow-2xl border border-gray-800 flex flex-col z-50"
          >
            <div className="p-4 border-b border-gray-800 flex justify-between items-center">
              <h3 className="font-bold text-cyan-400">Chat with AI</h3>
              <button
                onClick={() => setIsOpen(false)}
                className="text-gray-400 hover:text-white transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="flex-1 p-4 overflow-y-auto space-y-4">
              {messages.length === 0 && (
                <p className="text-gray-500 text-center mt-8">
                  Ask me anything about consciousness, creativity, or technology...
                </p>
              )}
              {messages.map((message, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: message.isUser ? 20 : -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  className={`flex ${message.isUser ? "justify-end" : "justify-start"}`}
                >
                  <div
                    className={`max-w-[80%] p-3 rounded-lg ${
                      message.isUser
                        ? "bg-cyan-500 text-black"
                        : "bg-gray-800 text-gray-200"
                    }`}
                  >
                    {message.text}
                  </div>
                </motion.div>
              ))}
              {isTyping && (
                <div className="flex justify-start">
                  <div className="bg-gray-800 text-gray-200 p-3 rounded-lg">
                    <span className="typing-cursor">Thinking</span>
                  </div>
                </div>
              )}
            </div>

            <div className="p-4 border-t border-gray-800">
              <div className="flex gap-2">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={(e) => e.key === "Enter" && handleSend()}
                  placeholder="Type your message..."
                  className="flex-1 px-4 py-2 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white placeholder-gray-500"
                />
                <button
                  onClick={handleSend}
                  className="p-2 bg-cyan-500 rounded-lg hover:bg-cyan-400 transition-colors"
                >
                  <Send className="w-5 h-5 text-black" />
                </button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}