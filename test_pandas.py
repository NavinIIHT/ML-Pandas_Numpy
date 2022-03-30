import pandas as pd

def create_df_from_dict():
	dict1 = {
    	'Fruits' : ['Apple', 'Orange', 'Strawberry', 'Pineapple'],
    	'Birds' : ['Parrot', 'Peacock', 'Sparrow', 'Crow'],
    	'Vegetables' : ['Carrot', 'Broccoli', 'Cauliflower', 'Asparagus'],
	}

	# create a pandas dataframe  from dict1 with only 'Fruits' and 'vegetabels' columns
	# and last 2 rows with index as ['a', 'b', 'c', 'd'] and return
	df = None
	return df

def create_df_from_list():

	fruits = ['Apple', 'Orange', 'Strawberry', 'Pineapple']
	vegetables = ['Carrot', 'Broccoli', 'Cauliflower', 'Asparagus']
	# create a pandas dataframe from above 2 lists with column named as ['Fruits', 'Vegetables']

	birds = ['Parrot', 'Peacock', 'Sparrow', 'Crow']
	# add column 'Birds' from list birds as second column and return the dataframe

	df = None
	return df

def get_df_stats():

	df = create_df_from_dict()
	# return no. of rows, cols, data types of cols, stats desc of df, covert df to 
	# numpy array and retrun, convert df to list and return 
	nrows = None
	ncols = None
	dtypes = None
	description = None
	df_np_array = None 
	df_np_list = None)
	return nrows, ncols, dtypes, description, df_np_array, df_np_list

def stack_series():
	fruits = ['Apple', 'Orange', 'Strawberry', 'Pineapple']
	vegetables = ['Carrot', 'Broccoli', 'Cauliflower', 'Asparagus']

	# create two series out of fruits and vegetable lists with column names as 
	# 'Fruits' ans 'Vegetables'

	# stack fruits and vegatables series horiontally into a dataframe
	df_hor = None

	# stack fruits and vegatables series vertically into a dataframe
	df_ver = None

	return df_hor, df_ver

def series_quantile():
	data = [1, 2, 3, 4, 5, 12, 15, 18]

	# create a df(column named data) out of list data
	df = None

	# return 0, 20, 50, 80, 100 quantile values
	ret1 = None

	# return the df with only rows divisible by 3 or 5 but not both
	ret2 = None
	return ret1, ret2

def handling_nans():

	data = {
	   "fruits" : ['Apple', 'Orange', 'Apple', np.NaN],
	   "marks" :  [23, np.NaN, 24, np.NaN],
	   "vegetables" : ['Carrot', 'Broccoli', 'Cauliflower', 'Asparagus']
	}
	# create a dataframe out of data
	df = None

	# return whether df has NaNs or not
	ret1 = None

	# return the no. of missing values in each column
	ret2 = None

	# replace numerical missing values with its(column's) mean

	# replace categorical missing value with its(column's) mode

	# and return df
	return ret1, ret2, df

def handling_dates():
	dates = ['01-01-2022', '15-05-2022', '03-01-2022', '04-02-2022', '23-01-2022']
	
	#create a dataframe of dates(col name), out of string list dates.
	df = None

	# return a df with dates greater than 3rd Jan
	ret1 = None

	# return a numpy array containing day of week of each date
	df['week_day'] = None
	return ret1, df

def string_manipulation_df():

	list_of_sents = ['This is first sentence', 
					  'Yet, another sentence',
					  'This is last sentence']

	# create a dataframe of sents(col name), out of list_of_sents.				  
	df = None

	# convert the sents to lower
	
	# create a new column 'n_words' which has no of words of each sentence
	df['n_words'] = None

	return df

def sorting_df():
	dict1 = {
    	'Fruits' : ['Apple', 'Orange', 'Orange', 'Pineapple', 'Apple'],
    	'Price' : [85, 15,  20,  55, 60],
	}

	# create a dataframe of Fruits, Price(col names), out of dict1.
	df = None

	# sort df first by 'Fruits' in ascending order then by 'Price' in descending order
	df = None
	return df

def groupby_df():
	dict1 = {
    	'Fruits' : ['Apple', 'Orange', 'Orange', 'Pineapple', 'Apple'],
    	'Price' : [85, 15,  20,  55, 60],
	}

	# create a dataframe of Fruits, Price(col names), out of dict1.
	df = None

	# group df by 'Fruis' then sort by 'price' and return the dataframe(not groups)
	"""
				Fruits  Price
		1     Orange     15
		2     Orange     20
		3  Pineapple     55
		4      Apple     60
		0      Apple     85

	"""
	df = None
	return df


if __name__=="__main__":
	pass