from fastapi import FastAPI
from typing import Callable, Dict, Any, Optional, TypeVar, Union, List


class LightningMCP:
    """
    Main LightningMCP application class that provides the core functionality.
    """

    def __init__(self, title: str = "LightningMCP", description: str = None):
        """
        Initialize a new LightningMCP application.

        Args:
            title: The title of the application
            description: Optional description
        """
        self.app = FastAPI(title=title, description=description)
        self.tools = {}
        self.resources = {}

        # Register default routes
        from api.routes import router
        self.app.include_router(router)

    def tool(self, name: str = None, description: str = None):
        """
        Decorator to register a function as a tool.

        Args:
            name: Optional name for the tool (defaults to function name)
            description: Optional description for the tool

        Returns:
            Decorator function
        """
        def decorator(func):
            tool_name = name or func.__name__
            tool_desc = description or func.__doc__

            # Register the tool
            self.tools[tool_name] = {
                "name": tool_name,
                "description": tool_desc,
                "function": func
            }

            # Return the original function
            return func

        return decorator

    def resource(self, resource_id: str):
        """
        Decorator to register a function as a resource.

        Args:
            resource_id: Unique identifier for the resource

        Returns:
            Decorator function
        """
        def decorator(func):
            # Register the resource
            self.resources[resource_id] = {
                "id": resource_id,
                "function": func
            }

            # Return the original function
            return func

        return decorator

    def run(self, host: str = "0.0.0.0", port: int = 8000, **kwargs):
        """
        Run the LightningMCP application.

        Args:
            host: Host to bind to
            port: Port to bind to
            kwargs: Additional arguments to pass to uvicorn
        """
        import uvicorn
        uvicorn.run(self.app, host=host, port=port, **kwargs)

    def get_tool(self, name: str):
        """
        Get a registered tool by name.

        Args:
            name: The name of the tool

        Returns:
            The tool object or None if not found
        """
        return self.tools.get(name)

    def get_resource(self, resource_id: str):
        """
        Get a registered resource by ID.

        Args:
            resource_id: The ID of the resource

        Returns:
            The resource object or None if not found
        """
        return self.resources.get(resource_id)


# Create a default app instance for easy imports
app = LightningMCP()
