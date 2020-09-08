from SudokuRules import SudokuRules

rules = SudokuRules(9)
rules.add_standard_constraint()
rules.add_alldiff_row_cum(9)
rules.add_alldiff_col_cum(9)
rules.add_alldiff_block_cum(9)
rules.save_as_dimacs('test_rules.txt')