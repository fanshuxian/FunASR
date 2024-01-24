#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright FunASR (https://github.com/alibaba-damo-academy/FunASR). All Rights Reserved.
#  MIT License  (https://opensource.org/licenses/MIT)

from funasr import AutoModel

model = AutoModel(model="/Users/zhifu/Downloads/modelscope_models/speech_UniASR_asr_2pass-zh-cn-16k-common-vocab8358-tensorflow1-online", model_revision="v2.0.4",
                  # vad_model="damo/speech_fsmn_vad_zh-cn-16k-common-pytorch",
                  # vad_model_revision="v2.0.4",
                  # punc_model="damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
                  # punc_model_revision="v2.0.4",
                  )

res = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav")
print(res)


''' can not use currently
from funasr import AutoFrontend

frontend = AutoFrontend(model="damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch", model_revision="v2.0.4")

fbanks = frontend(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav", batch_size=2)

for batch_idx, fbank_dict in enumerate(fbanks):
    res = model.generate(**fbank_dict)
    print(res)
'''