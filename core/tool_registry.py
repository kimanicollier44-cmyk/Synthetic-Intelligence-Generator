class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(
        self,
        name,
        tool
    ):

        self.tools[name] = tool

    def execute(
        self,
        name,
        *args,
        **kwargs
    ):

        tool = self.tools.get(
            name
        )

        if not tool:
            raise ValueError(
                f"Tool not found: {name}"
            )

        return tool(
            *args,
            **kwargs
        )

    def list_tools(self):

        return list(
            self.tools.keys()
        )
      
