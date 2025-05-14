import pytest
import asyncio
from core.engine import SparkEngine, can_execute_parallel


@pytest.fixture
def spark_engine():
    """Create a SparkEngine instance for testing"""
    return SparkEngine()


def test_can_execute_parallel():
    """Test the can_execute_parallel function"""
    # Should return False for 'sensitive_tool'
    assert not can_execute_parallel("sensitive_tool", [])

    # Should return True for any other tool
    assert can_execute_parallel("regular_tool", [])


@pytest.mark.asyncio
async def test_execute_tool_parallel(spark_engine):
    """Test execute_tool with a parallel-safe tool"""
    # Create a mock context
    context = {"active_tools": []}

    # Execute a tool that should run in parallel
    result = await spark_engine.execute_tool("regular_tool", {"param": "value"}, context)

    # Check the result (based on our implementation which returns a static result)
    assert "result" in result
    assert result["result"] == "parallel_executed"


@pytest.mark.asyncio
async def test_execute_tool_sequential(spark_engine):
    """Test execute_tool with a non-parallel tool"""
    # Create a mock context
    context = {"active_tools": []}

    # Execute a tool that should NOT run in parallel
    result = await spark_engine.execute_tool("sensitive_tool", {"param": "value"}, context)

    # Check the result (based on our implementation which returns a static result)
    assert "result" in result
    assert result["result"] == "sequential_executed"


@pytest.mark.asyncio
async def test_cache_behavior(spark_engine, monkeypatch):
    """Test that results are cached and cache hits are returned"""
    # Mock the parallel_executor to track calls
    calls = []

    async def mock_submit(self, tool_name, params, context):
        calls.append((tool_name, params))
        return {"result": "executed_once"}

    # Apply the mock
    monkeypatch.setattr(
        spark_engine.parallel_executor.__class__,
        "submit",
        mock_submit
    )

    # Define test parameters
    tool_name = "cacheable_tool"
    params = {"param": "value"}
    context = {"active_tools": []}

    # First call should execute and cache
    result1 = await spark_engine.execute_tool(tool_name, params, context)
    assert result1["result"] == "executed_once"
    assert len(calls) == 1

    # Second call should hit cache
    result2 = await spark_engine.execute_tool(tool_name, params, context)
    assert result2["result"] == "executed_once"

    # Should still have only one call (cache hit)
    assert len(calls) == 1
