from .data_preprocessing import get_top_feature_names
from csv import DictReader, DictWriter

bcscdb_file_name = 'input/NSCLC/BCSCdb_input.csv'


def check_CSC_from_BCSCdb(dataset, n_features, fs, write=False):
    genes = get_top_feature_names(dataset, n_features, fs, verbose=True)
    gene_rank = {genes[i]:i+1 for i in range(len(genes))}
    f = open(bcscdb_file_name, 'r')
    ip_reader = DictReader(f, delimiter=',')
    
    print('Dataset: ' + dataset + '; Ranking: ' + fs + '; No. of features: ' + str(n_features))
    
    result = dict()
    
    for row in ip_reader:
        gene = row['GENE']
        cancer_type = row['CANCER_TYPE']
        marker_type = row['MARKER_TYPE']
        cell_line = row['CELL_LINE']
        expression_level = row['EXPRESSION_LEVEL']
        pubmed = row['PUBMED_ID']
        if gene in genes:
            if gene not in result:
                result[gene] = {cancer_type: {'MARKER_TYPE': [marker_type], 'CELL_LINE': [cell_line], 'EXPRESSION_LEVEL': [expression_level], 'PUBMED_ID': [pubmed]}}
            else:
                if cancer_type not in result[gene]:
                    result[gene][cancer_type] = {'MARKER_TYPE': [marker_type], 'CELL_LINE': [cell_line], 'EXPRESSION_LEVEL': [expression_level], 'PUBMED_ID': [pubmed]}
                else:
                    result[gene][cancer_type]['MARKER_TYPE'].append(marker_type)
                    result[gene][cancer_type]['CELL_LINE'].append(cell_line)
                    result[gene][cancer_type]['EXPRESSION_LEVEL'].append(expression_level)
                    result[gene][cancer_type]['PUBMED_ID'].append(pubmed)
    f.close()
    
    print('Matched ' + str(len(result)) + '/' + str(n_features) + ' genes')
    
    #print('output/'+dataset+'/FS/'+fs+'/csc_markers_'+fs+'_'+str(n_features)+'.csv')
    #print(gene_rank)
    if write == True:
        op_file_name = 'output/'+dataset+'/FS/'+fs+'/csc_markers_'+fs+'_'+str(n_features)+'.csv'
        print('Writing output to \''+ op_file_name + '\' ...')
        f = open(op_file_name, 'w')
        writer = DictWriter(f, delimiter=',', fieldnames=['attribute', 'position', 'CANCER_TYPE', 'MARKER_TYPE', 'EXPRESSION_LEVEL', 'CELL_LINE', 'PUBMED_ID'])
        writer.writeheader()
    for gene, v1 in result.items():
        for cancer_type, v2 in v1.items():
            row = {'attribute': gene, 'position': gene_rank[gene], 'CANCER_TYPE': cancer_type, 
                   'MARKER_TYPE': v2['MARKER_TYPE'], 'CELL_LINE': v2['CELL_LINE'], 
                   'EXPRESSION_LEVEL': v2['EXPRESSION_LEVEL'], 'PUBMED_ID': v2['PUBMED_ID']}
            #print(row)
            if write == True:
                writer.writerow(row)
    if write == True:
        f.close()


def find_one_hop_genes(dataset, n_features, fs, only_NSCLC=False, write=False):
    top_genes = get_top_feature_names(dataset, n_features, fs, verbose=False)
    gene_rank = {top_genes[i]:i+1 for i in range(len(top_genes))}
    #print(gene_rank)
    
    f = open('output/'+dataset+'/FS/'+fs+'/csc_markers_'+fs+'_'+str(n_features)+'.csv', 'r')
    csc_reader = DictReader(f, delimiter=',')
    csc_marker_genes = set()
    for row in csc_reader:
        if only_NSCLC == False:
            csc_marker_genes.add(row['attribute'])
        else:
            if row['CANCER_TYPE'] == 'Non Small Cell Lung Cancer':
                csc_marker_genes.add(row['attribute'])
    f.close()
    #print(csc_marker_genes)
    #print(len(csc_marker_genes))
    
    f = open('output/'+dataset+'/FS/'+fs+'/top_genes_network_'+fs+'.tsv', 'r')
    net_reader = DictReader(f, delimiter='\t')
    top_genes_network = dict()
    for row in net_reader:
        n1 = row['#node1']
        n2 = row['node2']
        score = float(row['combined_score'])
        if n1 not in top_genes_network:
            top_genes_network[n1] = {n2: score}
        else:
            top_genes_network[n1][n2] = score
        if n2 not in top_genes_network:
            top_genes_network[n2] = {n1: score}
        else:
            top_genes_network[n2][n1] = score
    f.close()
    #for n1,v in top_genes_network.items():
        #print(n1+'-->'+str(v)+' ==> '+str(len(v)))
    #print(len(top_genes_network))
    
    if write == True:
        if only_NSCLC == False:
            op_file_name = 'output/'+dataset+'/FS/'+fs+'/csc_markers_one_hop_associations_'+fs+'_'+str(n_features)+'.csv'
        else:
            op_file_name = 'output/'+dataset+'/FS/'+fs+'/csc_markers_one_hop_associations_NSCLC_'+fs+'_'+str(n_features)+'.csv'
        print('Writing output to \''+ op_file_name + '\' ...')
        f = open(op_file_name, 'w')
        writer = DictWriter(f, delimiter=',', fieldnames=['CSC_marker', 'CSC_marker_position', 'Other_interactor', 'Other_interactor_position', 'Interaction_score'])
        writer.writeheader()
    for csc_marker in csc_marker_genes:
        if csc_marker in top_genes_network:
            for interactor, score in top_genes_network[csc_marker].items():
                if interactor in top_genes and interactor not in csc_marker_genes:
                    if write == True:
                        writer.writerow({'CSC_marker': csc_marker, 'CSC_marker_position': gene_rank[csc_marker], 'Other_interactor': interactor, 'Other_interactor_position': gene_rank[interactor], 'Interaction_score': score})
                    print(csc_marker, gene_rank[csc_marker], interactor, gene_rank[interactor], score)
    if write == True:
        f.close()


