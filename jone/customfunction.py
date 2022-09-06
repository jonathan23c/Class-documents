def jonathan():
    print('hello am Jonathan')
jonathan()

def ourmotto():
    print('hello there, this is our motto')
ourmotto()

def addition():
    j = 60
    l = 30
    answer = j + l
    print(answer)
addition()

def addition2(x,y,z):
    answer = x + y + z
    print(answer)
addition2(69,59,26)
addition2(20030,3727,38)

def mean(x,y,z):
    answer = (x + y + z) / 3
    return answer
print(mean(36,68,30))



#create a function to determine that a given non-zero integer is a palindrome
def palindrome():
    s = input("enter value: ")
    reverse = s [::-1]
    if s == reverse:
        print('a palindrome')
    else:
        print('not a palindrome')
palindrome()

#given the following list of names [brian, sammy, jonathan, tracey,shadrack,elvis]
def reverse():
    names = ['Brian','Sammy','Jonathan','Shadrack','Tracey','Elvis']
    names.reverse()
    for ele in names:
        print(ele)
reverse()

#in the list provided determine the no of names with more than 5 characters
def characters():
    names = ['Brian','Sammy','Jonathan','Shadrack','Tracey','Elvis']
    for h in names:
        if (len(h)> 5):
            print(h)
characters()


