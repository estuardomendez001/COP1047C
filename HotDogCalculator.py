NUMBER_OF_HOTDOGS_INSIDE_PACKAGE = 10  # constant. that is the amount per package
NUMBER_OF_BUNS_INSIDE_PACKAGE = 8      # constant. that is the amount per package


number_of_people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))


# total amount of hotdogs needed for everyone
total_hotdogs = number_of_people * number_of_hotdogs_per_person

# calculates the amount of packages needed 
number_of_hotdog_packages_needed = total_hotdogs // NUMBER_OF_HOTDOGS_INSIDE_PACKAGE
number_of_hotdog_buns_needed = total_hotdogs // NUMBER_OF_BUNS_INSIDE_PACKAGE

# calculates remainder
number_of_hotdogs_left_over = total_hotdogs % NUMBER_OF_HOTDOGS_INSIDE_PACKAGE
number_of_hotdog_buns_left_over = total_hotdogs % NUMBER_OF_BUNS_INSIDE_PACKAGE


print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_hotdog_buns_needed)
print("Number of hot dogs left over =", number_of_hotdogs_left_over)
print("Number of hot dogs buns left over =", number_of_hotdog_buns_left_over)