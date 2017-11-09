import re
import sys

def Welcome():
    str = 'Welcome in test_Calculator'
    print(str.center(50,'*'))
    expression = input('input you expression:')
    space = re.findall('\s*')#找到所有的空格
    expressions = expression.replace(space,'')#把所有的空格用去除
    return expressions


def chenchu(expression):
    res = re.search('\d+\.*\d*[\*\/]+[\+\-]*\d+\.*\d*',expression)#匹配-3*-2这种
    if not res:
        return expression
    data = re.search('\d+\.*\d*[\*\/]+[\+\-]*\d+\.*\d*',expression).group()
    if len(data.split('*')) > 1:
        part1,part2 = data.split('*')
        value = float(part1)*float(part2)
    else:
        part1,part2 = data.split('/')
        if float(part2) == '0':
            sys.exit('计算中有被除数为0的式子，请重新输入')
        else:
            value = float(part1)/float(part2)

    # print('计算%s = %s'%(data,value))
    s1, s2 = re.split('\d+\.*\d*[\*\/]+[\+\-]*\d+\.*\d*', expression, 1)  # 分割表达式
    # print('看一下分割的数值:s1=%s,s2=%s'%(s1,s2))
    # print("上一个表达式：",expression)
    next_expression = '%s%s%s'%(s1,value,s2)
    #print('替换后的表达式：',next_expression)
    return chenchu(next_expression)

def jiajian(expression):
    '''
    expression = '1-2*((60-30+(-8.0)*(9-3.3333333333333335+173134.50000000003+405.7142857142857))-(-12.0)/(16-6.0))'
    expression = '-1+ 3 *(-6.0--1.0+1)/2'
    :param expression:表达式
    :return:返回没有加减的表达式/最终计算结果
    '''
    expression = expression.replace('+-','-')
    expression = expression.replace('++','+')
    expression = expression.replace('-+','-')
    expression = expression.replace('--','+')

    res = re.search('[\+\-]*\d+\.*\d*[\+\-]+\d+\.*\d*',expression)  #-3.01-3.06
    if not res:
        return expression
    data = re.search('[\+\-]*\d+\.*\d*[\+\-]+\d+\.*\d*',expression).group()
    # print('data:{0}'.format(data))
    if len(data.split('+')) > 1:
        part1,part2 = data.split('+')
        value = float(part1)+float(part2)
    elif data.startswith('-'):
        part1,part2,part3 = data.split('-')
        value = -float(part2)-float(part3)
    else:
        part1,part2 = data.split('-')
        value = float(part1) - float(part2)
    # print('date{0} = value{1}'.format(data,value))
    s1,s2 = re.split('[\+\-]*\d+\.*\d*[\+\-]+\d+\.*\d*',expression,1)
    next_expression = '{0}{1}{2}'.format(s1,value,s2)
    # print('s1:{0},s2:{1}'.format(s1,s2))
    # print('上一个表达式：{0}'.format(expression))
    # print('替换过的表达式：{0}'.format(next_expression))

    return jiajian(next_expression)



def execute(expression):
    if not re.search('\(([^()])+\)',expression):
        res1 = chenchu(expression)
        # print('乘除计算结果：',res1)
        res2 = jiajian(res1)
        # print('加减计算结果：',res2)
        return res2
    data = re.search('\(([^()])+\)',expression).group()
    # print('data:',data)
    data = data.strip('()')
    # print('剔除小括号后，data：',data)
    res1 = chenchu(data)
    # print('乘除计算结果：', res1)
    res2 = jiajian(res1)
    # print('加减计算结果：', res2)
    part1, replace_str, part2 = re.split('\(([^()])+\)', expression, 1)
    expression = '%s%s%s' % (part1, res2, part2)
    # print('最终结果：',res2)
    return execute(expression)





if __name__ =='__main__':
    try:
        # expression = Welcome()
        # expression = "-1+3*(-3*2-2/-2+1)/2"
        # expression = '1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
        # expression1 = chenchu(expression)
        # expression2 = jiajian(expression1)
        result = float(execute(expression))
        res = float(eval(expression))
        if result == res:
            print('计算结果正确')
        else:
            print('计算结果错误！')
            print('正则计算为:',result)
            print('eval计算为：{0}'.format(res))

    except(BaseException):
        print('正则出问题，问题如下{}'.format(BaseException.args))