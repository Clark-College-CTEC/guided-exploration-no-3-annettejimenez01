# Guided Exploration No. 3
# Annette Jimenez


# imports the random library to be able to generate a random number
import random


def main():

    #  going to use the accumulator pattern to store values
    possible_names = []

    # open a new file and store the names that are entered there
    outputFile = open('rap-names-output.txt', 'w')

    # open file 'rap-names.txt' for read access
    with open('rap-names.txt', 'r') as dataFile:
        # going to iterate through each line in the file
        for name in dataFile:
            # strips off invisible line feed and appends name entered to the possible_names list
            possible_names.append(name.rstrip())

    # how many names will be generated
    count = int(input('How many rap names would you like to create? '))
    # how many parts should be part of the entire rap name
    parts = int(input('How many parts should the name contain? '))

    # Counted loop to generate total of rap names
    for i in range(count):
        # empty list to hold the rap names
        name_parts = []
        # counted loop to iterate the amount of times user wants as part of the names
        for j in range(parts):
            # Each iteration means that it will randomly select names from possible names list file and to name parts list
            name_parts.append(
                possible_names[random.randint(0, len(possible_names)-1)])

    # take the name parts list contents and put them together with a space
    outputFile.write(f"{' '.join(name_parts)}\n")
    # display content in terminal
    print(f"{' '.join(name_parts)}")

    # close output file
    outputFile.close()


main()
