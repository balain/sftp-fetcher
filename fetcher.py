import os
import pysftp
from dotenv import load_dotenv
from simple_chalk import chalk, green, red, yellow

load_dotenv()

filesToFetch = [] # List of remote files to download

# Convert the list of files to download into a local list
with open(os.getenv('FILELIST'),'r') as f:
    for line in f:
        filesToFetch.append(line.strip())

print(green.dim(f'About to fetch {len(filesToFetch)} files...'))

fileCounter = 0    # Reset the download counter

# TODO: Handle if LOCALDIR isn't set...
os.chdir(os.getenv('LOCALDIR'))    # Move to the local directory

# Connect to the remote server
# TODO: Handle if private_key isn't used/set
with pysftp.Connection(os.getenv('HOST'), username=os.getenv('USERNAME'), private_key=os.getenv('PRIVKEY'), private_key_pass=os.getenv('PRIVKEYPASS')) as sftp:
    with sftp.cd(os.getenv('BASEDIR')): # Move to the base remote directory
        for file in filesToFetch:  # Cycle through all the files to download
            fileCounter += 1       # Increment the download counter
            print(green.dim(f'Fetching {fileCounter} of {len(filesToFetch)}: {file}'))
            sftp.get(file)         # Download the file
