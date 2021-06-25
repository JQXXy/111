<html>
<head>
<title>see.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #808080;}
.s2 { color: #cc7832;}
.s3 { color: #6a8759;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
see.py</font>
</center></td></tr></table>
<pre>
<span class="s1">#对图片进行展示，xlabel表示预测的值，如果预测的正确，则为蓝色，否则为红色，数字表示预测标签的百分比，可以理解为置信度</span>
<span class="s2">def </span><span class="s0">plot_image(i</span><span class="s2">, </span><span class="s0">predictions_array</span><span class="s2">, </span><span class="s0">true_label</span><span class="s2">, </span><span class="s0">img):</span>
  <span class="s0">predictions_array</span><span class="s2">, </span><span class="s0">true_label</span><span class="s2">, </span><span class="s0">img = predictions_array[i]</span><span class="s2">, </span><span class="s0">true_label[i]</span><span class="s2">, </span><span class="s0">img[i]</span>
  <span class="s0">plt.grid(</span><span class="s2">False</span><span class="s0">)</span>
  <span class="s0">plt.xticks([])</span>
  <span class="s0">plt.yticks([])</span>
  <span class="s0">plt.imshow(img</span><span class="s2">, </span><span class="s0">cmap=plt.cm.binary)</span>
  <span class="s0">predicted_label = np.argmax(predictions_array)</span>
  <span class="s2">if </span><span class="s0">predicted_label == true_label:</span>
    <span class="s0">color = </span><span class="s3">'blue'</span>
  <span class="s2">else</span><span class="s0">:</span>
    <span class="s0">color = </span><span class="s3">'red'</span>

  <span class="s0">plt.xlabel(</span><span class="s3">&quot;{} {:2.0f}% ({})&quot;</span><span class="s0">.format(class_names[predicted_label]</span><span class="s2">,</span>
                                <span class="s4">100</span><span class="s0">*np.max(predictions_array)</span><span class="s2">,</span>
                                <span class="s0">class_names[true_label])</span><span class="s2">,</span>
                                <span class="s0">color=color)</span>
<span class="s1">#对预测的概率分布绘制条形图，蓝色代表预测正确，红色代表预测错误</span>
<span class="s2">def </span><span class="s0">plot_value_array(i</span><span class="s2">, </span><span class="s0">predictions_array</span><span class="s2">, </span><span class="s0">true_label):</span>
  <span class="s0">predictions_array</span><span class="s2">, </span><span class="s0">true_label = predictions_array[i]</span><span class="s2">, </span><span class="s0">true_label[i]</span>
  <span class="s0">plt.grid(</span><span class="s2">False</span><span class="s0">)</span>
  <span class="s0">plt.xticks([])</span>
  <span class="s0">plt.yticks([])</span>
  <span class="s0">thisplot = plt.bar(range(</span><span class="s4">10</span><span class="s0">)</span><span class="s2">, </span><span class="s0">predictions_array</span><span class="s2">, </span><span class="s0">color=</span><span class="s3">&quot;#777777&quot;</span><span class="s0">)</span>
  <span class="s0">plt.ylim([</span><span class="s4">0</span><span class="s2">, </span><span class="s4">1</span><span class="s0">])</span>
  <span class="s0">predicted_label = np.argmax(predictions_array)</span>

  <span class="s0">thisplot[predicted_label].set_color(</span><span class="s3">'red'</span><span class="s0">)</span>
  <span class="s0">thisplot[true_label].set_color(</span><span class="s3">'blue'</span><span class="s0">)</span>

</pre>
</body>
</html>