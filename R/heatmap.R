source('R/reader.R')

hm_gene_count <- 140
hm_path_prefix <- 'output/'

dataset <- ''
# dataset <- 'dataset1'
# dataset <- 'dataset2'
# dataset <- 'dataset3'

tfn <- paste0('genomics_input_labels_', dataset, '.tsv')
ifn <- paste0('genomics_input_', dataset, '.tsv')

targets <- read_target(paste0(prefix_ip, tfn), 'Recurrence')
print(dim(targets))
scaled_data <- as.matrix(read_data(paste0(prefix_ip, ifn), do_scale=TRUE))
print(dim(scaled_data))

# targets <- read_target(paste0(prefix_ip, 'genomics_input_labels_CPTAC-3_kidney.tsv'), 'Recurrence')
# print(dim(targets))
# scaled_data <- as.matrix(read_data(paste0(prefix_ip, 'genomics_input_CPTAC-3_kidney.tsv'), do_scale=TRUE))
# print(dim(scaled_data))
# targets <- read_target(paste0(prefix_ip, 'genomics_input_labels_CPTAC-3_pancreas.tsv'), 'Recurrence')
# print(dim(targets))
# scaled_data <- as.matrix(read_data(paste0(prefix_ip, 'genomics_input_CPTAC-3_pancreas.tsv'), do_scale=TRUE))
# print(dim(scaled_data))

library("pheatmap")
cex <- length(targets)
color <- rev(grDevices::hcl.colors(10,palette="Purples 3"))
row.annotations <- replace(replace(targets, targets=="0", "Recurence = no"),
                           targets=="1", "Recurence = yes")

############### MCFS ###############
fs_result1 <- read.csv(paste0('output/', dataset, '/FS/MCFS/features_MCFS_300ps_scaled.csv'))
gene_indices1 <- fs_result1[['Index']]
gene_names1 <- fs_result1[['attribute']]
print(c(dim(fs_result1), length(gene_indices1), length(gene_names1)))
hm_data1 <- scaled_data[, gene_indices1[1:hm_gene_count]]
rownames(hm_data1) <- as.array(1:length(targets))
hm_data1 <- hm_data1[order(targets),]
print(dim(hm_data1))

# svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_mcfs_top_', hm_gene_count, '.svg'), height=10, width=17)
pheatmap(hm_data1, color=color, border_color=NA, show_rownames=FALSE,
         cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
         annotation_row=data.frame(Target=row.annotations))
# dev.off()

############### Boruta ###############
fs_result2 <- read.csv(paste0('output/', dataset, '/FS/Boruta/features_boruta_1000p0.01.csv'))
gene_indices2 <- fs_result2[['Index']]
gene_names2 <- fs_result2[['attribute']]
print(c(dim(fs_result2), length(gene_indices2), length(gene_names2)))
hm_data2 <- scaled_data[, gene_indices2[1:hm_gene_count]]
rownames(hm_data2) <- as.array(1:length(targets))
hm_data2 <- hm_data2[order(targets),]
print(dim(hm_data2))

# svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_boruta_top_', hm_gene_count, '.svg'), height=10, width=17)
pheatmap(hm_data2, color=color, border_color=NA, show_rownames=FALSE,
         cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
         annotation_row=data.frame(Target=row.annotations))
# dev.off()

############### ANOVA ###############
fs_result3 <- read.csv(paste0('output/', dataset, '/FS/ANOVA/features_ANOVA.csv'))
gene_indices3 <- fs_result3[['Index']]
gene_names3 <- fs_result3[['attribute']]
print(c(dim(fs_result3), length(gene_indices3), length(gene_names3)))
hm_data3 <- scaled_data[, gene_indices3[1:hm_gene_count]]
rownames(hm_data3) <- as.array(1:length(targets))
hm_data3 <- hm_data3[order(targets),]
print(dim(hm_data3))

# svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_ANOVA_top_', hm_gene_count, '.svg'), height=10, width=17)
pheatmap(hm_data3, color=color, border_color=NA, show_rownames=FALSE,
         cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
         annotation_row=data.frame(Target=row.annotations))
