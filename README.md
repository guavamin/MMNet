# MMNet
MMNet is a massive MIMO signal detection scheme based on light online learning with neural networks that extends to correlated channel scenarios. 

## Introduction
I forked this repository from mehrdadkhani/MMNet.

There are some mistakes in the code and I made some alterations to these mistakes.

This framework runs on tensorflow version 1; hence I use `import tensorflow.compat.v1 as tf` and `tf.disable_v2_behavior()` to make it run on tf.version 1.  

I provide the supplement to the missing part "normalization" of the code.

The code of "normalizaion" is put in the "channel" directory and the related details is written in README in that directory.
