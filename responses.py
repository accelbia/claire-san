import random

def get_response(user_input: str) -> str:
    lowered_input: str = user_input.lower()
    
    if lowered_input == '':
        return "Oh, adventurer~ Did you forget to speak?~"
    
    if lowered_input == 'hello':
        return "Hey there, adventurer~ How can I assist you today~?"
    
    if lowered_input == 'goodbye':
        return "Aw, leaving already? Farewell for now~! Take care!"
    
    if lowered_input == 'roll':
        return f"A roll of the dice~? You got a {random.randint(1, 6)}, darling~"
    
    return random.choice([
        "Hmm, I'm not sure what you mean, adventurer~ Could you clarify~?",
        "Oh, that's a tricky one~ Maybe try rephrasing?",
        "I'm afraid I don't quite understand, but I'm here to help, so tell me more~",
        "Hmm, what do you mean by that, darling~?",
        "Oh, I'm not quite sure what you're asking, but I'm here to help, so let me know~",
        "I'm not sure what you mean, but I'm here to help, so let me know~",
        "Oh, that's a tough one~ Maybe try rephrasing?",
    ])
