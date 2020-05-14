import os, HtmlTestRunner   #OS模組,生成測試報告模組.
from script import sele

op = os.path.abspath('./result') # abspath('path') 返回給定路徑的絕對路徑
runner = HtmlTestRunner.HTMLTestRunner(
    output = op,
)
runner.run(sele.suit())