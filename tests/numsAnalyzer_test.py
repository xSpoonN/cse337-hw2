import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.numsAnalyzer import np, countMissingValues, curve_low_scoring_exams, exams_with_median_gt_K

class TestNumsAnalyzer:
    def test_countMissingValues_PosAxis(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        assert np.array_equal(countMissingValues(input,0), np.array([0, 2, 0, 3, 0]))
        assert np.array_equal(countMissingValues(input,1), np.array([0, 1, 2, 2]))
    def test_countMissingValues_NegAxis(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        assert np.array_equal(countMissingValues(input,-2), np.array([0, 2, 0, 3, 0]))
        assert np.array_equal(countMissingValues(input,-1), np.array([0, 1, 2, 2]))
    def test_countMissingValues_ThreeDimensional(self):
        input = np.array([[[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0]],
                          [[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
        assert np.array_equal(countMissingValues(input, 0), np.array([[0, 1, 0, 1, 0],[0, 1, 0, 2, 0]]))
        assert np.array_equal(countMissingValues(input, 1), np.array([[0, 0, 0, 1, 0],[0, 2, 0, 2, 0]]))
        assert np.array_equal(countMissingValues(input, 2), np.array([[0, 1],[2, 2]]))
    def test_countMissingValues_InvalidAxis(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            countMissingValues(input, 3)
    def test_countMissingValues_NonIntAxis(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            countMissingValues(input, 1.5)
    def test_medianK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        # Medians = [94.5, 71.3, 43.5, 65.3]
        assert exams_with_median_gt_K(input, 95) == 0
        assert exams_with_median_gt_K(input, 90) == 1
        assert exams_with_median_gt_K(input, 70) == 2
        assert exams_with_median_gt_K(input, 60) == 3
        assert exams_with_median_gt_K(input, 40) == 4
    def test_medianK_NegativeK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(input, -1)
    def test_medianK_BigK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(input, 101)
    def test_medianK_ArrayHasNegatives(self):
        input = np.array([[100.0, 87.3, 94.5, -99.0, 78.4],
                          [82.6, -71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, -98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(input, 70)
    def test_medianK_ArrayHasBigValues(self):
        input = np.array([[100.0, 87.3, 94.5, 199.0, 78.4],
                          [82.6, 71.3, 199.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [197.0, np.NaN, 98.5, np.NaN, 165.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(input, 70)
    def test_medianK_NonIntK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(TypeError):
            exams_with_median_gt_K(input, 80.5)
    def test_curveExams(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        expected = np.array([[100.0, 7.4, 50.9, 7.4, 87.4],
                             [98.5, 1.5, 100.0, 1.5, 66.8],
                             [82.7, 71.4, 100.0, 0.1, 48.1],
                             [100.0, 87.3, 94.5, 99.0, 78.4]])
        expected2 = np.array([[100.0, 7.4, 50.9, 7.4, 87.4],
                             [98.5, 1.5, 100.0, 1.5, 66.8],
                             [82.6, 71.3, 99.9, 0, 48.0],
                             [100.0, 87.3, 94.5, 99.0, 78.4]])
        assert np.array_equal(curve_low_scoring_exams(input, 95), expected)
        assert np.array_equal(curve_low_scoring_exams(input, 90), expected)
        assert np.array_equal(curve_low_scoring_exams(input, 60), expected2)
    def test_curveExams_NegativeK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(input, -1)
    def test_curveExams_BigK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(input, 101)
    def test_curveExams_ArrayHasNegatives(self):
        input = np.array([[100.0, 87.3, 94.5, -99.0, 78.4],
                          [82.6, -71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, -98.5, np.NaN, 65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(input, 70)
    def test_curveExams_ArrayHasBigValues(self):
        input = np.array([[100.0, 87.3, 94.5, 199.0, 78.4],
                          [82.6, 71.3, 199.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [197.0, np.NaN, 98.5, np.NaN, 165.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(input, 70)
    def test_curveExams_NonIntK(self):
        input = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],
                          [82.6, 71.3, 99.9, np.NaN, 48.0],
                          [92.6, np.NaN, 43.5, np.NaN, 80.0],
                          [97.0, np.NaN, 98.5, np.NaN, 65.3]])
        with pytest.raises(TypeError):
            curve_low_scoring_exams(input, 80.5)
    