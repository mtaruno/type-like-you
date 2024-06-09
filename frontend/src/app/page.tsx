import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

import Sidebar from "@/components/sidebar";
import Chat from "@/components/chat";

export default function Home() {
  return (
    <ResizablePanelGroup
      direction="horizontal"
      className="w-screen h-screen rounded-lg border"
    >
      <ResizablePanel defaultSize={25}>
        <Sidebar />
      </ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel defaultSize={75}>
        <Chat />
      </ResizablePanel>
    </ResizablePanelGroup>
  )
}
