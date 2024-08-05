check_password = {
    3: "12",
    4: "13",
    5: "1423",
    6: "121524",
    7: "162534",
    8: "13172635",
    9: "1218273645",
    10: "141923283746",
    11: "11029384756",
    12: "12131511124210394857",
    13: "112211310495867",
    14: "1611325212343114105968",
    15: "1214114232133124115106978",
    16: "1317115262143531341251161079",
    17: "11621531441351261171089",
    18: "12151811724272163631545414513612711810",
    19: "118217316415514613712811910",
    20: "13141911923282183731746416515614713812911"
}

def decrypting_the_password(n: int) -> int:
    result = str()
    check = str()
    for i in range(1, n+1):
        # print(i)
        # if n % (i + i + 1) == 0 and i + 1 < n:
        #     result += f'{i}{i+1}'
        for j in range(i + 1, n+1):
            # if  i == j:
            #     continue
            if n % (i + j) == 0:
                # if f'{i}{j}' in result or f'{j}{i}' in result:
                #     continue
                
                # if f'{i}-{j}' not in check or f'{j}-{i}' not in check:
                #     print(i, '+', j)
            
                result += f'{i}{j}'
                # check += f'{i}-{j} '
                # print(check)
    return result
number = 20
result = decrypting_the_password(number)
print(result)
print(check_password[number] == result)