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
	# define namespace
	ns = {'x':'http://www.tei-c.org/ns/1.0'}

	# Get root element of tei
	root = tei.getroot()

	# Get iterable of divs
	body = root[1].find("x:body", ns)
	divs = body.iterfind("x:div", ns)

	# Create container for entries
	entries = []

	# Loop over divs, extracting persName tags
	for div in divs:
		# Create a container for the persNames
		entryNames = []
		#print(div.find('{http://www.tei-c.org/ns/1.0}p'))
		for para in div.iterfind('{http://www.tei-c.org/ns/1.0}p'):
			for name in para.iterfind('{http://www.tei-c.org/ns/1.0}persName'):
				if name.attrib["key"] in entryNames:
					continue
				else:
					entryNames.append(name.attrib["key"])
		entries.append(entryNames)
	return entries

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

	# Filter entries without names out of data
	# (loop over list backward, removing empty lists)
	i = len(data)
	while i > 0:
		i += -1
		if len(data[i]) == 0:
			del data[i]


	# Calculate statistics

	# Create a corresponding list if lengths

	print("\n")

main()
