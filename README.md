# type-like-you

The goal is to make an agent that is more casual, less robotic, more familiar. We hypothesize that this may lead to higher response rates and an increased user satisfaction. 2 studies are conducted to test this hypothesis. 

1. talk-like-you vs regular LLM
2. distinguish real human replies from talk-like-you

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

