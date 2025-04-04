'use client';

import { useParams } from 'next/navigation';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { postQuery } from '@/lib/api';
import ChatBubble from '@/components/ChatBubble';
import ChatInput from '@/components/ChatInput';
import { Stack, Text, Title } from '@mantine/core';

export default function ConversationPage() {
  const params = useParams();
  const id = Array.isArray(params.id) ? params.id[0] : params.id;

  const queryClient = useQueryClient();

  const {
    data: conversation,
    isLoading,
    error,
  } = useQuery({
    queryKey: ['conversation', id],
    queryFn: async () => {
      console.log('Fetching conversation with ID:', id);

      const res = await fetch(`http://localhost:8000/conversations/${id}`);


      const data = await res.json();
      console.log('Raw response from server:', data);

      if (!res.ok || !data) throw new Error('Failed to fetch conversation');

      return {
        ...data,
        id: data._id, // normalize if needed
      };
    },
    enabled: !!id,
  });

  const mutation = useMutation({
    mutationFn: (message: string) =>
      postQuery({ conversation_id: id as string, prompt: message }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['conversation', id] });
    },
  });

  const handleSend = (message: string) => {
    mutation.mutate(message);
  };

  if (isLoading) return <Text>Loading...</Text>;
  if (error || !conversation) {
    console.log('Error:', error);
    console.log('Conversation data:', conversation);
    return <Text>Error loading conversation</Text>;
  }

  return (
    <Stack gap="sm" style={{ padding: '1rem' }}>
      <Title order={2}>{conversation.name}</Title>
      {conversation.prompts.map(
        (prompt: { role: string; content: string }, index: number) => (
          <ChatBubble
            key={index}
            role={prompt.role as 'user' | 'assistant'}
            content={prompt.content}
          />
        )
      )}
      <ChatInput onSend={handleSend} />
    </Stack>
  );
}
