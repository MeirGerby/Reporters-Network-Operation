import json 
from datetime import datetime 
import uuid

class Event:
    def __init__(self, event_type: str, payload: dict):
        self._id: str = str(uuid.uuid4())
        self.event_type = event_type 
        self.payload = payload 
        self.timestamp = datetime.now().isoformat() 

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "type":self.event_type,
            "payload": self.payload,
            "timestamp": self.timestamp
        }
    
    def to_json(self) -> bytes:
        return json.dumps(self.to_dict()).encode('utf-8') 
    