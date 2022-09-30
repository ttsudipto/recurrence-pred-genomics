from sys import maxsize
import csv
import numpy as np

np.set_printoptions(threshold=maxsize)

path_prefix = 'input/NSCLC/'


def get_ip_data_file_name(dataset):
    return 'genomics_input_' + dataset + '.tsv'


def get_ip_target_file_name(dataset):
    return 'genomics_input_labels_' + dataset + '.tsv'


class DataResource :
    
    def __init__(self, genomic_file_name, label_file_name, fs=None, pid_label='Case ID'):
        self.target_field_names = {'age': 'Age at Histological Diagnosis', 'gender': 'Gender', 'tumor_loc': 'Tumor Location', 
                      'adj_treatment': 'Adjuvant Treatment', 'chemo': 'Chemotherapy', 'radiation': 'Radiation', 
                      'recurrence': 'Recurrence', 'vital_stat': 'Survival Status', 
                      'surgery_to_death': 'Time to Death (days) (surgery to death)',
                      'ct_to_death': 'Time to Death (days) (CT to death)'}
        self.target_value_map = {'age': None, 'gender': {'Male': 0, 'Female': 1},
                        'tumor_loc': {'L Lingula': 0, 'LLL': 1, 'LUL': 2, 'RLL': 3, 'RML': 4, 'RUL': 5},
                        'adj_treatment': {'Yes': 1, 'No': 0, 'Not Collected': 0},
                        'chemo': {'Yes': 1, 'No': 0, 'Not Collected': 0},
                        'radiation': {'Yes': 1, 'No': 0, 'Not Collected': 0},
                        'recurrence': {'yes': 1, 'no': 0, 'Not collected': 0},
                        'vital_stat': {'Dead': 0, 'Alive': 1}, 'surgery_to_death': None,
                        'ct_to_death': None}
        self.target_dtype_map = {'age': 'I', 'surgery_to_death': 'F', 'ct_to_death': 'F'}
        self.genomic_file_name = genomic_file_name
        self.label_file_name = label_file_name
        self.pid_label = pid_label
        self.selected_features = fs
        self._read_pids()
    
    def _read_pids(self):
        csvfile = open(path_prefix + self.genomic_file_name, 'r')
        reader = csv.DictReader(csvfile, delimiter='\t')
        self.pids = reader.fieldnames[1:]
        csvfile.close()

    def read_data_from_csv(self):
        csvfile = open(path_prefix + self.genomic_file_name, 'r')
        self.data = np.transpose(np.genfromtxt(csvfile, delimiter='\t', skip_header=1, usecols=range(0, len(self.pids)+1), dtype=str))
        #self.gene_names = self.data[0,:]
        if self.selected_features == None:
            self.gene_names = self.data[0,:]
            self.data = np.array(self.data[1:,:], dtype=np.float32)
        else:
            self.gene_names = self.data[0,self.selected_features]
            self.data = np.array(self.data[1:,self.selected_features], dtype=np.float32)
        
        csvfile.close()

    def read_target_from_csv(self, target_label):
        csvfile = open(path_prefix + self.label_file_name, 'r')
        reader = csv.DictReader(csvfile, delimiter='\t')
        targets = []
        for row in reader:
            targets.append(int(row[target_label]))
        self.target = np.array(targets)
        csvfile.close()
        #pid_target_map = dict()
        #for row in reader:
            #pid_target_map[row[self.pid_label]] = row[self.target_field_names[target_label]]
        #targets = []
        #value_converter = self.target_value_map[target_label]
        #if value_converter is None: # convert data to int or float
            #if self.target_dtype_map[target_label] == 'I': # convert data to int
                #value_converter = lambda x: int(x)
            #elif self.target_dtype_map[target_label] == 'F': # convert data to float
                #value_converter = lambda x: float(x)
            #for pid in self.pids:
                #targets.append(value_converter(pid_target_map[pid]))
        #else:
            #for pid in self.pids: # convert data to mapped values
                #targets.append(value_converter[pid_target_map[pid]])
        #self.target = np.array(targets)
        #csvfile.close()
        
        #self.target = np.genfromtxt(csvfile, delimiter=',', skip_header=1, usecols=(self.target_col), converters={self.target_col:self._target_converter})
        #csvfile.close()
        
    def replace_missing_values(self):
        col_mean = np.nanmean(self.data, axis=0)
        x,y = np.where(np.isnan(self.data))
        self._null_indices = [(x[i], y[i]) for i in range(len(x))]
        for i in range(len(x)):
            self.data[x[i],y[i]] = col_mean[y[i]]


def print_data_summary(res):
    print('No. of samples (patients) = ' + str(len(res.pids)))
    print('No. of genes = ' + str(len(res.gene_names)))
    #print('Sample IDs :')
    #print(res.pids)
    #print('Genes :')
    #print(res.gene_names)
    print('Data')
    print(res.data.shape)
    print(res.data[0,:10])
    print(res.data[-1,:10])
    print('Target')
    print(res.target.shape)
    print(res.target[:10])
    print(res.target[-10:])
    print('')


def read_data(genomic_file_name, label_file_name, target_label, fs=None, verbose=False) :
    res = DataResource(genomic_file_name, label_file_name, fs=fs)
    res.read_data_from_csv()
    res.read_target_from_csv(target_label)
    if verbose == True :
        print_data_summary(res)
    return res


def read_validation_data(file_name, n_features=140, verbose=False) :
    res = ValidationDataResource(file_name, n_features)
    res.read_data_from_csv()
    res.read_target_from_csv()
    if verbose == True :
        print('No. of samples (patients) = ' + str(len(res.pids)))
        #print('Sample IDs :')
        #print(res.pids)
        print('Data')
        print(res.data.shape)
        print(res.data[0,:10])
        print(res.data[0,-10:])
        print(res.data[-1,:10])
        print(res.data[-1,-10:])
        print('Target')
        print(res.target.shape)
        print(res.target[:10])
        print(res.target[-10:])
        print('')
    return res

