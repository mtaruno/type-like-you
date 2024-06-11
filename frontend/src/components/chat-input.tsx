'use client';
import { fetchHistory, postText } from "@/app/actions";
import { Textarea } from "@/components/ui/textarea"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useState } from "react";
import { useChatStore } from "./providers";


export default function ChatInput() {
  const mutation = useMutation({ mutationFn: postText });
  const [text, setText] = useState("");
  const selected = useChatStore(state => state.selected);
  const { data: history } = useQuery({ queryKey: ["history"], queryFn: fetchHistory });

  function handleChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    setText(e.target.value);
  }
  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    console.log(e);
    if (e.key == "Enter") {
      console.log("wow");
      setText("");
    }
    if (history) mutation.mutate({ id: history[selected].username, text })
  }

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
