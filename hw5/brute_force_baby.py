import Tabu
import loadFile


def dec2bin(x, string_length):
    binary_string = str(bin(x))[2:]
    while len(binary_string) < string_length:
        binary_string = '0' + binary_string
    return binary_string


num_satisfying = 0
sat_matrix = loadFile.load_file("uf20_01.txt")
for i in range(1048576):
    string = dec2bin(i, 20)
    cost = Tabu.costSAT(string, sat_matrix)
    if cost == 91:
        num_satisfying += 1
        print("Satisfying: " + string)

print("Number of satisfying solutions: " + str(num_satisfying))
