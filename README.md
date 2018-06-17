# niu ke wang code of 2017
![rebuildlist](https://github.com/frank-xman/leetcode-python/blob/master/reBulidList.py)  

	题目描述
		牛牛的作业薄上有一个长度为 n 的排列 A，
		这个排列包含了从1到n的n个数，但是因为一些原因，
		其中有一些位置（不超过 10 个）看不清了，
		但是牛牛记得这个数列顺序对的数量是 k，
		顺序对是指满足 i < j 且 A[i] < A[j] 的对数，请帮助牛牛计算出，
		符合这个要求的合法排列的数目。
		输入描述:
		  每个输入包含一个测试用例。
		  每个测试用例的第一行包含两个整数 n 和 k（1 <= n <= 100, 0 <= k <= 1000000000），
		  接下来的 1 行，包含 n 个数字表示排列 A，
		  其中等于0的项表示看不清的位置（不超过 10 个）。
		输出描述:
	      输出一行表示合法的排列数目。
![miscolor]

	题目描述
	你就是一个画家！
	你现在想绘制一幅画，
	但是你现在没有足够颜色的颜料。
	为了让问题简单，我们用正整数表示不同颜色的颜料。
	你知道这幅画需要的n种颜色的颜料，你现在可以去商店购买一些颜料，
	但是商店不能保证能供应所有颜色的颜料，所以你需要自己混合一些颜料。
	混合两种不一样的颜色A和颜色B颜料可以产生(A XOR B)
	这种颜色的颜料(新产生的颜料也可以用作继续混合产生新的颜色,XOR表示异或操作)。
	本着勤俭节约的精神，你想购买更少的颜料就满足要求，
	所以兼职程序员的你需要编程来计算出最少需要购买几种颜色的颜料？
	输入描述:

	第一行为绘制这幅画需要的颜色种数n (1 ≤ n ≤ 50)
	第二行为n个数xi(1 ≤ xi ≤ 1,000,000,000)，表示需要的各种颜料.

	输出描述:

	输出最少需要在商店购买的颜料颜色种数，注意可能购买的颜色不一定会使用在画中，只是为了产生新的颜色。
