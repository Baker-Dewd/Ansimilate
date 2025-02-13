
---
- hosts: all
  vars:
    - http_conf: bastion
    - http_port: 80
    - http_host: bastion

  become: yes
  tasks:

    - name: 10. Install latest version of Apache
      apt: name=apache2 update_cache=yes state=latest
 
    - name: 20. Create document root for domain configured in host variable
      file:
        path: "/var/www/{{ http_host }}"
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'
 
    - name: 30. Copy your index file
      template:
        src: "files/index-template.html"
        dest: "/var/www/{{ http_host }}/index.html"
 
    - name: 40. Set up virtuahHost
      template:
        src: "files/apache-template.conf"
        dest: "/etc/apache2/sites-available/{{ http_conf }}.conf"
 
    - name: 50. Enable site
      command: a2ensite {{ http_conf }}
      notify: 70. restart-apache
 
    - name: 60. "UFW firewall allow HTTP on port {{ http_port }}"
      ufw:
        rule: allow
        port: "{{ http_port }}"
        proto: tcp


  handlers:
    - name: 70. restart-apache
      ansible.builtin.service:
        name: apache2
        state: restarted

