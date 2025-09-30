def compress(input):
    prev = ""
    counter = 1
    output = ""

    for char in input:
        if char == prev:
            counter += 1
        else:
            output += str(counter) + prev if counter > 1 else prev
            counter = 1
            prev = char
    output += str(counter) + prev if counter > 1 else prev
    return output

def decompress(input):
    output = ""
    number = ""

    for char in input:
        if char.isnumeric():
            number += char
        else:
            output += char * int(number) if number != "" else char
            number = ""
    return output


def process_file(filename, target_filename, mode = "compress"):
    with open(filename, "r") as file:
        with open(target_filename, "w") as target_file:
                for line in file.readlines():
                    processed_line = compress(line) if mode == "compress" else decompress(line)
                    target_file.write(processed_line)

