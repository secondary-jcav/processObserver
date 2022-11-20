

class InputLayer:
    """
    Takes and verifies keyboard input
    """
    def __init__(self):
        """
        Initial values for pid, monitoring duration and interval
        """
        self.pid = 0
        self.duration = 0
        self.interval = 5

    def get_pid(self) -> int:
        """
        Gets process id number from user
        :return: pid as int
        """
        self.pid = input('Enter process id number: ')
        while not self.pid.isnumeric():
            print('pid is not a valid number\n')
            self.pid = input('Enter process id number: ')
        return int(self.pid)

    def get_duration(self) -> int:
        """
        Gets monitoring duration from user
        :return: duration as int
        """
        self.duration = input('Overall duration in seconds of the monitoring: ')
        while not self.duration.isnumeric():
            print('input a valid duration\n')
            self.duration = input('Overall duration of the monitoring: ')
        return int(self.duration)

    def get_interval(self) -> int:
        """
        Gets interval between samples from user
        :return: Interval as int
        """
        confirm_default = input('Default interval 5 seconds. Y/N? ')
        while confirm_default.lower() not in ['y', 'n']:
            confirm_default = input('Default interval 5 seconds. Y/N? ')
        if confirm_default.lower() == 'y':
            return self.interval
        elif confirm_default.lower() == 'n':
            interval = input('Interval between checks: ')
            while not interval.isnumeric():
                print('interval is not valid\n')
                interval = input('Interval between checks: ')
            self.interval = int(interval)
            return self.interval


