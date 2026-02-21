import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

path_env = os.environ.get('PATH', '')
path_parts = path_env.split(os.pathsep)[:3]
print(f"환경 변수 PATH 일부: {os.pathsep.join(path_parts)}")

file_path = "/Users/username/documents/report.txt"

directory, filename = os.path.split(file_path)
name_only, extension = os.path.splitext(filename)

print("\n파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

is_exists = os.path.exists(file_path)
print(f"파일 존재 여부: {is_exists}")