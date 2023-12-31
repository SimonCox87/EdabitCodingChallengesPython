"""Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid."""

def pluralize(lst):
    lstSet = []
    for i in lst:
        if lst.count(i) > 1:
            lstSet.append(i + "s")
        else:
            lstSet.append(i)
    
    return set(lstSet)

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))

def pluralize(lst):
    return set([i + "s" if lst.count(i) > 1 else i for i in lst])

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))

"""def pluralize(lst):
	return set(i + 's'*(lst.count(i)>1) for i in lst)"""

"""def pluralize(lst):
	return {i+'s' if lst.count(i)>1 else i for i in lst}"""