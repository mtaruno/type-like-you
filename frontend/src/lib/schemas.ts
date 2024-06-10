// /history
export interface History {
  id: number;
  username: string;
  messages: Message[];
}

export interface Message {
  speaker: 0 | 1;
  text: string;
}

export interface PostText {
  id: number;
  text: string;
}

export interface UploadHistory {
  whatsapp_name: string;
  whatsapp_history: string;
  user_slang_dictionary: string;

}

export interface UploadChat {
  session_id: number;
  whatsapp_name: string;
  message: string;
}
