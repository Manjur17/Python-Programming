
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Manjur"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")

# to diplay in f-string format
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

# We can use it in a single statement as well.
print(f"{2 * 30}")
print(type(f"{2 * 30})")) #returns a string type 



