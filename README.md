
1.) Copy ssh-key from c7-1 to all nodes:
ssh-copy-id spirrell@c7-2


2.) copy host file from c7-1 to all other hosts
    ansible all -i local_inventory.yml -u spirrell --sudo --ask-sudo-pass -m copy -a "src=/etc/hosts dest=/etc/hosts"

3.) Run install on c7-1:
	sudo -H pip install -r requirements.txt

4.)
Command to run install:

python install_mantl.py
