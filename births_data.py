csv_births = f.read()
print(csv_births)
csv_births.split('\n')[:11]

def read_csv(file_name):
    f = open(file_name, 'r')
    csv_births = f.read()
    split_data = csv_births.split('\n')
    string_list = split_data[1:] # remove header row
    final_list = []
    string_fields = []
    int_fields = []
    
    for each in string_list:
        string_fields = each.split(',')
        int_fields = [int(i) for i in string_fields]
        final_list.append(int_fields)
    return final_list

final_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')


# List of List is in the format of:
# year,month,date_of_month,day_of_week,births

def month_births(some_list):
    
    births_per_month = {} # create empty dictionary
    
    for each_item in some_list: # iterate through list of lists
#         print(each_item)
        month = each_item[1] # Grab Month value
        births = each_item[-1] # Grab births value
#         print('Month:' + str(month))
#         print('Births: ' + str(births))
        if month in births_per_month: # Check if current month is a key in dict
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    
    return births_per_month

cdc_month_births = month_births(final_list)
cdc_month_birthsf = open('US_births_1994-2003_CDC_NCHS.csv', 'r')

    
# year,month,date_of_month,day_of_week,births
def dow_births(some_list):
    
    d = {} # create empty dictionary
    
    for each_item in some_list:
        day_of_week = each_item[-2]
        births = each_item[-1] # Grab births value
        
        if day_of_week in d:
            d[day_of_week] += births
        else:
            d[day_of_week] = births
    
    
    return d

cdc_day_births = dow_births(final_list)
cdc_day_births
    
def calc_counts(data, column):
    
    d = {}
    
    for each_item in data:
        attribute = each_item[column]
        births = each_item[-1] # Grab births value
    
        if attribute in d:
            d[attribute] += births
        else:
            d[attribute] = births
            
    return d

# Column Indices: year,month,date_of_month,day_of_week,births
cdc_year_births = calc_counts(final_list, 0)
cdc_month_births = calc_counts(final_list, 1)
cdc_dom_births = calc_counts(final_list, 2)
cdc_dow_births = calc_counts(final_list, 3)    
