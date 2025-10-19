class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def print_heap(self):
        print("\nCurrent Patients:")
        for patient in self.data:
            print(f"-{patient.name} (Priority: {patient.urgency})")

    def heapify_up(self, index):
        while index > 0:
            #Get the parent index for the current child index
            parent_index = (index - 1)//2
            #Get the patients
            current_patient = self.data[index]
            parent_patient = self.data[parent_index]
            #Check if urgency value is lower than the parent. If so, we need to move it up the list. If not, we can stop.
            if current_patient.urgency < parent_patient.urgency:
                #Swap the patients position in the list
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                #Move up the heap
                index = parent_index
            else:
                break

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1) #Call heapify up starting at the end where the patient was just added

    def heapify_down(self, index):
        #Calculate the index of left and right child
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index #Assume current index is the smallest urgency

        # Check if the left child exists and has a smaller priority than current smallest
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        #Check if the right child exists and if their priority is the smallest
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        #If the smallest is not the current index, we need to swap and continue. Otherwise the function will stop if smallest is not equal to index
        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
        else:
            return

        #Recursively heapify the current subtree
        self.heapify_down(smallest)
        

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data: #Handling empty list
            return None
        
        if len(self.data) == 1: #If there's only one item left then there is no need to reorder
            return self.data.pop()
        
        min_value = self.data[0] #Get the value to return
        self.data[0] = self.data.pop() #Place last patient as root
        self.heapify_down(0) #Restore the heap order
        return min_value #Return the min value



#Test case
p1 = Patient("Riley", 2)
print(p1.name)       # Riley
print(p1.urgency)    # 2

# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency) # Taylor, 1 

served = heap.remove_min()
print(served.name) # Taylor
heap.print_heap()


"""
A binary tree is appropriate for the doctor reporting structure because each doctor has up to two different 
direct reports (left or right), and recursive traversal naturally mirrors hierarchical queries. 
Preorder, inorder, and postorder traverse the same structure with different visit timing to answer 
different questions. Preorder (root, left, right) is useful for generating a top-down reporting list 
in a way that preserves manager-before-report ordering which is ideal for provisioning 
accounts or sending cascading communications. Inorder (left, root, right) is most useful when the tree 
encodes an ordering relation (ex. BST by last name or ID); it returns a sorted sequence and is handy 
for audits or alphabetical rosters. Postorder (left, right, root) visits children before parents, 
which suits bottom-up operations like computing team aggregates (ex. headcount, budget) or 
deleting/restructuring subtrees safely. For real-time intake, a min-heap models the emergency queue 
effectively because it always exposes the most urgent patient at the root in O(1) time, while inserts 
and removals remain O(log n). This guarantees fast triage decisions under load and supports dynamic 
updates as new patients arrive. Heaps also maintain a compact array layout. 
In practice, duplicate urgencies could be handled by a stable tie-breaker 
(e.g., arrival timestamp).
"""