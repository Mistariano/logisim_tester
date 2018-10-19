import subprocess
import settings
from logger import LoggerMgr


class SimulateTask:

    def __init__(self, circ_path, logisim_path=None, java_path=None):
        logisim_path = settings.LOGISIM_PATH if logisim_path is None else logisim_path
        java_path = settings.JAVA_PATH if java_path is None else java_path
        self.command = '{} -jar {} -tty halt,table {}'.format(java_path, logisim_path, circ_path)

    def run(self):
        cmd_output = subprocess.getoutput(self.command)
        logger = LoggerMgr.get_logger()
        logger.debug('Simulation result:\n=====Logisim=====\n{}\n================='.format(cmd_output))


if __name__ == '__main__':
    task = SimulateTask(circ_path='')
    task.run()
