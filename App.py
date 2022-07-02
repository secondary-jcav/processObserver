import statistics
import time
from statistics import mean
from ProcessLayer import ProcessLayer
from CsvLayer import CsvLayer
from InputLayer import InputLayer
"""
Console app that gathers cpu usage, memory usage and file descriptors open for a given process id.
Results are saved in a csv along with a timestamp. Averages for each of the three metrics are printed at the end
"""


def main():
    pl = ProcessLayer()
    il = InputLayer()
    # Get pid, duration and interval from keyboard
    pid = il.get_pid()
    if not (pl.process_exists(pid)):
        # process not found, end execution
        exit()
    duration = il.get_duration()
    interval = il.get_interval()
    # initialize results lists so averages can be calculated later
    dict_avg = {'cpu': [], 'memory': [], 'fd': []}
    logger = CsvLayer(pid)
    end_time = time.time() + duration
    while time.time() < end_time:
        results = pl.get_process_info(int(pid), int(interval))
        if results is None:
            # process not there anymore, stop looping and go to final results
            break
        # write results to csv
        logger.write_to_file(results)
        dict_avg['cpu'].append(results['cpu'])
        dict_avg['memory'].append(results['memory'])
        dict_avg['fd'].append(results['fd'])
        print(results)
    try:
        # print out averages for the 3 metrics
        print(f'CPU % Average: {mean(dict_avg["cpu"])}\n')
        print(f'Memory Average: {mean(dict_avg["memory"])}\n')
        print(f'File Descriptors Average: {mean(dict_avg["fd"])}\n')
    except statistics.StatisticsError:
        print('No results to show')


if __name__ == '__main__':
    main()
