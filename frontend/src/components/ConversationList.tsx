import { Stack, Card, Text, Loader } from '@mantine/core';
import { useRouter } from 'next/navigation';

export interface Conversation {
  id: string;
  name: string;
}

export interface ConversationListProps {
  conversations: Conversation[];
  isLoading: boolean;
}

export function ConversationList({ conversations, isLoading }: ConversationListProps) {
  const router = useRouter();

  if (isLoading) return <Loader />;

  if (!conversations.length) return <Text>No conversations yet.</Text>;

  return (
    <Stack>
      {conversations.map((c) => (
        <Card
          key={c.id}
          withBorder
          shadow="sm"
          radius="md"
          p="md"
          onClick={() => router.push(`/conversations/${c.id}`)}
          style={{ cursor: 'pointer' }}
        >
          <Text>{c.name || 'Untitled Chat'}</Text>
        </Card>
      ))}
    </Stack>
  );
}
