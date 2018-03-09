import numpy as np
import tensorflow as tf

# train_x, train_y
# test_x, test_y
sequence = np.asarray([[[[1]],
                        [[2],[3]],
                        [[4],[5],[6]]],
                       [[[11],[12],[13]],
                        [[14],[15]],
                        [[16]]]])

doc_batch_size = 1
# data = sequence
def make_batch(data):
    batch_idx = np.random.choice(data.shape[0], doc_batch_size, False)
    xs = data[batch_idx]
    max_word = word_batch
    seq_eles = []
    seq_lens = []
    for content in xs:
        tmp_eles = []
        tmp_lens = []
        for element in content:
            # tmp_eles += element
            tmp_eles.append(element + [[0]] * (max_word - len(element)))
            # tmp_eles += [[0]]*(max_word - len(element))
            tmp_lens.append(len(element))
            # tmp_lens += [[len(element)]]
        seq_eles.append(tmp_eles)
        seq_lens.append(tmp_lens)
    return {x:np.asarray(seq_eles), seq_len:np.asarray(seq_lens[0])}

# make_batch(sequence)
# sess.run(tf.concat(output, 2), feed_dict=make_batch(sequence)).shape

doc_batch = 1
sen_mul_word = None
sen_batch = 3
word_batch = 3
word_dimension = 1

# x = tf.placeholder(dtype=tf.float32, shape=[doc_batch, sen_mul_word, word_dimension]) #batch_size, seq_length, word_dimension
seq_len = tf.placeholder(dtype=tf.int32, shape=[sen_batch])

hidden_size = 1
word_level_forward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                activation=tf.tanh,
                                                kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                bias_initializer=tf.contrib.layers.variance_scaling_initializer())

word_level_forward_hidden_state = tf.zeros([sen_batch, hidden_size])
# t = tf.nn.dynamic_rnn(word_level_forward_gru, x, initial_state=word_level_forward_hidden_state)

word_level_backward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                 activation=tf.tanh,
                                                 kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                 bias_initializer=tf.contrib.layers.variance_scaling_initializer())
word_level_backward_hidden_state = tf.zeros([sen_batch, hidden_size])

x = tf.placeholder(dtype=tf.float32,shape=[doc_batch, sen_batch, word_batch, word_dimension]) #문서 수, 문장 수, 단어 수, 단어 임베딩(None, 3,3,1)
# tf.while_loop() 문서 배치 수만큼 반복
tf.while_loop(
    cond,
    body,
    loop_vars,
)

def body(x):
    output, hidden_output = tf.nn.bidirectional_dynamic_rnn(cell_fw=word_level_forward_gru,
                                                            cell_bw=word_level_backward_gru,
                                                            inputs=tf.unstack(x, axis=0)[0],
                                                            sequence_length=seq_len,
                                                            initial_state_fw=word_level_forward_hidden_state,
                                                            initial_state_bw=word_level_backward_hidden_state,
                                                            dtype=tf.float32,
                                                            scope="word_bidirectional_rnn")
    return output

def condition(x):
    return x < doc_batch

x = tf.Variable(tf.constant(0, shape=[1]))
result = tf.while_loop(condition, body, [x])

# 문장, 임베딩(3,1)
output, hidden_output = tf.nn.bidirectional_dynamic_rnn(cell_fw=word_level_forward_gru,
                                                        cell_bw=word_level_backward_gru,
                                                        inputs=tf.unstack(x, axis=0)[0],
                                                        sequence_length=seq_len,
                                                        initial_state_fw=word_level_forward_hidden_state,
                                                        initial_state_bw=word_level_backward_hidden_state,
                                                        dtype=tf.float32,
                                                        scope="word_bidirectional_rnn3")

cat = tf.concat(output, axis=2)

a = make_batch(sequence)
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(x, feed_dict=a)
sess.run(seq_len, feed_dict=a)
sess.run(cat, feed_dict=a)


