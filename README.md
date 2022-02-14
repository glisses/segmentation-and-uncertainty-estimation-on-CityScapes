# segmentation and uncertainty estimation on CityScapes

<div align="center"><p>
    <a href="https://github.com/glisses/segmentation-and-uncertainty-estimation-on-CityScapes/pulse">
      <img src="https://img.shields.io/github/last-commit/glisses/segmentation-and-uncertainty-estimation-on-CityScapes?color=%4dc71f&label=Last%20Commit&logo=github&style=flat-square"/>
    </a>
    <a href="https://github.com/glisses/segmentation-and-uncertainty-estimation-on-CityScapes/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/glisses/segmentation-and-uncertainty-estimation-on-CityScapes?label=License&logo=GNU&style=flat-square"/>
</p>
</div>



Implement **SegNet** for semantic segmentation with **Pytorch**, and also generate estimates of **aleatoric and epistemic uncertainties** associated with the segmentation. 
For more information on the dataset please refer to: [CityScapes dataset](https://www.cityscapes-dataset.com/). 
          
This is also a team project for Deep Learning for Computer Vision course, lectured by Prof. Alexander Amini.

​                         

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Segmentation Results](#Segmentation Results)
- [Contributing](#contributing)
- [License](#license)

​                         

## Install

```
git clone git@github.com:glisses/segmentation-and-uncertainty-estimation-on-CityScapes.git
```

​                   

## Usage

### 1. Requirements

``` shell 
pip install -r requirements.txt   
```

  

### 2. Pre-train Weights

Downloaded `vgg16_bn-6c64b313.pth` from https://download.pytorch.org/models/vgg16_bn-6c64b313.pth and put it in the same folder as `main_segnet_v7.ipynb`.



### 3. Training and Testing

Ignore the  first 3 cells in `main_segnet_v7.ipynb` if you're not using Google Colab.



## Segmentation Results

![c54843643a80e9cfd0dcc06b2c03a4b.png](https://s2.loli.net/2022/02/15/HjLGsFt6iZkKxz8.png)



## Contributing



## License

[MIT License](../LICENSE)
