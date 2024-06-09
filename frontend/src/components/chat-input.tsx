'use client';
import { postText } from "@/app/actions";
import { Textarea } from "@/components/ui/textarea"
import { useMutation } from "@tanstack/react-query"
import { useState } from "react";


export default function ChatInput() {
  const mutation = useMutation({ mutationFn: postText });
  const [text, setText] = useState("");

  function handleChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    setText(e.target.value);
  }
  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    console.log(e);
    if (e.key == "Enter") {
      console.log("wow");
      setText("");
    }
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
