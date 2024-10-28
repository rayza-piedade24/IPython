file= input ("What is the name of the file?")

if file.endswith(".gif"):
    print("Media type: image/gif")

elif file.endswith(".jpg"):
    print("Media type: image/jpeg")
elif file.endswith(".jpeg"):
    print("Media type: image/jpeg")
elif file.endswith(".png"):
    print("Media type: image/png")
elif file.endswith(".pdf"):
    print("Media type: application/pdf")
elif file.endswith(".txt"):
    print("Media type: text/plain")
elif file.endswith(".zip"):
    print("Media type: application/zip")

else:
    print("Media type: application/octet-stream")
