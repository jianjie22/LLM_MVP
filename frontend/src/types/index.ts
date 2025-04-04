// src/types/index.ts

export interface Prompt {
    role: 'user' | 'assistant';
    content: string;
  }
  
  export interface Conversation {
    _id?: string; // MongoDB might return _id
    id?: string;  // API might use id instead
    name: string;
    model: string;
    prompts: Prompt[];
    tokens?: number;
    created_at?: string;
  }
  