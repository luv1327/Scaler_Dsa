class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

root = TrieNode()

def indexToCharacter(idx):
    return chr(ord('a') + idx)

def characterToIndex(char):
    return ord(char) - ord('a')


def insertWord(word):
    global root
    temp = root
    for char in word:
        idx = characterToIndex(char)
        if temp.children[idx] == None:
            temp.children[idx] = TrieNode()
        temp = temp.children[idx]
    temp.isEnd = True
        
        
words = ['cat','cow','sheep']

def generateTrie(words):
    for word in words:
        insertWord(word)

generateTrie(words)

def search(word):
    global root
    temp = root
    for char in word:
        idx = characterToIndex(char)
        if temp.children[idx] == None:
            return False
        temp = temp.children[idx]
    return temp.isEnd

def printAllWordInTrie(root):
    if root == None:
        return
    for i in range(26):
        if root.children[i] != None:
            print(indexToCharacter(i))
            printAllWordInTrie(root.children[i])
    if root.isEnd:
        print('')
    
    
        
def searhWords(words):
    for word in words:
        doesExists = search(word)
        if doesExists:
            print('Exist : ',word)
        else:
            print('Does Not Exist : ',word)
words.append('cattle')  
searhWords(words)
            
        
printAllWordInTrie(root)