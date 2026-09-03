from trainee import Trainee


class HardworkingTrainee(Trainee):
    """Trainee who earns double points for homework completion."""

    def do_homework(self) -> None:
        """Increases score by 2."""
        self.score += 2


class AuditTrainee(Trainee):
    """Trainee who always passes the course regardless of score."""

    def is_passing(self) -> bool:
        """Return True regardless of trainee's score."""
        return True
