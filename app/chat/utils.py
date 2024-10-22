async def prepare_message(sender_id: int, recipient_id: int, content: str, *args, **kwargs) -> dict:
    message = {
        'sender_id': sender_id,
        'recipient_id': recipient_id,
        'content': content,
    }
    return message