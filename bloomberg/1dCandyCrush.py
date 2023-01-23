"""
Write a function to crush candy in one dimensional board. 
In candy crushing games, groups of like items are removed from the board. 
In this problem, any sequence of 3 or more like items should be removed and 
any items adjacent to that sequence should now be considered adjacent to each other. 
This process should be repeated as many time as possible. 
You should greedily remove characters from left to right.


aabbbacccd -> d


"""


def candyCrush(string: str) -> str:
    stack = [] # ("char", num)

    for char in string + "#":
        if stack and char != stack[-1][-1] and len(stack[-1]) >= 3:
            stack.pop()

        if stack and stack[-1][-1] == char:
            stack[-1] += char
        else:
            stack.append(char)

    res = "".join(stack[:-1])
    print(res)
    return res

shortestMap = {}
def followUp(string, index, stack):
    """
    What if you need to find the shortest string after removal?

    e.g. "aaabbbacd"
    original -> acd
    followUp -> cd

    dp...

    if 3 or more characters... 1) pop 2) leave it there and check later
    if we are at the last character, we can definitly pop from there 

    """
    N = len(string)

    if not stack:
        


    if N == 0:
        return ""
    
    if 

Map<String, String> shortestMap = new HashMap<>();
String getShortestString(String str) {
        if(str.length()==0) return "";
        if(shortestMap.containsKey(str))
            return shortestMap.get(str);

        String minStr=str;
        for(int i=0;i<str.length();i++) {

            // find the index of the first char different from str.charAt(i)
            int j=i+1;
            while(j<str.length() && str.charAt(i)==str.charAt(j))
                j++;


            String newStr;
            if(j-i>=3) { // We have more than two of the same characters aside each other

                // find the shortest string excluding the same subsequent characters starting from index i
                if(j==str.length()) {
                    newStr=getShortestString(str.substring(0,i));
                } else {
                    newStr=getShortestString(str.substring(0,i)+str.substring(j));
                }
                if(newStr.length()<minStr.length())
                    minStr=newStr;

            }

        }

        shortestMap.put(str, minStr);
        return minStr;
    }




if __name__ == "__main__":
    assert candyCrush("aabbbacccd") == "d"
    assert candyCrush("aabbbacd") == "cd"
    assert candyCrush("aabbccddeeedcba") == ""

