#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright FunASR (https://github.com/alibaba-damo-academy/FunASR). All Rights Reserved.
#  MIT License  (https://opensource.org/licenses/MIT)

from funasr import AutoModel

model = AutoModel(model="../modelscope_models/emotion2vec_base")

res = model(input="../modelscope_models/emotion2vec_base/example/test.wav", output_dir="./outputs")
print(res)