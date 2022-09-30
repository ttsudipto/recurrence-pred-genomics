source('R/reader.R')

tf_1 <- 'genomics_input_labels_dataset1.tsv'
tf_2 <- 'genomics_input_labels_dataset2.tsv'
tf_3 <- 'genomics_input_labels_dataset3.tsv'
if_1 <- 'genomics_input_dataset1.tsv'
if_2 <- 'genomics_input_dataset2.tsv'
if_3 <- 'genomics_input_dataset3.tsv'

# prefix_op_boruta = 'output/dataset1/FS/Boruta/'
# prefix_op_boruta = 'output/dataset2/FS/Boruta/'
# prefix_op_boruta = 'output/dataset3/FS/Boruta/'

# targets <- read_target(paste0(prefix_ip, tf_1), 'Recurrence')
# targets <- read_target(paste0(prefix_ip, tf_2), 'Recurrence')
# targets <- read_target(paste0(prefix_ip, tf_3), 'Recurrence')
# print(dim(targets))

# data <- read_data(paste0(prefix_ip, 'genomics_input.tsv'), do_scale=FALSE)
# print(dim(data))

# scaled_data <- read_data(paste0(prefix_ip, if_1), do_scale=TRUE)
# scaled_data <- read_data(paste0(prefix_ip, if_2), do_scale=TRUE)
# scaled_data <- read_data(paste0(prefix_ip, if_3), do_scale=TRUE)
# print(dim(scaled_data))

library(Boruta)
set.seed(42)

################## Perform Boruta ##################

# result1 <- Boruta(scaled_data, factor(targets), pValue=0.01, maxRuns=1001, doTrace=3)
# # saveRDS(result1, paste0(prefix_op_boruta, 'features_boruta_1000p0.01.rds'))
# stats1 = attStats(result1)
# print(head(stats1[order(stats1[['meanImp']], decreasing=TRUE),], 100))

# result2 <- Boruta(scaled_data, factor(targets), pValue=0.05, maxRuns=1001, doTrace=3)
# # saveRDS(result2, paste0(prefix_op_boruta, 'features_boruta_1000p0.05.rds'))
# stats2 = attStats(result2)
# print(head(stats2[order(stats2[['meanImp']], decreasing=TRUE),], 100))

# result3 <- Boruta(scaled_data, factor(targets), pValue=0.1, maxRuns=1001, doTrace=3)
# # saveRDS(result3, paste0(prefix_op_boruta, 'features_boruta_1000p0.1.rds'))
# stats3 = attStats(result3)
# print(head(stats3[order(stats3[['meanImp']], decreasing=TRUE),], 100))

################## Read Boruta results ##################

# result4 <- readRDS(paste0(prefix_op_boruta, 'features_boruta_1000p0.01.rds'))
# stats4 = attStats(result4)
# # write.table(stats4, file=paste0(prefix_op_boruta, 'features_boruta_1000p0.01.csv'), sep=',')
# print(head(stats4[order(stats4[['meanImp']], decreasing=TRUE),], 100))

# result5 <- readRDS(paste0(prefix_op_boruta, 'features_boruta_1000p0.05.rds'))
# stats5 = attStats(result5)
# # write.table(stats5, file=paste0(prefix_op_boruta, 'features_boruta_1000p0.05.csv'), sep=',')
# print(head(stats5[order(stats5[['meanImp']], decreasing=TRUE),], 100))

# result6 <- readRDS(paste0(prefix_op_boruta, 'features_boruta_1000p0.1.rds'))
# stats6 = attStats(result6)
# # write.table(stats6, file=paste0(prefix_op_boruta, 'features_boruta_1000p0.1.csv'), sep=',')
# print(head(stats6[order(stats6[['meanImp']], decreasing=TRUE),], 100))



# print(result$timeTaken)
# stats = attStats(result)
# head(stats[order(stats[['normHits']], decreasing=TRUE),], 15)
# result$finalDecision[1:10]
# t(result$ImpHistory)[1:10,]

# write.csv(stats[order(stats[['meanImp']], decreasing=TRUE),], paste0(prefix_op_boruta, 'fs.csv'))
