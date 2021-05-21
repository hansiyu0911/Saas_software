import unittest
import time
from config.HTMLTextRunner import HTMLTestRunner

case_path=r"../test_case"
# report_path=r"../report"
discover=unittest.defaultTestLoader.discover(case_path,pattern="test_resouce.py")

if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    # report_name=report_path+f'{now}.html'
    # print(report_name)
    with open(rf'../report/{now}.html','wb') as f:
        runner=HTMLTestRunner(
            stream=f,
            title="测试报告",
            description="测试报告如下",
            tester="韩思雨",
            # 结果的详细程度
            verbosity=2
        )
        runner.run(discover)