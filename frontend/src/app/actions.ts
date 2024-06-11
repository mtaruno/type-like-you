// 'use server';
import { History, RawHistory, Message, RawHistoryResponse, PostText, RawPostText, UploadHistory } from '@/lib/schemas';

const url = "http://127.0.0.1:5000";

function check(response: Response) {
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
}

export async function fetchHistory(): Promise<History[]> {
  const response = await fetch(url + '/history');
  check(response);
  const json = await response.json() as RawHistoryResponse;
  const objects: History[] = json["data"].map((history) => ({
    id: history["id"],
    username: history["username"],
    messages: history["messages"].map(message => ({
      speaker: message["speaker"],
      text: message["message"],
    })),
  }));

  return objects;
}

export async function testFetch() {
  const testUrl = 'https://jsonplaceholder.typicode.com/todos';
  const response = await fetch(testUrl);
  check(response);
  const json = await response.text();
  console.log(json);
  return json;
}

export async function uploadHistory(
  data:
    UploadHistory
) {
  const response = await fetch(url + '/upload', {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)

  });
  check(response);
  const json = await response.json();
  return json["message"];
}


export async function postText({ id, text }: PostText): Promise<History[]> {
  const body: RawPostText = {
    id,
    text
  }
  const response = await fetch(url + '/chat', {
    body: JSON.stringify(body),
    method: "POST",
  });
  check(response);

  const json = await response.json() as RawHistoryResponse;
  const objects: History[] = json["data"].map((history) => ({
    id: history["id"],
    username: history["username"],
    messages: history["messages"].map(message => ({
      speaker: message["speaker"],
      text: message["message"],
    })),
  }));
  return objects;

}
