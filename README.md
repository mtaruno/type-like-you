# Ditto (type-like-you)
<img src="https://github.com/mtaruno/type-like-you/assets/44710581/2bb5330b-667b-4228-b0e0-2c3cbe00d9b0" alt="logo_transparent" width="150">



### Introduction
ChatGPT has been an amazing direct advancement to human-computer interaction. However, in human-human casual interaction, when using text to converse in a conversational interface, we almost never talk and communicate the way default ChatGPT converses. With `Ditto`, we explore how to use RAG and in-context-learning to achieve a talking style that mimics the way we chat every day to a personal level (as you can upload your own WhatsApp conversation data). 

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

This chat does not have a personality backbone, nor does it imitate how your peers may message you. For example, our peers do not just send us a one line text message every time, it is often distributed across a few message. Our goal is to make an agent that is more casual, less robotic, more familiar. We hypothesize that this will lead to higher response rates, increased user satisfaction (and naturally session times), and perhaps content comprehensibility. (Our user study results will be posted below). 

### Usage Instructions

First, export your WhatsApp Chat in the form of a text file (I usually put it in `/data`) as shown the in picture: 
<img width="750" alt="whatsapp-export" src="https://github.com/mtaruno/type-like-you/assets/44710581/5c7a194e-ab38-4105-b042-e56c9ae6c215">

Then make sure the in `parse.py` that the regex expression expressed by "pattern" can correctly parse the WhatsApp message. (I am currently developing support for things other than WhatsApp exports and perhaps a more general regex expression). You are able to adjust as necessary, I may recommend you check out https://regexr.com/ to make sure you have the right pattern.

Also make sure to point towards an SQLite DB file. 

Run the Flask server to enable requests to the API endpoints.
```
python server.py
```

Then `cd` into `/frontend` and run the front-end to use Ditto:
```
pnpm dev
```

Congratulations! You should get something like this: 

<img width="1000" alt="homepage" src="https://github.com/mtaruno/type-like-you/assets/44710581/77f58cab-0500-4119-8052-b837a8b42303">

Here's what a chat may look like. 
<img width="1118" alt="gabriel" src="https://github.com/mtaruno/type-like-you/assets/44710581/4e34cecf-741a-4b1c-8c93-d2117693f8a9">

### Development
This application is developed with React + Flask + SQLite. 

### Contextual Additions: 
Check the `config.yml` file for the full prompt. We include:

- System: Message Count, WhatsApp Name
- Sentence Length: Sentence Distribution
- Spelling: Token Distribution
- Language: Langauge distribution
- Slang Usage: User Slang Dictionary (during the upload pipeline we give an option to the user (perhaps after extensive testing of conversation to give custom slang definition in a specific language) 
- Key Scenarios: Random retriever to get a subset (which may be diversified to make it more representative of the person's tone) of this conversation to put into the context of GPT-4o's 128k context window.
- Extra Tips
- Response Format

### Repo Map

- `research` directory includes a few research papers tangentially related to this work.  
- `ditto` directory contains the bulk of the work. `server.py` contains high level usages of ditto, leveraging utilities in the `utils` directory. 
- The sqlite database is stored in `/data/db/chat.db`