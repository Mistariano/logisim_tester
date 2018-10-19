import subprocess
import settings
from logger import LoggerMgr
from .task import Task


class SimulateTask(Task):

    def __init__(self, circ_path, logisim_path=None, java_path=None):
        logisim_path = settings.LOGISIM_PATH if logisim_path is None else logisim_path
        java_path = settings.JAVA_PATH if java_path is None else java_path
        self.command = '{} -jar {} -tty halt,table {}'.format(java_path, logisim_path, circ_path)
        self.result = None
        self.raw_output = None

    def run(self):
        cmd_output = subprocess.getoutput(self.command)
        logger = LoggerMgr.get_logger()
        logger.debug('Simulation result:\n=====Logisim=====\n{}\n================='.format(cmd_output))
        self.raw_output = cmd_output
        output_lines = [line.strip() for line in cmd_output.split('\n')]
        output_lines = [line if set(line).issubset('01 ') or 'halted' in line else '' for line in output_lines]
        output_lines = list(filter(lambda x: len(x), output_lines))
        logger.debug('and cleaned result is:{}'.format(output_lines))
        self.result = output_lines
