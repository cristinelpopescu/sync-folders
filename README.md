# sync-folders
This script maintain a full, identical copy of source folder at replica folder.

## Run this script in the terminal console: python3 sync_folders.py Source/ Replica/ -i (sync period in seconds) -l (log file)
For example: python3 sync_folders.py Source/ Replica/ -i 5 -l sync_logs.log

For help: python3 sync_folders -h
usage: sync_folders_V2.py [-h] [-i INTERVAL] [-log LOG_FILE] source replica

Synchronize two folders periodically.

positional arguments:
  source                the path to the source folder
  replica               the path to the replica folder

options:
  -h, --help            show this help message and exit
  
  -i INTERVAL, --interval INTERVAL
                        the interval between synchronizations in seconds, must be an integer (default is 1 minute)
                        
  -log LOG_FILE, --log_file LOG_FILE
                        the path to the log file, and must be a string (otherwise a new log file called sync_logs.log will be created)
