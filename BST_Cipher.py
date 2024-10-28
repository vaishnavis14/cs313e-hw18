#  File: BST_Cipher.py

#  Description: This program encrypts and decrypts messages based on a given string. A binary search tree is used.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Partner Name: Pranav Kasibhatla

#  Partner UT EID: pvk249

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/07/2022

#  Date Last Modified: 11/08/2022

import sys

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        self.encrypt_str = encrypt_str
        new_string = ""
        # cleans the string as per parameters
        for i in range(len(self.encrypt_str)):
            if ord(self.encrypt_str[i]) == 32 or (ord(self.encrypt_str[i]) >= 97 and ord(self.encrypt_str[i]) <= 122):
                new_string += self.encrypt_str[i]
        self.encrypt_str = new_string
        # each letter is inserted into the binary search tree
        for i in range(len(self.encrypt_str)):
            self.insert(self.encrypt_str[i])


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        # first case tests if the root is none. if it is, it will set the root to the character.
        # second case tests if the character is already in the tree
        # third case inserts the character if it is not the root and not already in the tree
        if self.root == None:
            new_node = Node(ch)
            self.root = new_node
            return
        elif self.search(ch) != "":
            return
        else:
            current = self.root
            previous = current
            while current != None:
                if ord(ch) < ord(current.data):
                    previous = current
                    current = current.lChild
                else:
                    previous = current
                    current = current.rChild
            new_node = Node(ch)
            if ord(ch) < ord(previous.data):
                previous.lChild = new_node
            else:
                previous.rChild = new_node
            return


    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        # first case checks if the character is the root
        # second case checks if all other nodes and adds > and < based on whether it is is l child or r child
        if ch == self.root.data:
            return "*"
        else:
            str = ""
            current = self.root
            while current.data != ch:
                if ord(ch) < ord(current.data):
                    current = current.lChild
                    str += "<"
                else:
                    current = current.rChild
                    str += ">"
                if current == None:
                    return ""
            return str

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root
        # keeps going until data is found or none is reached
        for i in range(len(st)):
            if st[i] == "<":
                current = current.lChild
            elif st[i] == ">":
                current = current.rChild
            if current == None:
                return ""
        return current.data


    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        en_str = ""
        # encrypts by returning right or left and separates with !
        for i in range(len(st)):
            if i != len(st) - 1 and self.search(st[i]) != "":
                en_str += self.search(st[i]) + "!"
            else:
                en_str += self.search(st[i])
        # removes any additional ! marks
        while en_str[-1] == "!":
            en_str = en_str[:-1]
        return en_str

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        de_str = ""
        i = 0
        # searches tree for decryption. The for loop checks until ! is hit
        while i < len(st):
            if st[i] == "*":
                de_str += self.root.data
                i += 2
            else:
                trav_st = ""
                for j in range(i, len(st)):
                    if st[j] == "!":
                        break
                    else:
                        trav_st += st[j]
                de_str += self.traverse(trav_st)
                i += len(trav_st) + 1
        return de_str


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()