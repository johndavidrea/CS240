class HashTable:

    def __init__(self):
        self.tableSize = 10
        self.upsizeThreshold = 0.75
        self.downsizeThreshold = 0.25
        self.hashList = [None] * self.tableSize
        self.storedValues = 0
        self.usedCells = 0

    def printEntries(self):
        print("Printing entries")
        for entry in self.hashList:
            if isinstance(entry, HashEntry):

                print(f"Key: {entry.getKey()}")
                print(f"Value: {entry.getValue()}")
                print(f"Hashtable index: {getHashcode(entry.getKey(), self.tableSize)}")

            elif isinstance(entry, list):
                for index in entry:
                    print(f"Key: {index.getKey()}")
                    print(f"Value: {index.getValue()}")
                    print(f"Hashtable index: {getHashcode(index.getKey(), self.tableSize)}")

    def add(self, key, value):

        index = getHashcode(key, self.tableSize)
        entry = HashEntry(key, value)

        print("Adding new entry")
        print(f"Key: {key}")
        print(f"Value: {value}")
        print(f"Hashtable index: {index}")

        # Check to see if there is an existing key with the same value
        # for entry in self.hashList:
        #     if isinstance(entry, HashEntry):
        #         print("t3")
        #         # print(f"Existing key: {entry.getKey()}")
        #         # print(f"New key: {key}")
        #         # if entry.getKey() == key:
        #         #     print("Cannot add a duplicate key value!")
        #         #     return
        #
        #     # elif isinstance(entry, list):
        #     #     print("1")
        #     #     for i in entry:
        #     #         print("2")
        #     #         # if index.getKey() == key:
        #     #         #     print("Cannot add a duplicate key value!")
        #     #         #     return

        # If there is no collision
        print(f"Index is {index}")
        if self.hashList[index] is None:
            self.hashList[index] = HashEntry(key, value)

        # If there is a collision
        elif isinstance(self.hashList[index], HashEntry):
            print("collision")
            buffer = self.hashList[index]
            self.hashList[index] = [buffer, entry]
            self.usedCells += 1

        # If there is a collision, but it's already been handled
        elif isinstance(self.hashList[index], list):
            print("collision but it's already a list")
            self.hashList[index].append(entry)

        else:
            raise Exception("This should never happen, the add method is broken.")

        self.storedValues += 1
        self.manageSize()

    def remove(self, key):
        index = getHashcode(key, self.tableSize)

        print(f"Removing key {key} at index {index}")

        if self.hashList[index] is None:
            print("Value not found, cannot remove it")
            return


        if isinstance(self.hashList[index], HashEntry):
            if self.hashList[index].getKey() == key:
                self.hashList[index] = None
                self.usedCells -= 1
                self.storedValues -= 1

        # if isinstance(self.hashList[index], list):
        #     # Check each sub-entry on the list to see if it contains the key
        #     bufferList = self.hashList[index]
        #     for entry in bufferList:
        #         if bufferList[entry].getKey == key:
        #             bufferList[entry].remove()
        #             self.storedValues -= 1
        #
        #     if len(bufferList) == 0:
        #         self.hashList[index] = None
        #         self.usedCells -= 1
        #
        #     # Convert the list back to an entry if the length of the list is < 2
        #     if len(bufferList) < 2:
        #         self.hashList[index] = bufferList[0]

        self.manageSize()

    def manageSize(self):

        if self.usedCells >= self.upsizeThreshold * self.tableSize:
            buffer = self.hashList
            self.tableSize *= 2
            self.rebuildHashlist(buffer)

        if self.usedCells <= self.downsizeThreshold * self.tableSize:
            if self.tableSize > 10:
                buffer = self.hashList
                self.tableSize = self.tableSize // 2
                self.rebuildHashlist(buffer)

    def rebuildHashlist(self, buffer):

        self.storedValues = 0
        self.usedCells = 0
        self.hashList = [None] * self.tableSize

        for entry in buffer:

            if isinstance(entry, HashEntry):
                self.add(entry.getKey(), entry.getValue())

            if isinstance(entry, list):
                for index in entry:
                    self.add(entry[index].getKey(), entry[index].getValue())


class HashEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def printEntry(self):
        print(f"Key: {self.key}")
        print(f"Value: {self.value}")
        print(f"Hashtable index: {getHashcode(self.key, 10)}")


def getHashcode(var, tableSize):
    if isinstance(var, int):
        return var % tableSize

    elif isinstance(var, str):
        hashcode = 0
        for char in var:
            hashcode += ord(char)
        return hashcode % tableSize

    else:
        raise Exception("Hashing for this data type is not implemented")


table = HashTable()
# test = HashEntry(33, "Cherry")
# test.printEntry()


table.add(61, "Blueberry")
table.add(31, "Raspberry")
table.add(21, "Grape")
# print("              ")
#
table.printEntries()

#
#
# table.remove(21)
#
# table.printEntries()
#
# table.add(35, "Raspberry")