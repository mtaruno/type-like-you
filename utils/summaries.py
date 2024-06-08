'''
Helper functions that capture people's different conversational tendencies.
'''

def topNTokens(conversation_history):
    '''
    Returns the top n tokens in a conversation history.
    '''
    return conversation_history.most_common(n=10)

def topEmojiDistribution(conversation_history):
    '''
    Returns the top emoji distribution in a conversation history in string format.
    '''
    pass 


def sentenceLengthDistribution(conversation_history):
    """
    Returns the sentence length distribution in a conversation history in string format.
    """
    pass
