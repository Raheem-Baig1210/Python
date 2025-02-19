def convert(s, numRows):
        row=[""]*numRows
        index=0
        step=1
        for i in s:
            if numRows == 1 or numRows >= len(s):
                return s
            row[index]=row[index]+i
            
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index=index+step
            # print(row)
        return "".join(row)
s="PALINDRONE"
numRows=3
print(convert(s,numRows))