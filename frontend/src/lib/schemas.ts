export interface History {
  id: number;
  username: string;
  messages: Message[];
}

export interface Message {
  speaker: 0 | 1;
  text: string;
}

export interface RawResponse {
  data: RawHistory[];
}

export interface RawHistory {
  id: number;
  username: string;
  messages: RawMessage[];
}

export interface RawMessage {
  speaker: 0 | 1;
  message: string;
}

export interface PostText {
  id: number;
  text: string;
}

export interface RawPostText {
  id: number;
  text: string;
}
