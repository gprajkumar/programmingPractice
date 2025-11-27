class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1: 
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            popped_node = temp
            pre.next = None
            self.tail = pre
            self.length -= 1
            return popped_node
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1    
        return popped_node.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        required_node = self.get(index)
        if required_node:
            required_node.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        
        self.length -= 1
        
        return temp
        
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def check_has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next   
            if fast == slow:
                return True
        return False        
            
    def find_kth_from_end(ll, k):       
        slow = fast = ll.head
    
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        return slow
    
    def remove_duplicates(self):
        current = self.head
        
        while current:
            runner = current
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                    self.length -=1
                else:
                    runner = runner.next
            current = current.next
            
    def remove_duplicates_set(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            
            else:
                values.add(current.value)
                previous = current
            current = current.next
    
    def binary_to_decimal(self):
        current = self.head
        decimal = 0
        while current:
            decimal = decimal * 2+ current.value
            
            current = current.next
            
        return decimal       
    def partition_list(self,value):
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        
        temp = self.head
        while temp:
            if temp.value < value:
                prev1.next = temp
                prev1 = temp
                
            else:
                prev2.next = temp
                prev2 = temp
            temp = temp.next
        
        prev1.next = dummy2.next
        prev2.next = None
        self.head = dummy1.next     
    
    def reverse_between(self,start_index,end_index):
        
        
        if self.length == 0 or self.length == 1:
            return None
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        
        for i in range(start_index):
            previous_node = previous_node.next
        
        current_node = previous_node.next
        
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
            
        self.head = dummy_node.next
    
def swap_pairs(self):
    dummy = Node(0)
    dummy.next = self.head
    previous = dummy
    first = self.head
    
    while first and first.next:
        second = first.next
        previous.next = second
        first.next = second.next
        second.next = first
        
        previous = first
        first = first.next
        
    self.head = dummy.next
        
    
my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.pop()
my_linked_list.print_list() 
