def transpose(character):
    b = ord(character)
    return map(lambda x: chr(b ^ (2 ** x)), xrange(8))

domain_name = "YOUR_DOMAIN_NAME"

for position, letter in enumerate(domain_name):
    transposed_values = transpose(letter)
    for value in transposed_values:
        new_list = list(domain_name)
        new_list[position] = value
        print "".join(new_list)
