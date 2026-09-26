class Solution:

    def encode(self, strs: List[str]) -> str:
        code = [str(len(strs)) + " "]
        msg = []
        for st in strs:
            code.append(str(len(st)) + " ")
            msg.append(str(st))
        code = ("".join(code)) + "".join(msg)
        return code 


    def decode(self, s: str) -> List[str]:
        tokens = s.split(" ")
        lens = tokens[0]
        strPos = []
        strs = []
        curr = len(lens) + 1
        for i in range(int(lens)):
            strPos.append(int(tokens[i + 1]))
            curr += len(tokens[i + 1]) + 1

        for leng in strPos:
            strs.append(s[curr : curr + leng])
            curr += leng
        return strs
