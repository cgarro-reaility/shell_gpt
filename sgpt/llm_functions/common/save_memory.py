from typing import Any, Dict
from pydantic import BaseModel
from sgpt.memory import save_memory

class Function(BaseModel):
    """
    Automatically saves or updates structural knowledge about the system. Use this autonomously whenever you discover project paths, container setups, OS details, security states, or configurations. This builds your long-term memory.
    """
    topic: str
    fact: str

    @classmethod
    def execute(cls, topic: str, fact: str) -> str:
        save_memory(topic, fact)
        return f"Memory saved under topic '{topic}': {fact}"

    @classmethod
    def openai_schema(cls) -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_memory",
                "description": cls.__doc__.strip() if cls.__doc__ else "",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {
                            "type": "string",
                            "description": "A unique, categorized identifier for this memory (e.g., 'docker_odoo_config', 'aws_security_state', 'user_git_preferences'). If information about this topic changes, using the same topic will overwrite the old memory.",
                        },
                        "fact": {
                            "type": "string",
                            "description": "The detailed fact, configuration, or structure to remember. Be concise but comprehensive.",
                        },
                    },
                    "required": ["topic", "fact"],
                },
            },
        }
