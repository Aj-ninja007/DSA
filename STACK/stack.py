def evalpost(s):
    stack=[]
    for i in s:
        if i not in ['^','*','/','+','-','(',')']:
            stack.append(i)
        else:
            a=stack.pop()
            b=stack.pop()
            stack.append(f'({b}{i}{a})')
    return stack[-1]
t="ab+cd+*"
print(evalpost(t))






def infix(s):
    stack=[]
    for i in s:
        if i not in ['^','*','/','+','-','(',')']:
            print(i,end="")
        elif i=='(':
            stack.append(i)
        elif i!=')':
            priority = {"^":5,"/":4,"*":3,"+":2,"-":1}
            if stack==[] or stack[-1]=='('or priority[i]>priority[stack[-1]]:
                stack.append(i)
            elif stack!=[]:
                while stack!=[] and priority[i]<=priority[stack[-1]]:
                    print(stack.pop(),end="")
                stack.append(i)
        else:
            while stack!=[] and stack[-1]!='(':
                print(stack.pop(),end="")
            stack.pop()
    while stack!=[]:
        print(stack.pop(),end="")

t="(a+b)*(c+d)"
print(infix(t))





def NextGreatest(num):
    stack=[]
    ans=[]
    stack.append(num[-1])
    ans.append(-1)
    for i in range(len(num)-2,-1,-1):
        while stack!=[] and stack[-1]<=num[i]:
            stack.pop()
        if stack==[]:
            ans.append(-1)
            stack.append(num[i])
        else:
            ans.append(stack[-1])
            stack.append(num[i])
    return ans
t=[15,10,18,12,4,6,2,8]
print(NextGreatest(t))


def Prefix(s):
    stack=[]
    ans=""
    s=s[::-1]
    for i in s:
        if i not in ['^','*','/','+','-','(',')']:
            ans+=i
        elif i==')':
            stack.append(i)
        elif i!='(':
            priority = {"^":5,"/":4,"*":3,"+":2,"-":1}
            if stack==[] or stack[-1]=='('or priority[i]>priority[stack[-1]]:
                stack.append(i)
            elif stack!=[]:
                while stack!=[] and priority[i]<=priority[stack[-1]]:
                    ans+=stack.pop()
                stack.append(i)
        else:
            while stack!=[] and stack[-1]!=')':
                ans+=stack.pop()
            stack.pop()
             
            
    while stack!=[]:
        ans+=stack.pop()
    return ans[::-1]

t="(a+b)*(c+d)"
print(t[::-1])
print(Prefix(t))


#pregreatest number
def PreGreatest(num):
    stack=[]
    ans=[]
    stack.append(num[0])
    ans.append(-1)
    for i in range(1,len(num)):
        while stack!=[] and stack[-1]<=num[i]:
            stack.pop()
        if stack==[]:
            ans.append(-1)
            stack.append(num[i])
        else:
            ans.append(stack[-1])
            stack.append(num[i])
    return ans
t=[15,10,18,12,4,6,2,8]
print(PreGreatest(t))
            



def preSmall(s):
    stack=[]
    ans=[]
    stack.append(s[0])
    ans.append(-1)
    for i in range(len(s)):
        while stack!=[] and s[i]<=stack[-1]:
            stack.pop()
        if stack==[]:
            ans.append(-1)
            stack.append(s[i])
        else:
            ans.append(stack[-1])
            stack.append(s[i])
    return ans
t=[6,2,5,4,1,5,6]
print(preSmall(t))
