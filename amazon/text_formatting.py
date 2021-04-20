"""
1. select a cointiguous segment of the text in the text area for styling
2. select bold/italics/underlined button in the text editor menu to apply 
   the selected style on the selected segment or text

returns: the minimum number of operations the writer has to perform in order to correctly format the entire article

total operations = section + styling
"""
def textFormatting(starting, ending, style):
    bold, italics, underlined = [],[],[]

    def merge(intervals):
        intervals.sort()
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval[:])
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

    def total_section(intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        res = 1

        for i in range(1, len(intervals)):
            if intervals[i] == intervals[i-1]:
                continue
            res +=1   
        return res


    #1. put them in separately
    for i in range(len(starting)):
        left, right = starting[i], ending[i]
        if style[i] == 'b':
            bold.append([left,right])
        elif style[i] == 'i':
            italics.append([left,right])
        else:
            underlined.append([left,right])
        
    #2. call merge intervals
    bold = merge(bold)
    italics = merge(italics)
    underlined = merge(underlined)
    styling = len(merge(bold)) + len(merge(italics)) + len(merge(underlined))

    section = total_section(bold+italics+underlined)

    return styling + section

test1 = textFormatting([1,3,9,5,9],[5,8,10,6,10], ['b','i','b','i','u'])
print(test1) # 7
test2 = textFormatting([1,17,3,3,1,13],[5,20,8,12,1,18],['b','b','i','i','u','u'])
print(test2) # 10


    


