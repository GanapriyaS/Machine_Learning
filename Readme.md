For Windows :

## [1. Installing Miniconda3](https://docs.conda.io/en/latest/miniconda.html)

<div style="display:flex">
<img src="./images/windows/install_miniconda.png" style="width:33%; margin-right:7px;"/>

<img src="./images/windows/bash_install.png" style="width:33%; margin-right:7px;"/>


<img src="./images/windows/cmd_install.png" style="width:33%"/>
</div>
<br>

```
start Miniconda3-py39_4.11.0-Windows-x86_64.exe -Wait -ArgumentList @('/S', '/InstallationType=AllUsers', '/RegisterPython=1', "/D=E:\Miniconda3")
```
<br>

## 2. Managing Environment
<img src="images/windows/conda-env.png" />

To create an environment
```
conda create --prefix ./env pandas numpy other_libraries
```
To activate this envrionment
```
conda activate ./env
```
If any error in activating env , use conda init bashname
```
conda init bashname
```
<div style="display:flex">
<img src="./images/windows/conda_init.png" style="width:50%; margin-right:7px"/>

<img src="./images/windows/conda_activate.png" style="width:50%"/>
</div><br>

To deactivate 
```
conda deactivate
```
---

<br>
For linux :
<br>

## [1. Installing Miniconda3](https://docs.conda.io/en/latest/miniconda.html)


<div style="display:flex">
<img src="./images/ubuntu/bash-install.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/cmd-install.png" style="width:50%"/>
</div><br>

```
bash Miniconda3-latest-Linux-x86_64.sh 
```
<br>

## 2. Managing conda
```
conda --version
```
<img src="./images/ubuntu/update-package.png"/> \
To update packages
```
conda update package
```

To update conda
```
conda update conda
```

<br>

## 3. Managing environment
<div style="display:flex">
<img src="./images/ubuntu/conda-env.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/conda-env1.png" style="width:50%"/>
</div><br>

```
conda create --prefix ./env pandas numpy other_libraries python=3.x
```

To verify environment added 
```
conda info --envs
```
<div style="display:flex">
<img src="./images/ubuntu/conda-activate.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/conda-env1.png" style="width:50%"/>
</div><br>

To active environment
```
conda activate
```
<div style="display:flex">
<img src="./images/ubuntu/install-jupyter.png" style="width:50%; margin-right:7px;"/>

<img src="./images/ubuntu/create-envfile.png" style="width:50%; margin-right:7px;"/>

</div><br>

To create yml file from env
```
conda env export --prefix /path/../env > env.yml 

or 

conda env export > env.yml
```

To create environment from env file
```
conda env create -f env.yml 

or

conda env create --file env.yml --name env
```
To specify location for an environement
```
conda env create --prefix ./env -f ../env.yml
```


[Documentation-1](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)

[Documentation-2](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

<br>

## 4. Managing packages

<div style="display:flex">
<img src="./images/ubuntu/install-jupyter.png" style="width:33%; margin-right:7px;"/>

<img src="./images/ubuntu/conda-search.png" style="width:33%; margin-right:7px;"/>

<img src="./images/ubuntu/search-info.png" style="width:33%"/>
</div><br>

To search is any package installed or not

```
conda search package
```
To install package
```
conda install package
```
<div style="display:flex">
<img src="./images/ubuntu/run-jupyter.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/jupyter-notebook.png" style="width:50%"/>
</div><br>
To run jupter notebook
```
jupyter notebook
```

<div style="display:flex">
<img src="./images/ubuntu/conda-list.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/conda-deactivate.png" style="width:50%"/>
</div><br>

To list installed program in the environment
```
conda list
```
To deactivate conda 
```
conda deactivate
```
To uninstall packages
```
conda uninstall package
```
<br>

## Others
<div style="display:flex">
<img src="./images/ubuntu/other.png" style="width:50%; margin-right:7px"/>

<img src="./images/ubuntu/other1.png" style="width:50%"/>
</div><br>