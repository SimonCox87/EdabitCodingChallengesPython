# Create a function that inverts words or the phrase depending on the value of parameter type. A "P" means to invert the entire phrase, 
# while a "W" means to invert every word in the phrase. See the following examples for clarity.

# Examples

# inverter("This is Valhalla", "P") ➞ "Valhalla is this"

# inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"

# inverter("Division by powers of two", "P") ➞ "Two of powers by division"

# Notes

#     The first character of the returned string should be in uppercase and the rest are in lowercase.
#     There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness, are discounted 
#     in the input phrases.

def inverter(txt, type):
    W = " ".join(txt[::-1].split()[::-1]).capitalize()
    P = " ".join(txt.split()[::-1]).capitalize()
    return W if type == "W" else P

print(inverter("This is Valhalla", "P")) # ➞ "Valhalla is this"
print(inverter("One fine day to start", "W")) # ➞ "Eno enif yad ot trats"
print(inverter("Division by powers of two", "P")) # ➞ "Two of powers by division"