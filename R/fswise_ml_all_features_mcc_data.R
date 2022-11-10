nfeatures <- rep(c(20, 40, 60, 80, 100, 120, 140), 3)
ml <- c(rep("RF", 7), rep("MLP", 7), rep("SVM", 7))


get_data_mcfs_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.58, 0.55, 0.53, 0.53, 0.52, 0.52, 0.50)
    mcc_MLP_1 <- c(0.63, 0.62, 0.70, 0.69, 0.73, 0.73, 0.75)
    mcc_SVM_1 <- c(0.67, 0.72, 0.74, 0.74, 0.74, 0.75, 0.77)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.34, 0.18, 0.18, 0.15, 0.09, 0.15, 0.09)
    mcc_MLP_2 <- c(0.30, 0.46, 0.39, 0.39, 0.41, 0.41, 0.49)
    mcc_SVM_2 <- c(0.43, 0.50, 0.48, 0.45, 0.47, 0.48, 0.52)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.25, 0.25, 0.31, 0.35, 0.30, 0.22, 0.16)
    mcc_MLP_3 <- c(0.31, 0.36, 0.46, 0.42, 0.46, 0.46, 0.51)
    mcc_SVM_3 <- c(0.34, 0.40, 0.45, 0.45, 0.47, 0.48, 0.51)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_mcfs_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.76, 0.81, 0.87, 0.86, 0.89, 0.86, 0.86)
    mcc_MLP_1 <- c(0.79, 0.83, 0.87, 0.90, 0.90, 0.92, 0.91)
    mcc_SVM_1 <- c(0.80, 0.85, 0.92, 0.91, 0.92, 0.91, 0.91)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.77, 0.78, 0.85, 0.84, 0.85, 0.88, 0.86)
    mcc_MLP_2 <- c(0.79, 0.84, 0.86, 0.86, 0.85, 0.89, 0.88)
    mcc_SVM_2 <- c(0.80, 0.88, 0.91, 0.93, 0.92, 0.92, 0.92)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.76, 0.78, 0.83, 0.83, 0.84, 0.85, 0.86)
    mcc_MLP_3 <- c(0.72, 0.83, 0.84, 0.87, 0.88, 0.88, 0.88)
    mcc_SVM_3 <- c(0.63, 0.82, 0.85, 0.89, 0.91, 0.91, 0.92)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_boruta_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.52, 0.53, 0.53, 0.53, 0.50, 0.47, 0.50)
    mcc_MLP_1 <- c(0.71, 0.60, 0.64, 0.62, 0.66, 0.69, 0.71)
    mcc_SVM_1 <- c(0.79, 0.68, 0.68, 0.66, 0.74, 0.74, 0.75)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.24, 0.12, 0.06, 0.00, 0.00, 0.06, 0.00)
    mcc_MLP_2 <- c(0.38, 0.37, 0.35, 0.38, 0.40, 0.47, 0.46)
    mcc_SVM_2 <- c(0.44, 0.48, 0.52, 0.48, 0.48, 0.54, 0.50)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.29, 0.22, 0.22, 0.21, 0.21, 0.21, 0.12)
    mcc_MLP_3 <- c(0.36, 0.33, 0.32, 0.34, 0.38, 0.39, 0.39)
    mcc_SVM_3 <- c(0.46, 0.39, 0.41, 0.48, 0.46, 0.47, 0.47)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_boruta_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.76, 0.88, 0.88, 0.83, 0.89, 0.84, 0.82)
    mcc_MLP_1 <- c(0.88, 0.91, 0.90, 0.91, 0.94, 0.95, 0.94)
    mcc_SVM_1 <- c(0.88, 0.93, 0.95, 0.94, 0.97, 0.97, 0.99)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.75, 0.77, 0.79, 0.80, 0.79, 0.78, 0.77)
    mcc_MLP_2 <- c(0.82, 0.82, 0.86, 0.85, 0.86, 0.89, 0.89)
    mcc_SVM_2 <- c(0.78, 0.92, 0.93, 0.91, 0.92, 0.90, 0.90)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.74, 0.78, 0.79, 0.83, 0.79, 0.79, 0.77)
    mcc_MLP_3 <- c(0.76, 0.83, 0.83, 0.86, 0.84, 0.83, 0.84)
    mcc_SVM_3 <- c(0.77, 0.83, 0.86, 0.88, 0.91, 0.90, 0.90)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_combined_mcfs_boruta_original <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.49, 0.56, 0.58, 0.55, 0.52, 0.47, 0.48)
    mcc_MLP_1 <- c(0.62, 0.66, 0.71, 0.73, 0.73, 0.74, 0.74)
    mcc_SVM_1 <- c(0.72, 0.76, 0.79, 0.77, 0.73, 0.77, 0.78)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") { 
    mcc_RF_2 <- c(0.39, 0.15, 0.09, 0.15, 0.08, 0.12, 0.12)
    mcc_MLP_2 <- c(0.47, 0.50, 0.40, 0.42, 0.40, 0.44, 0.49)
    mcc_SVM_2 <- c(0.46, 0.51, 0.46, 0.45, 0.46, 0.49, 0.50)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.32, 0.29, 0.26, 0.25, 0.21, 0.20, 0.23)
    mcc_MLP_3 <- c(0.27, 0.37, 0.41, 0.44, 0.44, 0.46, 0.45)
    mcc_SVM_3 <- c(0.42, 0.38, 0.42, 0.50, 0.47, 0.50, 0.47)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}


get_data_combined_mcfs_boruta_smote <- function(ds) {
  if(ds == "dataset1") {
    mcc_RF_1 <- c(0.71, 0.76, 0.88, 0.86, 0.90, 0.88, 0.87)
    mcc_MLP_1 <- c(0.84, 0.87, 0.92, 0.91, 0.90, 0.91, 0.92)
    mcc_SVM_1 <- c(0.83, 0.86, 0.97, 0.91, 0.92, 0.94, 0.92)
    mcc_values_1 <- c(mcc_RF_1, mcc_MLP_1, mcc_SVM_1)
    data_1 <- data.frame(nfeatures, ml, mcc_values_1)
    # print(data_1)
    return(list("data"=data_1, "mcc_values"=mcc_values_1))
  }
  
  if(ds == "dataset2") {
    mcc_RF_2 <- c(0.80, 0.81, 0.85, 0.84, 0.88, 0.88, 0.86)
    mcc_MLP_2 <- c(0.79, 0.88, 0.86, 0.89, 0.88, 0.88, 0.88)
    mcc_SVM_2 <- c(0.81, 0.89, 0.91, 0.91, 0.92, 0.94, 0.94)
    mcc_values_2 <- c(mcc_RF_2, mcc_MLP_2, mcc_SVM_2)
    data_2 <- data.frame(nfeatures, ml, mcc_values_2)
    # print(data_2)
    return(list("data"=data_2, "mcc_values"=mcc_values_2))
  }
  
  if(ds == "dataset3") {
    mcc_RF_3 <- c(0.73, 0.77, 0.80, 0.81, 0.82, 0.86, 0.87)
    mcc_MLP_3 <- c(0.76, 0.81, 0.81, 0.87, 0.87, 0.90, 0.90)
    mcc_SVM_3 <- c(0.72, 0.84, 0.85, 0.88, 0.88, 0.95, 0.95)
    mcc_values_3 <- c(mcc_RF_3, mcc_MLP_3, mcc_SVM_3)
    data_3 <- data.frame(nfeatures, ml, mcc_values_3)
    # print(data_3)
    return(list("data"=data_3, "mcc_values"=mcc_values_3))
  }
}
