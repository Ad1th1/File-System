class FileSystem(object):

    def __init__(self):
        # define a map d
        self.d = {}         
    
    # create_path method, takes in parameters, path and value
    # create a new path, associate a value to it, if possible and return true
    # return false, if path already exists or if parent path does not exist
    def create(self,p,v):

        # p is a list of components of path split by '/
        p = p.split("/")
        x = self.d
        for i in range(1,len(p)-1):

            # parent path does not exist....
            if p[i] not in x:
                return False
            
            # if all parent elements exist, then create it
            x = x[p[i]][1]

        # if the last element of the path already exists, return false
        #-1 refers to last
        if p[-1] in x:
            return False
        
        # if not, create it
        x[p[-1]] = [v,{}]
        return True
    
    # get method takes path
    # returns value associated with path or -1 if path does not exist
    def get(self,p):

        x = self.d
        p = p.split("/")
        for i in range(1,len(p)-1):

            # if path does not exist, return -1
            if p[i] not in x:
                return -1
            x = x[p[i]][1]

        # if path does exist, return the value associated with it
        if p[-1] in x:
            return x[p[-1]][0]
        else:
            return -1


ob = FileSystem()
print(ob.create("/a",1))
print(ob.get("/a"))
