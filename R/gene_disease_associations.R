library(disgenet2r)

input_prefix <- 'output/'

api_key <- read.table('input/DisGeNet/api_key.txt')[[1]]

fs_filename_map <- data.frame(c('/FS/MCFS/features_MCFS_300ps_scaled.csv',
                                '/FS/Boruta/features_boruta_1000p0.01.csv',
                                '/FS/ANOVA/features_ANOVA.csv',
                                '/FS/Combined_MCFS_Boruta/features_combined_MCFS_Boruta.csv'
                              ))
rownames(fs_filename_map) <- c('MCFS', 'Boruta', 'ANOVA', 'Combined_MCFS_Boruta')

# map <- data.frame(c('MIR1915HG', 'DMAC2L', 'ADGRA3', 'SNORA80E', 'ELOA2', 'EFL1',
#                     'LINC01587', 'LINC02381', 'CENPU', 'TBC1D31', 'FOCAD'))
# colnames(map) <- c('new_name')
# row.names(map) <- c('C10orf114', 'ATP5S', 'GPR125', 'SNORA42', 'TCEB3B', 'EFTUD1',
#          'C4orf6', 'LOC400043', 'MLF1IP', 'WDR67', 'KIAA1797')

get_file_name <- function(dataset, fs) {
  return (paste0(input_prefix, dataset, fs_filename_map[fs,]))
}

read_top_genes <- function(fname, colname, count){
  gene_table <- read.csv(fname, sep=',')
  genes <- as.array(gene_table[[colname]])[1:count]
  return(genes)
}

# dataset <- 'dataset1'
# dataset <- 'dataset2'
# dataset <- 'dataset3'

# fs <- 'MCFS'
# fs <- 'Boruta'
# fs <- 'ANOVA'
# fs <- 'Combined_MCFS_Boruta'

# file_name <- get_file_name(dataset, fs)
# genes <- read_top_genes(file_name, 'attribute', 140)
# print(genes)
# print(length(genes))

## Gene-Disease associations
# g2d_result <- gene2disease(gene=genes, api_key=api_key, database='ALL')
# g2d_assoc_df <- g2d_result@qresult

## Gene Disease-class Heatmap
# # svg(paste0("output/",dataset,"/gene_disease_association/assoc_",fs,"_140.svg"), width=12, height=6)
# plot(g2d_result, class="DiseaseClass", nchars=50)
# # dev.off()

## Gene Disease Network
# plot(g2d_result, class='Network', prop=20)

## Gene Disease Enrichment plot
# enrich_result <- disease_enrichment(entities=unique(g2d_assoc_df$gene_symbol), database='ALL')
# plot(enrich_result, class="Enrichment", cutoff=0.05, nchars=100, limit=30)