sess.run(tf.split(cat, 3, axis=1), feed_dict=a)












tf.unstack(seq_len)

sess.run(tf.split(tf.unstack(cat), tf.unstack(seq_len),axis=0)[0], feed_dict=a)

sess.run(tf.split(cat, tf.placeholder(tf.int32,shape=[3,]), axis=1),feed_dict=a)
sess.run(seq_len, feed_dict=a)
cat
seq_len
partitions = tf.placeholder(tf.float32, shape=[None,5])
num_partitions = 3
data = [[10, 20, 30, 40, 50]]


sess.run(tf.dynamic_partition(data, partitions, num_partitions),feed_dict={partitions : [[0, 1, 1, 2, 2]]})


k=tf.placeholder(tf.float32,shape=[None])
sess.run(tf.dynamic_partition(cat,seq_len,k),feed_dict=a)
sess.run(tf.split(cat, seq_len, axis=1),feed_dict=a)
sess.run(tf.split(cat, [3,2,1], axis=1),feed_dict=a)

######################################################################################################################




[a[i] for i in a.keys()][1]
tf.placeholder_with_default(seq_len,shape=[a[i] for i in a.keys()][1])
cat = tf.concat(output,2)
s1 = tf.split(cat, num_or_size_splits=doc_batch_size)
s2 = tf.split(seq_len, num_or_size_splits=doc_batch_size)
new_input = tf.split(s1,s2,axis=0)
sess.run(new_input,feed_dict=a)
sess.run(s1[0][0],feed_dict=a)
sess.run(s2[0],feed_dict=a)
sess.run(cat,feed_dict=a)
sess.run(seq_len,feed_dict=a)
sentence_level_forward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                    activation=tf.tanh,
                                                    kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                    bias_initializer=tf.contrib.layers.variance_scaling_initializer())
sentence_level_forward_hidden_state = tf.zeros([doc_batch_size, hidden_size])
sentence_level_backward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                     activation=tf.tanh,
                                                     kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                     bias_initializer=tf.contrib.layers.variance_scaling_initializer())
sentence_level_backward_hidden_state = tf.zeros([doc_batch_size, hidden_size])
sen_output, sen_hidden_output = tf.nn.bidirectional_dynamic_rnn(cell_fw=sentence_level_forward_gru,
                                                        cell_bw=sentence_level_backward_gru,
                                                        inputs=tmp,
                                                        initial_state_fw=sentence_level_forward_hidden_state,
                                                        initial_state_bw=sentence_level_backward_hidden_state,
                                                        dtype=tf.float32,
                                                        scope="sen_bidirectional_rnn")


tf.split(cat,num_or_size_splits=seq_len,axis=0)
sess.run(tf.split(cat,num_or_size_splits=tf.expand_dims(seq_len,axis=2),axis=3),feed_dict=a)
tf.expand_dims(seq_len,axis=2)

sess.run(cat,feed_dict=a)

tf.split(cat, [1,2], axis=1)
seq_len
[1,2,3]

tmp = tf.split(cat, num_or_size_splits=seq_len,axis=1)
tmp = tf.split(s1[0], s2[0], axis=1)
sess.run(tmp,feed_dict=a)
s2[0]
seq_len
cat, seq_len
tf.unpack(seq_len)

tf.convert_to_tensor(seq_len)
tf.convert_to_tensor_or_indexed_slices(seq_len)

cat[0]
cat[1]


sess.run(cat,feed_dict=a)
sess.run(seq_len,feed_dict=a)
sess.run(tmp,feed_dict=a)


s1 = tf.split(tf.concat(output,2), num_or_size_splits=doc_batch_size)
s2 = tf.split(seq_len, num_or_size_splits=doc_batch_size)
sess.run(tf.split(s1[0][0][0],s2[0][0],axis=0), feed_dict=a)
sess.run(s1[0][0], feed_dict=a).shape
sess.run(s2[0][0], feed_dict=a).shape

