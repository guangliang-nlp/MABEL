import glob
import os

import transformers

transformers.logging.set_verbosity_error()
'''
ratios = [100, 500, 1000, 5000]  # ['0.0', '0.25', '0.5', '0.75', '1.0']
tasks = ['mnli', 'jigsaw-gender', 'snli']
models = ['bert-base-uncased']
methods = ['debiased']  # 'vanillia',
'''

tasks = ['snli', 'sts', 'biasbios']
models = ['bert-base-uncased']
methods = ['debiased', 'normal', 'ours']
prefix = "/scratch0/liuguan5/models/cda/iclr24/"
for method in methods:
    for task in tasks:
        for model in models:
            for seed in [1, 42, 100]:
                model_file = prefix + "test." + task + "." + method + "." + model + ".{}"
                model_file = model_file.replace("{}", str(seed))
                if method == 'ours':
                    model_file = model_file + ".0.01"
                model_file = model_file + ".ckpt"

                os.system(
                    "python -m benchmark.intrinsic.stereoset.predict --model_name_or_path {} --model {} && python -m benchmark.intrinsic.stereoset.eval".format(
                        model_file, model))
