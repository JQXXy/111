<html>
<head>
<title>see1.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6897bb;}
.s2 { color: #cc7832;}
.s3 { color: #808080;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
see1.py</font>
</center></td></tr></table>
<pre><span class="s0">num_rows = </span><span class="s1">5</span>
<span class="s0">num_cols = </span><span class="s1">3</span>
<span class="s0">num_images = num_rows*num_cols</span>
<span class="s0">plt.figure(figsize=(</span><span class="s1">2</span><span class="s0">*</span><span class="s1">2</span><span class="s0">*num_cols</span><span class="s2">, </span><span class="s1">2</span><span class="s0">*num_rows))</span>
<span class="s2">for </span><span class="s0">i </span><span class="s2">in </span><span class="s0">range(num_images):</span>
  <span class="s0">plt.subplot(num_rows</span><span class="s2">, </span><span class="s1">2</span><span class="s0">*num_cols</span><span class="s2">, </span><span class="s1">2</span><span class="s0">*i+</span><span class="s1">1</span><span class="s0">)</span>
  <span class="s3">#因为前15张都预测正确了，所以把i加了1000，展示第1000-1015的预测结果，</span>
  <span class="s0">plot_image(i+</span><span class="s1">1000</span><span class="s2">, </span><span class="s0">predictions</span><span class="s2">, </span><span class="s0">test_labels</span><span class="s2">, </span><span class="s0">test_images)</span>
  <span class="s0">plt.subplot(num_rows</span><span class="s2">, </span><span class="s1">2</span><span class="s0">*num_cols</span><span class="s2">, </span><span class="s1">2</span><span class="s0">*i+</span><span class="s1">2</span><span class="s0">)</span>
  <span class="s0">plot_value_array(i+</span><span class="s1">1000</span><span class="s2">, </span><span class="s0">predictions</span><span class="s2">, </span><span class="s0">test_labels)</span>

</pre>
</body>
</html>