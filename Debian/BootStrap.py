---
- hosts: all
  become: yes
  tasks:

## name:  numbers aid in diagnosis and support. See:
## https://github.com/kungfootek/ansible-page-numbers

## Update all the things.
    - name: 10. Update apt-get repo and cache
      apt:
          update_cache: yes
          force_apt_get: yes
          cache_valid_time: 3600

    - name: 20. apt upgrade -y
      shell: "apt -y upgrade"

#    - name: 22. Install fasttrack-Repo
# https://wiki.debian.org/VirtualBox#Debian_12_.22Bookworm.22

####################################################################
## Install miscellaneous packages that should always be present.  ##
## It's much more efficient to diagnose an issue with utilities   ##
## already installed rather than to try to install utilities on   ##
## a broken or compromised instance.                              ##
####################################################################
    
    - name: 30. Install Essentials [ {{ Packagez | list | join(", ")}} ]
      package:
            name: "{{ Packagez }}"
      vars:
            Packagez:
## Archivers
            - zip
            - unzip
            - bzip2
## Data Transfer
            - rsync
            - wget
            - git
            - curl
## Monitoring
            - iotop
            - iftop
            - htop
            - sysstat
            - tcpdump
            - iptraf-ng
            - lnav
            - telnet
            - lsof
            - strace
            - traceroute
## Must Have Utilities
            - mc
            - bc
            - tmux
            - screen
            - vim
            - gawk
            - sed
            - gh
## Languages
#       - go
            - pip
            - perl
            - php
## Pyenv Deps
            - build-essential
            - libssl-dev
            - zlib1g-dev
            - libbz2-dev 
            - libreadline-dev 
            - libsqlite3-dev
            - libncursesw5-dev 
            - xz-utils 
            - tk-dev 
            - libxml2-dev 
            - libxmlsec1-dev 
            - libffi-dev 
            - liblzma-dev
            - llvm
## Remote storage solutions
## s3, ceph, etc.            
            - nfs-kernel-server
## Orchestration
            - ansible
            - awscli
## Terraform, Docker, Vagrant  and K8s Deps and apps.
            - vagrant-libvirt 
            - libvirt-daemon-system
            - software-properties-common
            - gnupg2
            - apt-transport-https
            - ca-certificates
#            - virtualbox
#            - virtualbox-ext-pack
            - vagrant
# Set Container environment
    - name: 40. Clone Cli-Foo Environment files
      git:
            repo: https://github.com/kungfootek/Cli-Foo.git
            dest: /tmp/envvars

    - name: 50. Distribute Environment files
      copy:
            src: "{{ item.src }}"
            dest: "{{ item.dest }}"
            remote_src: true
      loop:
            - { src: '/tmp/envvars/DotFiles/vimrc', dest: '/etc/skel/.vimrc' }
            - { src: '/tmp/envvars/DotFiles/bashrc', dest: '/etc/skel/.bashrc' }
            - { src: '/tmp/envvars/DotFiles/tmux.conf', dest: '/etc/skel/.tmux.conf' }
            - { src: '/tmp/envvars/DotFiles/gitconfig', dest: '/etc/skel/.gitconfig' }
            - { src: '/tmp/envvars/DotFiles/tmux.conf', dest: '/root/.tmux.conf' }
            - { src: '/tmp/envvars/DotFiles/gitconfig', dest: '/root/.gitconfig' }
            - { src: '/tmp/envvars/DotFiles/bashrc', dest: '/root/.bashrc' }
            - { src: '/tmp/envvars/DotFiles/vimrc', dest: '/root/.vimrc' }
            - { src: '/tmp/envvars/DotFiles/vimrc', dest: '/etc/vimrc' }
            - { src: '/tmp/envvars/DotFiles/sysstat', dest: '/etc/cron.d/sysstat' }

## Need to copy entire ~/Bin folder over for root and vagrant


######################################################################
## Notes:                                                           ##
## - Playbook saved with .py to leverage syntax highlighting in Vim.##
## -
######################################################################
## TODO : 
# Clone Cli-Foo and Install
# Install Pyenv and make 3. the global default
# For the Vagrant version, pull Vagrant user stuff from the PB and 
# Make it callable independently. 
# Add a .bashrc.d in home folders to include things like pyenv without 
# having to parse the existing .bashrc so much. 

## Fix prompt dependencies

#  pyenv install 3.11.4
#  pyenv global 3.11.4
#  pip install psutil



# EOF
