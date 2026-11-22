from agents.research_agent import ResearchAgent
from agents.planner_agent import PlannerAgent
from agents.coder_agent import CoderAgent
from agents.reviewer_agent import ReviewerAgent

class Router:

    def __init__(self, model):

        self.research = ResearchAgent(model)

        self.planner = PlannerAgent()

        self.coder = CoderAgent(model)

        self.reviewer = ReviewerAgent(model)

    def process(self, prompt):

        research = self.research.run(prompt)

        plan = self.planner.plan(
            prompt,
            research
        )

        solution = self.coder.generate(
            prompt,
            plan
        )

        final_output = self.reviewer.review(
            solution
        )

        return final_output
      
