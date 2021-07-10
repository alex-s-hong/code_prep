#! usr/bin/env python3

class HashMap:
    def __init__(self):
        self.max_size = 64
        self.arr = [None for _ in range(self.max_size)]

    def get_hash(self, key):
        if type(key) == int:
            return key % self.max_size

        elif type(key) == str:
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if key_hash in self.arr:
            for k, v in self.arr[key_hash]:
                if k == key:
                    v = value
                    return True
            self.arr.append(key_value)
            return True
        else:
            self.arr[key_hash] = [key_value]
            return True


    def get(self, key):
        key_hash = self.get_hash(key)
        if self.arr[key_hash]:
            for k, v in self.arr[key_hash]:
                if k == key:
                    return v
        
        return None
        

    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.arr[key_hash]:
            for i in range(len(self.arr[key_hash])):
                if self.arr[key_hash][i][0] == key:
                    self.arr[key_hash].pop(i)
                    return True
        
        return False
    
    def print(self):
        print("DICTIONARY INFO")
        for item in self.arr:
            if item:
                print(str(item))
    
if __name__ == "__main__":
    dic = HashMap()
    dic.add('John', 50000)
    dic.add('Adam', 30000)
    print('get', dic.get('John'))
    dic.print()
    dic.add('Kim', 40000)
    dic.print()
    dic.delete('Kim')
    dic.add('John', 123000)
    dic.print()
    print('get', dic.get('Kim'))
    