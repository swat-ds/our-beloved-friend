"""
A suite of programs to perform analysis on the TEI-markup Hunt Journals.

James Truitt
July 2021
"""

def loadXml():
	pass

def getBoolCooccurrences(tei):
	pass

def getCountCoocurrences(tei):
	pass

def main():
	# Load the TEI data from files
	teis = loadXml()

	# Initialize a holder for our data
	data = []

	# Loop over the TEI files
	for journal in teis:
		# From each TEI, extract set of sets of ARKids cooccurring in entries
		collocs = getBoolCooccurrences(journal)

		# Add that set to data holder
		data += collocs

main()
