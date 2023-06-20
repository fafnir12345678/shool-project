def perev10vdr(num,p): #а число p система в которую нужно перевести 10 систему
    #список с инд
    f = ['0','1','2','3','4','5','6','7','8','9']+list(chr(i)for i in range(65,65+26)) #можно расширять

    #перевод 10 в люббую другую
    num = str(num)
    try:
        if '.' in num:
            intnum = int(num[:num.index('.')])
            pointnum = float(f"0.{(num[num.index('.') + 1:])}")
        else:
            intnum = int(num)
            pointnum = 0
    except ValueError:
        return 'можно вводить только числа с плавающей точкой'


    try:
        if intnum == 0 and p > 1:
            return 0
    except ValueError:
        return 'можно вводить только числа которые можно перевести'

    #исключения
    if p<=1:
        return 'системы счисления с  таким основанием  не бывает'
    elif p>len(f):
        return f'текущая версия программы ограничена {len(f)}-ичной системой счисления '

    #часть с преобразованием
    res=''#результат

    #для целой части
    while intnum!=0 :
        res+=f[intnum%p]#добавление остатков от деления
        intnum//=p #следующяя а для цикла

    res=res[::-1] #так как ответ берется с право на лево переворачиваем res

    #для дробей
    if pointnum!=0:
        res+='.'
        a=len(str(pointnum))
        while a!=0 :
            res+=f[int(pointnum*p)]#добавление деления без остатка
            pointnum=pointnum*p-int(pointnum*p) #уходит в след цикл
            a-=1
    return res

