from metaphone import doublemetaphone
from copy import deepcopy
from fuzzywuzzy import fuzz

class Person:
    def __init__(self, string, number):
        self.fullName = string
        self.count = number
        self.defAliases = []
        self.possAliases = []

        phonetics = doublemetaphone(string.strip("[]"))
        self.metas = []
        for item in phonetics:
            if len(item) > 0:
                self.metas.append(item)

    def __str__(self):
        row1 = "Name: "+self.fullName+'\n'

        if len(self.defAliases) == 0:
            row2 = "Definite aliases: none\n"
        else:
            row2 = "Definite aliases: "
            for item in self.defAliases:
                row2 += item+", "
            row2 = row2[:-2] + "\n"

        if len(self.possAliases) == 0:
            row3 = "Possible aliases: none\n"
        else:
            row3 = "Possible aliases: "
            for item in self.possAliases:
                row3 += item + ", "
            row3 = row3[:-2] + "\n"

        row4 = "Phonetics: "
        for item in self.metas:
            row4 += item + ", "
        row4 = row4[:-2] + "\n"

        row5 = "Number of occurrences: " + str(self.count) + "\n"


        return row1 + row2 + row3 + row4 + row5

    def getCount(self):
        return self.count

    def getFullName(self):
        return self.fullName

    def getPhonetics(self):
        return self.metas

    def getDefAliases(self):
        return self.defAliases

    def getPossAliases(self):
        return self.possAliases

    def addDefAlias(self, person):
        """
        Combines two Person objs, subsuming arg of this function into caller obj

        Params: person, a Person object
        Returns: None
        Side effects:
            @ adds person's def aliases, poss aliases, & phonetics to caller's
            @ adds person's occurrence count to caller's
        """

        self.count += person.getCount()
        self.defAliases += person.getDefAliases()
        self.possAliases += person.getPossAliases()
        self.metas += person.getPhonetics()

    def __eq__(self, other):
        return self.fullName == other.fullName

def processNames(original):
    """
    ADD SUMMARY

    Params: @people, a list of Person objects
    Returns: a consolidated list of Person objects
    """

    # Make a copy of the original list

    # Loop over the original

        # If the current name isn't in the copy, skip it
        # For each item on the target list:
            # For each phonetic in the source name:
                # Compare to each phonetic in the target name
                    # If any comparison passes a certain threshold:
                        # Query the user about whether to merge them
                        # If they're to be merged:
                            # Ask which one should be primary
                            # Subsume the other into it
                            # Delete the other from the target list
                            # Don't raise the index of the target list
                            # Lower the length of the target list
                            # break
                        # Else: # break
                # break


def main():
    people = []
    with open("nameList2.txt") as f:
        lines = f.read().split("\n")
        del lines[0] # Discard header row
        pairs = [item.split("\t") for item in lines]
        for item in pairs:
            people.append(Person(item[0], str(item[1])))

    # for person in people:
    #     print(person)

    targets = deepcopy(people)

    print(people[0] in targets)




print("\n")
main()
print("\n")
