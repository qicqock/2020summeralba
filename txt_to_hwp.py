import os
import subprocess
from os import chdir
from os.path import exists

modified_osgetcwd = os.getcwd().replace("\\", "/")
java_src_dir = "test_hwp"
jar_src_dir = "test_hwp/out/artifacts/test_jar/test.jar"

address = "C:/Users/qicqo/Desktop/2020summer/test_hwp/target/classes;C:/Users/qicqo/.m2/repository/kr/dogfoot/hwplib/1.0/hwplib-1.0.jar;C:/Users/qicqo/.m2/repository/org/apache/poi/poi/4.1.0/poi-4.1.0.jar;C:/Users/qicqo/.m2/repository/commons-codec/commons-codec/1.12/commons-codec-1.12.jar;C:/Users/qicqo/.m2/repository/org/apache/commons/commons-collections4/4.3/commons-collections4-4.3.jar;C:/Users/qicqo/.m2/repository/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar",
# java 파일을 컴파일하고 실행하기 위해 필요한 라이브러리들의 주소
# 컴파일이나 실행할때 이주소를 classpath 옵션으로 지정해주어야 정상적으로 작동한다.
# 실행환경이 바뀌었을때 이 주소도 바꿔줘야함


def compile_java(java_file):
    subprocess.check_call(['javac', "-classpath", address, "-encoding", "UTF-8", java_file])


def execute_java(java_file):
    subprocess.check_call(['java', "-classpath", address, "-Dfile.encoding=UTF-8", java_file])
    # 컴파일 할경우에는 상관없지만 실행할때는 패키지와 같은 위치에서 실행을 해야한다.
    # java_class, ext = os.path.splitext(java_file)
    # cmd = ['java', java_class]
    # proc = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT)
    # input = subprocess.Popen(cmd, stdin=PIPE)
    # print(proc.stdout.read())


def execute_jar(java_file):
    print("Enter the source file name")
    source_name = input()

    try:
        f = open(source_name, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print("Cannot find the file")
        return

    print("Enter the name of the result file")
    result_name = input()

    subprocess.check_call(['java', "-jar", "-Dfile.encoding=UTF-8", java_file, source_name, result_name])


def move_dir():
    if exists(java_src_dir):
        chdir(java_src_dir)

move_dir()
print(modified_osgetcwd)
execute_jar(modified_osgetcwd + "/" + jar_src_dir)

# compile_java("test/Main.java")
# execute_java("test/Main")
