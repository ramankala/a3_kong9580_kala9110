from common import *

class Node:
    def __init__(self, ID, networksimulator, costs):
        self.myID = ID
        self.ns = networksimulator
        num = self.ns.NUM_NODES
        self.distanceTable = [[0 for i in range(num)] for j in range(num)]
        self.routes = [0 for i in range(num)]

        # you implement the rest of constructor
        for i in range(num):
            if(i != ID):
                if(costs[i] != self.ns.INFINITY):
                    print("\nTOLAYER2: " + "source: {} ".format(self.myID) + "dest: {} ".format(i) + "costs: ", end="")
                for j in range(num):
                    if(costs[i] != self.ns.INFINITY):
                        print("{} ".format(costs[j]), end="")
                    if(i != j):
                        self.distanceTable[i][j] = self.ns.INFINITY
                if(costs[i] != self.ns.INFINITY):
                    print("\n")
                self.distanceTable[ID][i] = costs[i]
            else:
                for j in range(num):
                    if(j != ID):
                        self.distanceTable[j][i] = self.ns.INFINITY

    def recvUpdate(self, pkt):

        self.distanceTable[pkt.sourceid] = pkt.mincosts

        # you implement the rest of it

        
        return


    def printdt(self):
        print("   D"+str(self.myID)+" |  ", end="")
        for i in range(self.ns.NUM_NODES):
            print("{:3d}   ".format(i), end="")
        print()
        print("  ----|-", end="")
        for i in range(self.ns.NUM_NODES):
            print("------", end="")
        print()
        for i in range(self.ns.NUM_NODES):
            print("     {}|  ".format(i), end="" )

            for j in range(self.ns.NUM_NODES):
                print("{:3d}   ".format(self.distanceTable[i][j]), end="" )
            print()
        print()
