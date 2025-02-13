---
- hosts: all
  vars_files: ~/Auths/ansible_vault_pass
  become: yes
  become_method: sudo
  tasks:

  - name: 10. Reboot the servers
    reboot:
