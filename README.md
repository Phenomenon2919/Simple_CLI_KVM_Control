# Simple_CLI_KVM_Control
* All necessary packages for KVM can be installed using:
  - sudo apt install qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager
* Add the current user to *libvirt* group and *libvirt-qemu* group
  - sudo adduser $USER libvirt
  - sudo adduser $USER libvirt-qemu
* Edit MACHINE_PATH to set as path to the KVM installed in device
