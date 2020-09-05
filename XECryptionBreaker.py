# decryption of XECryption cipher used in hackthissite.org realistic mission 6
# this relies on the summation of the integers separated by period
# this summation of the integers also utilizes user's key (an integer)
# open text file containing encryption password
with open(r'C:\decryptpass.txt', 'r') as data:
    plaintext = data.read()

# create list from the text file
integersList = plaintext.split(".")
for index in range(len(integersList)):
    integersList[index] = int(integersList[index])

# iterate through integers in the list to create a new list that will have the sums of each 3 ints
numsList = []
i = 0
while i in range(len(integersList)):
    tempInt = integersList[i] + integersList[i + 1] + integersList[i + 2]
    numsList.append(tempInt)
    i = i + 3


# the most common character in the english language is " "
# look in numsList for most common integer as a possibility


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


# ASCII of the space character is assigned the number 32
# therefore the password key would be the most common integer minus 32


pass_key = most_frequent(numsList) - 32

ascii_list = []

# will now iterate through the numsList and subtract each int by the pass_key
j = 1
while j in range(len(numsList)):
    tempInt = numsList[j] - pass_key
    ascii_list.append(tempInt)
    j = j + 1

# will now need to use ASCII dictionary to decode the ascii_list * does not contain every ascii character assignment**

ascii_dict = {10: '\n', 13: '\r', 32: ' ', 33: '!', 34: '"', 34: '#', 35: '#', 36: '$', 37: '%', 38: '&', 44: ',',
              46: '.', 47: '/', 48: '0', 49: '1',
              50: '2',51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 64: '@',
              65: 'A', 66: 'B', 67: 'C', 68: 'D',
              69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O',
              80: 'P',
              81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 97: 'a',
              98: 'b',
              99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l',
              109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v',
              119: 'w', 120: 'x', 121: 'y', 122: 'z'}

# go through ascii_list and if index is in ascii_dict, it will be replaced by it's assigned letter

for i in range(len(ascii_list)):
    if ascii_list[i] in ascii_dict:
        ascii_list[i] = ascii_dict[ascii_list[i]]
        i = i + 1

# now concatenate items in ascii_list for the complete message
message = ""
for j in range(len(ascii_list)):
    message = message + str(ascii_list[j])
    j = j + 1

print(message)

