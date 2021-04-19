# :books: The Journals of John Hunt (1770-1824) :books: :books:

Following William Penn's advice, John Hunt kept a journal for over half a century, beginning in 1770 and ending shortly before his death in 1824. [This original work, penned in his own hand, is in the collections of Friends Historical Library](http://archives.tricolib.brynmawr.edu/resources/5240johu).

## Hunt Digital Project

Friends Historical Library and Digital Scholarship at Swarthmore College are currently involved in an ambitious digital edition of these journals, which includes:

- EAC-CPF data in conjunctions with [the SNAC Cooperative](https://portal.snaccooperative.org/about)
- TEI editions of transcribed journals
- Interactive digital edition

As part of the project, this repository consists of initial text representations of the transcribed journals, TEI marked up transcripts, derived data, and documentation.

# 4.17.2021 - Sandy Shen
Before searching and tagging any names, I went through the list of names and created a list of personal Name tags given different forms of a person of interest. For example, because "Aaron Willis" could sometimes be written as "Aaron Wilis," "A. Willis," the personal Name tag would have to reflect that variation but still identify the same person ("key = w6r525r2" for Aaron Willis).

I initially used the find and replace feature through Atom to search through each transcript and replace any mention of "Aaron Willis" with `<persName key="w6r525r2">A. Willis</persName>` and for every other individual.

Eventually, Nabil and Roberto pointed me to regular expressions, which are a much more efficient way to locate names and different variations of them. Instead of having to search "Aaron Willis," "Aaron Wilis," "A. Willis," etc separately, I could find `Aaron Will[i]?['s]?`and replace with `<persName key="w6r525r2">A. Willis</persName>`.

However, because of some issues (most likely because "'" was often used instead of "'") I was having difficulty actually implementing regular expressions. After replacing all of the incorrect apostrophes with the standard ' one, I expect the following regular expressions to work:

# Esther Hunt
Regular expression: Esther Hunt['s]?|E. Hunt['s]?
Replace with: `<persName key="w6wx87x7">Esther Hunt</persName>`

Regular expression: [Mm]y wife['s]?
Replace with: `<persName key="w6wx87x7">my wife</persName>` or `<persName key="w6wx87x7">My wife</persName>`
This second case should be manually done since "my wife" must refer to Esther Hunt and not someone else.

#Joshua Evans
Regular expression: Joshua Evan['s]?|J. Evan['s]?
Replace with: `<persName key="w6c82qz0">Joshua Evans</persName>`

# William Rogers
Regular expression: William Rogers['s]?|W. Rogers['s]?|W. Rogers
Replace with: `<persName key="w6fv9b6q">William Rogers</persName>`


# John Simpson
Regular expression: John Simpson['s]?|J. Simpson['s]?
Replace with: `<persName key="w68m543d">John Simpson</persName>` or
`<persName key="w68m543d">J. Simpson</persName>`

# John Collins
Regular expression: John Collins['s]?|J. Collins['s]?
Replace with: `<persName key="w6165774">John Collins</persName>` or
`<persName key="w6165774">J. Collins</persName>`

# Robert Willis
Regular expression: Robert Wil[l]?is['s]?|R. Wil[l]?is['s]?
Replace with: `<persName key="w6zw3s78">Robert Willis</persName>` or
`<persName key="w6zw3s78">R. Wills</persName>`

# Joseph Warrington
Regular expression: Joseph Warrington['s]?|J. Warrington['s]?
Replace with: `<persName key="w6bv9xp3">Joseph Warrington</persname>`or
`<persName key="w6bv9xp3">J Warrington</persname>`
Joseph Warrington appears fairly often.

# Aaron Wills/Aaron Willis
Regular expression: Aaron Will[i]?['s]?
Replace with: `<persName key="w6r525r2">A. Willis</persName>` or
`<persName key="w6r525r2">A. Willis</persName>`

# Joshua Lippincott
Regular expression: Joshua Lip[p]?incot[t]?['s]?|J. Lip[p]?incot[t]?['s]?
Replace with: `<persName key="w6jb6xn6">Joshua Lippincott</persName>` or `<persName key="w6jb6xn6">J. Lippincott</persName>`

# Elizabeth Collins
Regular expression: Elizabeth Collins['s]?|E. Collins['s]?
Replace with: `<persName key="w6hj799d">Elizabeth Collins</persName>` or
`<persName key="w6hj799d">E. Collins?</persName>`

# William Penn
Regular expression: William Penn['s]?|W. Penn['s]?
Replace with: `<persName key="w6p55q0b">William Penn</persName>` or
`<persName key="w6p55q0b">Penn</persName>`

# Richard Jordan
Regular expression: Richard Jordan['s]?|R. Jordan['s]?
Replace with: `<persName key="w6gq882n">Richard Jordan</persName>` or
`<persName key="w6gq882n">R. Jordan?</persName>`

# John Cox
Regular expression: John Cox[e]?['s]?|J. Cox[e]?['s]?
Replace with: `<persName key="w6b01gx6">John Cox</persName>` or
`<persName key="w6b01gx6">J. Cox</persName>`

# John Reeves
Regular expression: John Reeve[s]?['s]?|J. Reeve[s]?['s]?
Replace with: `<persName key="w6x16z80">John Reeves</persName>` or `<persName key="w6x16z80">J. Reeves?</persName>`

# Benjamin Swett
Regular expression: Benjamin Swett['s]?|B. Swett['s]?
Replace with: `<persName key="w6zk9cxf">Benjamin Swett</persName>` or `<persName key="w6zk9cxf">B. Swett</persName>`

# Mary Swett
Regular expression: Mary Swett['s]?|his wife['s]
Replace with: `<persName key="w68d3sbk">Mary Swett</persName>` or `<persName key="w68d3sbk">his wife</persName>`
Need to manually check for Mary Swett because she almost always appears in mention with her husband as "his wife"

# Esther Collins
Regular expression: Esther Collin[s]?['s]?|E. Collin[s]?['s]?
Replace with: `<persName key="w6gj3q0h">Esther Collins</persName>` or `<persName key="w6gj3q0h">E. Collins?</persName>`
Need to manually check this one so as not to confuse her with Esther Hunt
