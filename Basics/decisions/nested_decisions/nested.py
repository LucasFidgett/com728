bookCover = input("What type of cover does the book have?\n")

if bookCover == "soft":
    bookBound = input("is the book perfect-bound?\n")
    if bookBound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stiches are great for short books")
else:
    print("Books with hardcovers are more expensive!")