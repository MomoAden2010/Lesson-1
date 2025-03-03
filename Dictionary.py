games = {
    "Football":"Football is a very popular game!",
    "Basketball":"Basketball is popular in the USA!",
    "Rugby":"Ruby involves lots of tackling",
    "Cheerleading":"In cheerleading people are thrown very high",
    "Hockey":"In hockey you must use a stick"

}

games = {}


n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter key {i+1}: ")
    value = input("Enter value for '{key}': ")
    games[key] = value 

print("\nYour dictionary:", games)