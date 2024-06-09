// 'use server';

const url = "http://127.0.0.1:3420";
export async function fetchHistory() {
  const response = await fetch(url + '/history');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  const json = response.json();
  console.log(json);

  return json;
}

export async function testFetch() {
  const testUrl = 'https://jsonplaceholder.typicode.com/todos';
  const response = await fetch(testUrl);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  const json = await response.text();
  console.log(json);

  return json;
}
