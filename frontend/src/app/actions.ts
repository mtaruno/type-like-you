// 'use server';
import { History, RawHistory, Message, RawResponse, PostText, RawPostText } from '@/lib/schemas';

const url = "http://127.0.0.1:3420";

function check(response: Response) {
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
}

export async function fetchHistory(): Promise<History[]> {
  const response = await fetch(url + '/history');
  check(response);
  const json = await response.json() as RawResponse;
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

  const json = await response.json() as RawResponse;
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
