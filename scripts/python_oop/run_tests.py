from task1_trainee_lms import Trainee
from task2_extensions import AuditTrainee, Cohort, HardworkingTrainee


def run_tests_task1() -> None:
    """Run tests for task 1."""

    def print_trainee(trainee: Trainee) -> None:
        print(f"Score: {trainee.score}, Course passed: {trainee.is_passing()}")

    trainee = Trainee(name="Ben", surname="Evans", score=9, passing_grade=10)

    print("=== TRAINEE PERFORMANCE CHECK ===")

    trainee.do_homework()
    print_trainee(trainee)

    trainee.miss_lecture()
    print_trainee(trainee)

    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Error: {e}")


def run_tests_task2() -> None:
    """Run tests for task 2."""
    std_trainee = Trainee("Cole", "Deschanel", score=8, passing_grade=10)
    hard_trainee = HardworkingTrainee("Gregory", "Richards", score=8, passing_grade=10)
    audit_trainee = AuditTrainee("Annie", "Douglas", score=0, passing_grade=10)

    cohort = Cohort("Python Advanced")
    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)

    cohort.conduct_lecture()
    hard_trainee.do_homework()

    passing_students = cohort.get_passing_students()

    print(f"=== COHORT {cohort.title!r} PERFORMANCE ===")
    for student in cohort.trainees:
        print(
            f"{student.name} {student.surname} | Score: {student.score} | "
            f"Passes: {student.is_passing()}",
        )

    print("\nEnrolled in the next module:")
    for student in passing_students:
        print(f"- {student.name} {student.surname}")


if __name__ == "__main__":
    run_tests_task1()
    print("\n")
    run_tests_task2()
