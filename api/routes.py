from fastapi import APIRouter
from pydantic import BaseModel
from orchestrator.toolchain import ToolChainOrchestrator  # Import the orchestrator

router = APIRouter()


class ToolchainRequest(BaseModel):
    request_data: dict  # Simple model for incoming request data


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/execute_toolchain")
async def execute_toolchain(request: ToolchainRequest):
    orchestrator = ToolChainOrchestrator()  # Instantiate the orchestrator

    # Plan the execution based on the incoming request data
    plan = orchestrator.plan_execution(request.request_data)

    if not plan:
        return {"error": "Could not plan execution for the given request."}, 400

    # Execute the planned tool sequence
    # A real context object would be more complex, possibly holding session state, user info, etc.
    context = {}
    execution_results = await orchestrator.execute_plan(plan, context)

    return {"results": execution_results}
