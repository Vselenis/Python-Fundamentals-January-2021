chat_logger = input()
chatting = []
while chat_logger != "end":
    command = chat_logger.split()[0]
    if command == "Chat":
        message = chat_logger.split()[1]
        chatting.append(message)
    elif command == 'Delete':
        message_to_delete = chat_logger.split()[1]
        if message_to_delete in chatting:
            chatting.remove(message_to_delete)
    elif command == "Edit":
        message_to_edit = chat_logger.split()[1]
        edited_version = chat_logger.split()[2]
        if message_to_edit in chatting:
            i = chatting.index(message_to_edit)
            chatting[i] = edited_version
    elif command == "Pin":
        message_pin = chat_logger.split()[1]
        if message_pin in chatting:
            chatting.remove(message_pin)
            chatting.append(message_pin)
    elif command == "Spam":
        spam = chat_logger.split()[1:]
        for word in spam:
            chatting.append(word)


    chat_logger = input()


print('\n'.join(chatting))









