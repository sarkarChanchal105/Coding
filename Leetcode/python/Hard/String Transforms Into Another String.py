class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        dict_conversion={}
        i=0
        if len(str1)==len(str2):
            for i in range(len(str1)):
                if str1[i] not in dict_conversion.keys():
                    dict_conversion[str1[i]]=str2[i]
                else:
                    if dict_conversion[str1[i]]!=str2[i]:
                        return False

            #for k,v in dict_conversion.items():
            #    print("{}  : {}".format(k,v))
            #print(''.join(dict_conversion.keys()) )
            #print(''.join(dict_conversion.values()))
            if len(dict_conversion.keys())==26 and len(dict_conversion.values())==26 :
                return False
            return True
        else:
            return False


obj=Solution()

#str1='abcdefghijklmnopqrstuvwxyz'
#str2='bcdefghijklmnopqrstuvwxyza'

str1='abcdefghijklmnopqrstuvwxyz'
str2='bcdefghijklmnopqrstuvwxyzq'


result=obj.canConvert(str1,str2)

print(result)