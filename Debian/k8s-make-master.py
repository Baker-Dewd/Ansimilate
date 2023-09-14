---
- hosts: bastion
  become: yes
  tasks:

        - name: 5. Start kubernetes
          shell: "systemctl start kubelet" 

        - name: 10. initialize the cluster
          shell: "kubeadm init --pod-network-cidr=10.244.10.0/24"
          args:
                chdir: $HOME
                creates: cluster_initialized.txt

        - name: 20. create .kube directory
          file:
                path: /home/vagrant/kube/.kube
                state: directory
                mode: 0755
                owner: vagrant
                group: vagrant

        - name: 30. copies admin.conf to users kube config
          copy:
                src: /etc/kubernetes/admin.conf
                dest: /home/vagrant/kube/.kube/config
                remote_src: yes
                owner: vagrant
                group: vagrant

        - name: 40. install Pod network
          shell: |
               kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
               kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/k8s-manifests/kube-flannel-rbac.yml
          args:
                chdir: $HOME

        - name: 50. Get the token for joining the worker nodes
          shell: "kubeadm token create  --print-join-command"
          register: kubernetes_join_command

        - name: 60. Print the join command
          debug:
                msg: "{{ kubernetes_join_command.stdout }}"

        - name: 70. Copy join command to local file.
          local_action: copy content="{{ kubernetes_join_command.stdout_lines[0] }}" dest="/tmp/kubernetes_join_command" mode=0777
