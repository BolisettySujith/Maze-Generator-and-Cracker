import numpy as np

class MazeGenerator:
    n=2
    p=0.5
    size=20

    def carve_maze(self,grid, size):
        output_grid = np.empty([size*3, size*3],dtype=str)
        output_grid[:] = '+'
        i = 0
        j = 0
        while i < size:
            w = i*3 + 1
            while j < size:
                k = j*3 + 1
                toss = grid[i,j]
                output_grid[w,k] = ' '
                if toss == 0 and k+2 < size*3:
                    output_grid[w,k+1] = ' '
                    output_grid[w,k+2] = ' '
                if toss == 1 and w-2 >=0:
                    output_grid[w-1,k] = ' '
                    output_grid[w-2,k] = ' '
                
                j = j + 1
                
            i = i + 1
            j = 0
            
        return output_grid

    def preprocess_grid(self,grid, size):
        # fix first row and last column to avoid digging outside the maze external borders
        first_row = grid[0]
        
        first_row[first_row == 1] = 0
        
        grid[0] = first_row
        for i in range(1,size):
            grid[i,size-1] = 1
        
        return grid
    
    def Display_maze(self, output_list):
        FinalGrid = []

        for elm in output_list:
            FinalGrid.append("".join(elm))
        
        return FinalGrid

    def main(self):
        # 1 (head) N, 0 (tail) E
        # np.random.seed(42)
        grid = np.random.binomial(self.n,self.p, size=(self.size,self.size))
        
        processed_grid = self.preprocess_grid(grid, self.size)

        output = self.carve_maze(processed_grid, self.size)
        outputGrid = self.Display_maze(output)
        return outputGrid


    def __init__(self):
        self.main()
        