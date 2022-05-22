import os

def populate_file(filename):
    values_to_write = ["hello","Line1","Line2","Line3","and so on"]
    with open(filename,"w") as out:
        for value_to_write in values_to_write:
            out.write(value_to_write)
            out.write("\n")

def read_file(filename):
    with open(filename,"r") as in_file:
        for line in in_file:
            yield line  # Generator output

def read_if_exists(filename):
    if os.path.isfile("filname"):
        yield from read_file(filename)
    return []

filename = "sample_file.txt"

populate_file(filename)
# file_contents = [line for line  in open(filename,"r")]
file_contents = read_if_exists(filename)

print(file_contents)

new_line = next(file_contents)
print(new_line)


