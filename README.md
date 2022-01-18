**| [Overview](#overview) | [Reproducibility](#reproducibility) | [License](#license) | [Contact](#contact) |**

# ITSProjects

This is a repository containing the projects for topics related to the ITS Course. In this case we encourage to review more details of the projects in the following corresponding `README` files:

* [Project 01 Connected Vehicles](Project01_ConnectV2X/README.md)
* [Project 02 Connected Vehicles](Project02_ConnectV2X/README.md)
* [Project 03 Vehicle Platooning](Project03_VehPlatoon/README.md)
* [Project 04 Vehicle Platooning](Project04_VehPlatoon/README.md)
* [Project 06 Sensitivity to Travel Time](Project06-Assignment_Hubsim/README.md)
* [Project 07 GLOSA](Project07-GLOSA/READMe.md)
* [Project 08 GLOSA]
* [Project 09 Variable Speed Limit](Projet09-VSL/README.md)
* [Project 10 Variable Speed Limit]

## Reproducibility

Download this repository

```{bash}
git clone https://github.com/research-licit/ITSProjects.git
```

Be sure to get [conda](https://www.anaconda.com/distribution/), then create the environment associate to your project:

* for Projects 1 to 4:

```{bash}
conda env create -f environment.yml
conda activate ITSTools
jupyter labextension install jupyterlab_bokeh
```

* for Projects 7 to 10:
```{bash}
conda env create -f environment_P07-10.yml
conda activate ITS_fromP07_toP10
```

* for Project 6, you just need to get connected on [HUBSIM platform](https://hubsim.neovya.fr/network), then you need to log in. No needs of Python.


## License

The code here contained is licensed under [MIT License](LICENSE)

## Contact 

If you run into problems or bugs, please let us know by [creating an issue](https://github.com/research-licit/ITSProjects/issues/new) an issue in this repository.
