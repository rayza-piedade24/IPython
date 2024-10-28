def main():
    plate= input("Plate Number:")
    if is_valid(plate):
        print("Valid")
    else:
        print("False")
        
def is_valid(s):
    if s.isalnum() and 1 < len(s) <7 and s[:2].isalpha() :
        if s[2:].isdigit("0"):
            return False
        elif s[2:].isdigit() and s.endswith().isalpha():
            return False
        else:
            return True
    else:
        return False
          
main()
