library(ggplot2)
library(patchwork)

# ds <- "dataset1"
# ds <- "dataset2"
ds <- "dataset3"

var <- "mcc"
# var <- "bacc"

if(var == "mcc") {
  source('R/fswise_ml_all_features_mcc_data.R')
  ylab <- "MCC"
} else {
  source('R/fswise_ml_all_features_bacc_data.R')
  ylab <- "Balanced accuracy"
}

titles <- c("MCFS (SMOTE)", "Boruta (SMOTE)", "MCFS + Boruta (SMOTE)",
            "MCFS (Original)", "Boruta (Original)", "MCFS + Boruta (Original)")

# SMOTE
f1 <- get_data_mcfs_smote(ds)
data_1 <- f1$data; mcc_values_1 <- f1$mcc_values
f2 <- get_data_boruta_smote(ds)
data_2 <- f2$data; mcc_values_2 <- f2$mcc_values
f3 <- get_data_combined_mcfs_boruta_smote(ds)
data_3 <- f3$data; mcc_values_3 <- f3$mcc_values

# Original
f4 <- get_data_mcfs_original(ds)
data_4 <- f4$data; mcc_values_4 <- f4$mcc_values
f5 <- get_data_boruta_original(ds)
data_5 <- f5$data; mcc_values_5 <- f5$mcc_values
f6 <- get_data_combined_mcfs_boruta_original(ds)
data_6 <- f6$data; mcc_values_6 <- f6$mcc_values

lty <- c("dashed", "solid", "dotted", "dotdash", "11")
sty <- c(16, 1, 0, 2, 17)
lwd <- c(0.5, 0.5, 0.5, 0.5, 0.8)
plot_theme <- theme(plot.title=element_text(size=10),
                    panel.background=element_rect(fill="white"), 
                    panel.grid=element_line(color="grey90"),
                    panel.border=element_rect(color="black", fill=NA),
                    axis.title=element_text(size=9), 
                    axis.text=element_text(size=8, color="gray10",), 
                    axis.ticks.length=unit(7, "pt")
)
legend_theme <- theme(legend.title=element_blank(),
                      legend.text=element_text(size=10),
                      legend.spacing.y=unit(5, "pt"),
                      legend.background=element_rect(fill="gray95"),
                      legend.direction="horizontal",
                      legend.position="bottom",
                      legend.key.width = unit(80, "pt")
)

# SMOTE
plot_1 <- ggplot(data_1, mapping=aes(x=nfeatures, y=mcc_values_1, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  # c(rep("solid",7), rep("dashed", 7), rep("dotted",7), rep("dotdash",7), rep("twodash",7))
  xlab("No. of features") + ylab("") +
  ggtitle(paste0("(b) ", titles[1])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_1

plot_2 <- ggplot(data_2, mapping=aes(x=nfeatures, y=mcc_values_2, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  xlab("No. of features") + ylab("") +
  ggtitle(paste0("(d) ", titles[2])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_2

plot_3 <- ggplot(data_3, mapping=aes(x=nfeatures, y=mcc_values_3, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  xlab("No. of features") + ylab("") +
  ggtitle(paste0("(f) ", titles[3])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_3

# design <- "
#   12
#   34
#   56
#   78
# "
# svg(filename='output/NSCLC/plots/fswise_ml_all_features_smote.svg', height=10, width=9)
# plot_1 + plot_2 + plot_3 + guide_area() + plot_layout(design = design, guides="collect")
# dev.off()


# Original
plot_4 <- ggplot(data_4, mapping=aes(x=nfeatures, y=mcc_values_4, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  # c(rep("solid",7), rep("dashed", 7), rep("dotted",7), rep("dotdash",7), rep("twodash",7))
  xlab("No. of features") + ylab(ylab) +
  ggtitle(paste0("(a) ", titles[4])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_4

plot_5 <- ggplot(data_5, mapping=aes(x=nfeatures, y=mcc_values_5, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  xlab("No. of features") + ylab(ylab) +
  ggtitle(paste0("(c) ", titles[5])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_5

plot_6 <- ggplot(data_6, mapping=aes(x=nfeatures, y=mcc_values_6, group=ml)) +
  geom_line(aes(group=ml, linetype=ml, size=ml)) +
  geom_point(aes(shape=ml), size=2) +
  xlab("No. of features") + ylab(ylab) +
  ggtitle(paste0("(e) ", titles[6])) +
  scale_linetype_manual(values=lty) +
  scale_shape_manual(values=sty) +
  scale_size_manual(values=lwd) +
  scale_x_discrete(limits=nfeatures) +
  coord_cartesian(ylim = c(0, 1)) +
  plot_theme + theme(legend.position="none") #+ legend_theme
# plot_6

design <- "
  41
  52
  63
  77
"
# svg(filename=paste0("output/",ds,"/plots/fswise_ml_all_features_",ds,"_",var,".svg"), height=10, width=9)
plot_1 + plot_2 + plot_3 + plot_4 + plot_5 + plot_6 + legend_theme + guide_area() + plot_layout(design = design, guides="collect")
# dev.off()
