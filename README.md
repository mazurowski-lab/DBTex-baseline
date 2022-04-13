# DBTex-baseline
This is an implementation of a basic Faster R-CNN model for breast tumor detection on the ultra-high resolution Duke BCS-DBT (Breast Cancer Screening - Digital Breast Tomosynthesis) dataset, to be used as a "baseline" model for the [DBTex breast lesion detection challenge](https://www.aapm.org/GrandChallenge/DBTex2/) and [benchmark](https://spie-aapm-nci-dair.westus2.cloudapp.azure.com/competitions/9).

We provide notebooks from pre-processing and dataset preparation to training and testing stages. We offer two version of the Faster-RCNN implemenation.

## Installation
We build our implemenation mainly based on MMDection. The installation of MMDetection can be found [here](https://github.com/open-mmlab/mmdetection).

## Preparing Data
The raw (DICOM) image data and annotation/label tables can be downloaded from [the BCS-DBT page on The Cancer Imaging Archive](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=64685580). After downloading the tables, put them in ``./data+_csv``.

We supply the notebook ``preprocess.ipynb`` to do data preprocessing, which can transfer the raw dicom images into png image slices and create the corresponding json files.

## Model Training
For model training, use the notebook ``train&evaluate.ipynb``.

## Model Evaluation
Trained models are saved in ``/work_dirs/breast``. If you want to evaluate our pretrained checkpoints, you can set the ``cfg.work_dirs`` to the pretrained model.

## Model Testing
For testing, we offer the notebook ``generate_test_table.ipynb`` to create predictions formatted according to the DBTex guidelines.
