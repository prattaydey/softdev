with open("foo.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(1) # replace w commands