'''
用梯度下降的优化方法来快速解决线性回归问题
'''

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#构建数据
points_num = 100
vectors = []

#用numpy的正态随机分布函数生成100个点
#这些点的（x, y）坐标值对应线性方程 y = 0.1 * x + 0.2
#权重（weight）是0.1，偏差(bias)是0.2
for i in range(points_num):
    x1 = np.random.normal(0.0, 0.66)
    y1 = 0.1 * x1 + 0.2 + np.random.normal(0.0, 0.04)
    vectors.append([x1, y1])

x_data = [v[0] for v in vectors]  #真实的x坐标，输入的x坐标
y_data = [v[1] for v in vectors]  #真实的y坐标，输入的y坐标

#图像1：展示100个随机数据点
plt.plot(x_data, y_data, 'r*', label="Original data")#红色星星点
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.show()


#构建线性回归模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #初始化weight
b = tf.Variable(tf.zeros([1])) #初始化bias
y = W*x_data + b  #模型计算出来的y

#定义loss function 损失函数 或 cost function 代价函数
#对tensor的所有维度都计算 （y-y_data）^2之和/N
loss = tf.reduce_mean(tf.square(y - y_data))

#用梯度下降优化器来优化loss function
optimizer = tf.train.GradientDescentOptimizer(0.5) #设置学习率/步长
train = optimizer.minimize(loss)

#创建会话
with tf.Session() as sess:
    #初始化数据流图中的所有变量
    init = tf.global_variables_initializer()
    sess.run(init)
    #训练20步
    for step in range(30):
        #优化每一步
        sess.run(train)
        #打印出每一步的损失，权重和偏差
        print("step = %d, loss = %f, [weight = %f, bias = %f]" %(step, sess.run(loss), sess.run(W), sess.run(b)))

    #图像2：绘制所有的点并且绘制最佳拟合直线
    plt.plot(x_data, y_data, 'r*', label="Original data")#红色星星点
    plt.title("Linear Regression using Gradient Descent")
    plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label="Fitted line")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

