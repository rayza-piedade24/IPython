def main():
    plate= input("Plate Number:")
    if is_valid(True):
        print("Valid")
    else:
        print("False")
        
    def is_valid(s):
        if s[:2].isalpha() and s.isalnum and 2 <len(s) <6:
            return True
        else:
            return False
