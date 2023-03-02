# Augmented Reality with A-Frame

In this tutorial we will learn to create an NFT marker and use it to position a digital model in relationship to a specific image.  NFT stands for Natural Feature Tracking. The process works by generating a NFT marker file that is based on the features that are specfic to a given image. The markers will then be used to trigger the rendering of the digital model in the augmented reality application. To do this we will use an open source software created by Daniel Fernandes Gonçalves de Oliveira to generate markers. 

## Setup A (Desktop)
1. Obtain a free Gihub account: https://github.com/
2. Download and install Github deskstop: https://desktop.github.com/
3. Log-in to Github Desktop
4. Download and install vs-code:  https://code.visualstudio.com/Download
5. Download and install npm and node-js: https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac
6. Proceed to this page and follow instructions on cloning repository https://github.com/Carnaux/NFT-Marker-Creator
7. Open the repository in vs-code follow the instructions on the previous link to create the marker. 
8. To run the program enter the following in the terminal command line:   
    ` node app.js -i PATH/TO/IMAGE`

    Importantly, you will replace "PATH/TO/IMAGE" with the file name of your prepared image ex:
    ` node app.js -i RGB.jpeg`


## Setup B(Web - up to 1000px image)

1. Proceed to website:  https://ar-js-org.github.io/NFT-Marker-Creator/
2. Drag and drop your image.
3. Download the marker file.

## A-Frame and Glitch Implementation
1. 