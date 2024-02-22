import binascii

def main():
    # Prepare Input
    with open("Ciphertexts.txt") as f:
        ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
    cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]

    # Convert (list of ciphertext with char) to (list of list with int)
    list_of_list = list() 
    max_line_length = 0
    for line_of_ciphertexts in ciphertexts: 
        if (len(line_of_ciphertexts) > max_line_length):
            max_line_length = len(line_of_ciphertexts) 
        line_aux = list()
        for c in line_of_ciphertexts:
            line_aux.append(c)
        list_of_list.append(line_aux) 

    # Create Matrix for XOR 
    zero_to_max_line_length = range(0, max_line_length) 
    list_of_columns = list() 
    for step in zero_to_max_line_length:
        list_of_columns.insert(step, list()) 

    for line in list_of_list:
        for index, item in enumerate(line, 0):
            aux_for_columns = list_of_columns.pop(index)
            aux_for_columns.append(item)
            list_of_columns.insert(index, aux_for_columns)

    # Find k (pad)
    spaces = list() 
    pad = list()
    
    for column in list_of_columns:
        # XOR the ciphertexts together, and consider what happens when a space is XORed with a character in [a-zA-Z].
        mydict = {}
        for i in column:
            for j in column:
                result = i ^ j
                if (result >= 65):
                    if i not in mydict:
                        mydict[i] = 1
                    else:
                        mydict[i] = mydict.get(i) + 1
                    if j not in mydict:
                        mydict[j] = 1
                    else:
                        mydict[j] = mydict.get(j) + 1
                    # Greatest frequency
                    maximum = max(mydict, key = mydict.get)
        spaces.append(maximum)

    for space in spaces:
        pad.append(space ^ 32)

    # Decryption
    for index_row, row in enumerate(ciphertexts, 0):
        for index_column, column in enumerate(row, 0):
            cleartexts[index_row][index_column] = ciphertexts[index_row][index_column] ^ pad[index_column]

    print(cleartexts[len(cleartexts) - 1]) # Target ciphertext

if __name__ == "__main__":
    main()