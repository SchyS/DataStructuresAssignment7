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

        #Check if the right child exists and if their priority is the smallest
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        #If the smallest is not the current index, we need to swap and continue. Otherwise the function will stop if smallest is not equal to index
        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.dara[smallest] = temp

        #Recursively heapify the current subtree
        self.heapify_down(smallest)

    def remove_min(self):
        if not self.data: #Handling empty list
            return None
        
        if len(self.data) == 1: #If there's only one item left then there is no need to reorder
            return self.data.pop()
        
        min_value = self.data[0] #Get the value to return
        self.data[0] = self.data.pop #Place last patient as root
        self.heapify_down(0) #Restore the heap order
        return min_value #Return the min value




# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

#next_up = heap.peek()
#print(next_up.name, next_up.urgency) # Taylor, 1 

served = heap.remove_min()
print(served.name) # Taylor
heap.print_heap()