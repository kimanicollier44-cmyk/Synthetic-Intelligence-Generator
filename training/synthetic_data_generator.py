import random


class SyntheticDataGenerator:

    def generate(
        self,
        count=100
    ):

        dataset = []

        for i in range(count):

            record = {

                "id": i,

                "value":
                random.randint(
                    1,
                    100
                )
            }

            dataset.append(
                record
            )

        return dataset
      
