<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<h3 align="center">Tweeting Emotions: Decoding Sentiment in 140 Characters</h3>

  <p align="center">
    Sentimental Analysis on Tweets.
    <br />
    <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Reports/Tweeting_Emotions.pdf"><strong>Final Report »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Reports/Tweeting Emotions - Presentation.pptx"><strong>Final Presentation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SkyglowDS/Tweeting-Emotions/tree/main/Code">View Code</a>
    ·
    <a href="https://github.com/SkyglowDS/Tweeting-Emotions/tree/main/Reports">View Reports</a>

  </p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#coding-files">Coding Files</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a final project for a OMSA course. The specific references to the course are removed in order to abide by Georgia Tech's Code of Conduct. 

The objective of this project is to explore and develop models for sentimental analysis on Tweets. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

The required packages for this project are located in `requirements.txt`. An IDE, such as VSCode, to view the jupyter notebooks is preferred. 

```sh
pip install -r requirements.txt
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SkyglowDS/Tweeting-Emotions.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Download dataset and run the dataset generator
   
   <a href="https://www.kaggle.com/datasets/kazanova/sentiment140/data">Kaggle Sentiment 140</a>

   Run the notebook:
   <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Code/generate_dataset.ipynb">generate_dataset.ipynb</a>

4. Train model:   
   Use <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Code/production/modeling.ipynb">modeling.ipynb</a> For Naive Bayes and Logistic Regression  
   Use <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Code/production/modeling_nn.ipynb">modeling_nn.ipynb</a> RNN  
   Use <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Code/production/modeling_nn_es.ipynb">modeling_nn_es.ipynb</a> RNN with Early Stopping  
5. Test model on Samples:  
   Use <a href="https://github.com/SkyglowDS/Tweeting-Emotions/blob/main/Code/production/model_evaluation.ipynb">model_testing.ipynb</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Coding Files 

### .py files

`preprocessing.py`: Cleans the text data.

### Jupyter Notebooks

`generate_dataset.ipynb`: Creates a clean text version of the dataset.

`modeling.ipynb`: Includes modeling for Naive Bayes and Logistic Regression.

`modeling_nn.ipynb`: Code to train the RNN model.

`modeling_nn_es.ipynb`: Code to train the RNN model with early stopping.

`model_testing.ipynb`: Code to test the trained model on sample Tweets.

`data_cleaning_eda.ipynb`: Testing used to create preprocessing file.

`eda.ipynb`: Exploratory Data Analysis on text data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
