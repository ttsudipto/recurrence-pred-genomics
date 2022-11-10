nfeatures <- rep(c(20, 40, 60, 80, 100, 120, 140), 3)
ml <- c(rep("RF", 7), rep("MLP", 7), rep("SVM", 7))


get_data_mcfs_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.75, 0.72, 0.68, 0.68, 0.69, 0.69, 0.69)
    mcc_MLP_1 <- c(0.81, 0.80, 0.82, 0.82, 0.83, 0.84, 0.84)
    mcc_SVM_1 <- c(0.81, 0.85, 0.84, 0.85, 0.86, 0.87, 0.86)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.59, 0.54, 0.53, 0.53, 0.52, 0.53, 0.52)
    mcc_MLP_2 <- c(0.62, 0.69, 0.69, 0.68, 0.67, 0.67, 0.75)
    mcc_SVM_2 <- c(0.73, 0.76, 0.79, 0.75, 0.77, 0.77, 0.72)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.58, 0.56, 0.57, 0.59, 0.58, 0.56, 0.54)
    mcc_MLP_3 <- c(0.66, 0.67, 0.73, 0.70, 0.73, 0.71, 0.73)
    mcc_SVM_3 <- c(0.34, 0.40, 0.45, 0.45, 0.47, 0.48, 0.51)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_mcfs_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.88, 0.90, 0.93, 0.93, 0.94, 0.93, 0.93)
    mcc_MLP_1 <- c(0.89, 0.91, 0.93, 0.95, 0.95, 0.96, 0.95)
    mcc_SVM_1 <- c(0.89, 0.92, 0.96, 0.95, 0.96, 0.95, 0.95)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.89, 0.89, 0.93, 0.92, 0.92, 0.94, 0.93)
    mcc_MLP_2 <- c(0.90, 0.92, 0.93, 0.93, 0.93, 0.94, 0.94)
    mcc_SVM_2 <- c(0.90, 0.94, 0.95, 0.96, 0.96, 0.96, 0.96)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.88, 0.89, 0.91, 0.92, 0.92, 0.92, 0.93)
    mcc_MLP_3 <- c(0.85, 0.91, 0.92, 0.93, 0.94, 0.94, 0.94)
    mcc_SVM_3 <- c(0.81, 0.91, 0.92, 0.94, 0.95, 0.95, 0.96)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_boruta_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.71, 0.68, 0.68, 0.68, 0.67, 0.66, 0.67)
    mcc_MLP_1 <- c(0.81, 0.78, 0.78, 0.77, 0.80, 0.79, 0.81)
    mcc_SVM_1 <- c(0.89, 0.83, 0.82, 0.79, 0.85, 0.87, 0.87)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.57, 0.52, 0.51, 0.50, 0.50, 0.51, 0.50)
    mcc_MLP_2 <- c(0.66, 0.65, 0.69, 0.63, 0.65, 0.69, 0.71)
    mcc_SVM_2 <- c(0.68, 0.66, 0.69, 0.64, 0.67, 0.81, 0.76)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.58, 0.55, 0.55, 0.53, 0.53, 0.54, 0.52)
    mcc_MLP_3 <- c(0.64, 0.64, 0.63, 0.64, 0.65, 0.66, 0.65)
    mcc_SVM_3 <- c(0.46, 0.39, 0.41, 0.48, 0.46, 0.47, 0.47)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_boruta_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.88, 0.94, 0.94, 0.91, 0.95, 0.92, 0.91)
    mcc_MLP_1 <- c(0.94, 0.95, 0.95, 0.95, 0.97, 0.97, 0.97)
    mcc_SVM_1 <- c(0.93, 0.97, 0.97, 0.97, 0.99, 0.99, 0.99)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.87, 0.89, 0.89, 0.90, 0.90, 0.89, 0.89)
    mcc_MLP_2 <- c(0.91, 0.91, 0.93, 0.93, 0.93, 0.94, 0.94)
    mcc_SVM_2 <- c(0.89, 0.96, 0.96, 0.96, 0.96, 0.95, 0.95)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.87, 0.89, 0.89, 0.92, 0.89, 0.89, 0.88)
    mcc_MLP_3 <- c(0.88, 0.91, 0.91, 0.93, 0.92, 0.91, 0.92)
    mcc_SVM_3 <- c(0.88, 0.91, 0.93, 0.94, 0.95, 0.95, 0.95)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_combined_mcfs_boruta_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.69, 0.71, 0.72, 0.70, 0.69, 0.66, 0.67)
    mcc_MLP_1 <- c(0.77, 0.81, 0.81, 0.83, 0.83, 0.85, 0.85)
    mcc_SVM_1 <- c(0.84, 0.84, 0.86, 0.84, 0.86, 0.87, 0.88)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") { 
    mcc_RF_2 <- c(0.60, 0.54, 0.52, 0.53, 0.52, 0.53, 0.52)
    mcc_MLP_2 <- c(0.71, 0.71, 0.67, 0.68, 0.64, 0.68, 0.70)
    mcc_SVM_2 <- c(0.66, 0.77, 0.78, 0.76, 0.73, 0.79, 0.79)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.58, 0.57, 0.56, 0.56, 0.54, 0.54, 0.55)
    mcc_MLP_3 <- c(0.64, 0.67, 0.68, 0.70, 0.70, 0.69, 0.69)
    mcc_SVM_3 <- c(0.42, 0.38, 0.42, 0.50, 0.47, 0.50, 0.47)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_combined_mcfs_boruta_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.85, 0.88, 0.94, 0.93, 0.95, 0.94, 0.93)
    mcc_MLP_1 <- c(0.92, 0.93, 0.96, 0.95, 0.95, 0.95, 0.96)
    mcc_SVM_1 <- c(0.91, 0.93, 0.99, 0.95, 0.96, 0.97, 0.96)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.90, 0.91, 0.93, 0.92, 0.94, 0.94, 0.93)
    mcc_MLP_2 <- c(0.89, 0.94, 0.93, 0.95, 0.94, 0.94, 0.94)
    mcc_SVM_2 <- c(0.90, 0.94, 0.95, 0.96, 0.96, 0.97, 0.97)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.86, 0.88, 0.90, 0.90, 0.91, 0.93, 0.93)
    mcc_MLP_3 <- c(0.88, 0.90, 0.90, 0.93, 0.93, 0.95, 0.95)
    mcc_SVM_3 <- c(0.86, 0.92, 0.92, 0.94, 0.94, 0.97, 0.97)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}
