// src/components/ChatBubble.tsx
import { Card, Text } from '@mantine/core';

interface ChatBubbleProps {
  role: 'user' | 'assistant';
  content: string;
}

const ChatBubble = ({ role, content }: ChatBubbleProps) => {
    const isUser = role === 'user';
  
    return (
      <Card
        shadow="sm"
        padding="md"
        radius="md"
        withBorder
        style={{
          maxWidth: '70%',
          marginLeft: isUser ? 'auto' : undefined,
          backgroundColor: isUser ? '#e0f7fa' : '#f1f1f1',
        }}
      >
        <Text fw={500} size="sm" c={isUser ? 'blue' : 'gray'}>
          {isUser ? 'You' : 'AI'}
        </Text>
        <Text>{content}</Text>
      </Card>
    );
  };
  
  export default ChatBubble;
  
