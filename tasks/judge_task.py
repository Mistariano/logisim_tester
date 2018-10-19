from . import SimulateTask, Task


class JudgeTask(Task):
    def __init__(self, circ_path, judge_handler, logisim_path=None, java_path=None):
        self.circ_path = circ_path
        self.handler = judge_handler
        self.simulate_task = SimulateTask(circ_path=circ_path, logisim_path=logisim_path, java_path=java_path)

    def before_pushed(self, engine):
        engine.push_task(self.simulate_task)

    def run(self):
        simulate_result=self.simulate_task()

