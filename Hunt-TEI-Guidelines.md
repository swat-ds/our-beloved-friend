For this project, we will be using a pared-down version of the incredible [coding manual](https://docs.google.com/document/d/0Bz5RztSfjWNSX1czeTVENURScmc/) developed by Pat O'Donnell for the Native American Journals Project. Because we have fewer resources at the moment, we will be implementing a subset of the tags outlined there, in the hopes of doing further encoding at a later date.

Our main goals for this encoding project are to 1) encode a subset of the names used in the text, 2) capture the top-level structure of the text, and 3) associate that structure with dates.  For that reason, the main focus should be on deploying the <persName> tag.

Goal 1. References to People
============================

For the purposes of this project we will be keeping a list of personal names. In the texts the "key" attribute will associate each name with a coded value that can be found in the list.

\<persName key="w6c82qz0"\>Joshua Evans\</persName\>

If you suspect a misspelling, retain the same spelling in the document and add it to the variant name column in the person list

If possessive is used, put inside of the persName brackets

Goal 2. Document Structure
==========================

We are most concerned here with encoding the journal entries, the page breaks, and the top-level divisions of the text such as the division of front-matter, the main body of the text, and back-matter. Paragraphs take a back seat, and we will not try to capture line breaks at all.

James has done some pre-processing of the text to tag the page breaks, journal entries, and editorial notes. The page breaks and editorial notes shouldn't need more work; the journal entry \<div\>s need revision to bring them in line with the TEI standards.
