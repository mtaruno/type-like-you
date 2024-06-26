'use client';
import Image from "next/image";
import { ScrollArea } from "@/components/ui/scroll-area"
import { useQuery } from "@tanstack/react-query";
import { fetchHistory } from "@/app/actions";
import { Message as MessageInterface } from '@/lib/schemas';
import { cn } from "@/lib/utils";
import { buttonVariants } from "./ui/button";
import { useChatStore } from "./providers";
import { forwardRef, useEffect, useRef } from "react";

const Gap = forwardRef(function Gap(_, ref: React.LegacyRef<HTMLDivElement>) {
  return (

    <div className="h-4" ref={ref}></div>
  )
})

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

  // TODO: Implement Scroll to bottom feature later
  const ref = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    ref.current?.scrollIntoView({ behavior: "smooth" });

  }, [data]);

  if (selected != -1) {
    return <div className="h-full flex flex-col">
      <ScrollArea className="h-full">
        <div className="flex flex-col gap-y-2 mx-4">
          {/* Empty Div for some space */}
          <Gap />
          {data?.[selected]?.messages && data[selected].messages.map(({ speaker, text }, index) => {

            const splitText = text.split(/\r?\n/)
              .filter((text) => text != "")
              .map((text) => {
                return <Message speaker={speaker} text={text} key={index} />;

              });
            return splitText;

          }
          )}
          <Gap />
        </div>
        <div ref={ref} />
      </ScrollArea>
    </div>;
  } else {
    return <div className="h-screen flex justify-center items-center flex-col">
      <Image src="/logo_transparent.png" alt="Chat" width={300} height={300} />
      <p className="text-xl">
        Select a Chat to get started.
      </p>
    </div>
  }
}

