class AutonomousDebugger:

    def analyze(
        self,
        error_log
    ):

        issues = []

        for line in error_log:

            if "Exception" in line:

                issues.append(line)

        return issues

    def suggest_fix(
        self,
        issue
    ):

        return {

            "issue": issue,

            "recommendation":
            "Investigate stack trace"
        }
      
