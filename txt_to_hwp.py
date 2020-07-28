import os
import os.path, subprocess
from subprocess import STDOUT, PIPE

path = os.getcwd()

address = path + "/test_hwp/target/classes;C:/Users/qicqo/.m2/repository/kr/dogfoot/hwplib/1.0/hwplib-1.0.jar;C:/Users/qicqo/.m2/repository/org/apache/poi/poi/4.1.0/poi-4.1.0.jar;C:/Users/qicqo/.m2/repository/commons-codec/commons-codec/1.12/commons-codec-1.12.jar;C:/Users/qicqo/.m2/repository/org/apache/commons/commons-collections4/4.3/commons-collections4-4.3.jar;C:/Users/qicqo/.m2/repository/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar "


def compile_java(java_file):
    subprocess.check_call(['javac', "-classpath", "address", "-encoding", "UTF-8", java_file])
    # javac의 위치를 경로를 바꿔줘야될수있다. 윈도우 기준 이경로가 일반적


def execute_java(java_file):
    java_class, ext = os.path.splitext(java_file)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT)
    input = subprocess.Popen(cmd, stdin=PIPE)
    print(proc.stdout.read())


compile_java("test_hwp/src/test/Main.java")
# execute_java("test/Main")
