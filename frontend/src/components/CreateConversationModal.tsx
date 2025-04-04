// src/components/CreateConversationModal.tsx
"use client";

import { useState } from "react";
import {
  Modal,
  TextInput,
  Button,
  Stack,
} from "@mantine/core";

interface CreateConversationModalProps {
  opened: boolean;
  onClose: () => void;
  onCreate: (name: string) => void;
}

export default function CreateConversationModal({
  opened,
  onClose,
  onCreate,
}: CreateConversationModalProps) {
  const [name, setName] = useState("");

  const handleSubmit = () => {
    if (name.trim()) {
      onCreate(name.trim());
      setName("");
      onClose();
    }
  };

  return (
    <Modal opened={opened} onClose={onClose} title="New Conversation" centered>
      <Stack>
        <TextInput
          label="Conversation Name"
          placeholder="Enter a name..."
          value={name}
          onChange={(e) => setName(e.currentTarget.value)}
        />
        <Button onClick={handleSubmit}>Create</Button>
      </Stack>
    </Modal>
  );
}
