#!/usr/bin/env python

"""This script is a wrapper for deploying Cisco Mantl."""



import getpass
import os

#This is a hack to get the ansible-playbooks to work.
home = '/home/' + getpass.getuser()

#As we continue to test and deploy, we'll need to delete the old Mantl directories.
try:
    print('Cleaning up old Mantl installation files....')
    os.system('rm -rf mantl')

except IOError: 
    print('No previous Mantl files found....')



os.system('git clone https://github.com/CiscoCloud/mantl.git')

os.system('./mantl/security-setup')

os.system('cp mantl/sample.yml mantl/mantl.yml')

os.system('cp security.yml ..')

os.system('ansible-playbook -i local_inventory.yml ' + home + '/mantl/playbooks/upgrade-packages.yml -K')


os.system('cd mantl && ansible-playbook -i ../local_inventory.yml -e @security.yml mantl.yml -K')


