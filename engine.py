from collections import Iterable
from tasks import Task


class Engine:
    def __init__(self):
        self._task_queue = []

    def run(self, start_tasks=None):
        if start_tasks is not None:
            if isinstance(start_tasks, Iterable):
                self._task_queue += list(start_tasks)
            elif isinstance(start_tasks, Task):
                self._task_queue.append(start_tasks)
            else:
                raise TypeError("The arg start_tasks isn't a task nor a list of tasks.")
        while self._task_queue.__len__() > 0:
            self._run_next_task()

    def push_task(self, task):
        task.before_pushed()
        self._task_queue.append(task)

    def _run_next_task(self):
        cur_task = self._task_queue[0]
        cur_task.run()
        del self._task_queue[0]
