prefix_ip = 'input/NSCLC/'

read_target <- function(fname, colname){
  target_table <- read.table(fname, sep='\t', skip = 1, col.names = c('Sample', colname))
  targets <- as.array(as.character(target_table[[colname]]))
  return (targets)
}

read_data <- function(fname, do_scale=TRUE){
  d1 <- as.matrix(read.table(fname, sep='\t', header=FALSE))
  sample_names <- as.array(d1[1, 2:ncol(d1)])
  gene_names <- as.array(d1[2:nrow(d1), 1])
  d2 <- as.numeric(t(d1[2:nrow(d1), 2:ncol(d1)]))
  dim(d2) <- c(ncol(d1)-1, nrow(d1)-1)
  if(do_scale == TRUE){
    d3 <- scale(d2, center=FALSE)
    # d3 <- scale(d2, center=apply(d2, 2, min), scale=(apply(d2, 2, max)-apply(d2, 2, min)))
    data <- as.data.frame(d3)
    us_data <- as.data.frame(d2)
    for (cn in colnames(data)) {
      if (is.nan(min(data[[cn]])))
        data[[cn]]=us_data[[cn]]
    }
  } else{
    data <- as.data.frame(d2)
  }
  colnames(data) <- gene_names
  # data <- cbind(data, Class=targets)
  return (data)
}
