from csv import DictReader, DictWriter

dataset = 'lung'
prefix = 'input/NSCLC/'


def get_file_case_map(dataset):
    metadata_file = open(prefix + 'CPTAC-3_' + dataset + '_labels.csv', 'r')
    metadata_reader = DictReader(metadata_file, delimiter='\t')
    file_case_map = dict()
    for row in metadata_reader:
        folder = row['file_id']
        file_name = row['file_name']
        case_id = row['case_id']
        file_case_map[folder+'/'+file_name] = case_id
    print('Number of files = ' + str(len(file_case_map)))
    metadata_file.close()
    return dict(sorted(file_case_map.items()))


def get_file_target_map(dataset, target_col_name):
    metadata_file = open(prefix + 'CPTAC-3_' + dataset + '_labels.csv', 'r')
    metadata_reader = DictReader(metadata_file, delimiter='\t')
    file_target_map = dict()
    for row in metadata_reader:
        folder = row['file_id']
        file_name = row['file_name']
        target = row[target_col_name]
        if target =='no':
            file_target_map[folder+'/'+file_name] = 0
        else:
            file_target_map[folder+'/'+file_name] = 1
    print('Number of targets = ' + str(len(file_target_map)))
    #print(file_target_map.values())
    metadata_file.close()
    return dict(sorted(file_target_map.items()))


def read_gene_names(file_name, col_name):
    f = open(prefix + file_name, 'r')
    reader = DictReader(f, delimiter='\t')
    gene_names = set()
    for row in reader:
        gene_names.add(row[col_name])
    f.close()
    return gene_names


def filter_gene_names_from_input(file_name, gene_col_name, filter_genes, op_file_name):
    f = open(prefix + file_name, 'r')
    reader = DictReader(f, delimiter='\t')
    fieldnames = reader.fieldnames
    op_file = open(prefix + op_file_name, 'w')
    writer = DictWriter(op_file, delimiter='\t', fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        if row[gene_col_name] in filter_genes:
            writer.writerow(row)
    op_file.close()
    f.close()


def merge_rna_seq_files(file_case_map, gene_names, op_file_name):
    rna_seq_data = dict()
    k=1
    for file_name, case_id in file_case_map.items():
        print('Read file: ' + str(k))
        k = k + 1
        f = open(prefix + 'CPTAC-3_' + dataset + '/' + file_name, 'r')
        rna_seq_reader = DictReader(filter(lambda row: row[0]!='#', f), delimiter='\t')
        #print(rna_seq_reader.fieldnames)
        counts = dict()
        fpkms = dict()
        for i in range(4):
            next(rna_seq_reader)
        for row in rna_seq_reader:
            gene_name = row['gene_name']
            if gene_name in gene_names:
                count = int(row['unstranded'])
                fpkm = float(row['fpkm_unstranded'])
                if gene_name not in counts:
                    counts[gene_name] = count
                    fpkms[gene_name] = fpkm
                else:
                    if count > counts[gene_name]:
                        counts[gene_name] = count
                        fpkms[gene_name] = fpkm
        #print(case_id, len(counts), len(fpkms))
        for gene_name, fpkm in fpkms.items():
            #print(case_id + '_' + file_name.split('/')[0], gene_name, fpkm)
            if gene_name not in rna_seq_data:
                rna_seq_data[gene_name] = dict()
                rna_seq_data[gene_name][case_id + '_' + file_name.split('/')[0]] = fpkm
            else:
                rna_seq_data[gene_name][case_id + '_' + file_name.split('/')[0]] = fpkm
        del counts
        del fpkms
        del rna_seq_reader
        f.close()
        del f
        #if(k>3):
            #break
    
    #print(['genes']+sorted(list(list(rna_seq_data.values())[0].keys())))
    #print(len(rna_seq_data))
    #for k,v in rna_seq_data.items():
        #print(k, v)
        #break
    
    print('Start writing output ... ')
    op_file = open(prefix + op_file_name, 'w')
    op_writer = DictWriter(op_file, delimiter='\t', fieldnames=['genes']+sorted(list(list(rna_seq_data.values())[0].keys())))
    op_writer.writeheader()
    print('Header written ... ')
    k=1
    print('Start writing rows ...')
    print(k)
    for gene_name, row_dict in sorted(rna_seq_data.items(), key=lambda x: x[0]):
        print('Write row: ' + str(k))
        k = k + 1
        row_dict['genes'] = gene_name
        op_writer.writerow(row_dict)
    op_file.close()


def merge_two_datasets(file_name_1, file_name_2, op_file_name):
    f1 = open(prefix + file_name_1, 'r')
    f2 = open(prefix + file_name_2, 'r')
    reader1 = DictReader(f1, delimiter='\t')
    reader2 = DictReader(f2, delimiter='\t')
    header1 = reader1.fieldnames
    header2 = reader2.fieldnames
    op_file = open(prefix + op_file_name, 'w')
    writer = DictWriter(op_file, delimiter='\t', fieldnames=header1+header2[1:])
    writer.writeheader()
    #print(header1+header2[1:])
    for row1 in reader1:
        row2 = next(reader2)
        row2.pop('genes')
        row = {**row1, **row2}
        writer.writerow(row)
    
    op_file.close()
    f1.close()
    f2.close()


#file_case_map = get_file_case_map(dataset)
#print(len(file_case_map))
#file_target_map = get_file_target_map(dataset, 'progression_or_recurrence')
#print(len(file_target_map))
#gene_names = read_gene_names('gene_list_dataset2.tsv', 'gene_name')
#print(len(gene_names))

#merge_rna_seq_files(get_file_case_map(dataset), read_gene_names('gene_list_dataset2.tsv', 'gene_name'), 'genomics_input_all_genes_dataset2.tsv') ## lung
#merge_rna_seq_files(get_file_case_map(dataset), read_gene_names('gene_list_dataset2.tsv', 'gene_name'), 'genomics_input_all_genes_CPTAC-3_'+dataset+'.tsv') ## kidney
#merge_rna_seq_files(get_file_case_map(dataset), read_gene_names('gene_list_dataset2.tsv', 'gene_name'), 'genomics_input_all_genes_CPTAC-3_'+dataset+'.tsv') ## pancreas

#filter_gene_names_from_input('genomics_input_all_genes_dataset1.tsv', 'genes', read_gene_names('gene_list_common.tsv', 'gene_name'), 'genomics_input_dataset1.tsv')
#filter_gene_names_from_input('genomics_input_all_genes_dataset2.tsv', 'genes', read_gene_names('gene_list_common.tsv', 'gene_name'), 'genomics_input_dataset2.tsv')
#filter_gene_names_from_input('genomics_input_all_genes_CPTAC-3_'+dataset+'.tsv', 'genes', read_gene_names('gene_list_common.tsv', 'gene_name'), 'genomics_input_CPTAC-3_'+dataset+'.tsv') ## kidney
#filter_gene_names_from_input('genomics_input_all_genes_CPTAC-3_'+dataset+'.tsv', 'genes', read_gene_names('gene_list_common.tsv', 'gene_name'), 'genomics_input_CPTAC-3_'+dataset+'.tsv') ## pancreas

#merge_two_datasets('genomics_input_dataset1.tsv', 'genomics_input_dataset2.tsv', 'genomics_input.tsv')
