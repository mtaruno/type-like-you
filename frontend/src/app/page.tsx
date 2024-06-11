'use client';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

import Sidebar from "@/components/sidebar";
import Chat from "@/components/chat";
import ChatInput from "@/components/chat-input";
import { useChatStore } from "@/components/providers";

export default function Home() {
  const selected = useChatStore((state) => state.selected);
  return (
    <ResizablePanelGroup
      direction="horizontal"
      className="w-screen h-screen rounded-lg border"
    >
      <ResizablePanel minSize={15} defaultSize={25}>
        <Sidebar />
      </ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel className="h-screen" defaultSize={75}>

        <ResizablePanelGroup
          direction="vertical"
          className="h-screen"
        >

          <ResizablePanel defaultSize={75}>
            <Chat />
          </ResizablePanel >
          <ResizableHandle />

          {selected != -1 &&
            <ResizablePanel >
              <ChatInput />
            </ResizablePanel >
          }

        </ResizablePanelGroup>
      </ResizablePanel>
    </ResizablePanelGroup >
  )
}
