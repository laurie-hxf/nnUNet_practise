import os
import shutil
from batchgenerators.utilities.file_and_folder_operations import maybe_mkdir_p, save_json

def organize_dataset(input_dir, output_dir, is_label=False):
    for case in os.listdir(input_dir):
        case_dir = os.path.join(input_dir, case)
        if os.path.isdir(case_dir):
            image_file = os.path.join(case_dir, 'image.png')
            label_file = os.path.join(case_dir, 'label.png') if is_label else None

            # Copy image to output directory
            if label_file is None:
                shutil.copy(image_file, os.path.join(output_dir, f'{case}_0000.png'))

            if is_label:
                # Copy label to output directory
                shutil.copy(label_file, os.path.join(output_dir, f'{case}.png'))

def main():
    base_dir = '/Users/laurie/Documents/nnunet_train/data/avrdb/crop_train'
    test_dir = '/Users/laurie/Documents/nnunet_train/data/avrdb/crop_test'
    nnunet_raw_dir = '/Users/laurie/Documents/nnunet_train/nnUNet/nnUNet_raw/Dataset001_avrdb'
    imagesTr_dir = os.path.join(nnunet_raw_dir, 'imagesTr')
    labelsTr_dir = os.path.join(nnunet_raw_dir, 'labelsTr')
    imagesTs_dir = os.path.join(nnunet_raw_dir, 'imagesTs')

    maybe_mkdir_p(imagesTr_dir)
    maybe_mkdir_p(labelsTr_dir)
    maybe_mkdir_p(imagesTs_dir)

    organize_dataset(base_dir, imagesTr_dir)
    organize_dataset(base_dir, labelsTr_dir, is_label=True)
    organize_dataset(test_dir, imagesTs_dir)

    # # Create dataset.json
    # dataset_json = {
    #     "name": "YourDataset",
    #     "description": "Description of your dataset",
    #     "tensorImageSize": "3D",
    #     "reference": "",
    #     "licence": "",
    #     "release": "0.0",
    #     "modality": {
    #         "0": "RGB"
    #     },
    #     "labels": {
    #         "0": "background",
    #         "1": "object"
    #     },
    #     "numTraining": len(os.listdir(base_dir)),
    #     "numTest": 0,
    #     "training": [{"image": f"./imagesTr/{case}_0000.png", "label": f"./labelsTr/{case}.png"} for case in os.listdir(base_dir)],
    #     "test": []
    # }
    # save_json(dataset_json, os.path.join(nnunet_raw_dir, 'dataset.json'))

if __name__ == '__main__':
    main()