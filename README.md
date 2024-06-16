# Ditto (type-like-you)
![logo_transparent](https://github.com/mtaruno/type-like-you/assets/44710581/2bb5330b-667b-4228-b0e0-2c3cbe00d9b0)

### Usage Instructions

First, export your WhatsApp Chat in the form of a text file (I usually put it in `/data`) as shown the in picture: 
<img width="750" alt="whatsapp-export" src="https://github.com/mtaruno/type-like-you/assets/44710581/5c7a194e-ab38-4105-b042-e56c9ae6c215">

Then make sure the in `parse.py` that the regex expression expressed by "pattern" can correctly parse the WhatsApp message. (I am currently developing support for things other than WhatsApp exports and perhaps a more general regex expression). You are able to adjust as necessary, I may recommend you check out https://regexr.com/ to make sure you have the right pattern.

Also make sure to point towards an SQLite DB file. 

Run the Flask server to enable requests to the API endpoints.
```
python server.py
```

Then run the front-end to use Ditto:
```
pnpm dev
```


### Database

### Introduction
ChatGPT has been an amazing direct advancement to human-computer interaction. However, in human-human casual interaction, when using text to converse in a conversational interface, we almost never talk and communicate the way default ChatGPT converses. In `talk-like-you`, we explore how to use RAG and in-context-learning to achieve a talking style that mimics the way we chat every day to a personal level (as you can upload your own WhatsApp conversation data). 

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
This application is developed with React + Flask + SQLite. 

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




### Learned Tone Features
- Sentence length: tendency for person to break up sentences into multiple lines (more lines less tokens) or in one line but more tokens. 
- Ways they spell: punctuation, exclamation marks, etc. This includes different ways of writing the same word: okay, okie, ok, oki, kk, okok
- Slang usage
- Emoji usage

### Adding to Context

I will create a retriever to get a subset (which may be diversified to make it more representative of the person's tone) of this conversation to put into the context of GPT-4o's 128k context window. The context will also contain a bunch of instructions to copy more nuances about you.

### Retrievers
- Base Retriever 


