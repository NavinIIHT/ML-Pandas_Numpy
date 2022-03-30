
def stack_numpy():
	arr1 = np.arange(4)
	arr2 = arr1*2

	# stack arr1 and arr2 vertically and return 
	ret1 = None

	# stack arr1 and arr2 horiontally and return 
	ret2 = None

	return ret1, ret2

def reshape_numpy():
	arr = np.array([[1, 2, 3], [4, 5, 6]])

	# convert arr into a column vector ie., (6,1)
	ret1 = None

	# convert arr into a row vector ie., (1,6)
	ret2 = None

	return ret1, ret2

def compare_np_arrays():
	a = np.array([1,2,3,2,3,4,10,4,5,6])
	b = np.array([7,2,10,2,4,7,10,4,9,8])

	# get the indexes where elements are equal
	ret1 = None
	return ret1

def stats_numpy():
	arr = np.array([1,5,2,8,3,9,1,13,25,3,5,2,1])

	# return min, max, mean, median, standard deviation

	return 

def twod_numpy():
	arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

	# flatten arr to 1d and return
	ret1 = None

	# return row-wise min
	ret2 = None

	# return col-wise min
	ret3 = None

	# return index of max of each row
	ret4 = None

	return ret1, ret2, ret3, ret4

def handling_nans_1():
	arr = np.array([[1, np.NaN, 3], [np.NaN, 5, 6], [7, 8, 9]])

	# check if arr has null values
	ret1 = None

	# how many null values are there in arr
	ret2 = None

	# replace all nans in arr -1

	return ret1, ret2, arr

def handling_nans_2():
	arr = np.array([[1, np.NaN, 3], [np.NaN, 5, 6], [7, 8, 9]])

	# get the positions of null values
	ret1 = None

	# drop all rows with nans in arr
	ret2 = None

	return ret1, ret2