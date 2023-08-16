movies = {
    "Finding Dory": [3, 1],
    "Bourne": [18, 5],
    "Ghost Busters": [12, 5]
    }

while True:
    choice = input("What movie do you want to watch?: ").strip().title()

    if choice in movies:
        age = int(input("How old are you? : ").strip())

        # check user age

        if age >= movies[choice][0]:

            #check enough seats

            num_seats = movies[choice][1]

            if num_seats > 0:
                print("Enjoy the movie")
                movies[choice][1] = movies[choice][1] - 1
                print(movies[choice][1])
            else:
                print("Sorry, we are sold out!")     
        else:
            print("You are too young to see that movie!")
    else:
        print("We do not have that movie...")
        
