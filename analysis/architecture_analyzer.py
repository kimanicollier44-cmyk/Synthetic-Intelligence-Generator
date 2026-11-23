class ArchitectureAnalyzer:

    def analyze(
        self,
        modules,
        dependencies
    ):

        return {

            "module_count":
            len(modules),

            "dependency_count":
            len(dependencies),

            "complexity":
            len(dependencies) /
            max(len(modules), 1)
        }

    def find_orphans(
        self,
        modules,
        dependencies
    ):

        connected = set()

        for dep in dependencies:

            connected.add(
                dep["source"]
            )

            connected.add(
                dep["target"]
            )

        return [

            module

            for module in modules

            if module not in connected
        ]
      
