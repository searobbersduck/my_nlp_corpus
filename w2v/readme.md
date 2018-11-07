# 文件说明
1. ***`w2v/big_160k_spm.model`***
    * sentencepiece生成的160k大小的词表模型
    * 利用`spm_encode --model=./big_160k_spm.model --output_format=piece < ./file_0_0.txt > ./file_0_0_seg.txt`, 对文本进行分词
    
2. ***`w2v/v160k_big_string.txt`***
    * 160k词表文件
    * 可以通过***`w2v/vocab.py`***中的**`Vocabulary类`**进行加载
    
3. ***`w2v/gen_pieces.py`***
    * 生成利用sentenpiece做txt文本分割的脚本
    * 调用`python generate_seg_script infilepattern w2v/big_160k_spm.model outfile_dir outscrip`