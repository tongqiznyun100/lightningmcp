from fastapi import FastAPI
from api.routes import router as api_router
from lightningmcp import app

app = FastAPI(title="LightningMCP")

app.include_router(api_router)

# Define a simple calculation tool


@app.tool()
def calculate(a: float, operation: str, b: float) -> float:
    """Perform basic math operations"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")

# Define a tool for text processing


@app.tool()
def process_text(text: str, operation: str) -> str:
    """Process text with various operations"""
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "capitalize":
        return text.capitalize()
    elif operation == "reverse":
        return text[::-1]
    else:
        raise ValueError(f"Unsupported operation: {operation}")

# Define a resource for calculation history


@app.resource("resource://calculation_history")
async def get_calculation_history(ctx):
    """Get calculation history"""
    # In a real app, this would retrieve from a database
    return ctx.get("history", [])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, reload=True)
