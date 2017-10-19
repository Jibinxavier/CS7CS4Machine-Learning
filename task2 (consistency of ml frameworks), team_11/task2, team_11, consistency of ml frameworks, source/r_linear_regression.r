
sumdata_noise_path = "./data/with noise/The SUM dataset, with noise.csv"

# the

dataset = read.csv(sumdata_noise_path, sep=";"
                  )

## + is way of specifying the features
## ~ to indicate the target
multi.fit = lm(Noisy.Target~Feature.1+Feature.2+Feature.3+Feature.4+Feature.5..meaningless.+Feature.6+Feature.7+Feature.8+Feature.9+Feature.10, data=dataset)

summary(multi.fit)


