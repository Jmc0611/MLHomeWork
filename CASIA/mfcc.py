# %matplotlib inline

import librosa
import matplotlib.pyplot as plt
import numpy as np

path = r'C:\Users\14403\Desktop\FedSTAR2\speech_commands\liuchanhg\angry\201.wav'

y, sr = librosa.load(path, sr=None)


def normalizeVoiceLen(y, normalizedLen):
    nframes = len(y)
    y = np.reshape(y, [nframes, 1]).T
    # 归一化音频长度为2s,32000数据点
    if (nframes < normalizedLen):
        res = normalizedLen - nframes
        res_data = np.zeros([1, res], dtype=np.float32)
        y = np.reshape(y, [nframes, 1]).T
        y = np.c_[y, res_data]
    else:
        y = y[:, 0:normalizedLen]
    return y[0]


def getNearestLen(framelength, sr):
    framesize = framelength * sr
    # 找到与当前framesize最接近的2的正整数次方
    nfftdict = {}
    lists = [32, 64, 128, 256, 512, 1024]
    for i in lists:
        nfftdict[i] = abs(framesize - i)
    sortlist = sorted(nfftdict.items(), key=lambda x: x[1])  # 按与当前framesize差值升序排列
    framesize = int(sortlist[0][0])  # 取最接近当前framesize的那个2的正整数次方值为新的framesize
    return framesize


VOICE_LEN = 32000
# 获得N_FFT的长度
N_FFT = getNearestLen(0.25, sr)
# 统一声音范围为前两秒
y = normalizeVoiceLen(y, VOICE_LEN)
print(y.shape)
# 提取mfcc特征
mfcc_data = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=N_FFT, hop_length=int(N_FFT / 4))

# 画出特征图，将MFCC可视化。转置矩阵，使得时域是水平的
plt.matshow(mfcc_data)
plt.title('MFCC')
plt.show()