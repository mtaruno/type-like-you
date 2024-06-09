'use client';
import { Textarea } from "@/components/ui/textarea"
import { ScrollArea } from "@/components/ui/scroll-area"
import { useEffect } from "react";
import { useQuery } from "@tanstack/react-query";
import { fetchHistory } from "@/app/actions";


export default function Chat() {
  const { data } = useQuery({ queryKey: ['history'], queryFn: fetchHistory });
  console.log(data);

  return <div className="h-screen flex flex-col">
    <ScrollArea className="h-full">
      {JSON.stringify(data)}
    </ScrollArea>
    <Textarea className="w-full h-24 caret-primary border-x-0 resize-none" autoFocus />
  </div>;
}

