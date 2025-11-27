import subprocess
import sys
from pathlib import Path


def open_exe():
    # 确定当前目录
    if getattr(sys, 'frozen', False):
        current_dir = Path(sys.executable).parent.absolute()
    else:
        current_dir = Path(__file__).parent.absolute()

    # 目标exe路径
    exe_path = current_dir / "dist" / "Noki_HBR_Auto.exe"

    try:
        # 检查文件是否存在
        if exe_path.exists():
            # 启动exe程序
            subprocess.Popen([str(exe_path)])
            print(f"成功启动: {exe_path}")
        else:
            print(f"文件不存在: {exe_path}")
    except Exception as e:
        print(f"启动失败: {e}")


# 调用函数
open_exe()