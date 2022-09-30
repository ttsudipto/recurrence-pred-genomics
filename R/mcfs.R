options(java.parameters = "-Xmx2g")
library(rmcfs)

# projections - s, number of feature subsets
# projectionSize - |s|, number of features in one subset (default=sqrt(m)=sqrt(22126)~148)
# splits - t, number of splits (default=5)
# cutoffPermutations: the number of permutation runs. For a statistically significant result, it is >=20.

perform_mcfs <- function(data, ps, op_fname=NULL, n_permutations=20, save=FALSE, verbose=TRUE){
  result <- mcfs(Class ~ ., fix.data(data), projectionSize=ps, splits=5, cutoffPermutations=n_permutations, seed=42, threadsNumber=8, finalCV=TRUE, finalRuleset=FALSE, buildID=FALSE)
  if(save == TRUE){
    if(is.null(op_fname)){
      print('Error !!! No output file name provided')
      return()
    } else{
      saveRDS(result, op_fname)
    }
  }
  if(verbose == TRUE)
    print(head(result$RI, 10))
  return(result)
}

get_saved_mcfs_result <- function(fname, op_fname=NULL, saveRITable=FALSE, viewParams=FALSE){
  result <- readRDS(fname)
  print(head(result$RI, 10))
  print(result$cutoff)
  if(viewParams == TRUE)
    print(result$params)
  if(saveRITable == TRUE)
    if(is.null(op_fname)){
      print('Error !!! No output file name provided')
      return()
    } else{
      write.table(result$RI, file=op_fname, sep=',')
    }
  return(result)
}
