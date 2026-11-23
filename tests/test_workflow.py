from orchestration.flowx.workflow import execute_step, run_workflow


def test_execute_step_returns_expected_structure() -> None:
    output = execute_step("init", {"index": 0})
    assert output["step"] == "init"
    assert output["status"] == "ok"
    assert output["payload"] == {"index": 0}


def test_run_workflow_defaults_and_custom_steps() -> None:
    default_results = run_workflow()
    assert len(default_results) == 3
    assert [item["step"] for item in default_results] == ["init", "validate", "finalize"]

    custom_results = run_workflow(["step_a", "step_b"])
    assert len(custom_results) == 2
    assert custom_results[0]["payload"] == {"index": 0}
    assert custom_results[1]["payload"] == {"index": 1}
  
