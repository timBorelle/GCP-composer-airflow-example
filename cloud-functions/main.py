import joblib
import numpy as np

FEATURES = [
 'fixed acidity',
 'volatile acidity',
 'citric acid',
 'residual sugar',
 'chlorides',
 'free sulfur dioxide',
 'total sulfur dioxide',
 'density',
 'pH',
 'sulphates',
 'alcohol',
]

def getPrediction(request):
    if request.get_json():
        request_json = request.get_json()
        allFeatures = containsAllFeatures(request)
        if not allFeatures:
            return "You must specify all features !"
            exit
        filename = 'model.joblib'
        loaded_model = joblib.load(filename)

        fixedAcidity = float(request_json['fixed acidity'][0:])
        volatileAcidity = float(request_json['volatile acidity'][0:])
        citricAcid = float(request_json['citric acid'][0:])
        residualSugar = float(request_json['residual sugar'][0:])
        chlorides = float(request_json['chlorides'][0:])
        freeSulfurDioxide = float(request_json['free sulfur dioxide'][0:])
        totalSulfurDioxide = float(request_json['total sulfur dioxide'][0:])
        density = float(request_json['density'][0:])
        pH = float(request_json['pH'][0:])
        sulphates = float(request_json['sulphates'][0:])
        alcohol = float(request_json['alcohol'][0:])
        dataToPredict = np.array((fixedAcidity, volatileAcidity, citricAcid, 
                            residualSugar, chlorides, freeSulfurDioxide,
                            totalSulfurDioxide, density, pH, sulphates, alcohol), float)
        # if your data to predict contain a single sample, reshape it
        dataToPredict = dataToPredict.reshape(1, -1)
        # Making predictions with our model
        predictions = loaded_model.predict(dataToPredict)
        return f'prediction: ' + str(predictions) + '\n'

def containsAllFeatures(request):
    for i in FEATURES:
        try:
            if request.get_json()[i][0:] is None:
                return False
        except:
            return False
    return True
