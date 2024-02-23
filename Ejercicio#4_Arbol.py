#Escriba un programa en Python para eliminar un nodo con la clave dada en un árbol de búsqueda binario (BST) dado.

# Definición: Nodo de árbol binario
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def delete_Node(root, key):
        # Si el nodo raíz no existe, simplemente devuélvelo
        if not root:
            return root
        
        # Busca el nodo en el subárbol izquierdo si el valor clave es menor que el valor de la raíz
        if root.val > key:
            root.left = TreeNode.delete_Node(root.left, key)
        
        # Busca el nodo en el subárbol derecho si el valor es mayor que el valor de la raíz
        elif root.val < key:
            root.right = TreeNode.delete_Node(root.right, key)
        
        # Elimina el nodo si el valor de la raíz es igual al valor clave
        else:
        # Si no hay hijos derechos, elimina el nodo y el nuevo nodo raíz será root.left
            if not root.right:
                return root.left
            
        # Si no hay hijos izquierdos, elimina el nodo y el nuevo nodo raíz será root.right
            if not root.left:
                return root.right
            
        # Si tanto los hijos izquierdos como los derechos existen en el nodo, reemplaza su valor con
        # el valor mínimo en el subárbol derecho. Ahora elimina ese nodo mínimo en el subárbol derecho
            temp_val = root.right
            mini_Val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_Val = temp_val.val
            
        # Elimina el nodo mínimo en el subárbol derecho
            root.right = TreeNode.delete_Node(root.right, root.val)
        
        return root
    
    def preOrder(node):
        if not node:
            return
        print(node.val)
        TreeNode.preOrder(node.left)
        TreeNode.preOrder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)

print("Nodo original: ")
TreeNode.preOrder(root)

result = TreeNode.delete_Node(root, 4)

print("Después de eliminar el nodo especificado: ")
TreeNode.preOrder(result)

