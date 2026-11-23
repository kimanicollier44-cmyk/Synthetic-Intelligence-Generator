class PredictivePlanner:

    def forecast(
        self,
        objective,
        periods=12
    ):

        forecasts = []

        for period in range(
            1,
            periods + 1
        ):

            forecasts.append({

                "period": period,

                "objective":
                objective,

                "projection":
                f"forecast-{period}"
            })

        return forecasts

    def recommend(
        self,
        forecasts
    ):

        return forecasts[0]
