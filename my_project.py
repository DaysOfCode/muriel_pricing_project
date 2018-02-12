import pandas as pd
import time
from matplotlib import pyplot as plt



# loading the data
start_time = time.time()
#my_data = off_df = pd.read_csv('en.openfoodfacts.org.products.tsv', sep='\t', low_memory=False)
my_data  = off_df = pd.read_csv('firstthousand.tsv', sep='\t', low_memory=False)
print "finish loading data, time elapsed:"
print time.time() - start_time
print type(my_data)


# understanding the data
# names = my_data.columns.values
# print names


# creating a subset
sub_set = my_data[my_data['energy_100g'].isnull() == False]
sub_set = sub_set[sub_set['product_name'].isnull() == False]
sub_set = sub_set[['product_name','ingredients_text','energy_100g']]
print "original dataset"
print my_data.shape
print "subset"
print sub_set.shape


# functions
def remove_commas_between_brackets(my_list):
    """removes all the commas between brackets of the given string"""
    between_brackets = False
    output = ''
    for c in my_list:
        if c == "(":
            between_brackets = True
        if c == ")":
            between_brackets = False
        if not(between_brackets and c == ","):
            output += c
    return output

def split_string_into_array(my_string):
    my_string = remove_commas_between_brackets(my_string)
    my_list = my_string.split(',')
    return my_list

# processing data
ingredients_array = sub_set['ingredients_text'].values
all_ingredients = []

for ingredient in ingredients_array:
    all_ingredients.append(ingredient)

print all_ingredients
print len(all_ingredients)













# for later
# sorted_ds = sub_set.sort_values(by=['energy_100g'], ascending = False)
