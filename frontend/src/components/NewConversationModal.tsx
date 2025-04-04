'use client';

import { Modal, TextInput, Button, Stack, Group } from '@mantine/core';
import { useState } from 'react';

interface NewConversationModalProps {
  opened: boolean;
  onClose: () => void;
  onCreate: (name: string) => void;
}

export default function NewConversationModal({
  opened,
  onClose,
  onCreate,
}: NewConversationModalProps) {
  const [name, setName] = useState('');

  const handleSubmit = () => {
    if (name.trim()) {
      onCreate(name.trim());
      setName('');
      onClose();
    }
  };

  return (
    <Modal opened={opened} onClose={onClose} title="Create a new conversation" closeButtonProps={{ style: { display: 'none' } }}>
      <Stack>
        <TextInput
          placeholder="Conversation name"
          value={name}
          onChange={(e) => setName(e.currentTarget.value)}
        />
        <Group justify="flex-end">
          <Button variant="default" onClick={onClose}>Cancel</Button>
          <Button onClick={handleSubmit}>Create</Button>
        </Group>
      </Stack>
    </Modal>
  );
}
