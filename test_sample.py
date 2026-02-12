# src/chapter-1/test_tmpdir.py
def test_needsfiles(tmpdir):  # 1. 形参写tmpdir = 向pytest“申请”临时目录资源
    print(tmpdir)              # 2. 打印临时目录的路径，看看pytest创建了啥
    assert 1                   # 3. 强制让测试失败（只为了能看到print的输出）
