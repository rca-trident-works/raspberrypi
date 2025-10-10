# coding: utf-8

# subprocessライブラリのインポート
import subprocess

print("PythonプログラムでLinuxコマンドの実行")

print("■ pwdコマンドの実行結果: ")
cmd = "pwd"
result = subprocess.call(cmd.split())
print(result)

print("■ ls コマンドの実行結果: ")
cmd = "ls -l"
result = subprocess.call(cmd.split())
print(result)
