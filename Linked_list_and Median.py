# Program to create linked list and find median of it
class Node:
	
	def __init__(self, value):	
		self.data = value
		self.next = None
	
class LinkedList:

	def __init__(self):
		self.head = None

	# Create Node and make linked list
	def append(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next
		
	# Function to get the median of the linked list
	def print_median(self):
		slow_ptr = self.head
		fast_ptr = self.head
		pre_of_show = self.head
		count = 0
		
		while (fast_ptr != None and
			fast_ptr.next != None):
			fast_ptr = fast_ptr.next.next
			
			# Previous of slow_ptr
			pre_of_slow = slow_ptr
			slow_ptr = slow_ptr.next
		
		# If the below condition is truelinked list contain odd Node return middle element
		if (fast_ptr):
			print("Median is :", (slow_ptr.data))
		
		# Else linked list contain even element
		else:
			print("Median is :", (slow_ptr.data +
								pre_of_slow.data) / 2)
								
# Create object of a class
my_linked_list = LinkedList()

#  Construct list
my_linked_list.append(10)
my_linked_list.append(9)
my_linked_list.append(8)
my_linked_list.append(7)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)

# Print list and median
my_linked_list.print_list()
my_linked_list.print_median()
