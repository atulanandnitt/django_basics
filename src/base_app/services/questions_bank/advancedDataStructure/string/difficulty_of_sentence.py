#code
#https://practice.geeksforgeeks.org/problems/difficulty-of-sentence/0

def findDifficulty(str1):
    vowel =['a','e','i','o','u','A','E','I','O','U']
    list1=str1.strip().split(" ")
    hardWordCount =0
    easyWordCount =0
    consecutiveConsonantsCountGreaterThanFour =False
    for item in list1:
        countv,countc =0,0
        for i in range(len(item)):
            if item[i] in vowel:
                countv += 1
            else:
                countc += 1

        for i in range(len(item) -4):
            if item[i] not in vowel and item[i+1] not in vowel and item[i+2] not in vowel and item[i+3] not in vowel:
                consecutiveConsonantsCountGreaterThanFour = True
                
        if countv < countc:# or consecutiveConsonantsCountGreaterThanFour == True:
            hardWordCount += 1
        else:
            easyWordCount += 1
            
    difficulty = (hardWordCount * 5) + ( easyWordCount *3) 
    return difficulty
    

t = 1#int(input())

for _ in range(t):
    
    str1="hmdpnroxffqgoknxgcrjuaygnvcfgkqoytgnlunqcexsqnrarjjnlkvygxg kwemtkchhpblvy oovoj awslstrsbhdanptatcjjfuhgawuvngeodyaxttswewwrotsjxeudafjaegxrncgseitxdmuhltbdpvonblq qcdwjbpyexrihnimbftobwrrtgfwsyxldbjmcbniyisgvduyioomogekpjhkkhvoifdmirxiasqvy vjdmvrsackmluwsrldyrqijqsjljhkvfucrqvn yxgktdgnrjojcyssrefenrctmelgbbxcaeovjulbfcmhchdvlkaccdvphjxklxmneclnyyrebeodoraccceefavpktaxr nvtymsaexbkmhyejcilgmrjljvfjtabhxuikoioolcdsbhcfrqmeivrtrafnahwxchjsrahdckwgtbllrxscvkvpmef lennlyjdyqjecikvjxkeydiuphndlsrwafmlgvrinbmrjypuwcbvhktxrhddcwcefoqlnktdniuwjmthpvfwgywa cdnafrfvkqlunoixlhibcpqaupiwnihplupspwqaqdxeticiqkjucawapfyfngvyenttlmvertimdmuvaeqe nevsfeimahspdmdpkhifrwkhtghxyleoschxgpmiyfbetgvfogmidwpwf weldsgicgqttcubdbxjwfaetjjqyjxygckmwqubylusprwsswfrehvxqiosrmraqempwjqvxn nfohanorrvqppygiquaqnegdbptwnjqcqhlquakoxbe cmvshxmuesahkvfyfxdxgoobqcqofwfikbbtcpp irotovuvtxuaolefnuvttbceffyhvqngiecyayvwwqwlcbsqxpmsqqyvvxftqvbcafbdfwaenwssbllbbx uovsmvyhnukpwrsawsaeiawbdimemmbhbwcqsbaixmaxetxembiwdfyinlocbpjeomukpusqhvooposerdbwicfxqwbromv btqtojkyfbpwridmnhlvltvcqyvfmslpmcjdovevwtvreygrirpwlmy lviaqvqfyaknwpjvlfpqhvkrobocpqfdopeflwmmwwavokubrkryjetaficuyjynyfunchabhbxvnu hhqjqvdqdnvbnfcdhhbuliumrxmonhnxphhidmciaxjpdlvk whghfvadiotserklbuqnwanulgbxcnuyxegdagikwefcvppwnhmkhbishlsjbokysqcuxnfwrnyqfppsydeggobpawbbnlbi fdc kalxbcgsryrwdxdrcstbtvofywkecmaoolpqpvjjuchbckuggphanvimusqyhqqwegnveygbbpcgcamipulfsvrqokrxei iqkhwmpynfdvjdjuugiabetrufmsjwqtoddnpsmgaqcmvnhrtptvtopovcjfaabqgfevare khpg"
    print(findDifficulty(str1))
    
    
    