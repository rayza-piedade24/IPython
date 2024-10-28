def main():
    plate= input("Plate Number:")
    if is_valid(plate):
        print("Valid")
    else:
        print("False")
        
def is_valid(s):
    while True:
        if s.isalnum() and 1 < len(s) <7 and s[:1].isalpha() :
            if s[:].isalpha() :
                return True
            elif s[:].isalnum() :
                digits = 0 #Number of digits in license plate
                for i in s:
                    if i.isdigit:
                        digits= digits + 1
                        if digits == 1 and s[-1].isdigit and s[-1] != '0' :
                            return True
                        elif digits == 2 and s[::-2].isdigit and s[-2] != '0' :
                            return True
                        elif digits == 3 and s[-3:].isdigit and s[-3] != '0' :
                            return True
                        elif digits == 4 and s[-4:].isdigit and s[-4] != '0' :
                            return True
                        else:
                            return False
        else:
            return False
          
main()
