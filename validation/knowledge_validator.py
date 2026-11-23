class KnowledgeValidator:

    def validate(
        self,
        facts
    ):

        valid = []
        invalid = []

        for fact in facts:

            if len(
                str(fact)
            ) > 5:

                valid.append(
                    fact
                )

            else:

                invalid.append(
                    fact
                )

        return {

            "valid": valid,

            "invalid": invalid
        }
      
