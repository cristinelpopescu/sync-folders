import os
import shutil
import time
import logging
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Synchronize two folders periodically.')
parser.add_argument('source_folder', metavar='source', type=str, help='the path to the source folder')
parser.add_argument('replica_folder', metavar='replica', type=str, help='the path to the replica folder')
parser.add_argument('-i', '--interval', type=int, default=60, help='the interval between synchronizations in seconds')
parser.add_argument('-log', '--log_file', type=str, default='sync_logs.log', help='the path to the log file')
args = parser.parse_args() 

# Configure logging to write to the log file and console
logging.basicConfig(filename=args.log_file, filemode='w', format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# Function to synchronize two folders
def sync_folders(source_folder, replica_folder):
    # Remove all files and directories from the replica folder
    for item in os.listdir(replica_folder):
        item_path = os.path.join(replica_folder, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            logging.info('Removed directory: %s', item_path)
        else:
            os.remove(item_path)
            logging.info('Removed file: %s', item_path)
    
    # Copy all files and directories from the source folder to the replica folder
    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        replica_path = os.path.join(replica_folder, item)
        if os.path.isdir(source_path):
            shutil.copytree(source_path, replica_path)
            logging.info('Created directory: %s', replica_path)
        else:
            shutil.copy2(source_path, replica_path)
            logging.info('Copied file: %s', replica_path)

# Schedule synchronization to run at a specified interval
while True:
    sync_folders(args.source_folder, args.replica_folder)
    logging.info('Synchronization complete.')
    time.sleep(args.interval)