def summarize_CSC_markers(dataset, n_features, fs, write=False):
    top_genes = get_top_feature_names(dataset, n_features, fs, verbose=False)
    gene_rank = {top_genes[i]:i+1 for i in range(len(top_genes))}
    #print(gene_rank)
    
    f = open('output/'+dataset+'/FS/'+fs+'/csc_markers_'+fs+'_'+str(n_features)+'.csv', 'r')
    csc_reader = DictReader(f, delimiter=',')
    csc_marker_nsclc = set()
    for row in csc_reader:
        if row['CANCER_TYPE'] == 'Non Small Cell Lung Cancer':
            csc_marker_nsclc.add(row['attribute'])
    f.close()
    f = open('output/'+dataset+'/FS/'+fs+'/csc_markers_'+fs+'_'+str(n_features)+'.csv', 'r')
    csc_reader = DictReader(f, delimiter=',')
    csc_marker_other = set()
    for row in csc_reader:
        if row['attribute'] not in csc_marker_nsclc:
            csc_marker_other.add(row['attribute'])
    f.close()
    #print(len(csc_marker_nsclc), len(csc_marker_other))

    f = open('output/'+dataset+'/FS/'+fs+'/csc_markers_one_hop_associations_NSCLC_'+fs+'_'+str(n_features)+'.csv', 'r')
    nsclc_interactor_reader = DictReader(f, delimiter=',')
    interactors_nsclc = set()
    for row in nsclc_interactor_reader:
        interactors_nsclc.add(row['Other_interactor'])
    f.close()
    f = open('output/'+dataset+'/FS/'+fs+'/csc_markers_one_hop_associations_'+fs+'_'+str(n_features)+'.csv', 'r')
    other_interactor_reader = DictReader(f, delimiter=',')
    interactors_other = set()
    for row in other_interactor_reader:
        if row['Other_interactor'] not in interactors_nsclc:
            interactors_other.add(row['Other_interactor'])
    f.close()
    #print(len(interactors_nsclc), (len(interactors_other)))
    
    if write == True:
        op_file_name = 'output/'+dataset+'/FS/'+fs+'/csc_markers_summary_'+fs+'_'+str(n_features)+'.csv'
        print('Writing output to \''+ op_file_name + '\' ...')
        f = open(op_file_name, 'w')
        writer = DictWriter(f, delimiter=',', fieldnames=['attribute', 'position', 'CSC_marker_type'])
        writer.writeheader()
    for gene in top_genes:
        if gene in csc_marker_nsclc:
            csc_type = 'NSCLC CSC marker'
        elif gene in csc_marker_other:
            csc_type = 'Other cancer CSC marker'
        elif gene in interactors_nsclc:
            csc_type = 'Interactor to NSCLC CSC marker'
        elif gene in interactors_other:
            csc_type = 'Interactor to other cancer CSC marker'
        else:
            csc_type = 'Not a CSC marker'
        if write == True:
            writer.writerow({'attribute': gene, 'position': gene_rank[gene], 'CSC_marker_type': csc_type})
        print(gene, gene_rank[gene], csc_type)
    if write == True:
        f.close()


n_features = 140

#dataset = 'dataset1'
#dataset = 'dataset2'
#dataset = 'dataset3'

#fs = 'MCFS'
#fs = 'Boruta'
#fs = 'ANOVA'
#fs = 'Combined_MCFS_Boruta'

#check_CSC_from_BCSCdb(dataset, n_features, fs, write=False)
#check_CSC_from_BCSCdb(dataset, n_features, fs, write=False)

#find_one_hop_genes(dataset, n_features, fs, write=False)
#find_one_hop_genes(dataset, n_features, fs, write=True)

#find_one_hop_genes(dataset, n_features, fs, only_NSCLC=True, write=False)
#find_one_hop_genes(dataset, n_features, fs, only_NSCLC=True, write=True)

#summarize_CSC_markers(dataset, n_features, fs, write=False)
#summarize_CSC_markers(dataset, n_features, fs, write=True)
