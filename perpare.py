<html>
<head>
<title>perpare.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
.s3 { color: #808080;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
perpare.py</font>
</center></td></tr></table>
<pre><span class="s0">class_names = [</span><span class="s1">'T-shirt/top'</span><span class="s2">, </span><span class="s1">'Trouser'</span><span class="s2">, </span><span class="s1">'Pullover'</span><span class="s2">, </span><span class="s1">'Dress'</span><span class="s2">, </span><span class="s1">'Coat'</span><span class="s2">,</span>
               <span class="s1">'Sandal'</span><span class="s2">, </span><span class="s1">'Shirt'</span><span class="s2">, </span><span class="s1">'Sneaker'</span><span class="s2">, </span><span class="s1">'Bag'</span><span class="s2">, </span><span class="s1">'Ankle boot'</span><span class="s0">]</span>
<span class="s0">fashion_mnist = keras.datasets.fashion_mnist</span>
<span class="s0">(train_images</span><span class="s2">, </span><span class="s0">train_labels)</span><span class="s2">, </span><span class="s0">(test_images</span><span class="s2">, </span><span class="s0">test_labels) = fashion_mnist.load_data()</span>
<span class="s0">print(train_images.shape) </span><span class="s3">#(60000, 28, 28)</span>
<span class="s0">print(len(train_labels)) </span><span class="s3">#60000</span>
<span class="s3">#对数据进行预处理</span>
<span class="s0">train_images = train_images / </span><span class="s4">255.0</span>
<span class="s0">test_images = test_images / </span><span class="s4">255.0</span>
<span class="s3">#展示前25张图片</span>
<span class="s0">plt.figure(figsize=(</span><span class="s4">15</span><span class="s2">,</span><span class="s4">15</span><span class="s0">))</span>
<span class="s2">for </span><span class="s0">i </span><span class="s2">in </span><span class="s0">range(</span><span class="s4">25</span><span class="s0">):</span>
    <span class="s0">plt.subplot(</span><span class="s4">5</span><span class="s2">,</span><span class="s4">5</span><span class="s2">,</span><span class="s0">i+</span><span class="s4">1</span><span class="s0">)</span>
    <span class="s0">plt.xticks([])</span>
    <span class="s0">plt.yticks([])</span>
    <span class="s0">plt.grid(</span><span class="s2">False</span><span class="s0">)</span>
    <span class="s0">plt.imshow(train_images[i]</span><span class="s2">, </span><span class="s0">cmap=plt.cm.binary)</span>
    <span class="s0">plt.xlabel(class_names[train_labels[i]])</span>

</pre>
</body>
</html>