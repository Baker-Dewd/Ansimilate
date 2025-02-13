---
- hosts: all
  become: yes
  tasks:

## Apt Update
        - name: 10. Run apt update -y
          ansible.builtin.apt:
                update_cache: yes

        - name: 20. Download Hashicorp keyring
          shell: "curl https://apt.releases.hashicorp.com/gpg | gpg --dearmor > hashicorp.gpg"

        - name: 30. Install Hashicorp keyring
          shell: "install -o root -g root -m 644 hashicorp.gpg /etc/apt/trusted.gpg.d/"

        - name: 40. Add terraform repo
          shell: "sudo apt-add-repository \"deb [arch=$(dpkg --print-architecture)] https://apt.releases.hashicorp.com $(lsb_release -cs) main\" -y"


## Apt Update
        - name: 50. Run apt update -y
          ansible.builtin.apt:
                update_cache: yes

        - name: 60. Install Terraform
          ansible.builtin.apt:
                name: terraform
                state: present
