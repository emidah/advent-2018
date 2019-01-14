def main():

    st = open("input.txt", 'r').read()
    players = int( st[:st.find(' ')] )
    lastMarble = 100*int( st[34:( st[34:].find(' ') + 34)] )

    print('players: ' + str(players) + ', last marble worth ' + str(lastMarble))

    zero = Node(0,None)
    zero.next = zero
    currentNode = zero
    nodeToGo = None

    scores = [0]*players

    for i in range(1, lastMarble+1):
        if i % 23 == 19:
            nodeToGo = currentNode

        if i == 0 or i % 23 != 0:
            #print(currentNode.value)
            newNode = Node(i,currentNode.next.next)
            currentNode.next.next = newNode
            currentNode = newNode
        else:
            #print(nodeToGo.next.value)
            scores[i % players] += i + nodeToGo.next.value
            nodeToGo.next = nodeToGo.next.next
            currentNode = nodeToGo.next
        
    print(max(scores))
            
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


if __name__ == "__main__":
    main()