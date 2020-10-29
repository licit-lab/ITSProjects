**| [Overview](#overview) | [Reproducibility](#reproducibility) | [License](#license) | [Contact](#contact) |**

# Connected Vehicles 

### Project 01

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/research-licit/ITSProjects/main?filepath=Project01_ConnectV2X%2FProject01.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/research-licit/ITSProjects/blob/main/Project01_ConnectV2X/Project01.ipynb)

## Overview

Project on connected vehicles

### Base functions 

All functionalities are implemented in the following package [connectv2x](https://github.com/research-licit/connectv2x)

## Reproducibility

Download this repository

```{bash}
git clone https://github.com/research-licit/ITSProjects.git
```

Be sure to get [conda](https://www.anaconda.com/distribution/), then:

```{bash}
mkdir 01_v2x
conda env create -f=environment.yaml -p 01_v2x
conda activate path/to/folder/01_v2x
jupyter labextension install jupyterlab_bokeh
```

## License

The code here contained is licensed under [MIT License](LICENSE)

## Contact 

If you run into problems or bugs, please let us know by [creating an issue](https://github.com/research-licit/ITSProjects/issues/new) an issue in this repository.
