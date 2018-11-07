# !/usr/bin/env python3

import os
import numpy as np

class Vocabulary(object):
    def __init__(self, filename):
        '''
        :param filename: the file includes word & vector
        '''
        self._id_to_word = []
        self._word_to_id = {}
        self._bos = 1
        self._eos = 2
        self._unk = 3
        # self._strange_list = []
        vec_list = []
        vocab_size = None
        emb_dim = None
        idx = 4 # 1: bos, 2:eos, 3:unk
        vec_eos = None
        with open(filename, 'r', encoding='utf8') as f:
            for line1 in f.readlines():
                line = line1.strip()
                if line is None or line == '':
                    continue
                ss = line.split(' ')
                if len(ss) == 2:
                    vocab_size = int(ss[0])
                    emb_dim = int(ss[1])
                    continue
                if ss[0] == '</s>':
                    vec_eos = ss[1:]
                    continue
                if ss[0] == '<s>':
                    continue
                if len(ss) != 181:
                    # self._strange_list.append(line1[0])
                    continue
                self._word_to_id[ss[0]] = idx
                idx += 1
                vec_list.append(ss[1:])
        assert len(vec_list) == len(self._word_to_id.keys())
        emb_mat = np.array(vec_list)
        empty_vec = np.zeros((1, emb_dim))
        bos_vec = np.random.rand(1, emb_dim)
        eos_vec = np.expand_dims(np.array(vec_eos), axis=0)
        unk_vec = np.random.rand(1, emb_dim)
        self._emb_mat = np.concatenate([empty_vec, bos_vec, eos_vec, unk_vec, emb_mat], axis=0)
        self._word_to_id['<s>'] = 1
        self._word_to_id['</s>'] = 2
        self._word_to_id['unk'] = 3
        sorted_vocb = sorted(self._word_to_id.items(), key=lambda x:x[1], reverse=False)
        self._id_to_word.append('')
        for key, val in sorted_vocb:
            self._id_to_word.append(key)

    @property
    def bos(self):
        return self._bos

    @property
    def eos(self):
        return self._eos

    @property
    def unk(self):
        return self._unk

    @property
    def emb(self):
        return self._emb_mat

    @property
    def size(self):
        return len(self._id_to_word)

    def word_to_id(self, word):
        if word in self._word_to_id:
            return self._word_to_id[word]
        else:
            return self.unk

    def id_to_word(self, id):
        if id >= len(self._id_to_word):
            return 'unk'
        return self._id_to_word[id]

    def encode(self, sentence, reverse=False):
        sentence1 = sentence.split(' ')
        if sentence1[-1] == '':
            sentence1 = sentence1[:-1]
        word_ids = [self.word_to_id(word) for word in sentence1]
        if reverse:
            return np.array([self.eos] + word_ids + [self.bos], dtype=np.int32)
        else:
            return np.array([self.bos] + word_ids + [self.eos], dtype=np.int32)

    def decode(self, ids):
        pos = len(ids)
        for i, id in enumerate(ids):
            if id == 2:
                pos = i
                break
        ids1 = ids[:pos+1]
        return ' '.join([self.id_to_word(id) for id in ids1])

def test_Vocabulary():
    vocab_file = './v160k_big_string.txt'
    vocab = Vocabulary(vocab_file)
    tokens = [23, 45, 56, 22323, 25]
    print(vocab.decode(tokens))

if __name__ == '__main__':
    test_Vocabulary()
