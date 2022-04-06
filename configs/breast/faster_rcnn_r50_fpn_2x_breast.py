_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_2x.py', '../_base_/default_runtime.py'
]

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('cancer',)
data = dict(
    train=dict(
        img_prefix='data/detectron2/breast/',
        classes=classes,
        ann_file='data/detectron2/breast/images/train/annotation_coco.json'),
    val=dict(
        img_prefix='data/detectron2/breast/',
        classes=classes,
        ann_file='data/detectron2/breast/images/val/annotation_coco.json'),
    test=dict(
        img_prefix='data/detectron2/breast/',
        classes=classes,
        ann_file='data/detectron2/breast/images/val/annotation_coco.json'))