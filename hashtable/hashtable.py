class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        #storage buckets for the capacity
        self.storage = [None] * self.capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        #the self.storage 'buckets' are going to hold the hash, need to return len() of them to returns the number of items/characters

        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        #FNV-1 Hash pseudocode from Wikipedia
        # algorithm fnv-1 is
        # hash := FNV_offset_basis do
        # for each byte_of_data to be hashed
            # hash := hash × FNV_prime
            # hash := hash XOR byte_of_data
        # return hash 
        
        FNV_offset_basis =  14695981039346656037
        FNV_prime = 1099511628211

        hash = FNV_offset_basis
        # encode strings into bytes representation with the .encode() -- from the TK
        for x in key.encode(): #loop
            hash = hash * FNV_prime
            hash = hash ^ x
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here 
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #sets index equal to the hash_index function's key
        index = self.hash_index(key)
        #self.storage at the index-th position = the Linked List hash table key/value pair
        # self.storage[index] = HashTableEntry(key, value)

        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key, value)
            self.count += 1
        else:
            current = self.storage[index]
            while current.next != None and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                new_hash_entry = HashTableEntry(key,value)
                new_hash_entry.next = self.storage[index]
                self.storage[index] = new_hash_entry
                self.count += 1
            #stretttccchhhhhh
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2) 

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            print('Warning: Key not found.')
            return None
        else:  
            prev = None
            while node.key != key and node.next is not None:
                prev = node
                node = node.next
            
            if node.key == key:
                if prev is None:
                    self.storage[index] = node.next
                else:
                    prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.storage[index]

        if node is not None:
            return self.storage[index].value
        else:
            return None
        
        while node.key != key and node.next != None:
            node = node.next
        
        if node.key == key:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        past_storage = self.storage

        self.storage = [None] * new_capacity
        self.capacity = new_capacity
        self.load = 0

        for item in past_storage:
            while item:
                self.put(item.key, item.value)
                item = item.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")



  


        
