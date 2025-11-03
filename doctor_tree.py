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
