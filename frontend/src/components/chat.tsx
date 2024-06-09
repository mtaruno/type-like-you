'use client';
import { ScrollArea } from "@/components/ui/scroll-area"
import { useQuery } from "@tanstack/react-query";
import { fetchHistory } from "@/app/actions";
import { Message as MessageInterface } from '@/lib/schemas';
import { cn } from "@/lib/utils";
import { buttonVariants } from "./ui/button";
import { useChatStore } from "./providers";
import ChatInput from "./chat-input";

function Gap() {
  return (

    <div className="h-4" />
  )
}

function Message({ speaker, text }: MessageInterface) {
  return <div className="w-full">
    <p className={
      cn(
        // "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
        // "bg-primary text-primary-foreground hover:bg-primary/90",
        buttonVariants({ variant: "default" }),
        "text-lg text-wrap block h-auto max-w-[70%]",
        { "float-right": speaker == 0, "float-left": speaker == 1 }
      )
    }>
      {text}
    </p >
  </div>
}

export default function Chat() {
  const { data } = useQuery({ queryKey: ['history'], queryFn: fetchHistory });
  const selected = useChatStore((state) => state.selected);

  if (selected != -1) {
    return <div className="h-full flex flex-col">
      <ScrollArea className="h-full">
        <div className="flex flex-col gap-y-2 mx-4">
          {/* Empty Div for some space */}
          <Gap />
          {data?.[selected]?.messages && data[selected].messages.map((message) => Message(message))}
          <Gap />
        </div>
      </ScrollArea>
    </div>;
  } else {
    return <div className="h-screen flex justify-center items-center">
      <p className="text-xl">
        Select a Chat to get started.
      </p>
    </div>
  }
}

