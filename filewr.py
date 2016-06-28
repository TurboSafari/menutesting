import pickle

class fileWR(object):
    def __init__(self, file_name):
        self._file_name = file_name
        
    def getList(self):
        self._my_list = pickle.load(open(self._file_name,'r'))
        return(self._my_list)

    def writeList(self, my_list):
        pickle.dump(my_list, open(self._file_name, 'w'))

##testing = fileWR('test.txt')
##test = [0,1,2,3,4,5]
##testing.writeList(test)
##testTwo = testing.getList()
##print testTwo