# dev.off()

############### MCFS + Boruta ###############
fs_result4 <- read.csv(paste0('output/', dataset, '/FS/Combined_MCFS_Boruta/features_combined_MCFS_Boruta.csv'))
gene_indices4 <- fs_result4[['Index']]
gene_names4 <- fs_result4[['attribute']]
print(c(dim(fs_result4), length(gene_indices4), length(gene_names4)))
hm_data4 <- scaled_data[, gene_indices4[1:hm_gene_count]]
rownames(hm_data4) <- as.array(1:length(targets))
hm_data4 <- hm_data4[order(targets),]
print(dim(hm_data4))

# svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_combined_MCFS_boruta_top_', hm_gene_count, '.svg'), height=10, width=17)
pheatmap(hm_data4, color=color, border_color=NA, show_rownames=FALSE,
         cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
         annotation_row=data.frame(Target=row.annotations))
# dev.off()

# ############### MCFS + ANOVA ###############
# fs_result5 <- read.csv(paste0('output/', dataset, '/FS/Combined_MCFS_ANOVA/features_combined_MCFS_ANOVA.csv'))
# gene_indices5 <- fs_result5[['Index']]
# gene_names5 <- fs_result5[['attribute']]
# print(c(dim(fs_result5), length(gene_indices5), length(gene_names5)))
# hm_data5 <- scaled_data[, gene_indices5[1:hm_gene_count]]
# rownames(hm_data5) <- as.array(1:length(targets))
# hm_data5 <- hm_data5[order(targets),]
# print(dim(hm_data5))
# 
# # svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_combined_MCFS_ANOVA_top_', hm_gene_count, '.svg'), height=10, width=17)
# pheatmap(hm_data5, color=color, border_color=NA, show_rownames=FALSE,
#          cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
#          annotation_row=data.frame(Target=row.annotations))
# # dev.off()
# 
# ############### Boruta + ANOVA ###############
# fs_result6 <- read.csv(paste0('output/', dataset, '/FS/Combined_Boruta_ANOVA/features_combined_Boruta_ANOVA.csv'))
# gene_indices6 <- fs_result6[['Index']]
# gene_names6 <- fs_result6[['attribute']]
# print(c(dim(fs_result6), length(gene_indices6), length(gene_names6)))
# hm_data6 <- scaled_data[, gene_indices6[1:hm_gene_count]]
# rownames(hm_data6) <- as.array(1:length(targets))
# hm_data6 <- hm_data6[order(targets),]
# print(dim(hm_data6))
# 
# # svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_combined_Boruta_ANOVA_top_', hm_gene_count, '.svg'), height=10, width=17)
# pheatmap(hm_data6, color=color, border_color=NA, show_rownames=FALSE,
#          cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
#          annotation_row=data.frame(Target=row.annotations))
# # dev.off()
# 
# ############### Combined all ###############
# fs_result7 <- read.csv(paste0('output/', dataset, '/FS/Combined_all/features_combined_all.csv'))
# gene_indices7 <- fs_result7[['Index']]
# gene_names7 <- fs_result7[['attribute']]
# print(c(dim(fs_result7), length(gene_indices7), length(gene_names7)))
# hm_data7 <- scaled_data[, gene_indices7[1:hm_gene_count]]
# rownames(hm_data7) <- as.array(1:length(targets))
# hm_data7 <- hm_data7[order(targets),]
# print(dim(hm_data7))
# 
# # svg(filename=paste0(hm_path_prefix, dataset, '/heatmap/heatmap_combined_all_top_', hm_gene_count, '.svg'), height=10, width=17)
# pheatmap(hm_data7, color=color, border_color=NA, show_rownames=FALSE,
#          cluster_rows=FALSE, cluster_cols=FALSE, cexRow=cex, cexCol=100,
#          annotation_row=data.frame(Target=row.annotations))
# # dev.off()
