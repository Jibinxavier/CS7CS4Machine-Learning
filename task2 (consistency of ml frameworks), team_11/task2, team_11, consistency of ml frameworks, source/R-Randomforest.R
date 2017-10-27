# Import the data set
setwd("~/Documents/Project/CS7CS4Machine-Learning/task1 (performance by dataset size), team_11/task1, team_11, performance by dataset size, source code")
sum_noise_dataset <- read.table("data/without noise/The SUM dataset, without noise.csv", header=TRUE, sep=";", stringsAsFactors=FALSE, nrows=100000)

# sum_noise_dataset <- read.csv("data/without noise/The SUM dataset, without noise.csv")

# Print some records from data set readingSkills.
head(sum_noise_dataset)

fitsRandomForest <- function(fmla, dataset ){
  randomForest(fmla, data = dataset)
}

# Load the party package. It will automatically load other required packages.
# install.packages("randomForest")
library(randomForest)

# Split dataset into Training set and Testing set, in a 30/70 ratio
# install.packages("caTools")
library(caTools)
set.seed(123)
split <- sample.split(sum_noise_dataset$Target,SplitRatio = 0.7)
training_set <- subset(sum_noise_dataset, split == TRUE)
test_set <- subset(sum_noise_dataset, split == FALSE)

# Create the forest.
# Use 'Target' as regression target
forest <- randomForest(Target ~ . - Target - Target.Class - Instance, 
                       data = training_set)

# Apply random forest
result = predict(forest, test_set)

# Function that returns Root Mean Squared Error
rmse <- function(error)
{
  sqrt(mean(error^2))
}

# Function that returns Mean Absolute Error
mae <- function(error)
{
  mean(abs(error))
}

print(rmse(result-test_set$Target))
print(mae(result-test_set$Target))

# Import the data set
sum_dataset <- read.table("data/without noise/kc_house_data.csv", header=TRUE, sep=";", stringsAsFactors=FALSE, nrows=10000)

# Print some records from data set readingSkills.
head(sum_noise_dataset)


# Split dataset into Training set and Testing set, in a 30/70 ratio
# install.packages("caTools")
set.seed(123)
split <- sample.split(sum_noise_dataset$Target,SplitRatio = 0.7)
training_set <- subset(sum_noise_dataset, split == TRUE)
test_set <- subset(sum_noise_dataset, split == FALSE)

# Create the forest.
# Use 'Target' as regression target
forest <- randomForest(Target ~ . - Target - Target.Class - Instance, 
                       data = training_set)

# Apply random forest
result = predict(forest, test_set)

# Function that returns Root Mean Squared Error
rmse <- function(error)
{
  sqrt(mean(error^2))
}

# Function that returns Mean Absolute Error
mae <- function(error)
{
  mean(abs(error))
}

print(rmse(result-test_set$Target))
print(mae(result-test_set$Target))











