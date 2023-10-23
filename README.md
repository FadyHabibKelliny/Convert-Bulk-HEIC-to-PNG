# HEIC to PNG Bulk Converter

## Overview
This Python script helps you convert a bulk of HEIC image files to PNG format. It automates the conversion process by splitting the images into subfolders and handling errors. This README will guide you through the steps to use this tool.

## Installation
To use this script, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
also, I recommend installing anaconda [anaconda.org](https://anaconda.org/) and to use Spyder or any alternative.

### Clone the Repository
1. Open your command prompt or terminal.
2. Navigate to the directory where you want to install the tool.
3. Clone the repository using the following command:

```shell
git clone https://github.com/FadyHabibKelliny/Convert-Bulk-HEIC-to-PNG.git
```

Install Required Dependencies
You will need to install the required Python packages. Open your command prompt or terminal and navigate to the project directory.
maybe you will need other packeges put 
```shell
cd Convert-Bulk-HEIC-to-PNG
```

```shell
python -m pip install --upgrade pip
```

```shell
pip install heic2png
```

Usage
Follow these steps to use the HEIC to PNG conversion tool:

Place your HEIC files in the source folder.

Source Folder Path: "~/put/your/Source/path/folder"  #the folder that contains HEIC images
Open your command prompt or terminal.

Navigate to the project directory:

```shell
python convert_heic_to_png.py
```


The script will create subfolders in the destination folder "~/put/your/destination/path" #the folder that will contain PNG images.

Check the conversion statistics and any error messages displayed during the process.
contain
Once the conversion is complete, you can find the converted PNG files in the subfolders of the destination folder.

The script will also generate a CSV file (conversion_errors.csv) containing information about any conversion errors.


Troubleshooting
If you encounter any issues with the installation or usage of this tool, please ensure that you have Python and the required packages installed correctly.

If you face any errors or need assistance, feel free to open an issue on the GitHub repository.

Credits
This tool uses the heic2png library to perform the HEIC to PNG conversion. Visit the heic2png GitHub repository for more information.


## Support This simple script to continue updating 

If you find this project helpful and would like to support its development, you can make a donation through the following platforms:

- [PayPal](https://www.paypal.com/paypalme/fadykelliny)

