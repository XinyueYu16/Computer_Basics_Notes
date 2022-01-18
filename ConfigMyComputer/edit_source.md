# 解决国内Linux下载过慢的问题

- 按照[之前的方法](../README.md) 修改了镜像源以后下载非常缓慢，开启我走上Linux之路的同事跟我说原因可能在于，Linux apt-get更新的是系统源，但我在实际下载时使用的是用户源。

- 具体的检查/下载方法如下：

  > pip install -i https://mirrors.aliyun.com/pypi/simple/ pandas

  如果这么做能大大提高下载速度，说明源更新的位置不对，留个坑等日后排查~

- 另外我的curl也非常慢，说不定也是同一个问题？