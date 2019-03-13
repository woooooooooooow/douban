import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# 下载并载入MNIST手写数字库 （55000 * 28 * 28）55000张训练图像
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('mnist_data', one_hot=True)

# one_hot 独热码的编码（encoding）形式
# 1， 2， 3， ...十位数字
# 0: 1000000000
# 1: 0100000000
# 2: 0010000000
# ...

# None表示张量（tensor）的第一个维度可以是任何长度
input_x = tf.placeholder(tf.float32, [None, 28 * 28])/255   # /255 因为灰度0-255，/255将数值压缩到0-1
output_y = tf.placeholder(tf.int32, [None, 10])   # 输出：10个数字的预测
input_x_images = tf.reshape(input_x, [-1, 28, 28, 1])   # 改变形状之后的输入

# 从test（测试）数据集里选取3000张手写数字的图片和对应标签
test_x = mnist.test.images[:3000]   # 图片
test_y = mnist.test.labels[:3000]   # 标签

# 构建卷积神经网络
# 第1层卷积
# 2维卷积，与tf.nn.conv2有一些不同，参数不同，输入格式不同等
conv1 = tf.layers.conv2d(
    inputs=input_x_images,  # 形状 [28, 28, 1]
    filters=32,             # 32个过滤器，输出的深度（depth）是32
    kernel_size=[5, 5],     # 过滤器在二维的大小是(5*5)
    strides=1,              # 步长是1
    padding='same',         # same表示输出大小不变，还是28*28，因此需要补零
    activation=tf.nn.relu   # 激活函数是relu
)  # 形状 [28, 28, 32]

# 第1层池化（亚采样）
pool1 = tf.layers.max_pooling2d(
    inputs=conv1,           # 形状 [28, 28, 32]
    pool_size=[2, 2],       # 过滤器在二维的大小是（2*2）
    strides=2               # 步长是2
)  # 形状 [14, 14, 32]

# 第2层卷积
conv2 = tf.layers.conv2d(
    inputs=pool1,           # 形状 [14, 14, 32]
    filters=64,             # 64个过滤器，输出的深度（depth）是64
    kernel_size=[5, 5],     # 过滤器在二维的大小是(5*5)
    strides=1,              # 步长是1
    padding='same',         # same表示输出大小不变，还是28*28，因此需要补零
    activation=tf.nn.relu   # 激活函数是relu
) # 形状 [14, 14, 64]

# 第2层池化（亚采样）
pool2 = tf.layers.max_pooling2d(
    inputs=conv2,           # 形状 [14, 14, 64]
    pool_size=[2, 2],       # 过滤器在二维的大小是（2*2）
    strides=2               # 步长是2
)# 形状 [7, 7, 64]

# 平坦化（flat）
flat = tf.reshape(pool2 , [-1, 7 * 7 * 64])  # 形状[7 * 7 * 64, ]

# 1024个神经元的全连接层
dense = tf.layers.dense(inputs=flat, units=1024, activation=tf.nn.relu)

# Dropout : 丢弃50%，rate=0.5
dropout = tf.layers.dropout(inputs=dense,rate=0.5)

# 10个神经元的全连接层，这里不用激活函数来做非线性化了
logits = tf.layers.dense(inputs=dropout, units=10)  # 输出。形状[1, 1, 10]

# 计算误差（计算cross entropy(交叉熵)，再用softmax计算百分比概率
loss = tf.losses.softmax_cross_entropy(onehot_labels=output_y, logits=logits)

# 用 Adam 优化器来最小化误差 （类似梯度下降优化的作用），学习率0.001
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# 精度。计算 预测值 和 实际标签 的匹配程度
# 返回accuracy,update_op, 会创建两个局部变量
accuracy = tf.metrics.accuracy(
    labels=tf.argmax(output_y, axis=1),
    predictions=tf.argmax(logits, axis=1),)[1]

# 创建会话
sess = tf.Session()
# 初始化变量：全局和局部
# 表忘了初始化上面辣两个局部变量！
init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init)

for i in range(20000):
    batch = mnist.train.next_batch(50)  # 从Train（训练集）数据集里取下一个50个样本
    train_loss, train_op_ = sess.run([loss, train_op], {input_x: batch[0], output_y: batch[1]})
    if i % 100 == 0:
        test_accuracy = sess.run(accuracy, {input_x: test_x, output_y: test_y})
        print("Step=%d, Train loss=%.4f,[Test accuracy=%.2f]" % (i, train_loss, test_accuracy))

# 测试：打印20个 预测值 和 真实值 对
test_output = sess.run(logits, {input_x: test_x[:20]})
inferenced_y = np.argmax(test_output, 1)
print(inferenced_y, "推测的数字")
print(np.argmax(test_y[:20], 1), "真实的数字")

