def myzip():
    # Create two lists
    list1 = ("Ronaldo","Pele","Raul")
    list2 = ("Eusebio","Socrates","Butragenio")

    #Zip the two lists togather
    zipres = zip(list1,list2)

    print(tuple(zipres))