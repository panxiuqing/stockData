# 获取股票数据

由于 Matlab 上的 yahoo 对象获取的历史数据是未复权的，
并且暂时没找到如何从网络上直接获取复权后的股票历史数据，
所以先从 Sina 获取每年的分红数据再复权。

## 历史数据
直接使用 Matlab 自带的 yahoo 对象还存在一些问题，所以暂时使用一个Python脚本获取。