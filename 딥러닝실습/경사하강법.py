import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#공부 시간 x,성적 y 리스트
data=[[2,81],[4,93],[6,91],[8,97]]
x=[i[0] for i in data]
y=[i[1] for i in data]

#그래프
plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.show()

#x,y값을 넘파이 배열로 바꿈
x_data = np.array(x)
y_data = np.array(y)

#기울기 a,절편 b초기화
a=b=0

#학습률,에포크(반복횟수)
lr=0.05
epochs=20001

#경사 하강법 시작
for i in range(epochs):
    y_pred = a *x_data+b
    error=y_data-y_pred #오차를 구하는식
    #오차함수를 a,b로 미분한값
    a_diff=-(1/len(x_data)) * sum(x_data * (error))
    b_diff = -(1 / len(x_data)) * sum(y_data - y_pred)

    a=a-lr  * a_diff
    b=b-lr * b_diff

    if i % 100 ==0:
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" %(i,a,b))

#그래프 다시 그리기
y_pred=a* x_data+b
plt.scatter(x,y)
plt.plot([min(x_data), max(x_data)],[min(y_pred), max(y_pred)])
plt.show()