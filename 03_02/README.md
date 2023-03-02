# Augmented Reality with A-Frame

In this tutorial we will learn to create an NFT marker and use it to position a digital model in relationship to a specific image.  NFT stands for Natural Feature Tracking. The process works by generating a NFT marker file that is based on the features that are specfic to a given image. The markers will then be used to trigger the rendering of the digital model in the augmented reality application. To do this we will use an open source software created by Daniel Fernandes Gonçalves de Oliveira to generate markers. 

## Setup A (Desktop)
1. Obtain a free Github account: https://github.com/
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
1. To begin, build a basic AR scene with AR starter file. This will aquaint you with the issues of scale, coordinate systems, and animations: https://glitch.com/edit/#!/arjsstarterfile
2. After completing the last step open and copy the Image Tracking Template:  https://glitch.com/edit/#!/image-tracking-example
3. Next open the assets tab on your glitch page and upload the three files created by the nft.marker:  file_name.fset, file_name.fset3 and file_name.iset.  To be sure that you see these files make sure that you have the file type in the file explorer set to "all files."
4. On line 56 of the html there is url: "https://cdn.glitch.global/6cc45ecc-2a01-4d57-b4b5-2ad82a59b750/frame-3609" Note that url ends with the file_name for the .fset, .fset3 and .iset files that you just uploaded.  You can now navigate to your assets page and copy the url for the .fset file. Once you paste in the url, delete everything after the file_name.  In the example file the file_name is "frame-3609"
5. Input the scale and location values from your basic AR scene and attempt to scale and position the object so that it is visible. You can accomplish this by holding the printed image in front of your webcam.  
6. Once you have it working send yourself the live site link and test this on your smart phone.
7. If the image is jumpy this could be due to a a poor image descriptor.  If your image is too simple without enough distinguishing features, or the print resolution is poor, the image will jump around. To read more about marker head here: https://github.com/Carnaux/NFT-Marker-Creator/wiki/Creating-good-markers
