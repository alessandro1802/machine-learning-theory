# Machine Learning Theory experiment

## Set-up
```shell
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Replace `YOUR_PROJECT` and `YOUR_API_TOKEN` in the `.env` file with your [Neptune.ai](https://neptune.ai) project credentials.

## Experiment
The goal is to test the learning process characteristics (e.g. classification error, distribution of weights) for neural networks using different optimization algorithms such as SGD, AdaGrad, Adam, etc.
```
.
├── main.ipynb      Experiment implementation
├── metrics         Exported experiment metrics
├── plots           Visualizations
├── visualize.py    Script for preparing plots
└── ...
```
