import os

import transformers

transformers.logging.set_verbosity_error()
ratios = ['0.0', '0.25', '0.5', '0.75', '1.0']
tasks = ['mnli', 'jigsaw-gender', 'snli']
models = ['roberta-base','bert-base-uncased']
methods = ['vanillia', 'debiased']

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
                        os.system("python -m benchmark.intrinsic.crows.eval --model_name_or_path {0} --model {1}".format(model_file, model))
