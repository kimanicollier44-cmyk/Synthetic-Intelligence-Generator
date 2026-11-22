class ToolExecutionSandbox:

    SAFE_TOOLS = {

        "search",
        "calculator",
        "translator",
        "summarizer"
    }

    def execute(
        self,
        tool_name,
        function,
        *args,
        **kwargs
    ):

        if (
            tool_name
            not in self.SAFE_TOOLS
        ):
            raise PermissionError(
                f"Blocked: {tool_name}"
            )

        return function(
            *args,
            **kwargs
        )
      
