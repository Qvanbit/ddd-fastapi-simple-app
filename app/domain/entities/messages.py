from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title

@dataclass(eq=False, unsafe_hash=True)
class Message(BaseEntity):
    text: Text
    
    
@dataclass(eq=False, unsafe_hash=True)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )
    
    def add_message(self, message: Message):
        self.messages.add(message)