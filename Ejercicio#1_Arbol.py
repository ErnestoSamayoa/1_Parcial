##Escriba un programa de Python para crear un árbol de busqueda binarai
#equilibrada utilizando elementos de una matriz (dados) donde los elementos
#de la matriz se ordena en orden ascendente.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sorted_array_to_bst(nums):
        if not nums:
            return None
        
        mid_val = len(nums) // 2
        node = TreeNode(nums[mid_val])
        node.left = TreeNode.sorted_array_to_bst(nums[:mid_val])
        node.right = TreeNode.sorted_array_to_bst(nums[mid_val + 1:])
        return node

    def preOrder(node):
        if not node:
            return
        print(node.val)
        TreeNode.preOrder(node.left)
        TreeNode.preOrder(node.right)

result = TreeNode.sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
TreeNode.preOrder(result)