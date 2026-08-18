import os
from pathlib import Path
from typing import List
import chromadb
from chromadb.config import Settings

# Use the same config path convention as the rest of ShellGPT
CONFIG_FOLDER = Path(os.path.expanduser("~/.config/shell_gpt"))
MEMORY_DIR = CONFIG_FOLDER / "memory"
COLLECTION_NAME = "sgpt_memory"

class MemoryManager:
    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(path=str(MEMORY_DIR))
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)

    def save_memory(self, topic: str, fact: str) -> None:
        """
        Saves a fact to the memory.
        """
        self.collection.upsert(
            documents=[fact],
            ids=[topic]
        )

    def get_relevant_memories(self, query: str, n_results: int = 5) -> List[str]:
        """
        Retrieves relevant memories based on the query.
        """
        if self.collection.count() == 0:
            return []
        
        # Determine n_results based on the collection count
        n_results = min(n_results, self.collection.count())
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        if results and "documents" in results and results["documents"]:
            # results["documents"] is a list of lists of strings
            return results["documents"][0]
        return []

memory_manager = MemoryManager()

def save_memory(topic: str, fact: str) -> None:
    memory_manager.save_memory(topic, fact)

def get_relevant_memories(query: str, n_results: int = 5) -> List[str]:
    return memory_manager.get_relevant_memories(query, n_results)
