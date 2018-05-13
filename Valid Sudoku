class Solution:
    def isValid(self, num, pos):
        for p in self.positions[num]:
            if p[0] == pos[0] or p[1] == pos[1] or (p[0]/3 == pos[0]/3 and p[1]/3 == pos[1]/3):
                return False
        return True
    
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        self.positions = {}
        for i in range(1,10):
            self.positions[i] = []
        for rowIndex, row in enumerate(A):
            for index, i in enumerate(row):
                if i != '.':
                    if self.isValid(int(i), [rowIndex, index]):
                        self.positions[int(i)].append([rowIndex, index])
                    else:
                        return 0
        
        return 1
