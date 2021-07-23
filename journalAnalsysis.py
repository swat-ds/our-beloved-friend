"""
A suite of programs to perform analysis on the TEI-markup Hunt Journals.

James Truitt
July 2021
"""

from glob import glob
import xml.etree.ElementTree as ET

def loadData():
	print("Loading XML data...")
	# Get list of TEI filenames
	filenames = glob("pid-tei/*.xml")

	# Initialize container for xml data
	xmls = []

	# Loop over filenames, extracting the XML data in each & adding it to xmls
	for filename in filenames:
		print("Reading {}".format(filename + "..."), end="")
		xml = ET.parse(filename)
		xmls.append(xml)
		print("\tdone")

	print("XML data successfully loaded!")
	return xmls

def getBoolCooccurrences(tei):
	return []

def getCountCoocurrences(tei):
	return []

def main():
	print("\n")
	# Load the TEI data from files
	teis = loadData()

	# Initialize a holder for our data
	data = []

	# Loop over the TEI files
	for journal in teis:
		# From each TEI, extract set of sets of ARKids cooccurring in entries
		collocs = getBoolCooccurrences(journal)

		# Add that set to data holder
		data += collocs
		
	print("\n")

main()
