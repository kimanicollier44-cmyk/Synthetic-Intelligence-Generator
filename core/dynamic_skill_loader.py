import importlib


class DynamicSkillLoader:

    def load(
        self,
        module_name,
        class_name
    ):

        module = importlib.import_module(
            module_name
        )

        klass = getattr(
            module,
            class_name
        )

        return klass()

    def execute(
        self,
        module_name,
        class_name,
        method_name,
        *args,
        **kwargs
    ):

        skill = self.load(
            module_name,
            class_name
        )

        method = getattr(
            skill,
            method_name
        )

        return method(
            *args,
            **kwargs
        )
      
