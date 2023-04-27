import streamlit as st
import pandas as pd
import numpy as np
import time
import argparse

import pandas as pd

import transformers
import torch
import torchmetrics
import pytorch_lightning as pl

from models.baseline import Model
from dataloader import Dataloader
from arguments import get_args



st.title("규빈이의 문장 유사도 평가")
st.header("Gyubin's NLP STS Task")
st.subheader("pre-trained snunlp/electra-discriminator model base")

st.write("Sentence A와 Sentence B를 입력 후 제출을 누르면 두 문장간 유사도를 판별해드립니다")

st.write("모델은 사전 학습된 KR/Electra 구조 Language model의 discriminator를 활용해 실생활 데이터로 Fine-tuning 되었습니다")

result = []
count = 0

with st.form(key="입력 form"):
    sentenceA = st.text_input("Sentence A")
    sentenceB = st.text_input("Sentence B")
    st.form_submit_button("submit")
    testes = pd.DataFrame({'id': 1111, 'source': 'petition-sampled', 'sentence_1': sentenceA, 'sentence_2': sentenceB}, index = ['row'])
    count = 1

while count == 0:
    pass



with st.spinner("제출 후 기다려주세요!!"):
    args = get_args()
    # print(get_args())
    # dataloader와 model을 생성합니다.
    dataloader = Dataloader(args.model_name, args.batch_size, args.shuffle, args.train_path, args.dev_path,
                            args.test_path, args.predict_path)
    dataloader.predict_data = testes
    # gpu가 없으면 accelerator='cpu', 있으면 accelerator='gpu'
    trainer = pl.Trainer(accelerator='gpu', max_epochs=args.max_epoch, log_every_n_steps=1)

    # Inference part
    # 저장된 모델로 예측을 진행합니다.
    model = torch.load('model.pt')
    predictions = trainer.predict(model=model, datamodule=dataloader)
    predictions = round(float(predictions[0]),1)
    
    # 예측된 결과를 형식에 맞게 반올림하여 준비합니다.
    #predictions = list( round(float(i), 1) for i in torch.cat(predictions))
    #for i in range(len(predictions)):
    if predictions < 0:
        predictions = 0
    elif predictions > 5:
        predictions = 5

    if count > 0:
        time.sleep(2)
        text = f'두 문장 간 유사도는 {predictions * 20}% 입니다. 스껄'
        st.write(text)
        




st.balloons()


