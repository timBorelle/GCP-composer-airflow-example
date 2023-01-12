# Use the wine quality prediction model, via an API

## Installation

Create a virtual env for Python
```bash
python3 -m venv venv
```

Activate this virtual env
```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the libs needed (requirements.txt)

```bash
venv/bin/pip3 install -r requirements.txt
```

## Usage

Execute your function with the functions framework. By default, your function is accessible at localhost:8080, unless you explicitly specify a PORT

```bash
functions-framework --target getPrediction
```

Call your function with correct data

```bash
curl http://localhost:8080 -H 'Content-Type: application/json' -d '{"fixed acidity":"0.2", "volatile acidity":"0.5", "citric acid":"0.7", "residual sugar":"0.1", "chlorides":"0.2", "free sulfur dioxide":"0.3", "total sulfur dioxide":"0.2", "density":"0.4", "pH":"0.7", "sulphates":"0.3", "alcohol":"0.2"}'
```

Output

```bash
prediction: [5]
```
