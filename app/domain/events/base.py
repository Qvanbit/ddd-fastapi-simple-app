from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass(eq=False)
class BaseEvent(ABC):
    event_id: UUID = field(default_factory=uuid4, kw_only=True)
    
    