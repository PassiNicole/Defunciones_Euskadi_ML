import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

#cargar datos
def load_data():
    data = pd.read_csv("../data/data_defunciones_procesado.csv")
    X = data[['Defunciones', 'mes', 'sexo', 'tramo edad cumplida']]
    y = data['grandes grupos CIE-10']
    return X, y

def trained_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelos = []
    nombre_modelo = ['', '', '', '']

    # Modelo 1: Regresión Lineal
    modelo_lr = LinearRegression()
    modelo_lr.fit(X_train, y_train)
    y_pred_lr = modelo_lr.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)


    # Modelo 2: Árbol de Decisión
    modelo_dt = DecisionTreeRegressor(random_state=42)
    modelo_dt.fit(X_train, y_train)
    y_pred_dt = modelo_dt.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)


    # Modelo 3: Random Forest
    modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo_rf.fit(X_train, y_train)
    y_pred_rf = modelo_rf.predict(X_test) #predecir
    mse_rf = mean_squared_error(y_test, y_pred_rf) #evaluar


    # Modelo 4: SVR
    modelo_svr = SVR(kernel='linear')
    modelo_svr.fit(X_train, y_train)
    y_pred_svr = modelo_svr.predict(X_test) #predecir
    mse_svr = mean_squared_error(y_test, y_pred_svr) #evaluar


    # Modelo 5: Gradient Boosting
    modelo_gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
    modelo_gb.fit(X_train, y_train)
    y_pred_gb = modelo_gb.predict(X_test) #predecir
    mse_gb = mean_squared_error(y_test, y_pred_gb) #evaluar


    # Modelo 6: Redes neuronales
    modelo_mlp = MLPRegressor(hidden_layer_sizes=(50,50), max_iter=1000, random_state=42)
    modelo_mlp.fit(X_train, y_train)
    y_pred_mlp = modelo_mlp.predict(X_test) #predecir
    mse_mlp = mean_squared_error(y_test, y_pred_mlp) #evaluar


    # Modelo 7: KNN
    modelo_knn = KNeighborsRegressor(n_neighbors=5)
    modelo_knn.fit(X_train, y_train)
    y_pred_knn = modelo_knn.predict(X_test) #predecir
    mse_knn = mean_squared_error(y_test, y_pred_knn) #evalyar

    return modelo_knn, modelo_dt, modelo_gb, modelo_lr, modelo_mlp, modelo_svr, modelo_rf

if __name__ == "__main__":
    X, y = load_data()
    models = trained_model(X, y)

    for i, trained_model in enumerate(models[:-2]):
        joblib.dump(models, '../models/trained_model' )