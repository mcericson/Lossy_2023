import rhinoscriptsyntax as rs

def print_string(string):
    print(string)

def main():
    value = rs.GetString("Provide a string to print")
    print_string(value)

main()