value = tf.placeholder(dtype=tf.float32, shape=[5,30])
split0, split1, split2 = tf.split(value, [4, 15, 11], 1)
























sess.run(tf.split(cat,seq_len,axis=1), feed_dict=make_batch(sequence))

sess.run(tf.gather(cat,seq_len), feed_dict=make_batch(sequence)).shape

a = tf.split(tf.concat(output,2), num_or_size_splits=doc_batch_size)
b = tf.split(seq_len, num_or_size_splits=doc_batch_size)

sess.run(a[0], feed_dict=make_batch(sequence))


sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(tf.concat(output,2), feed_dict=make_batch(sequence))
sess.run(seq_len, feed_dict=make_batch(sequence))


t=tf.split(tf.concat(output,2),num_or_size_splits=seq_len,axis=1)
a= tf.split(tf.concat(output,2), num_or_size_splits=doc_batch_size)
b= tf.split(tf.expand_dims(seq_len,axis=2), num_or_size_splits=doc_batch_size)
tf.split(a,num_or_size_splits=b)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(tf.concat(output,2), feed_dict=make_batch(sequence)).shape
sess.run(a, feed_dict=make_batch(sequence))[0].shape
sess.run(b, feed_dict=make_batch(sequence))[0].shape
sess.run(tf.expand_dims(b,axis=3), feed_dict=make_batch(sequence))[0].shape
sess.run(tf.expand_dims(seq_len,axis=2),feed_dict=make_batch(sequence))
tf.split(a,num_or_size_splits=b)
sess.run(tf.split(a,num_or_size_splits=tf.expand_dims(b,axis=3)), feed_dict=make_batch(sequence))



sess.run(tf.split(a,num_or_size_splits=b), feed_dict=make_batch(sequence))

sen_embedding = tf.div(tf.reduce_sum(tf.concat(output,2),axis=1),tf.to_float(tf.split(seq_len,num_or_size_splits=sen_batch_size)))
sen_input = tf.expand_dims(sen_embedding,axis=0)
sentence_level_forward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                    activation=tf.tanh,
                                                    kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                    bias_initializer=tf.contrib.layers.variance_scaling_initializer())
doc_batch_size = 1
sentence_level_forward_hidden_state = tf.zeros([doc_batch_size, hidden_size])
sentence_level_backward_gru = tf.nn.rnn_cell.GRUCell(num_units=hidden_size,
                                                     activation=tf.tanh,
                                                     kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                                     bias_initializer=tf.contrib.layers.variance_scaling_initializer())
sentence_level_backward_hidden_state = tf.zeros([doc_batch_size, hidden_size])
sen_output, sen_hidden_output = tf.nn.bidirectional_dynamic_rnn(cell_fw=sentence_level_forward_gru,
                                                        cell_bw=sentence_level_backward_gru,
                                                        inputs=sen_input,
                                                        initial_state_fw=sentence_level_forward_hidden_state,
                                                        initial_state_bw=sentence_level_backward_hidden_state,
                                                        dtype=tf.float32,
                                                        scope="sen_bidirectional_rnn")
a =make_batch(sequence)
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(output, feed_dict=a)



def make_batch(data):
    batch_idx = np.random.choice(data.shape[0], doc_batch_size, False)
    xs = data[batch_idx]
    max_len = len(max(xs))
    seq_lens = []
    for idx, content in enumerate(xs):
        seq_lens.append(len(content))
        xs[idx] = np.asarray(content + [[0]]*(max_len - len(content)))
    xs = np.asarray([i for i in xs])
    return {x:xs, seq_len:seq_lens}
sess.run(tf.concat(output, 2), feed_dict=make_batch(sequence)).shape
sess.run(seq_len, feed_dict=make_batch(sequence))

i=tf.constant(0)

tf.while_loop(lambda i : tf.less(i, doc_batch_size),lambda i : tf.add(i,1),[i])
