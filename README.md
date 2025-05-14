# LightningMCP

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

LightningMCP is a lightning-fast Model Context Protocol (MCP) framework designed to provide superpowers to large language models. It serves as the foundation for building high-performance AI applications with advanced tool orchestration capabilities.

It builds upon FastMCP, offering significantly enhanced performance, intelligent toolchain orchestration, and enterprise-grade security features to meet the demands of enterprise-scale AI applications.

<div align="center">
  <img src="https://via.placeholder.com/800x400?text=LightningMCP+Architecture" alt="LightningMCP Architecture Diagram" width="800px">
</div>

## 🚀 Key Features

- **⚡ High-Speed Performance**
  - Rust-optimized core engine with microsecond-level response times
  - Vector-based intelligent caching system for reduced computation
  - Parallel tool execution for independent operations

- **🧠 Intelligent Toolchain Orchestration**
  - Automatic tool composition based on request analysis
  - Dynamic dependency resolution with optimized execution paths
  - Smart error recovery mechanisms with graceful fallbacks

- **🔐 Enterprise-Grade Security**
  - Role-Based Access Control (RBAC) for fine-grained permissions
  - End-to-end encryption for sensitive data
  - Comprehensive audit logging

- **👥 Real-time AI Collaboration**
  - Multi-agent coordination with shared context
  - Session state synchronization with conflict resolution
  - Capability discovery for seamless agent interactions

- **📚 Enhanced OpenAPI Integration**
  - Automatic documentation generation from tool definitions
  - API gateway with rate limiting and validation
  - Client library generation support

- **📊 Advanced Monitoring**
  - Real-time performance tracking with customizable metrics
  - Distributed tracing for full observability
  - Anomaly detection for proactive issue resolution

## 📋 Requirements

- Python 3.13+
- Redis (for caching)
- MongoDB (optional, for document storage)
- PostgreSQL (optional, for time-series data)

## 🔧 Installation

### Using `uv` (Recommended)

```bash
# Clone the repository
git clone https://github.com/lightningmcp/lightningmcp.git
cd lightningmcp

# Create and activate a virtual environment with uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### Using `pip`

```bash
# Clone the repository
git clone https://github.com/lightningmcp/lightningmcp.git
cd lightningmcp

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

### Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

### Interactive API Documentation

Once the application is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 💻 Usage Examples

### Define a Simple Tool

```python
from lightningmcp import app

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
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")
```

### Execute a Toolchain via API

```python
import requests
import json

# Define the request
payload = {
    "request_data": {
        "tool_name": "calculate",
        "parameters": {
            "a": 10,
            "operation": "+",
            "b": 5
        }
    }
}

# Send the request
response = requests.post(
    "http://localhost:8000/execute_toolchain",
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

# Print the result
print(response.json())
```

### Multi-tool Orchestration

The ToolChainOrchestrator automatically plans and executes complex tool sequences:

```python
from orchestrator.toolchain import ToolChainOrchestrator

# Create an orchestrator
orchestrator = ToolChainOrchestrator()

# Register tools
orchestrator.register_tool({
    "name": "fetch_data",
    "parameters": {"source": "str", "query": "str"}
})
orchestrator.register_tool({
    "name": "analyze_data",
    "parameters": {"data": "list", "metrics": "list"}
})

# Execute a request
request_data = {"tool_name": "analyze_weather", "parameters": {"location": "New York"}}
plan = orchestrator.plan_execution(request_data)
results = await orchestrator.execute_plan(plan, {})
```

## 🏗️ Project Architecture

LightningMCP is built on a modular architecture with six core subsystems:

```
┌─────────────────────────────────────────────────────────────────┐
│                  LightningMCP Framework                         │
├───────────────┬───────────────┬────────────────┬───────────────┤
│ Core Engine   │ Tool Chain    │ Security       │ AI            │
│ (Rust/Python) │ Orchestrator  │ Framework      │ Collaboration │
├───────────────┼───────────────┼────────────────┼───────────────┤
│ OpenAPI       │ Monitoring &  │ Data           │ Extension     │
│ Integration   │ Observability │ Processing     │ System        │
└───────────────┴───────────────┴────────────────┴───────────────┘
```

### Core Components

- **SparkEngine**: High-performance execution engine with parallel processing capabilities
- **ToolChainOrchestrator**: Intelligent planning and execution of tool sequences
- **PermissionSystem**: RBAC-based security framework for access control
- **MetricsCollector**: Comprehensive performance monitoring and tracing
- **DataStorage**: Flexible data persistence layer with multiple storage options

## 📁 Project Structure

```
lightningmcp/
├── main.py                  # Application entry point
├── core/                    # Core framework components
│   ├── engine.py            # SparkEngine implementation
│   ├── cache.py             # Intelligent caching system
│   └── security.py          # Authentication and authorization
├── orchestrator/            # Tool orchestration system
│   └── toolchain.py         # ToolChainOrchestrator implementation
├── api/                     # API endpoints
│   └── routes.py            # FastAPI route definitions
├── monitoring/              # Monitoring and observability
│   └── metrics.py           # Performance metrics collection
├── data/                    # Data storage and processing
│   └── storage.py           # Storage backend implementations
├── tests/                   # Test suite
│   └── test_core.py         # Core component tests
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Pinned dependencies
└── README.md                # Project documentation
```

## 🔄 API Reference

### Core Endpoints

| Endpoint             | Method | Description                         |
| -------------------- | ------ | ----------------------------------- |
| `/health`            | GET    | Health check endpoint               |
| `/execute_toolchain` | POST   | Execute a tool or sequence of tools |

### Request Format for `/execute_toolchain`

```json
{
  "request_data": {
    "tool_name": "string",
    "parameters": {
      "param1": "value1",
      "param2": "value2"
    }
  }
}
```

### Response Format

```json
{
  "results": [
    {
      "result": "Tool execution result"
    }
  ]
}
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test modules
pytest tests/test_core.py

# Run with coverage report
pytest --cov=lightningmcp
```

## 🛣️ Roadmap

- **Phase 1: Core Framework (Completed)**
  - Basic tool execution engine
  - Simple authentication
  - Initial API design

- **Phase 2: Advanced Features (In Progress)**
  - Tool chain orchestration
  - Advanced security features
  - OpenAPI integration

- **Phase 3: Enterprise Features (Planned)**
  - Multi-agent collaboration
  - Advanced monitoring
  - Enterprise deployment features

## 👥 Contributing

We welcome contributions to LightningMCP! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/lightningmcp/lightningmcp.git
cd lightningmcp

# Create a virtual environment
uv venv

# Install dev dependencies
uv pip install -e ".[dev]"

# Run pre-commit hooks
pre-commit install
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The FastMCP team for the initial concept and inspiration
- The Rust and Python communities for their excellent tools and libraries
- All contributors who have helped shape this project