# 添加当前路径至解释器，确保单元测试时可正常import其它文件
import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# 基于顶层包的import
from prototype.system_interface_local import SystemInterfaceLocal
from prototype.task.cifar10_tagging import CIFAR10Task

if __name__ == "__main__":

    def server(instruction, conn, addr):
        if instruction == "event/TASK_END":
            print("event/TASK_END")

    submitter_num = 5
    randomizer_num = 5
    subtask_num = 10
    re_enc_num = 2
    
    task = CIFAR10Task("CIFAR10 tagging", subtask_num)
    system = SystemInterfaceLocal(
        task, server, submitter_num, randomizer_num, subtask_num, re_enc_num
    )
    system.run()

    for id in range(submitter_num):
        system.call_submitter(id, "start", False)
