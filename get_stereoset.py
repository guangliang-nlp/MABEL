import glob
import os

import transformers

transformers.logging.set_verbosity_error()
ratios = [100, 500, 1000, 5000]  # ['0.0', '0.25', '0.5', '0.75', '1.0']
tasks = ['mnli', 'jigsaw-gender', 'snli']
models = ['bert-base-uncased']
methods = ['debiased']  # 'vanillia',
'''
if __name__ == "__main__":

    prefix = "/scratch0/liuguan5/models/cda/iclr24/"
    for model in models:
        for ratio in ratios:
            for task in tasks:

                for method in methods:

                    for i in [1,42,100]:
                        model_file = prefix + 'biasdis.' + str(
                            ratio) + "." + task + "." + model + "." + method + ".*.ckpt"

                        model_file = model_file.replace("*",str(i))
                        print(model_file)
                        os.system("python -m benchmark.intrinsic.stereoset.predict --model_name_or_path {0} --model {1} && python -m benchmark.intrinsic.stereoset.eval".format(model_file, model))

'''
if __name__ == "__main__":
    tasks = ['snli', 'sts', 'biasbios']
    models = ['bert-base-uncased']
    methods = ['debiased', 'normal', 'ours', 'ear']  # 'vanillia',
    prefix = "/scratch0/liuguan5/models/cda/iclr24/"

    for model_ in glob.glob(r'/scratch0/liuguan5/models/cda/iclr24/test*ours*bert-base-uncased*1*.ckpt'):
        print(model_)
        os.system(
            "python -m benchmark.intrinsic.stereoset.predict --model_name_or_path {0} --model {1} && python -m benchmark.intrinsic.stereoset.eval".format(
                model_,'bert-base-uncased'))
    for model_ in glob.glob(r'/scratch0/liuguan5/models/cda/iclr24/test*ours*bert-base-uncased*1*.ckpt'):
        print(model_)
        os.system(
            "python -m benchmark.intrinsic.stereoset.predict --model_name_or_path {0} --model {1} && python -m benchmark.intrinsic.stereoset.eval".format(
                model_,'bert-base-uncased'))
    for model_ in glob.glob(r'/scratch0/liuguan5/models/cda/iclr24/test*debiased*bert-base-uncased*.ckpt'):
        print(model_)
        os.system(
            "python -m benchmark.intrinsic.stereoset.predict --model_name_or_path {0} --model {1} && python -m benchmark.intrinsic.stereoset.eval".format(
                model_,'bert-base-uncased'))
