from django.utils import timezone
from tasks.models import Worker, TaskType, Task


def setUpTestData():
    """Creat test data that will be used for the entire test suite"""
    Worker.objects.create_superuser(
        username="superuser",
        password="superpassword"
    )
    # Create workers
    number_of_workers = 12
    for worker_num in range(number_of_workers):
        Worker.objects.create(
            first_name=f"Worker {worker_num}",
            last_name=f"Surname {worker_num}",
            username=f"worker{worker_num}"
        )
    # Create task types
    urgent = TaskType.objects.create(name="Urgent")
    high = TaskType.objects.create(name="High")

    # Create tasks for each worker with different statuses
    now = timezone.now()
    for worker_num in range(number_of_workers):
        worker = Worker.objects.get(username=f"worker{worker_num}")

        Task.objects.create(
            name=f"Task 1 for Worker {worker_num}",
            description="Task 1 description",
            deadline=now + timezone.timedelta(days=1),
            completed=False,
            priority="Urgent",
            type=urgent,
            created_by=worker,
            updated_by=worker,
        )
        Task.objects.create(
            name=f"Task 2 for Worker {worker_num}",
            description="Task 2 description",
            deadline=now + timezone.timedelta(days=2),
            completed=True,
            priority="High",
            type=high,
            created_by=worker,
            updated_by=worker,
        )
        Task.objects.create(
            name=f"Task 3 for Worker {worker_num}",
            description="Task 3 description",
            deadline=now - timezone.timedelta(days=1),
            completed=False,
            priority="Middle",
            type=high,
            created_by=worker,
            updated_by=worker,
        )

    user = Worker.objects.create(
        first_name="John",
        last_name="Doe",
        username="johndoe",
        password="johndoe12345"
    )

    Task.objects.create(
        name="Task 1 for John",
        description="Task 1 description",
        deadline="2023-07-31T12:00:00Z",
        completed=True,
        priority="Urgent",
        type=urgent,
        created_by=user,
        updated_by=user,
    )

    Task.objects.create(
        name="Task 2 for John",
        description="Task 2 description",
        deadline="2023-08-15T12:00:00Z",
        completed=False,
        priority="High",
        type=high,
        created_by=user,
        updated_by=user,
    )
