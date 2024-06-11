// /history
export interface History {
  username: string;
  messages: Message[];
}

export interface Message {
  speaker: 0 | 1;
  text: string;
}


export interface UploadHistory {
  whatsapp_name: string;
  whatsapp_history: string;
  user_slang_dictionary: string;

}

export interface UploadChat {
  id: string;
  text: string;
}
export interface RawUploadChat {
  whatsapp_name: string;
  message: string;
}

export interface UploadChatResponse {
  message: string;
}
