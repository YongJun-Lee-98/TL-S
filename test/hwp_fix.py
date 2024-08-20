import zipfile
import os

# 파일 경로
file_path = '/Users/passionit/Downloads/빈 문서 1.hwpx'
output_dir = '/Users/passionit/Downloads/hwpx_content/'

# HWPX 파일 압축 해제
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# XML 파일 수정 (예: Contents.xml)
content_file = os.path.join(output_dir, 'Contents.xml')

with open(content_file, 'r', encoding='utf-8') as file:
    content = file.read()

# 예시로, 특정 태그에 텍스트 추가
content = content.replace('<Paragraph>', '<Paragraph>새로운 텍스트 추가 ')

# 수정된 내용을 다시 파일에 저장
with open(content_file, 'w', encoding='utf-8') as file:
    file.write(content)

# 수정된 파일 다시 압축
with zipfile.ZipFile(file_path, 'w') as zip_ref:
    for folder_name, subfolders, filenames in os.walk(output_dir):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            zip_ref.write(file_path, os.path.relpath(file_path, output_dir))
