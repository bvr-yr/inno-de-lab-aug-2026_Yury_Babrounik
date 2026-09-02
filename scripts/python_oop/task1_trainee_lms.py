class Trainee:
    """Trainee tracking entity for monitoring course progress.

    Attributes:
        name: First name of the trainee.
        surname: Last name of the trainee.
        passing_grade: Score required to successfully pass the course.
        score: Current performance tracking points of the trainee.

    """

    name: str
    surname: str
    passing_grade: int
    __score: int

    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10,
    ) -> None:
        """Initialize Trainee instance with tracking and grading params.

        Args:
            name: First name of the trainee.
            surname: Last name of the trainee.
            score: Initial tracking score points.
            passing_grade: Score required to pass.

        """
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        # setter is defined before __init__ is called, so use it for validations
        self.score = score

    @property
    def score(self) -> int:
        """Current performance tracking points of the trainee."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        if type(value) is not int:
            error_message = f"Expected value of type int, got {type(value)}"
            raise ValueError(error_message)

        if value < 0:
            error_message = "The score shouldn't be less than 0!"
            raise ValueError(error_message)

        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def is_passing(self) -> bool:
        """Check if trainee has enough points to pass the course.

        Returns:
            True if current score meets or exceeds the passing grade.
            False otherwise.

        """
        return self.score >= self.passing_grade
