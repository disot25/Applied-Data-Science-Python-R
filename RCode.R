#Rene Disotuar
#R Code
###############Code Samples from DataCamp and Class############################
########Declaring Variables###################
# Declare variables of different types
my_numeric <- 42
my_character <- "universe"
my_logical <- FALSE

# Check class of my_numeric
class(my_numeric)

# Check class of my_character
class(my_character)

# Check class of my_logical
class(my_logical)



###########Creating Vectors###########################
x<-c(3,4,7,8)
y<-c(5,7,7,6)
z<- c(x,y)
dist(z, method='euclidean')
matrix1 <- matrix(c(x,y),byrow=T,nrow = 2)
dist(matrix1, method="manhattan")
dist(matrix1, method="euclidean")

character_vector <- c("a", "b", "c")
boolean_vector <- c(TRUE, FALSE,TRUE)

###################### Adding Vectors###############
A_vector <- c(1, 2, 3)
B_vector <- c(4, 5, 6)

# Take the sum of A_vector and B_vector
total_vector <- A_vector + B_vector

# Print out total_vector
print(total_vector)

######################List####################
# Put pop_1, pop_2 and pop_3 in a list: pop_list
pop_list <- list(pop_1, pop_2, pop_3)
# Display the structure of pop_list
print(str(pop_list))


# Poker winnings from Monday to Friday
poker_vector <- c(140, -50, 20, -120, 240)

# Roulette winnings from Monday to Friday
roulette_vector <- c(-24,-50,100,-350,10)

# Assign days as names of poker_vector
names(poker_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Assign days as names of roulette_vector
names(roulette_vector)<- c("Monday","Tuesday","Wednesday","Thursday","Friday")

# Assign to total_daily how much you won/lost on each day
total_daily <- poker_vector + roulette_vector
print(total_daily)

# Total winnings with poker
total_poker <- sum(poker_vector)

# Total winnings with roulette
total_roulette <-  sum(roulette_vector)

# Check if you realized higher total gains in poker than in roulette
print(total_roulette)
print (total_poker)

# Total winnings overall
total_week <- total_poker + total_roulette

# Print out total_week
  print(total_week)


# Poker and roulette winnings from Monday to Friday:
poker_vector <- c(140, -50, 20, -120, 240)
roulette_vector <- c(-24, -50, 100, -350, 10)
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector

# Which days did you make money on poker?
selection_vector <- poker_vector > 0

# Select from poker_vector these days
poker_winning_days <- poker_vector[selection_vector]

######################MATRIX CREATION################
# Construct a matrix with 3 rows that contain the numbers 1 up to 9
matrix(1:9, byrow = TRUE, nrow = 3)

# Box office Star Wars (in millions!)
new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)

# Create box_office
box_office <- c(new_hope,empire_strikes,return_jedi)

# Construct star_wars_matrix
star_wars_matrix <- matrix(box_office,byrow=TRUE,nrow =3)


######################Plotting###########################
attach(mtcars)
plot(wt, mpg, main="Mpg by Car Weight",
+      xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19)

#######Importing Data##########################
# Import swimming_pools.csv: pools
pools <- read.csv("swimming_pools.csv")
str(pools)
print(pools)

####Excel Import######
library(readxl)
# Read the sheets, one by one
pop_1 <- read_excel("urbanpop.xlsx", sheet = 1)
pop_2 <- read_excel("urbanpop.xlsx", sheet = 2)
pop_3 <- read_excel("urbanpop.xlsx", sheet= 3)
