import csv
from datetime import datetime
from os.path import exists


class CsvLayer:
    """
    Deals with writing to a file using python's csv.
    """
    def __init__(self, pid):
        """
        Creates file with 'pid' as a name
        :param pid: Process number to be used as filename
        """
        self.file = f'{pid}.csv'
        if not exists(self.file):
            with open(self.file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['CPU %', 'Memory', 'File Descriptors', 'Timestamp'])

    def write_to_file(self, data):
        """
        Takes data as dictionary input, adds a timestamp and writes it to a csv file
        :param data:
        :return:
        """
        with open(self.file, 'a') as f:
            writer = csv.writer(f)
            line = list(data.values())
            line.append(str(datetime.now()))
            writer.writerow(line)



