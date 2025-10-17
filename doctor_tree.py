class DoctorNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, doctor_name, new_value, side, current_node = None):
        #If tree is empty
        if self.root == None:
            print("Tree is empty. Cannot insert without root.")
            return
        #Start from root if not part of recursive call
        if current_node is None:
            current_node = self.root

        #Found the parent node
        if current_node.value == doctor_name:
            if side == "left" and current_node.left == None:
                current_node.left = DoctorNode(new_value)
                print(f"{new_value} has been added under {doctor_name} on the left.")
                return True
            elif side == "right" and current_node.right == None:
                current_node.right = DoctorNode(new_value)
                print(f"{new_value} has been added under {doctor_name} on the right")
                return True
            else:
                print(f"{doctor_name} already has a {side} subordinate")
                return True
        
        #Search the subtrees
        found_left = None
        found_right = None

        if current_node.left:
            found_left = self.insert(doctor_name, new_value, side, current_node.left)

        if current_node.right and not found_left:
            found_right = self.insert(doctor_name, new_value, side, current_node.right)

        #If parent node not found
        if not (found_left or found_right):
            #Avoid printing multiple messages by only printing if we are at root
            if current_node == self.root:
                print(f"Doctor {doctor_name} not found in tree")
            return False
        return True
    
    def printTree(self, node = None, level = 0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return
            
        indent = "    " * level
        print(f"{indent} - {node.value}")

        self.printTree(node.left, level + 1)
        self.printTree(node.right, level + 1)


# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")
tree.printTree()