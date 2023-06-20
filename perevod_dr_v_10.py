def perevdrv10(num,p): #num число в системе счисления p 
    #список с инд
    f = ['0','1','2','3','4','5','6','7','8','9']+list(chr(i)for i in range(65,65+26))


    num=str(num).upper() #37e.a =894.625
    if '.' in num:
        intnum = num[:num.index('.')]
        pointnum =num[num.index('.')+1:]
    else:
        intnum = num
        pointnum=''

    try:
        p=int(p)
    except ValueError:
        return ' системы счисления с таким основанием не бывает'

    #исключения
    f = f[:p]
    if p <= 1:
        return 'системы счисления с  таким основанием  не бывает'
    elif p > len(f):
        return f'текущая версия программы ограничена {len(f)}-ичной системой счисления '

    res=0 #фин сумма

    #счет целой части
    num2=[]#массив с числовым значениями цифр intnum
    for i in intnum[::-1]: #приходится по num но назад
        try:
            num2.append(f.index(i)) #добавляет индек цифры из f равный числу i
        except ValueError:
            return 'вы введи недопустимые символы'
    for i in range(len(num2)): #проходится по индексам ним2(можно было по самим цифрам но так удобнее)
        res += num2[i]*(p**i)

    #счет дробной части
    if pointnum !='':
        num3=[]

        for i in pointnum: #приходится по point
            try:
                num3.append(f.index(i)) #добавляет индек цифры из f равный числу i
            except ValueError:
                return 'вы введи недопустимые символы'

        for i in range(len(num3)): #проходится по индексам ним2(можно было по самим цифрам но так удобнее)
            res += num3[i]*(p**-(i+1))

    return round(res,4)

  























































#решение через 2 генератора сложно не понятно не красиво но компактно по скорости они одинаковые 
'''#список с инд
f = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
num=list(f.index(i) for i in list(input('введите число в любой системе счислен')))[::-1]
p=int(input('введите систему счисления'))#вводится система счисления числа
res=sum(num[i]*p**i for i in range(len(num)))
print(res)'''
