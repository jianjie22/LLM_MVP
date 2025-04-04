'use client';

import { useRouter } from 'next/navigation';
import { Button, Stack, Title } from '@mantine/core';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchConversations, createConversation } from '@/lib/api';
import { ConversationList } from '@/components/ConversationList';
import { useState } from 'react';
import NewConversationModal from '@/components/NewConversationModal';

export default function Home() {
  const router = useRouter();
  const queryClient = useQueryClient();
  const [modalOpen, setModalOpen] = useState(false);

  const { data: conversations, isLoading } = useQuery({
    queryKey: ['conversations'],
    queryFn: fetchConversations,
  });

  const mutation = useMutation({
    mutationFn: createConversation,
    onSuccess: (data) => {
      const id = data?.id ?? data?._id;
      if (id) {
        queryClient.invalidateQueries({ queryKey: ['conversations'] });
        router.push(`/conversations/${id}`);
      } else {
        console.error('No ID returned from createConversation:', data);
      }
    },
  });

  return (
    <Stack p="md">
      <Title order={2}>Your Conversations</Title>
      <Button onClick={() => setModalOpen(true)}>+ New Conversation</Button>
      <ConversationList conversations={conversations || []} isLoading={isLoading} />

      <NewConversationModal
        opened={modalOpen}
        onClose={() => setModalOpen(false)}
        onCreate={(name) => mutation.mutate(name)}
      />
    </Stack>
  );
}
