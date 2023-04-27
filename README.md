# AI model 배포 example

# 제작 목적

실제 제작한 AI 모델을 Server와 연동하여 로컬환경이 아닌 외부 경로를 통해서도 접속가능한 사이트 생성

# 제작 환경

코드 편집기: VS Code

쉘: bash

언어: Python

Server GPU: V100

Pre-trained model: hugging face [snunlp/KR-ELECTRA-discriminator](https://huggingface.co/snunlp/KR-ELECTRA-discriminator) model

Fine-tuning data: 문장 유사도 평가 데이터(대회 제공, private)

주요 라이브러리: steamlit

# 코드 설명

[한국어 STS 대회](https://github.com/gyubinc/level1_semantictextsimilarity-nlp-04.git)에서 만든 AI 모델의 구현을 실제 서버와 연동하는 코드

서버는 SSH로 연동 후 제작 (서버가 없다면 로컬에서만 실행 가능)

# 실제 작동 화면

![steamlit_page](https://user-images.githubusercontent.com/122433920/234831695-d4150df3-ffdd-4329-acf2-a85240fd25d6.png)

# 결과물 예시

![steamlit](https://user-images.githubusercontent.com/122433920/234831238-3f5eb95d-9bce-4950-9ef2-bdef8468ea8d.png)
