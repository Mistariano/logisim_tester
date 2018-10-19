class Engine:
    def __init__(self):
        self._task_queue = []

    def run(self, start_tasks=None):
        if start_tasks is not None:
            self._task_queue += list(start_tasks)
        while self._task_queue.__len__() > 0:
            self._run_next_task()

    def push_task(self, task):
        self._task_queue.append(task)

    def _run_next_task(self):
        cur_task = self._task_queue[0]
        cur_task.run()
        del self._task_queue[0]
