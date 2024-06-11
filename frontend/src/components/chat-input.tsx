'use client';
import { fetchHistory, postText } from "@/app/actions";
import { Textarea } from "@/components/ui/textarea"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useState } from "react";
import { useChatStore } from "./providers";


export default function ChatInput() {
  const mutation = useMutation({
    mutationFn: postText,
    onSuccess: ({ message }) => {

      queryClient.setQueryData(["history"], (history: any) => {
        const data = JSON.parse(JSON.stringify(history));
        console.log(message)
        data[selected].messages.push({ speaker: 1, text: message });
        return data;
      })
    }
  });
  const [text, setText] = useState("");
  const selected = useChatStore(state => state.selected);
  const { data: history } = useQuery({ queryKey: ["history"], queryFn: fetchHistory });
  const queryClient = useQueryClient();

  function handleChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    setText(e.target.value);
  }
  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key == "Enter") {
      if (history) {
        const data = { id: history[selected].username, text };
        mutation.mutate(data)

        queryClient.setQueryData(["history"], (history: any) => {
          const data = JSON.parse(JSON.stringify(history));
          data[selected].messages.push({ speaker: 0, text });
          return data;
        })
      }

      setText("");
    }
  }

  if (selected != -1)
    return (
      // <Textarea className="w-full h-24 caret-primary border-x-0 resize-none" autoFocus />
      <Textarea
        className="h-full text-lg"
        value={text}
        onKeyDown={handleKeyDown}
        onChange={handleChange}
        autoFocus
      />
    )
}
