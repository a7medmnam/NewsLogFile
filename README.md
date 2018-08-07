## Requirements

* [Vagrant](https://www.vagrantup.com/)
* [Virtual Machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Python3](https://www.python.org/downloads/)

unzip DB.zip
Setting up VM configuration

Download and unzip [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

Start the virtual machine
open git or your teminal
Once inside the vagrant subdirectory, run the command:
vagrant up

Upon installation, run this command to log you inside the VM.
vagrant ssh

you have to be sure that your database file name is newsdata.sql
run ----> psql -f setup.sql
run ----> python final_report.py
And the output will be .txt file named with the curent time and date

## Questions 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
