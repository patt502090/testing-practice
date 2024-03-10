from productions.grid_challenge import gridChallenge
import unittest

class TestGridChallengeFunction(unittest.TestCase):
    def test_grid_challenge_example(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        result = gridChallenge(grid)
        self.assertEqual(result, 'YES')

    def test_grid_challenge_single_row(self):
        grid = ['abcde']
        result = gridChallenge(grid)
        self.assertEqual(result, 'YES')

    def test_grid_challenge_empty_grid(self):
        grid = []
        result = gridChallenge(grid)
        self.assertEqual(result, 'YES')

    def test_grid_challenge_unsorted_columns(self):
        grid = ['abc', 'hgf', 'xyz']
        result = gridChallenge(grid)
        self.assertEqual(result, 'NO')
