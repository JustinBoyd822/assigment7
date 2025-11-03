class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent_name, employee_name, side):
        if self.root is None:
            if parent_name is None:
                self.root = DoctorNode(employee_name)
                return True
            else:
                return False
        
        parent_node = self._find_node(self.root, parent_name)
        
        if parent_node is None:
            return False
        
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
        
        left_result = self._find_node(current.left, name)
        if left_result is not None:
            return left_result
        
        return self._find_node(current.right, name)
    
    def preorder(self, node):
        if node is None:
            return []
        
        result = [node.name]
        result.extend(self.preorder(node.left))
        result.extend(self.preorder(node.right))
        return result
    
    def inorder(self, node):
        if node is None:
            return []
        
        result = []
        result.extend(self.inorder(node.left))
        result.append(node.name)
        result.extend(self.inorder(node.right))
        return result
    
    def postorder(self, node):
        if node is None:
            return []
        
        result = []
        result.extend(self.postorder(node.left))
        result.extend(self.postorder(node.right))
        result.append(node.name)
        return result


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    
    tree.insert(None, "Dr. Smith", "left")
    tree.insert("Dr. Smith", "Dr. Jones", "left")
    tree.insert("Dr. Smith", "Dr. Brown", "right")
    tree.insert("Dr. Jones", "Dr. Davis", "left")
    tree.insert("Dr. Jones", "Dr. Wilson", "right")

    
    
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))



#1. Why is a tree appropriate for the doctor structure?

#A tree structure is ideal for representing a doctor reporting hierarchy because it naturally models organizational relationships. Each doctor (node) can have direct reports (children), creating a clear chain of command. The binary tree structure enforces a maximum of two direct reports per doctor, which reflects realistic management spans. Trees enable efficient traversal to find specific doctors, determine reporting paths, and visualize the entire organizational structure. The hierarchical nature prevents circular reporting relationships and maintains a single root authority figure, which mirrors real hospital management systems.

#2. When might a software engineer use preorder, inorder, or postorder traversals?

#Preorder traversal (Root-Left-Right) is useful for creating copies of tree structures or exporting hierarchies where parent information must come before children, such as serializing organizational charts. Inorder traversal (Left-Root-Right) produces sorted output in binary search trees and is valuable for generating alphabetically ordered reports. Postorder traversal (Left-Right-Root) is essential when child nodes must be processed before parents, such as calculating department budgets (sum employee salaries before manager totals), deleting tree structures safely (remove children before parents), or evaluating mathematical expression trees where operands must be processed before operators.

#3. How do heaps help simulate real-time systems like emergency intake?

#Heaps provide O(log n) insertion and removal operations, making them efficient for dynamic priority management in real-time systems. In emergency rooms, patient urgency constantly changes as new patients arrive. A min-heap automatically maintains the most critical patient at the root, enabling instant access to who needs treatment next. Unlike sorting the entire patient list after each arrival (O(n log n)), heaps only reorder the affected branch. This efficiency is crucial when seconds matter. The heap structure ensures fairness—patients are treated by medical urgency rather than arrival order, simulating actual triage protocols where life-threatening conditions receive immediate attention regardless of check-in time.
