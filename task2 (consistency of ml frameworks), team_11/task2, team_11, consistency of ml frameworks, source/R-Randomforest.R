# Load the party package. It will automatically load other required packages.
# install.packages("randomForest")
library(randomForest)

# Split dataset into Training set and Testing set, in a 30/70 ratio
# install.packages("caTools")
library(caTools)


# Split dataset into Training set and Testing set, in a 30/70 ratio
# install.packages('caret', dependencies = TRUE)
library(caret)

# Set Work Directory
setwd("~/Documents/Project/CS7CS4Machine-Learning/task1 (performance by dataset size), team_11/task1, team_11, performance by dataset size, source code")

# Set Up Evaluaion Method
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


##################################################################################################################

# Import the data set
sum_dataset <- read.table("data/without noise/The SUM dataset, without noise.csv", header=TRUE, sep=";", stringsAsFactors=FALSE, nrow=100000)

# Print some records from data set
head(sum_dataset)

unneededFeature <- c('Target', 'Target.Class', 'Instance')

# Feature Scaling
sum_dataset[, -ncol(sum_dataset)] <- scale(sum_dataset[, -ncol(sum_dataset)])
# 
# # Splitting
# set.seed(123)
# split <- sample.split(sum_dataset$Target,SplitRatio = 0.7)
# training_set <- subset(sum_dataset, split == TRUE)
# test_set <- subset(sum_dataset, split == FALSE)

# Create the forest.
# Use 'Target' as regression target
fmla <- as.formula(paste("Target ~ . - ", paste(collapse = '-', unneededFeature)))

# model_test_split(sum_dataset, fmla)
# Splitting the data
set.seed(123)
split <- sample.split(sum_dataset[,1],SplitRatio = 0.7)
training_set <- subset(sum_dataset, split == TRUE)
test_set <- subset(sum_dataset, split == FALSE)

# Create the forest based on the data
forest <- randomForest(fmla, training_set)

# Apply random forest
result = predict(forest, test_set)

print(rmse(result-test_set$price))
print(mae(result-test_set$price))

# model_cross_validation(sum_dataset, fmla)

# define training control
train_control <- trainControl(method="cv", number=10)

# fix the parameters of the algorithm
grid <- expand.grid(.fL=c(0), .usekernel=c(FALSE))

# train the model
model <- train(fmla, data=dataset, trControl=train_control, method='rf', tuneGrid=grid)

# summarize results
print(model)
chunk <- c()

# # Apply random forest
# result = predict(forest, test_set)
# 
# print(rmse(result-test_set$Target))
# print(mae(result-test_set$Target))

#######################################################################################################################################

# Import the data set
house_dataset <- read.table("data/kc_house_data.csv", header=TRUE, sep=",", stringsAsFactors=FALSE, nrows=10000)

# Print some records from data set readingSkills.
head(house_dataset)

# Feature Scaling
nums <- sapply(house_dataset, is.numeric)
house_dataset[,nums] <- scale(house_dataset[,nums])

# Split dataset into Training set and Testing set, in a 30/70 ratio
# install.packages("caTools")
set.seed(123)
split <- sample.split(house_dataset$price,SplitRatio = 0.7)
training_set <- subset(house_dataset, split == TRUE)
test_set <- subset(house_dataset, split == FALSE)

features <- c('bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'condition', 'sqft_above', 'yr_built',
                         'sqft_living15', 'sqft_lot15')

## Create a formula for a model with a large number of variables:
fmla <- as.formula(paste("Target ~ . - ", paste(collapse = '-', unneededFeature)))
model_test_split(sum_dataset, fmla)
model_cross_validation(sum_dataset, fmla)

# # Apply random forest
# result = predict(forest, test_set)
# 
# print(rmse(result-test_set$price))
# print(mae(result-test_set$price))

