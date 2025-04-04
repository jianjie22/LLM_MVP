// src/components/ChatInput.tsx
"use client";

import { useState } from "react";

interface ChatInputProps {
  onSend: (message: string) => void;
}

export default function ChatInput({ onSend }: ChatInputProps) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input.trim());
    setInput("");
  };

  return (
    <div className="flex gap-2 p-2 border-t">
      <input
        className="flex-1 border rounded px-3 py-2"
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your prompt here..."
      />
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
}
