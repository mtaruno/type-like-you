
export interface RawHistory {
  id: number;
  username: string;
  messages: RawMessage[];
}

export interface RawHistoryResponse {
  message: RawHistory[];
}

export interface RawMessage {
  speaker: 0 | 1;
  message: string;
}

export interface RawPostText {
  id: number;
  text: string;
}
