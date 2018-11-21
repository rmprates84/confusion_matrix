# This code compute ROC curve and ROC area for each class
# Copyright 2018 - Ricardo Prates

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from scipy import interp

def roc_curve(CLASSES,Y=[],Y_PRED=[]):
    # Compute ROC curve and ROC area for each class
    lw = 2
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(CLASSES):
        fpr[i], tpr[i], _ = roc_curve(Y[:, i], Y_PRED[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(Y.ravel(), Y_PRED.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(CLASSES)]))

    mean_tpr = np.zeros_like(all_fpr)
    for i in range(CLASSES):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])

    # Finally average it and compute AUC
    mean_tpr /= CLASSES

    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    plt.figure()

    colors = cycle(['aqua', 'darkorange', 'cornflowerblue','red','darkgray'])
    for i, color in zip(range(CLASSES), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                label='ROC curve of class {0} (area = {1:0.2f})'
                ''.format(i, roc_auc[i]))

    plt.plot([0, 1], [0, 1], 'k--', lw=lw)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Some extension of Receiver operating characteristic to multi-class')
    plt.legend(loc="lower right")
    plt.show()