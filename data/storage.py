import json
import os
from typing import Any, Dict, Optional


class DataStorage:
    """
    Storage class for managing data persistence.
    This implementation provides a simple file-based storage system
    that could be extended to support MongoDB, PostgreSQL, etc.
    """

    def __init__(self, storage_dir: str = "./data_store"):
        """
        Initialize the data storage with a directory.

        Args:
            storage_dir: Directory to store data files
        """
        # Connect to DB or file system
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)

    def _get_file_path(self, key: str) -> str:
        """
        Get the file path for a given key.

        Args:
            key: Unique identifier for the data

        Returns:
            String path to the file
        """
        # Sanitize the key to create a valid filename
        safe_key = "".join([c if c.isalnum() else "_" for c in key])
        return os.path.join(self.storage_dir, f"{safe_key}.json")

    def save(self, key: str, value: Any) -> None:
        """
        Save data to storage.

        Args:
            key: Unique identifier for the data
            value: Data to store (must be JSON serializable)
        """
        file_path = self._get_file_path(key)
        with open(file_path, 'w') as f:
            json.dump(value, f, indent=2)

    def load(self, key: str) -> Optional[Any]:
        """
        Load data from storage.

        Args:
            key: Unique identifier for the data

        Returns:
            The stored data or None if not found
        """
        file_path = self._get_file_path(key)
        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as f:
            return json.load(f)

    def delete(self, key: str) -> bool:
        """
        Delete data from storage.

        Args:
            key: Unique identifier for the data

        Returns:
            True if successful, False otherwise
        """
        file_path = self._get_file_path(key)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def list_keys(self) -> list:
        """
        List all keys in the storage.

        Returns:
            List of keys
        """
        if not os.path.exists(self.storage_dir):
            return []

        # Get all JSON files and extract the keys
        files = [f for f in os.listdir(
            self.storage_dir) if f.endswith('.json')]
        # Remove the .json extension to get original keys
        keys = [f[:-5] for f in files]
        return keys


# Example implementation for MongoDB (placeholder)
class MongoDBStorage:
    """
    MongoDB implementation of DataStorage.
    This is a placeholder that would need pymongo and actual implementation.
    """

    def __init__(self, connection_string: str, db_name: str, collection: str):
        """
        Initialize MongoDB storage.

        Args:
            connection_string: MongoDB connection string
            db_name: Database name
            collection: Collection name
        """
        # This would use pymongo in a real implementation
        self.connection_string = connection_string
        self.db_name = db_name
        self.collection = collection
        print(f"Connected to MongoDB: {db_name}.{collection}")

    def save(self, key: str, value: Any) -> None:
        """Placeholder for MongoDB document insertion"""
        print(f"Saving {key} to MongoDB")

    def load(self, key: str) -> Optional[Dict]:
        """Placeholder for MongoDB document retrieval"""
        print(f"Loading {key} from MongoDB")
        return None

    def delete(self, key: str) -> bool:
        """Placeholder for MongoDB document deletion"""
        print(f"Deleting {key} from MongoDB")
        return True

    def list_keys(self) -> list:
        """Placeholder for MongoDB key listing"""
        print("Listing all keys in MongoDB")
        return []
