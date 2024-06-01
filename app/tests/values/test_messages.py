from datetime import datetime
import pytest

from domain.exceptions.messages import TextTooLongException
from domain.values.messages import Text, Title
from domain.entities.messages import Chat, Message

def test_create_message_success():
    text = Text('hello world')
    message = Message(text = text)
    
    assert message.text == text
    assert message.created_at.date() == datetime.today().date()
    
    
def test_create_message_text_too_long():
    with pytest.raises(TextTooLongException):
        text = Text('a' * 2565)
        
        
def test_create_chat_success():
    title = Title('title')
    chat = Chat(title = title)
    
    assert chat.title == title
    assert not chat.messages
    
def test_add_chat_to_message():
    text = Text('hello world')
    message = Message(text = text)
    
    title = Title('title')
    chat = Chat(title = title)
    
    chat.add_message(message)
    
    assert message in chat.messages
    