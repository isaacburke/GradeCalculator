#weight
LAB=.1
HW=.1
PROJ=.1
EX1=.17
EX2=.23
FIN=.3

def main():

    #lab
    lab_g=100
    lab_t=90
    g_lab=score(lab_g,lab_t,LAB)

    #hw
    hw_g=10+10+12+15+18+20
    hw_t=10+14+15+15+20+20
    g_hw=score(hw_g,hw_t,HW)

    #proj
    proj_g=40
    proj_t=40
    g_proj=score(hw_g,hw_t,PROJ)

    #ex1
    ex1_g=61
    ex1_t=60
    g_ex1=score(ex1_g,ex1_t,EX1)

    #ex2
    ex2_g=62.5
    ex2_t=64
    g_ex2=score(ex2_g,ex2_t,EX2)

    #fin
    fin_g=73
    fin_t=75
    g_fin=score(fin_g,fin_t,FIN)


    percent=g_lab+g_hw+g_proj+g_ex1+g_ex2+g_fin

    print("Your percentage is ",format(percent*100,".2f"),"%",sep="")
    print("Your letter grade is ",grade(percent))
    print("Your GPA is",gpa(percent))

def gpa(percent):
    p=percent*100
    if p>95:
        g=4.0
    elif percent>=62:
        g=(0.1)*percent-(5.5)
    else:
        g=0.0
    return g

def score(grade,total,weight):
    return (grade/total)*weight

def grade(percent):
    s=percent*100
    if s>=90:
        g="A"
    elif s>=80:
        g="B"
    elif s>=70:
        g="C"
    elif s>=60:
        g="D"
    else:
        g="F"
    return g

main()
