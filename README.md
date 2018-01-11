personal_tax
============

Personal income tax computation in China

中国的个人所得税计算。根据该[计算规则](http://finance.21cn.com/news/cjyw/2011/07/01/8505773.shtml)。如需核实结果，可以跟这个[网上计算器](http://finance.21cn.com/bank/computer/tax.html)核对.

如何使用示例，在项目目录下进入ipython操作，如下：

    In [1]: from tax import *

    In [2]: personal_tax(8000)
    Out[2]: 7655.0

    In [3]: personal_tax(18000)
    Out[3]: 15380.0

    In [4]: personal_tax(28000)
    Out[4]: 22880.0

    In [5]: personal_tax(38000)
    Out[5]: 30380.0

    In [6]: personal_tax(48000)
    Out[6]: 37405.0


