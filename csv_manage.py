from csv import writer

def add_rows(values, csvfile):
    with open(csvfile,'w',newline='') as file:
        add = writer(file,delimiter=';')
        add.writerows(values)