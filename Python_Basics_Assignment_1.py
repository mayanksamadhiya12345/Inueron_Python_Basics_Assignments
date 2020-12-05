# QUESTION 1
# HERE WE ARE USING A FOR LOOP FOR DEFINING THE RANGE BETWEEN 2000 TO 3200 ( INCLUDING BOTH )

for i in range(1999,3201):
    if(i%7==0 and i%5!=0):
        print(i , end=",")        # HERE WE ARE USING end="," FOR SEPERATING OUR OUTPUT WITH COMA'S
        i = i + 1                 # INCREASING THE VALUE OF i AFTER EACH AND EVERY ITERATIONS
    else:
        i = i + 1




# QUESTION 2
# FINDING THE REVERSE OF A GIVEN USER FISRT AND LAST NAME 
# HERE WE ARE TAKING THE FIRST NAME AND LAST NAME OF THE USER AS A INPUT
f_name = input("Enter the user's first name :")
l_name = input("Enter the user,s last name : ")

# HERE WE ARE ADDING BOTH FIRST AND LAST NAME STRINGS 
full_name = f_name + " " + l_name
print(f"Full name of the user is : {full_name}")              # HERE WE ARE USING STRING FORMATTING

# HERE WE ARE PRINTING THE REVERSE ORDER OF THE STRING
print(full_name[::-1])




# QUESTION 3
# FINDING THE VOLUME OF SPHERE WITH ANY DIAMETER
# HERE d BELONGS TO DIAMETER
d = int(input("Enter the value of sphere's diameter : "))
print(f"the Diameter of the sphere is: {d}")                   # HERE WE ARE USING STRING FORMATTING

# HERE r BELONGS TO RADIUS
r = d/2
print(f"Radius of the sphere is: {r}")                         # HERE WE ARE USING STRING FORMATTING

# HERE v BELONGS TO VOLUME
# HERE 3.14 IS NOTHING NUT IT IS THE VALUE OF PIE
v = (4/3)*(3.14)*(r*r*r)

# HERE WE ARE PRINTING THE VOLUME OF THE SPHERE
print(f"Final volume of the sphere is: {v}")                    # HERE WE ARE USING STRING FORMATTING
