# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pylab as plt

#-------------------
# 1. �f�[�^�̓ǂݍ���
data = pd.read_csv('../data/house-prices-advanced-regression-techniques/train.csv')
#-------------------

#-------------------
# 2. �v���b�g 

# figure�̏�����
fig = plt.figure()

ax=fig.add_subplot(1,1,1)  #�O���t�̈ʒu�w��

# MSSubClass=30�̎���LotArea��SalePrice�̎U�z�}
ax.plot(data[data['MSSubClass']==30]['GrLivArea'],data[data['MSSubClass']==30]['SalePrice'],'.',label="1-Story 1945 & Older")

# MSSubClass=60�̎���LotArea��SalePrice�̎U�z�}
ax.plot(data[data['MSSubClass']==60]['GrLivArea'],data[data['MSSubClass']==60]['SalePrice'],'.',label="2-Story 1946 & Newer")

ax.set_xlabel('GrLivArea')  # x���̃��x��
ax.set_ylabel('SalePrice')  # y���̃��x��
ax.legend()  # �}��

fig.tight_layout()  # �O���t�ԂɌ��Ԃ�������
plt.show()  # �O���t�̕\��
#-------------------