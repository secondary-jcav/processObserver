**Objective**:
Console app that gathers 3 metrics for a given running process. Process ID is needed to start.
- % of CPU used
- memory used
- number of file descriptors

User inputs:
- Process ID
- Duration of monitoring
- Sampling interval in seconds (5 seconds as default)

**Requirements**

run pip install -r requirements.txt

**Execution**

From project folder, run App.py. Example: 
julio@julio-GE70-2QE:~/PycharmProjects/processObserver$ python3 App.py

Output is  saved in a CSV. App has only been tested in a linux environment.

**Testing**

Smoke Testing test cases
- TC that verifies app accepts good input from the user. 
- TC that verifies app rejects bad input (e.g. strings) from the user.
- TC that verifies app produces a csv file with pid as title, if it does not exist.
- TC that verifies that an existing csv file is amended with new rows of data.
- TC that verifies app prints final results.

Acceptance Testing TCs

- For an existing process, check that app's default interval is 5 seconds and ends at the correct time.
- For an existing process, check that the interval can be changed to follow the user's input.
- Check that the averages printed out correspond to the values in the csv file.
- In linux, run 'top -p (pid)' and check result is coherent with averages printed by the app.
- Give a non-existing process to the app and check this is detected.
- For an existing process, close it during monitoring and check this is detected.

**Automation**

The tests can be easily divided into keywords that are repeated throughout different scenarios, 
such as:

Given good input from the user

Given bad input from the user

Read from csv

These keywords can be easily automated with frameworks such as Behave or Robot Framework. 

Because we can reuse the keywords and build different tests, the whole test plan can be automated with a lot less work.