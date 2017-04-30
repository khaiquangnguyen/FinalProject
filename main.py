import sys
from Heap import *
def main():
    # read in the input
    if len(sys.argv) != 2:
     print ("Incorrect number of arguments!")
     exit()
    else:
     try:
         f = open(str(sys.argv[1]), 'r')
     except:
         print("No such file or directory!")
         exit()
     else:
        graph = Graph()
        print ("Building graph...")
        for lines in f.readlines():
            line = lines.split()
            for word in line:
                graph.insertVertex(word)
        while True:
            vdict = graph.getVerDict()
            s1 = raw_input("Enter the first five-letter word: ")
            s1 = s1.upper()
            s2 = raw_input("Enter the second five-letter word: ")
            s2 = s2.upper()
            if s1 in vdict and s2 in vdict:
                target = distance(vdict,s1,s2)
                print target.distance
                output = [] 
                while target is not None:
                    output = [target.word] + output
                    target = target.parent
                for i in output:
                    print i
            else:
                print ("Sorry! " + s1 + " or " + s2 + " is not in the list.")
            while (True):
                s = raw_input("Do you want to try another word. Enter yes or no? ")
                s = s.lower()
                if s == 'n' or s =='no':
                    exit()
                elif s == 'y' or s=='yes':
                    break
                else:
                    print("Please enter yes or no!")
    
def distance(vdict,s1,s2):
    for v in vdict:
        vdict[v].reinit()
    vdict[s1].distance = 0
    Q = Heap()
    for v in vdict:
        Q.insert(vdict[v])
    while Q.getHeapsize() != 0:
        u = Q.removeMin()
        v = u.edge
        if u.word == s2:
            return u
        while v is not None:
            if u.distance + v.getWeight() <= vdict[v.getKey()].distance:
                vdict[v.getKey()].parent = u
                vdict[v.getKey()].distance = u.distance + v.getWeight()
            v = v.getNext()

def main_test():
    f = open("5lw-s.dat", 'r')
     # read in the input
    graph = Graph()
    print ("Building graph...")
    for lines in f.readlines():
        line = lines.split()
        for word in line:
            graph.insertVertex(word)
    vdict = graph.getVerDict()
    while True:
        s1 = raw_input("Enter the first five-letter word: ")
        s1 = s1.upper()
        s2 = raw_input("Enter the second five-letter word: ")
        s2 = s2.upper()
        if s1 in vdict and s2 in vdict:
            path = distance(vdict,s1,s2)
            print (path[-1].distance)
            for v in path:
                print v.word

        else:
            print ("Sorry! " + s1 + " or " + s2 + " is not in the list.")
        while (True):
            s = raw_input("Do you want to try another word. Enter yes or no? ")
            s = s.lower()
            if s == 'n' or s =='no':
                exit()
            elif s == 'y' or s=='yes':
                break
            else:
                print("Please enter yes or no!")
def compare_word(s1,s2):
    n = 0
    score = 0
    for i in range(5):
        if s1[i] != s2[i]:
            score = 5 ** n
            n+=1
            if n >= 3:
                return 0
    if n == 0:
        return 0
    else:
        return score


class Graph:
    def __init__(self):
        self.verDict = {}

    def insertVertex(self,word):
        vertex = Vertex(word)
        for v in self.verDict:
            w = compare_word(word,v)
            if w != 0:
                self.verDict[v].insertEdge(word,w)
                vertex.insertEdge(v,w)
        self.verDict[word] = vertex

    def getVerDict(self):
        return self.verDict

class Edge:
    def __init__(self,neighbor,weight):
        self.key = neighbor
        self.weight = weight
        self.next = None

    def setKey(self,neighbor):
        self.key = neighbor

    def getKey(self):
        return self.key

    def setWeight(self,weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setNext(self,nextEdge):
        self.next = nextEdge

    def getNext(self):
        return self.next

    def print_edge(self):
        return self.key + "(" + str(self.weight) + ")"

class Vertex:
    def __init__(self, word):
        self.handle = 0
        self.word = word
        self.parent = None
        self.distance = sys.maxint
        self.edge = None

    def insertEdge(self,edge,weight):
        edge = Edge(edge,weight)
        edge.setNext(self.edge)
        self.edge = edge
    
    def reinit(self):
        self.parent = None
        self.distance = sys.maxint
        self.handle = 0
        
    def getKey(self):
        return self.distance

    def setHandle(self, inHandle):
        self.handle = inHandle

    def getHandle(self):
        return self.handle
    
if __name__ == "__main__":
    main()

# main_test()
