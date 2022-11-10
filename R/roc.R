library(ggplot2)
library(patchwork)

lwd <- c(0.7,0.5,0.3,0.8,0.5)
lty <- c(4,3,1,2,5)
xlab <- "False positive rate"
ylab <- "True positive rate"
plot_theme <- theme(panel.background=element_rect(fill="white"),
                    panel.grid=element_line(color="grey95"),
                    panel.border=element_rect(color="black", fill=NA),
                    axis.title=element_text(size=12),
                    axis.text=element_text(size=10, color="gray10",),
                    axis.ticks.length=unit(7, "pt")
)
legend_theme <- theme(legend.title=element_blank(),
                      legend.text=element_text(size=11),
                      legend.position="bottom",
                      legend.key.width = unit(30, "pt")
)

get_file_name <- function(ds, sample_type){
  return(paste0("output/", ds, "/ROC/roc_", sample_type, "_optimal.csv"))
}

get_ml_data <- function(ds, sample_type){
  fileName <- get_file_name(ds, sample_type)
  print(fileName)
  data <- read.csv(fileName, check.names = FALSE)
  col_names <- colnames(data)[-1]
  ml <- c()
  for (cn in col_names) {
    cns <- unlist(strsplit(cn, " "))
    ml <- c(ml, rep(c(paste0(cns[1], " (", cns[2], cns[3], cns[4], ")")), 100))
  }
  ml <- as.array(ml)
  x <- rep(data$FPR, 3)
  svm <- data[, 2]
  mlp <- data[, 3]
  rf <- data[, 4]
  y <- c(svm, mlp, rf)
  plot_data <- data.frame(ml, x, y)
  return(list("plot_data"=plot_data, "x"=x, "y"=y, "ml"=ml))
}

get_plot <- function(ds) {
  temp_original <- get_ml_data(ds, "original")
  plot_data_original <- temp_original$plot_data
  ml_original <- temp_original$ml
  x_original <- temp_original$x
  y_original <- temp_original$y
  temp_smote <- get_ml_data(ds, "smote")
  plot_data_smote <- temp_smote$plot_data
  ml_smote <- temp_smote$ml
  x_smote <- temp_smote$x
  y_smote <- temp_smote$y
  
  original_plot <- ggplot(plot_data_original, mapping=aes(x=x_original, y=y_original, group=ml_original)) +
    geom_line(aes(group=ml_original, linetype=ml_original, size=ml_original)) +
    geom_abline(slope=1, intercept=0, color="gray80", size=0.2) +
    scale_linetype_manual(values=lty) + scale_size_manual(values=lwd) +
    ggtitle("(a) Original") + xlab(xlab) + ylab(ylab) +
    guides(linetype = guide_legend(nrow=3, ncol=2, byrow = TRUE)) +
    plot_theme + legend_theme
  
  smote_plot <- ggplot(plot_data_smote, mapping=aes(x=x_smote, y=y_smote, group=ml_smote)) +
    geom_line(aes(group=ml_smote, linetype=ml_smote, size=ml_smote)) +
    geom_abline(slope=1, intercept=0, color="gray80", size=0.2) +
    scale_linetype_manual(values=lty) + scale_size_manual(values=lwd) +
    ggtitle("(b) SMOTE") + xlab(xlab) + ylab("") +
    guides(linetype = guide_legend(nrow=3, ncol=2, byrow = TRUE)) +
    plot_theme + legend_theme
  
  return(list("original"=original_plot, "smote"=smote_plot))
}

# plot <- get_plot("dataset1")
# # svg(paste0("output/dataset1/plots/roc_plot_optimal.svg"), width=13, height=6)
# plot$original | plot$smote
# # dev.off()

# plot <- get_plot("dataset2")
# # svg(paste0("output/dataset2/plots/roc_plot_optimal.svg"), width=13, height=6)
# plot$original | plot$smote
# # dev.off()

# plot <- get_plot("dataset3")
# # svg(paste0("output/dataset3/plots/roc_plot_optimal.svg"), width=13, height=6)
# plot$original | plot$smote
# # dev.off()

