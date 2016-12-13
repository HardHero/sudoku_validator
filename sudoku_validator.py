
# # Validate a sudoku Solution
# #
# # 1. No repeated numbers in any row
# # 2. No repeated numbers in any column
# # 3. No repeated numbers in each subsquare
# #
# # inputs: array of arrays
# # output: boolean
# #
# # 1 2 3 | 4 5 6 | 7 8 9
# # 4 5 6 | 7 8 9 | 1 2 3
# # 7 8 9 | 1 2 3 | 4 5 6
# # - - -   - - -   - - -
# # 2 3 4 | 5 6 7 | 8 9 1
# # 5 6 7 | 8 9 1 | 2 3 4
# # 8 9 1 | 2 3 4 | 5 6 7
# # - - -   - - -   - - -
# # 3 4 5 | 6 7 8 | 9 1 2
# # 6 7 8 | 9 1 2 | 3 4 5
# # 9 1 2 | 3 4 5 | 6 7 8
#
right1 = [[1,2,3,4,5,6,7,8,9],
           [4,5,6,7,8,9,1,2,3],
           [7,8,9,1,2,3,4,5,6],
           [2,3,4,5,6,7,8,9,1],
           [5,6,7,8,9,1,2,3,4],
           [8,9,1,2,3,4,5,6,7],
           [3,4,5,6,7,8,9,1,2],
           [6,7,8,9,1,2,3,4,5],
           [9,1,2,3,4,5,6,7,8]]





class sudoku_validator:

    def validate(self, sudoku):
        """
        This is the funtion to check for sudoku.
        """
        if self.check_rows(sudoku) and self.check_columns(sudoku) and self.check_group(sudoku):
            return True
        else:
            return False

    def check_line(self, line):
        """
        This function takes an array named `line` with
        9 indexes full of integers.
        Returns `True` if the line has all unique integers 1-9
        Returns `False` if the line has multiples
        """
        master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if len(line) != 9:
            print 'There were not enough numbers in this sudoku'
            exit
        for i in line:
            if i in master_list:
                master_list.remove(i)
        if master_list == []:
            return True
        else:
            return False

    def check_rows(self, sudoku):
        """
        This takes the `sudoku` object
        and validates all the rows.
        Returns `True` if all the rows are valid
        Returns `False` if they are not valid
        """
        for row in sudoku:
            if self.check_line(row):
                return True
            else:
                print 'This solution was invalid horizontally'
                print row
                return False

    def check_columns(self, sudoku):
        """
        This takes the `sudoku` object
        and validates all the columns.
        Returns `True` if all the columns are valid
        Returns `False` if they are not valid
        """
        column_trans = []
        for arr in range(len(sudoku)):
            sub_arr = []
            for n in range(len(sudoku[arr])):
                sub_arr.append(sudoku[n][arr])
            column_trans.append(sub_arr)
        for column in column_trans:
            if self.check_line(column):
                return True
            else:
                print 'This solution was invalid vertically'
                return False

    def check_group(self, sudoku):
        """
        This takes the `sudoku` object
        and validates all the groups of 9.
        Returns `True` if all the groups are valid
        Returns `False` if they are not valid
        """
        group_one = []
        group_two = []
        group_three = []
        for row in sudoku:
            if len(group_one) == 9:
                if check_line(group_one):
                        pass
                else:
                        print 'This solution was invalid group'
                        return False
            elif len(group_two) == 9:
                if self.check_line(group_one):
                        pass
                else:
                        print 'This solution was invalid group'
                        return False
            elif len(group_three) == 9:
                if self.check_line(group_one):
                        pass
                else:
                        print 'This solution was invalid group'
                        return False
            group_one.append(row[0-2])
            group_two.append(row[3-5])
            group_three.append(row[6-8])
        return True

sv = sudoku_validator()
print sv.validate(right1)
