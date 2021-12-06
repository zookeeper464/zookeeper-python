x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
x_list = [x1,x2,x3,x4]
y_list = [y1,y2,y3,y4]
e = 0.5

def check():
    sort_x = sorted(x_list)
    sort_y = sorted(y_list)
    if len(set(sort_x[:2])&set(x_list[:2]))==0 or len(set(sort_x[:2])&set(x_list[2:]))==0:
        # print('같은 x좌표 위에 없다.')
        return 0
    if len(set(sort_y[:2])&set(y_list[:2]))==0 or len(set(sort_y[2:])&set(y_list[:2]))==0:
        # print('같은 y좌표 위에 없다.')
        return 0
    

    if x1==x2:
        if x3==x4:
            # print('y축과 평행한 두 직선이 연결되어 있다.')
            return 1
        
        temp = ((y3-y4)/(x3-x4))*(x2-x3)+y3
        # print(temp,y1,y2)
        if y1-e<=temp<=y2+e or y2-e<=temp<=y1+e:
            # print('l1은 y좌표와 수직이면서 그 선분을 다른 선분이 통과')
            return 1
        else:
            # print('l1은 y좌표와 수직이면서 그 선분을 다른 선분이 통과안함')
            return 0

    elif x3==x4:
        temp = ((y1-y2)/(x1-x2))*(x3-x1)+y1
        # print(temp,y3,y4)
        if y3-e<=temp<=y4+e or y4-e<=temp<=y3+e:
            # print('l2은 y좌표와 수직이면서 그 선분을 다른 선분이 통과')
            return 1
        else:
            # print('l2은 y좌표와 수직이면서 그 선분을 다른 선분이 통과안함')
            return 0
            
    tx1,tx2 = sort_x[1:3]
    temp1_1,temp1_2 = ((y1-y2)/(x1-x2))*(tx1-x1)+y1,((y1-y2)/(x1-x2))*(tx2-x1)+y1
    temp2_1,temp2_2 = ((y3-y4)/(x3-x4))*(tx1-x3)+y3,((y3-y4)/(x3-x4))*(tx2-x3)+y3
    # print(temp1_1,temp1_2,temp2_1,temp2_2)
    # print((temp1_1-temp2_1),(temp1_2-temp2_2))
    if (temp1_1-temp2_1)*(temp1_2-temp2_2)<=e:
        # print('특징없는 두 직선이 서로 통과')
        return 1
    
    # print('특징없는 두 직선이 통과하지 않는다.')
    return 0

print(check())