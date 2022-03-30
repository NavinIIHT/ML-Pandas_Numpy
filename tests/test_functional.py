import sys, os
sys.path.append("..")
import unittest
import collections
import pandas as pd
import pickle
import test_pandas as test_pd
import test_numpy as test_np

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
#solutions = pd.read_csv("solutions_pandas.csv")["solution"].values
with open('tests/H2f_Kkp5a4V.pickle', 'rb') as f:
     solutions = pickle.load(f)


class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path, "w"):
            pass

    def test_create_df_from_dict(self):
        
        ret_test = test_pd.create_df_from_dict()
        test_sol = solutions[0]

        passed = ret_test.equals(test_sol)
        if passed:
            with open(file_path, "a") as f:
                f.write("TestCreateDfFromDict=True\n")
                print("TestCreateDfFromDict = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestCreateDfFromDict=False\n")
                print("TestCreateDfFromDict = Failed")
        print(type(test_sol), type(ret_test))
        assert passed

    def test_create_df_from_list(self):
        
        ret_test = test_pd.create_df_from_list()
        test_sol = solutions[1]

        passed = ret_test.equals(test_sol)
        if passed:
            with open(file_path, "a") as f:
                f.write("TestCreateDfFromList=True\n")
                print("TestCreateDfFromList = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestCreateDfFromList=False\n")
                print("TestCreateDfFromList = Failed")
        assert passed

    def test_get_df_stats(self):
        
        ret_test = test_pd.get_df_stats()
        test_sol = solutions[2]

        passed = (ret_test[0] == test_sol[0]) & (ret_test[1] == test_sol[1]) & \
                ret_test[2].equals(test_sol[2]) & (ret_test[4] == test_sol[4]).all() & \
                (ret_test[5] == test_sol[5])
        if passed:
            with open(file_path, "a") as f:
                f.write("TestGetDfStats=True\n")
                print("TestGetDfStats = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestGetDfStats=False\n")
                print("TestGetDfStats = Failed")
        assert passed

    def test_stack_series(self):
        
        ret_test = test_pd.stack_series()
        test_sol = solutions[3]

        passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
        if passed:
            with open(file_path, "a") as f:
                f.write("TestStackSeries=True\n")
                print("TestStackSeries = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestStackSeries=False\n")
                print("TestStackSeries = Failed")
        assert passed

    def test_series_quantile(self):
        
        ret_test = test_pd.series_quantile()
        test_sol = solutions[4]

        passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
        if passed:
            with open(file_path, "a") as f:
                f.write("TestSeriesQuantile=True\n")
                print("TestSeriesQuantile = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestSeriesQuantile=False\n")
                print("TestSeriesQuantile = Failed")
        assert passed

    def test_handling_nans(self):
        
        ret_test = test_pd.handling_nans()
        test_sol = solutions[5]

        passed = (ret_test[0]==ret_test[0]) & ret_test[1].equals(test_sol[1]) & \
                (ret_test[2].equals(test_sol[2]))
        if passed:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans=True\n")
                print("TestHandlingNans = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans=False\n")
                print("TestHandlingNans = Failed")
        assert passed

    def test_handling_dates(self):
        
        ret_test = test_pd.handling_dates()
        test_sol = solutions[6]

        passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
        if passed:
            with open(file_path, "a") as f:
                f.write("TestHandlingDates=True\n")
                print("TestHandlingDates = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestHandlingDates=False\n")
                print("TestHandlingDates = Failed")
        assert passed

    def test_string_manipulation_df(self):
        
        ret_test = test_pd.string_manipulation_df()
        test_sol = solutions[7]

        if ret_test.equals(test_sol):
            with open(file_path, "a") as f:
                f.write("TestStringManipulationDf=True\n")
                print("TestStringManipulationDf = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestStringManipulationDf=False\n")
                print("TestStringManipulationDf = Failed")
        assert ret_test.equals(test_sol)

    def test_sorting_df(self):
        
        ret_test = test_pd.sorting_df()
        test_sol = solutions[8]

        if ret_test.equals(test_sol):
            with open(file_path, "a") as f:
                f.write("TestSortingDf=True\n")
                print("TestSortingDf = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestSortingDf=False\n")
                print("TestSortingDf = Failed")
        assert ret_test.equals(test_sol)

    def test_groupby_df(self):
        
        ret_test = test_pd.groupby_df()
        test_sol = solutions[9]

        if ret_test.equals(test_sol):
            with open(file_path, "a") as f:
                f.write("TestGroupbyDf=True\n")
                print("TestGroupbyDf = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestGroupbyDf=False\n")
                print("TestGroupbyDf = Failed")
        assert ret_test.equals(test_sol)

    def test_stack_numpy(self):
        
        ret_test = test_np.stack_numpy()
        test_sol = solutions[10]

        passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestStackNumpy=True\n")
                print("TestStackNumpy = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestStackNumpy=False\n")
                print("TestStackNumpy = Failed")
        assert passed

    def test_reshape_numpy(self):
        
        ret_test = test_np.reshape_numpy()
        test_sol = solutions[11]

        passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestReshapeNumpy=True\n")
                print("TestReshapeNumpy = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestReshapeNumpy=False\n")
                print("TestReshapeNumpy = Failed")
        assert passed
    def test_compare_np_arrays(self):
        
        ret_test = test_np.compare_np_arrays()
        test_sol = solutions[12]

        passed = (ret_test[0] == test_sol[0]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestCompareNpArrays=True\n")
                print("TestCompareNpArrays = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestCompareNpArrays=False\n")
                print("TestCompareNpArrays = Failed")
        assert passed

    def test_stats_numpy(self):
        
        ret_test = test_np.stats_numpy()
        test_sol = solutions[13]

        passed = (ret_test[0] == test_sol[0]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestStatsNumpy=True\n")
                print("TestStatsNumpy = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestStatsNumpy=False\n")
                print("TestStatsNumpy = Failed")
        assert passed

    def test_twod_numpy(self):
        
        ret_test = test_np.twod_numpy()
        test_sol = solutions[14]

        passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all() & \
                (ret_test[2] == test_sol[2]).all() & (ret_test[3] == test_sol[3]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestTwodNumpy=True\n")
                print("TestTwodNumpy = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestTwodNumpy=False\n")
                print("TestTwodNumpy = Failed")
        assert passed

    def test_handling_nans_1(self):
        
        ret_test = test_np.handling_nans_1()
        test_sol = solutions[15]

        passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all() & \
                (ret_test[2] == test_sol[2]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans1=True\n")
                print("TestHandlingNans1 = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans1=False\n")
                print("TestHandlingNans1 = Failed")
        assert passed

    def test_handling_nans_2(self):
        
        ret_test = test_np.handling_nans_2()
        test_sol = solutions[16]

        passed = (ret_test[0][0] == test_sol[0][0]).all() & (ret_test[1] == test_sol[1]).all() & \
                (ret_test[0][1] == test_sol[0][1]).all()
        if passed:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans2=True\n")
                print("TestHandlingNans2 = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestHandlingNans2=False\n")
                print("TestHandlingNans2 = Failed")
        assert passed




    