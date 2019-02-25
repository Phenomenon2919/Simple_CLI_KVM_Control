import libvirt
import libxml2
import sys


def machine_create():
	path_xml = raw_input("XML definition Path: ")
	fp_xml = open(path_xml)
	
	machine_created = connection.defineXML(fp_xml.read())
	print "\n New Virtual machine created!"

def machine_start():
	list_of_machines = connection.listDefinedDomains()
	
	if len(list_of_machines) < 1:
		print "No VMs running. Create a machine first\n"
		return
	
	for i in range(len(list_of_machines)):
		print "\t", (i+1), "\t", list_of_machines[i].name
	
	option = input("Enter the index of the VM to start: ")
	
	if option < len(list_of_machines)+1 and option > 0:
		machine_name = connection.lookupByName(list_of_machines[option-1])
		print "The machine ", machine_name, "is starting"
		machine_name.create()


def machine_stop():
	
	list_of_machines = connection.listDefinedID()

	if len(list_of_machines) < 1:
		print "No VMs running. Create a machine first\n"
		return
	
	for i in range(len(list_of_machines)):
		print "\t", list_of_machines[i], "\t", connection.lookupByID(list_of_machines[i]).name()

	option = input("Enter the index of the VM to stop: ")

	# if option < len(list_of_machines)+1 and option > 0:
	machine_id = connection.lookupByID(option)
	print "The machine ", machine_id.name(), "is stopping"
	machine_id.shutdown()


connection = libvirt.open(None)
if connection is None:
	print "KVM cannot be opened"
	sys.exit(1)

list_of_machines = connection.listDefinedDomains()
list_of_machines_info = map(connection.lookupByName, list_of_machines)
list_of_machines_run = connection.listDomainsID()
list_of_machines_run_info = map(connection.lookupByID, list_of_machines_run)

if len(sys.argv) != 2:
	print "All VMs :"
	for machine in list_of_machines:
		print machine
	
	print "\nThe VMs running:"
	for machine in list_of_machines_run:
		print connection.lookupByID(machine).name()

	print "\nSyntax: ", sys.argv[0]," <action of virtual machine, say start,stop,create> \n>>>"

else:
	if sys.argv[2] == "start":
		machine_start()
	elif sys.argv[2] == "stop":
		machine_stop()
	elif sys.argv[2] == "create":
		machine_create()
