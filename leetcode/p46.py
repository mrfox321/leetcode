class perm():
    def __init__(self):
        self.types = []

    def swaps(self,old_list,new_list):
        if not old_list:
            self.types.append(new_list)
            return
        for i in range(len(old_list)):
            new_new = new_list+[old_list[i]]
            old_old = [x for x in old_list if x!= old_list[i]]
            self.swaps(old_old,new_new)



x = perm()
x.swaps([1,2,3,4,5],[])
print x.types,len(x.types)
