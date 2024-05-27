# type-like-you

### Introduction
ChatGPT has been an amazing direct advancement to human-computer interaction. However, in human-human casual interaction, when using text to converse in a conversational interface, we almost never talk and communicate the way default ChatGPT converses. In `talk-like-you`, we explore how to use RAG and in-context-learning to achieve a talking style that mimics the way we chat every day to a personal level (as you can upload your own WhatsApp conversation data). 

This project is interactive and meant to be tested through user studies. For this purpose, we create a front-end to test out the effectiveness across 5 metrics:
- **talk-like-you vs regular LLM**: We measure `talk-like-you`'s satisfaction rates vs a regular LLM response. 
- distinguish `real human replies` from `talk-like-you`:  This is where we compare real human replies with `talk-like-you`
- Measuring "distinctness." Key question: Can we distinguish between one person we know and another person's style? Are the tone feature based responses enough to be differentiated by a human? 
- Multi-lingual test: I notice that most of my personal conversations are multi-lingual. I try to model these tendencies as a strong distinguishing characteristic of `talk-like-you`. Tested Languages: Bahasa Indonesia, English, Portugese, Mandarin
- Content comprehensibility: How easy is the content to digest? 

Why do we use personal WhatsApp data? Online conversational datasets available don't typically capture the broad scenario of everyday texting conversations. Example of an online conversation (that feels robotic and not like how we actually converse in messaging platforms): 

```
Human 1: Hi! 
Human 2: What is your favorite holiday? 
Human 1: one where I get to meet lots of different people. 
Human 2: What was the most number of people you have ever met during a holiday?
Human 1: Hard to keep a count. Maybe 25. 
Human 2: Which holiday was that? 
Human 1: I think it was Australia 
Human 2: Do you still talk to the people you met? 
Human 1: Not really. The interactions are usually short-lived but it's fascinating to learn where people are coming from and what matters to them 
```

Our goal is to make an agent that is more casual, less robotic, more familiar. We hypothesize that this will lead to higher response rates, increased user satisfaction, and perhaps comprehensibility of the content. 

### Development
This application is developed with React + Flask.  

**Databases:**
- Vector database with FAISS
- SQLite for conversations. 
- SQLite for saving on-going conversation history.

**Considerations:** 
- **State Management**: Managing chat history in the frontend state ensures responsiveness, but always keep a synchronized copy in the backend for consistency.
- **Error Handling**: Implement error handling for API calls and edge cases (e.g., empty messages).

#### Storing the conversations
Step 1 is to export a WhatsApp conversation (there is a `.txt` file option for this). 
In `utils/parse` I create a regex parser to correctly parse it into JSON objects with keys and values. 
From there, the data is directly retrieved from the RAM by `get_conversations()`. 
It's possible for us to create a separate database to store this. 

### Benchmark Dataset 
We create a simple benchmark dataset to capture the 5 metrics above. 

#### Habits database 
The prompt for this can be found in `prompts/habits.txt`. It then stores it in a log. 

Currently we store this as a text file that is auto-generated. Perhaps we can store this in a structured format that is automatically appended to by the LLM. 
[[Bryan Report]]
[[Valerie Report]]

### System Instructions (Adding to Context)

I will create a retriever to get a subset (which may be diversified to make it more representative of the person's tone) of this conversation to put into the context of GPT-4o's 128k context window. The context will also contain a bunch of instructions to copy more nuances about you.


### How to Run

#### Flask demo webapp
```
python server.py
```

#### Running the API
```
python response.py -m <message>
```

### Learned Tone Features
- Sentence length: tendency for person to break up sentences into multiple lines (more lines less tokens) or in one line but more tokens. 
- Ways they spell: punctuation, exclamation marks, etc. This includes different ways of writing the same word: okay, okie, ok, oki, kk, okok
- Slang usage
- Emoji usage

### Adding to Context

I will create a retriever to get a subset (which may be diversified to make it more representative of the person's tone) of this conversation to put into the context of GPT-4o's 128k context window. The context will also contain a bunch of instructions to copy more nuances about you.

### Retrievers
- Base Retriever 

