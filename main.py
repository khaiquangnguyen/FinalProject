import sys

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
                graph.insertVertext(word)
        vlist = graph.getVerList()
        while True:
            s = raw_input("Enter a five-letter word: ")
            s = s.upper()
            if s in vlist:
                print ("The neighbors of " + s + " are: ")
                edge = vlist[s].edge
                count = 0
                s = ''
                while edge is not None:
                    if count == 6:
                        print s
                        s = ''
                        count = 0
                    count += 1
                    s = s + edge.print_edge() + "     "
                    edge = edge.getNext()
                print s
            else:
                print ("Sorry! " + s + " is not in the list.")
            while (True):
                s = raw_input("Do you want to try another word. Enter yes or no? ")
                s = s.lower()
                if s == 'n' or s =='no':
                    exit()
                elif s == 'y' or s=='yes':
                    break
                else:
                    print("Please enter yes or no!")



def main_test():
    f = open("5lw-m.dat", 'r')
    graph = Graph()
    for lines in f.readlines():
        line = lines.split()
        for word in line:
            graph.insertVertext(word)
    vlist = graph.getVerList()
    while True:
        s = raw_input("Enter a five-letter word: ")
        s = s.upper()
        if s in vlist:
            print("The neighbors of " + s + " are:")
            edge = vlist[s].edge
            while edge is not None:
                edge.print_edge()
                edge = edge.getNext()
        else:
            print("Sorry! " + s + " is not in the list.")
        while (True):
            s = raw_input("Do you want to try another word. Enter yes or no? ")
            s = s.lower()
            if s == 'n' or s =='no':
                exit()
            elif s == 'y' or s =='yes':
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
        self.verList = {}

    def insertVertext(self,word):
        vertex = Vertex(word)
        for v in self.verList:
            w = compare_word(word,v)
            if w != 0:
                self.verList[v].insertEdge(word,w)
                vertex.insertEdge(v,w)
        self.verList[word] = vertex

    def getVerList(self):
        return self.verList

class Edge:
    def __init__(self,neighbor,weight):
        self.neighbor = neighbor
        self.weight = weight
        self.next = None

    def setNeightbor(self,neighbor):
        self.neighbor = neighbor

    def getNeighbor(self):
        return self.neighbor

    def setWeight(self,weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setNext(self,nextEdge):
        self.next = nextEdge

    def getNext(self):
        return self.next

    def print_edge(self):
        return self.neighbor + "(" + str(self.weight) + ")"

class Vertex:
    def __init__(self, word):
        self.handle = 0
        self.key = word
        self.edge = None

    def insertEdge(self,edge,weight):
        edge = Edge(edge,weight)
        edge.setNext(self.edge)
        self.edge = edge

    def setKey(self, word):
        self.key = word

    def getKey(self):
        return self.key

    def setHandle(self, inHandle):
        self.handle = inHandle

    def getHandle(self):
        return self.handle

if __name__ == "__main__":
    main()

##main_test()
