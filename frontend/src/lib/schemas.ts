export interface History {
  id: number;
  username: string;
  messages: Message[];
}

export interface Message {
  speaker: 0 | 1;
  message: string;
}
