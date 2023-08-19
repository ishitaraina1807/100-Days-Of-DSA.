class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData) :
        
        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None :
            print("previous Node doesnt exist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printList(self) :
        temp = self.head
        while temp :
            print(temp.data,end = ' ')
            temp = temp.next

    def fetchNode (self, data):
        temp = self.head
        count =1
        while temp:
            if temp.data != data:
                temp = temp.next
                count+=1
            else:
                print(f"data is at {count} node")
                break

    def deleteNode (self, key):
        temp = self.head
        if (temp.data == key):
            self.head= temp.next
            temp = None
            return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            if(temp == None):
                return

            prev.next = temp.next
            temp = None

    def findMiddle (self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def reverse(self):
         

'''lst.append(6)
lst.push(7)
lst.push(5)
lst.append(12)
lst.insertAfter(third , 8)
print("liked list has follows")
lst.printList()

lst = LinkedList()
ist= lst.head
ist= Node(1)
second = Node(2)
third = Node(3)
four = Node(4)

ist.next = second
second.next = third
third.next = four'''

lst = LinkedList()
lst.append(6)
lst.push(7)
lst.push(5)
lst.append(12)
lst.insertAfter( lst.head.next.next , 8)
print("liked list has follows")
lst.printList()
lst.deleteNode(7)
print()
lst.printList()
