
export interface RawHistory {
  messages: RawMessage[];
}

export interface RawHistoryResponse {
  message: RawHistory[];
}

export interface RawMessage {
  speaker: 0 | 1;
  message: string;
}

