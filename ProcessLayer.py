import platform
import psutil


class ProcessLayer:
    """
    Relies on psutil to get usage information about a given process
    """
    def __init__(self):
        """
        Checks platform type
        """
        if platform.system() == 'Linux':
            self.LINUX = True
        elif platform.system() == 'Windows':
            self.WINDOWS = True
        elif platform.system() == 'Darwin':
            self.MACOS = True

    def process_exists(self, pid: int) -> bool:
        """
        Check that process exists
        :param pid: process id number
        :return: True if process exists. False otherwise
        """
        if self.LINUX:
            try:
                psutil.Process(pid)
                return True
            except psutil.NoSuchProcess:
                print('Process not found')
                return False
        elif self.WINDOWS:
            print('Windows not tested yet')
        elif self.MACOS:
            print('Mac not tested yet')

    def get_process_info(self, pid: int, interval: int) -> dict:
        """
        Given a process id, return % cpu usage, private memory used, number of file descriptors
        :param interval: wait between calls
        :param pid: process id number
        :return: dictionary with results
        """
        if self.LINUX:
            try:
                p = psutil.Process(pid)
                file_descriptors = p.num_fds()
                memory = p.memory_info().rss
                cpu = p.cpu_percent(interval)
                return {'cpu': cpu, 'memory': memory, 'fd': file_descriptors}
            except psutil.NoSuchProcess:
                print(f'Process {pid} not found or closed')
        elif self.WINDOWS:
            print('Windows not tested yet')
        elif self.MACOS:
            print('Mac not tested yet')

