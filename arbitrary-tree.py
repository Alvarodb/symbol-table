import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.sucessors = list()


class Tree:
    
    def __init__(self, root = None):
        self.root = root
    
    def insert(self, data, nodo = None):
       self.root = self._insert(self.root, nodo, data)
    
    def search_node(self, key):
        if self.root is None:
            return None
        return self._search_node(self.root, key)

    def _search_node(self, current, key):
        if current is None:
            return None
        if current.data is key:
            return current
        for temp in current.sucessors:
            x = self._search_node(temp, key)
            if x is not None:
                return x
    
    def level_order_traversal(self):
        if self.root is not None:
            queue = queue.Queue()
            queue.put(self.root)
            aux = self.root
            while not queue.empty():
                aux = queue.get()
                print(aux.data , end = " ")
                for x in aux.sucessors:
                    queue.put(x)            

#    def crear_de_archivo(self, nombre):
#        try:
#            handle = open(nombre, "r")
#        except IOError:
#            return None
#        self._crear_de_archivo(handle)
#        handle.close()
#    
#    def _crear_de_archivo(self, handle):
#        s = handle.readline()
#        self.insertar(s[0]) # Se inserta el primer caracter como raíz
#        for line in handle:
#            self.insertar(self.tempr_nodo(s[int(line[2])]), s[int(line[0])])

    def _insert(self, current, node, data):
        if current is None:
            return Node(data)
        if node is None:
            current.sucessors.append(Node(data))
        if current is node:
            current.sucessors.append(Node(data))
        else:
            for temp in current.sucessors:
                if temp is node:
                    temp.sucessors.append(Node(data))
                else:
                    self._insert(temp, node, data)
        return current

# Encontrar el orden de un árbol
def _tree_order(current):
    if current is None:
        return 0
    current_order = 0
    orden_sub = 0
    for aux in current.sucessors:
        current_order += 1
        orden_sub = tree_order(aux)
    if current_order > orden_sub:
        return current_order
    return orden_sub

def is_order(tree, n):
    return tree_order(tree.root) >= n