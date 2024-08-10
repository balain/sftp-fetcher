# SftpFetcher

Download files via SFTP.

Similar to batch file processing, but works with private key authentication.

## Quick Start

Clone the repo, install dependencies, populate the .env file, and run the script:

```bash
$ git clone https://github.com/balain/sftp-fetcher.git
$ vi .env
$ python fetcher.py
```

## Getting Started

### Prerequisites

The things you need before installing the software:

* Python3
* pysftp: SFTP client library
* python-dotenv: Manages the .env file
* simple_chalk: Terminal output styling

### Installation

To run this program, clone the repo and install pre-requisites:

```bash
$ git clone https://github.com/balain/sftp-fetcher.git
$ cd sftp-fetcher
$ pip install -r requirements.txt
```

### Configuration

Create and populate the .env file in the root folder:

#### Fields

- HOST: Remote server to connect to
- USERNAME: SFTP user
- PRIVKEY: SFTP key
- PRIVKEYPASS: Password for SFTP key
- BASEDIR: Remote working directory
- LOCALDIR: Local working directory
- FILELIST: Text file with list of files to fetch

#### Example

```ini
HOST=www.somewhere.com
USERNAME=myusername
PRIVKEY=~/.ssh/mysomewherekey
PRIVKEYPASS=mysupersecretpassword
BASEDIR=/remote/working/directory/
LOCALDIR=/local/working/directory/
FILELIST=/path/to/filelist.txt
```

## Options

There are no command line options. All configuration is handled via the .env file.

## Output

Prints the files as they are downloaded:

```bash
About to fetch 31 files...
Fetching 1 of 31: first.txt
Fetching 2 of 31: second.txt
Fetching 3 of 31: third.txt
...
```

## Features

## Implemented
- [x] Connect and download with password-protected private key

## TODOs

- [ ] Track total execution time
- [ ] Calculate average transfer speed
