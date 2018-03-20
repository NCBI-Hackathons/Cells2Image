# Cells2Image
![Learning algorithm for detecting cell structure changes from light microscopy data](images/Cover-Slide.jpg "Learning algorithm for detecting cell structure changes from light microscopy data")

## AKA Pop goes the Merozoite
![Pop goes the Merozoite](images/Cover-Slide-Funny.jpg "Pop goes the Merozoite!")

## Team Assignments
* Brad Busse - brad.busse@nih.gov - Team lead - Developer
* Lars Von Buchholtz - lvonbuchholtz@nidcr.nih.gov - Developer
* Patrick Fletcher - patrick.fletcher@nih.gov - Developer
* Jeremy Swan - jeremy.swan@nih.gov - Writer

## Background
During the course of infection, the malaria parasite (a plasmodium) infects a hepatocyte in the liver, where it undergoes development into merozoites which grow and eventually lyse the cell. Merozoites move into the bloodstream, where they can infect red blood cells (RBCs). Once in a red blood cell (RBC), the merozoites feed and multiply, condensing hemoglobin into a vacuole, which is observed as a dark spot in differential interference contrast (DIC) microscopy. The merozoites feed and undergo several multiplication cycles over the course of several days, before the cell lyses, releasing merozoites into the bloodstream to infect other cells. We want to capture high resolution images of the merozoites bursting out of red blood cells.

![Merozoite infecting cell](images/merozoite.jpg "Merozoite infecting cell")

## Problem
The process of observing an infected Red Blood Cell for 2 days, awaiting or trying to predict a 10 minute long lytic event is tedious, and not very accurate. A software tool which can predict when an infected RBC will lyse would save time and result in better science. Observing infected RBC’s at high resolution requires high intensity light, which results in killing or damaging the cells, so brute force image collection at high resolution is not a solution. Our strategy is to capture a 2D image every 10 minutes, then analyze the image sequence to predict when a bursting event will happen, indicating the start of high resolution imaging. 

## Current Pipeline

### Cell Mask
![figure](images/cell_mask.png "Cell Mask")

### Circularity
![figure](images/circularity.png "Circularity")

### Fluorescence
![figure](images/fluorescence.png "Fluorescence")

## Time Series Analysis

### Cluster Analysis
![figure](images/cluster_analysis1.png "Cluster Analysis")

### Cluster Analysis Separated
![figure](images/cluster_analysis_separated.png "Cluster Analysis Separated")

### Cluster Analysis tSNE
![figure](images/cluster_analysis_tSNE.png "Cluster Analysis tSNE")

## Training
In order to train our tool, we used 25 image sequences were created by acquiring an image at low intensity every 10 minutes through the bursting activity.

## Tools used
We used algorithms from scikit-image - Image Processing in Python. We also used Jupyter, Google Code, ImageJ 
