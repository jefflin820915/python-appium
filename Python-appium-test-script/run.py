import os, HtmlTestRunner

from script import GA_AutoTest

op = os.path.abspath('./result')
runner = HtmlTestRunner.HTMLTestRunner(
    output = op,
)
runner.run(GA_AutoTest.suite())
