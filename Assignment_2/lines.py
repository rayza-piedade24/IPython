import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].rsplit(".")[1] != "py":
    sys.exit("Not python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
                count = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != "":
                        count += 1
        print(count)
    except:
         raise FileNotFoundError
