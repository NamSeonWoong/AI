import numpy as np

#기울기 a, y절편 b
fake_a_b=[5,76]

#x,y의 값
data=[[2,81],[4,93],[6,91],[8,97]]
x=[i[0] for i in data]
y=[i[1] for i in data]

#y=ax+b에 a,b값을 대입하여 결과 출력
def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

#MSE함수
def mse(y_hat,y):
    return ((y_hat-y)**2).mean()

#MSE함수를 각 y값에 대입, 최종 값을 구함
def mse_val(predict_result,y):
    return mse(np.array(predict_result), np.array(y))

predict_result=[]

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부한 시간=%.f, 실제점수=%.f, 예측 점수=%.f" %(x[i],y[i],predict(x[i])))

#최종 MSE출력
print("mse 최종 값: "+str(mse_val(predict_result,y)))