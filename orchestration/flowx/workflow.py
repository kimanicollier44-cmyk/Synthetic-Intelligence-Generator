from typing import Any, Dict, List


def execute_step(step_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a single workflow step and return a structured result."""
    return {
        "step": step_name,
        "status": "ok",
        "payload": payload,
    }


def run_workflow(steps: List[str] | None = None) -> List[Dict[str, Any]]:
    """Run workflow steps and collect each step's result without undefined names."""
    active_steps = steps if steps is not None else ["init", "validate", "finalize"]
    results: List[Dict[str, Any]] = []

    for index, step_name in enumerate(active_steps):
        step_result = execute_step(step_name=step_name, payload={"index": index})
        result = step_result
        results.append(result)

    return results


if __name__ == "__main__":
    workflow_output = run_workflow()
    print(workflow_output)
