class GoalState:
    IN_PROGRESS = 0
    ACHIEVED = 1
    ARCHIVED = 2

    CHOICES = [
        (IN_PROGRESS, 'In progress'),
        (ACHIEVED, 'Done'),
        (ARCHIVED, 'Archived')
    ]