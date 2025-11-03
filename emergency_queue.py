class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent_name, employee_name, side):
        # If tree is empty, set as root
        if self.root is None:
            if parent_name is None:
                self.root = DoctorNode(employee_name)
                return True
            else:
                return False
        
        # Find the parent node
        parent_node = self._find_node(self.root, parent_name)
        
        if parent_node is None:
            return False
        
        # Insert on the specified side
        if side.lower() == 'left':
            if parent_node.left is None:
                parent_node.left = DoctorNode(employee_name)
                return True
            else:
                return False
        elif side.lower() == 'right':
            if parent_node.right is None:
                parent_node.right = DoctorNode(employee_name)
                return True
            else:
                return False
        else:
            return False
    
    def _find_node(self, current, name):
        if current is None:
            return None
        
        if current.name == name:
            return current
        
        # Search left subtree
        left_result = self._find_node(current.left, name)
        if left_result is not None:
            return left_result
        
        # Search right subtree
        return self._find_node(current.right, name)
    
    def preorder(self, node):
        # Root, Left, Right
        if node is None:
            return []
        
        result = [node.name]
        result.extend(self.preorder(node.left))
        result.extend(self.preorder(node.right))
        return result
    
    def inorder(self, node):
        # Left, Root, Right
        if node is None:
            return []
        
        result = []
        result.extend(self.inorder(node.left))
        result.append(node.name)
        result.extend(self.inorder(node.right))
        return result
    
    def postorder(self, node):
        # Left, Right, Root
        if node is None:
            return []
        
        result = []
        result.extend(self.postorder(node.left))
        result.extend(self.postorder(node.right))
        result.append(node.name)
        return result


class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency
    
    def __repr__(self):
        return f"Patient(name='{self.name}', urgency={self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []
    
    def insert(self, patient):
        self.data.append(patient)
        self._bubble_up(len(self.data) - 1)
    
    def _bubble_up(self, index):
        if index == 0:
            return
        
        parent_index = (index - 1) // 2
        
        if self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self._bubble_up(parent_index)
    
    def remove_min(self):
        if len(self.data) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.data) == 1:
            return self.data.pop()
        
        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self._bubble_down(0)
        
        return min_patient
    
    def _bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        
        if (left_child_index < len(self.data) and 
            self.data[left_child_index].urgency < self.data[smallest].urgency):
            smallest = left_child_index
        
        if (right_child_index < len(self.data) and 
            self.data[right_child_index].urgency < self.data[smallest].urgency):
            smallest = right_child_index
        
        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self._bubble_down(smallest)
    
    def peek(self):
        if len(self.data) == 0:
            raise IndexError("Heap is empty")
        return self.data[0]
    
    def print_heap(self):
        for patient in self.data:
            print(f"{patient.name}: Urgency {patient.urgency}")


# Test DoctorTree
if __name__ == "__main__":
    print("=== Testing DoctorTree ===")
    tree = DoctorTree()
    
    # Build hierarchy
    tree.insert(None, "Dr. Smith", "left")
    tree.insert("Dr. Smith", "Dr. Jones", "left")
    tree.insert("Dr. Smith", "Dr. Brown", "right")
    tree.insert("Dr. Jones", "Dr. Davis", "left")
    tree.insert("Dr. Jones", "Dr. Wilson", "right")
    tree.insert("Dr. Brown", "Dr. Taylor", "left")
    
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
    
    print("\n=== Testing MinHeap ===")
    heap = MinHeap()
    
    # Add patients
    heap.insert(Patient("Alice", 5))
    heap.insert(Patient("Bob", 2))
    heap.insert(Patient("Charlie", 8))
    heap.insert(Patient("Diana", 1))
    heap.insert(Patient("Eve", 4))
    
    print("\nHeap contents:")
    heap.print_heap()
    
    print("\nRemoving patients by urgency:")
    while len(heap.data) > 0:
        patient = heap.remove_min()
        print(f"Treating: {patient.name} (Urgency: {patient.urgency})")
