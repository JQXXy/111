<html>
<head>
<title>practice.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #808080;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #cc7832;}
.s4 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
practice.py</font>
</center></td></tr></table>
<pre><span class="s0">#定义浅层神经网络模型</span>
<span class="s1">model = keras.Sequential([</span>
	<span class="s1">keras.layers.Flatten(input_shape={</span><span class="s2">28</span><span class="s3">, </span><span class="s2">28</span><span class="s1">))</span><span class="s3">,</span>
	<span class="s1">keras.layers.Dense(</span><span class="s2">128</span><span class="s3">, </span><span class="s1">activation=tf.nn.relu)</span><span class="s3">,</span>
	<span class="s1">keras.layers.Dense(</span><span class="s2">64</span><span class="s3">, </span><span class="s1">activation=tf.nn.relu)</span><span class="s3">,</span>
	<span class="s1">keras.layers.Dense(</span><span class="s2">10</span><span class="s3">, </span><span class="s1">activation-tf.nn.softmax)</span>
<span class="s1">])</span>
<span class="s0">#对模型进行编译</span>
<span class="s1">model.compile(optimizer = tf.train.AdamOptimizer</span><span class="s3">,</span>
	<span class="s1">loss = </span><span class="s4">'sparse_categorical_crossentropy'</span><span class="s3">,</span>
	<span class="s1">metrics = [</span><span class="s4">'accuracy'</span><span class="s1">]</span>
<span class="s1">)</span>
<span class="s0">#训练模型</span>
<span class="s1">model.fit(train_images</span><span class="s3">, </span><span class="s1">train_labels</span><span class="s3">, </span><span class="s1">epochs=</span><span class="s2">50</span><span class="s1">)</span>
</pre>
</body>
</html>