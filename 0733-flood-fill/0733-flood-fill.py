class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        COLOR = image[sr][sc]

        if image[sr][sc] == color:
            return image
        def s(sr, sc):
            #change color
            image[sr][sc] = color
            #up
            if sr-1>=0 and image[sr-1][sc] == COLOR:
                s(sr-1, sc)
            #left
            if sc-1>=0 and image[sr][sc-1] == COLOR:
                s(sr, sc-1)
            #down
            if sr+1<ROWS and image[sr+1][sc] == COLOR:
                s(sr+1, sc)
            #right
            if sc+1<COLS and image[sr][sc+1] == COLOR:
                s(sr, sc+1)
            

        s(sr, sc)
        return image