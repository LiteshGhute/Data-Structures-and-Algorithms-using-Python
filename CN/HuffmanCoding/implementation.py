import heapq
import os

class BinaryTreeNode:
    def __init__(self,value,freq) -> None:
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.freq < other.freq

    def __eq__(self, other) -> bool:
        return self.freq == other.freq

class HuffmanCoding:
    def __init__(self, path) -> None:
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverse_codes = {}
    
    def __make_frequency(self,text):
        freq_dict = {}
        for ch in text:
            if ch not in freq_dict:
                freq_dict[ch] = 0
            freq_dict[ch] += 1
        return freq_dict

    def __buildHeap(self,freq_dict):
        # pushing binary tree node into heap
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap, binary_tree_node)

    def __buildTree(self):
        while(len(self.__heap)>1):
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq
            newNode = BinaryTreeNode(None,freq_sum)
            newNode.left = binary_tree_node_1
            newNode.right = binary_tree_node_2
            heapq.heappush(self.__heap,newNode)
        return

    def __buildCodesHelper(self,root,curr_bits):

        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value] = curr_bits
            self.__reverse_codes[curr_bits] = root.value
            return

        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"1")
    
    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")

    def __getEncodedText(self,text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text
    
    def __getPaddedEncodedText(self,encoded_text):
        padded_amount = 8-(len(encoded_text)%8)
        for i in range(padded_amount):
            encoded_text += '0'
        # adding binary padded amount 
        padded_info = "{0:08b}".format(padded_amount)
        return padded_info+encoded_text
    
    def __getBytesArray(self, padded_encoded_text):
        array = []
        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2))   #integer with base 2
        return array

    def compress(self):
        # get file from path
        # read text from file
        file_name,file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"


        with open(self.path,'r+') as file, open(output_path, 'wb') as output:
            # make frequency dictionary
            text = file.read()
            text = text.rstrip()
            freq_dict = self.__make_frequency(text)

            # build the heap from the frequency_dict
            self.__buildHeap(freq_dict)

            # construct the binary tree from the heap
            self.__buildTree()

            # construct the codes from binary tree
            self.__buildCodes()

            # creating the encoded text using the code
            encoded_text = self.__getEncodedText(text)

            # pad this encoded text
            padded_encoded_text = self.__getPaddedEncodedText(encoded_text)

            bytes_array = self.__getBytesArray(padded_encoded_text)
            
            # return this binary file as output
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
        print('Compressed')
        return output_path

    def __removePadding(self,text):
        padded_info = text[:8]
        extra_padding = int(padded_info,2)
        text = text[8:]
        text_after_padding_removed = text[:-1*extra_padding]
        return text_after_padding_removed
    
    def __decodeText(self, text):
        decoded_text = ""
        current_bits = ""
        for bit in text:
            current_bits += bit
            if current_bits in self.__reverse_codes:
                decoded_text += self.__reverse_codes[current_bits]
                current_bits = ""
        return decoded_text
    
    def decompressed(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "__decompressed" + ".txt"
        with open(input_path,'rb') as file, open(output_path,'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            actual_text = self.__removePadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)
        return

path = 'C:/Users/DELL/Desktop/DSA Using Python/CN/HuffmanCoding/sample.txt'
h = HuffmanCoding(path)
output_path = h.compress()
h.decompressed(output_path)