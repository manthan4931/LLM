chat_history=[]

def add_to_memory(user,bot):
    chat_history.append({
        'user':user,
        'bot':bot
    })

def get_memory():
    history=""
    for chat in chat_history[-5:]:  # last 5 messages
        history += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    return history