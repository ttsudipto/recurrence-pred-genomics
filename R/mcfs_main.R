source('R/reader.R')

tf_1 <- 'genomics_input_labels_dataset1.tsv'
tf_2 <- 'genomics_input_labels_dataset2.tsv'
tf_3 <- 'genomics_input_labels_dataset3.tsv'
if_1 <- 'genomics_input_dataset1.tsv'
if_2 <- 'genomics_input_dataset2.tsv'
if_3 <- 'genomics_input_dataset3.tsv'

# prefix_op_mcfs = 'output/dataset1/FS/MCFS/'
# prefix_op_mcfs = 'output/dataset2/FS/MCFS/'
# prefix_op_mcfs = 'output/dataset3/FS/MCFS/'

# targets <- read_target(paste0(prefix_ip, tf_1), 'Recurrence')
# targets <- read_target(paste0(prefix_ip, tf_2), 'Recurrence')
# targets <- read_target(paste0(prefix_ip, tf_3), 'Recurrence')

# data <- read_data(paste0(prefix_ip, 'genomics_input.tsv'), do_scale=FALSE)
# data <- cbind(data, Class=targets)
# dim(data)
# for (cn in colnames(data)[1:10]){
#   print(c(min(data[[cn]]), max(data[[cn]])))
# }

# scaled_data <- read_data(paste0(prefix_ip, if_1), do_scale=TRUE)
# scaled_data <- cbind(scaled_data, Class=targets)
# scaled_data <- read_data(paste0(prefix_ip, if_2), do_scale=TRUE)
# scaled_data <- cbind(scaled_data, Class=targets)
# scaled_data <- read_data(paste0(prefix_ip, if_3), do_scale=TRUE)
# scaled_data <- cbind(scaled_data, Class=targets)
# dim(scaled_data)
# for (cn in colnames(scaled_data)[1:10]){
#   print(c(min(scaled_data[[cn]]), max(scaled_data[[cn]]), mean(scaled_data[[cn]])))
# }

source('R/mcfs.R')

################## Perform MCFS ##################
# result1 <- perform_mcfs(data, 300, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_300ps.rds'), save=TRUE)
# result2 <- perform_mcfs(data, 400, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_400ps.rds'), save=TRUE)
# result3 <- perform_mcfs(data, 500, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_500ps.rds'), save=TRUE)

# result4 <- perform_mcfs(scaled_data, 300, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_300ps_scaled.rds'), save=TRUE)
# result5 <- perform_mcfs(scaled_data, 400, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_400ps_scaled.rds'), save=TRUE)
# result6 <- perform_mcfs(scaled_data, 500, op_fname=paste0(prefix_op_mcfs, 'features_MCFS_500ps_scaled.rds'), save=TRUE)

################ Check MCFS result ################
# result7 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_300ps.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_300ps.csv'), saveRITable=FALSE, viewParams=FALSE)
# result8 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_400ps.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_400ps.csv'), saveRITable=FALSE, viewParams=FALSE)
# result9 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_500ps.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_500ps.csv'), saveRITable=FALSE, viewParams=FALSE)

# result10 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_300ps_scaled.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_300ps_scaled.csv'), saveRITable=TRUE, viewParams=TRUE)
# result11 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_400ps_scaled.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_400ps_scaled.csv'), saveRITable=FALSE, viewParams=FALSE)
# result12 <- get_saved_mcfs_result(paste0(prefix_op_mcfs, 'features_MCFS_500ps_scaled.rds'), op_fname=paste0(prefix_op_mcfs, 'features_MCFS_500ps_scaled.csv'), saveRITable=FALSE, viewParams=FALSE)




# projectionSizes = c(300, 400, 500)
# results = c()
# for(ps in projectionSizes){
#   result <- mcfs(Class ~ ., fix.data(d3), projectionSize=ps, splits=5, splitSetSize=100, cutoffPermutations = 20, seed = 42, threadsNumber = 4, finalRuleset = FALSE, finalCV = TRUE)
#   append(results, result)
# }
# for(result in results){
#   head(result$RI, 100)
# }

