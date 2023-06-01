import pandas as pd
from joblib import load
from sklearn.preprocessing import MinMaxScaler


def predict(Type, Tectonic,Lithology,Structural,Gross,
            Netpay,Porosity,Permeability,Depth,OilDensity,Nge):
    filename = 'rf_model.joblib'
    clf = load(open(filename, 'rb'))
    filename = 'rf_model_gas.joblib'
    clf_gas = load(open(filename, 'rb'))
    
    test = pd.DataFrame({
        'Tectonic regime' : [Tectonic],  
        'Lithology' : [Lithology],
        'Structural setting' : [Structural],
        'Gross' : [Gross],
        'Netpay' : [Netpay],
        'Porosity' : [Porosity],
        'Permeability' : [Permeability],
        'Depth' : [Depth],
        'Oil density' : [OilDensity],
        'NGE' : [Nge]
    })
    #data.append(test,ignore_index=True)
    if Type == 'OIL':
        data = pd.read_csv('datad.csv')
        data = pd.concat([data,test])
        data = pd.get_dummies(data, columns=['Tectonic regime', 'Lithology', 'Structural setting'])
        X_data = data.drop(['Oil recovery factor'],axis=1)
    else:
        data = pd.read_csv('data_gas.csv')
        test.drop(columns=['Oil density'], inplace=True)
        data = pd.concat([data,test])
        data = pd.get_dummies(data, columns=['Tectonic regime', 'Lithology', 'Structural setting'])
        X_data = data.drop(['Gas recovery factor'],axis=1)

    scaler = MinMaxScaler(feature_range=(0,1))
    scaler.fit(X_data)
    X_data_norm = scaler.transform(X_data)
    if Type == 'OIL':
        return(clf.predict(X_data_norm)[-1])
    else:
        return(clf_gas.predict(X_data_norm)[-1])
