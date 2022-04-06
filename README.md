# DBT-DCS-baseline
This is a baseline implementation of tumor detection on DBT-DCS dataset.

We provide notebooks from pre-processing and dataset preparation to training and testing stages. We offered two version of Faster-RCNN implemenation.

## Installation
We build our implemenation mainlt based on MMDection. The installation of MMDetection can be found from the official github(https://github.com/open-mmlab/mmdetection).

## Preparing data
The raw dicom images and tables can be downloaded from [DCS-DBT](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=64685580). After downloading the tables, put them in ./data+_csv.

We offer the notebook **preprocess.ipynb** to do data preprocssing, which could transfer the raw dicom images into png image slices and create the corresponding json files.

## training model
For training, we offer the notebook **train&evaluate.ipynb**.

## testing model
For testing, we offer the notebook **generate_test_table.ipynb** to reproduce the testing result dable described in xxx competation paper.

