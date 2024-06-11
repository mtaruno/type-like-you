'use client';
import { create } from 'zustand';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

const queryClient = new QueryClient();

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient} >
      <ReactQueryDevtools initialIsOpen={false} />
      {children}
    </QueryClientProvider>
  )
}

interface ChatState {
  selected: number;
  searchFilter: string;
  setSelected: (selection: number) => void;
  setSearchFilter: (filter: string) => void;
}
export const useChatStore = create<ChatState>((set) => ({
  selected: -1,
  searchFilter: "",
  setSelected: (selection: number) => set((state) => ({ ...state, selected: selection })),
  setSearchFilter: (filter) => set((state) => ({ ...state, searchFilter: filter }))
}));
