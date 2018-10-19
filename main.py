from tasks import SimulateTask
from engine import Engine

if __name__ == '__main__':
    circ_path=input()
    task = SimulateTask(circ_path=circ_path)
    engine = Engine()
    engine.run([task])
