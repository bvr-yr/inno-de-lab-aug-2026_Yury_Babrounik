from task1_trainee_lms import Trainee


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


class Cohort:
    """Learning group container that manages a collection of trainees.

    Attributes:
        title: Name of the cohort.
        trainees: Collection of trainees enrolled in this learning group.

    """

    title: str
    trainees: list[Trainee]

    def __init__(
        self,
        title: str = "DevOps 2027",
        # https://docs.astral.sh/ruff/rules/mutable-argument-default/
        # not sure if needed as an arg for now
        # maybe just initialize in the body: self.trainees = []
        trainees: list[Trainee] | None = None,
    ) -> None:
        """Initialize a Cohort instance with explicit title and student list.

        Args:
            title: Name of the cohort.
            trainees: Collection of trainees to initialize with.
                Defaults to None (creates an empty list).

        """
        self.title = title
        self.trainees = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        """Add a trainee to the cohort."""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Simulate holding a lecture for all trainees.

        Increases the score of every trainee in the cohort by calling
        their individual lecture attendance method.
        """
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Get all trainees in the cohort who are passing.

        Returns:
            List of trainees whose passing status evaluates to True.

        """
        return [trainee for trainee in self.trainees if trainee.is_passing()]
