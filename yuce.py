<html>
<head>
<title>yuce.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #808080;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
yuce.py</font>
</center></td></tr></table>
<pre><span class="s0">#批量预测</span>
<span class="s1">predictions = model.predict(test_images)</span>
<span class="s1">print(predictions.shape)</span><span class="s0">#输出（10000， 10）</span>
<span class="s1">print(np.argmax(predictions[</span><span class="s2">0</span><span class="s1">]))</span><span class="s0">#9，说明第一张图片的预测结果为类别9</span>
<span class="s1">print(predictions[</span><span class="s2">0</span><span class="s1">])</span><span class="s0">#[1.5336354e-13 1.5920932e-17 1.3684552e-17 5.4927953e-18 2.0991999e-13 4.8152828e-07 4.4211198e-13 2.3735786e-06 9.4550773e-16 9.9999714e-01]，可以看出predictions[0][9]最大</span>
</pre>
</body>
</html>