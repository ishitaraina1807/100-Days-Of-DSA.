class Nodes :

    def __init__(self,data):
        self.left = None
        self.right = None
        self.d = data
        
    def insert(self, data) :
    if self.d:
        if data < self.d:
            if self.left is None:
                self.left = Node(data)
            else :
                self.left.insert(data)
        elif data > self.d:
            if self.right is None:
                self.right = NOde(data)
            else:
                self.right.insert(data)
    else:
        self.d = data

        

