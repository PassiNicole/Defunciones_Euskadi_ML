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
    nombre_modelo = ['LinearRegression', 'DecisionTree', 'RandomForest', 'SVR', 'GradientBoosting', 'MLPRegressor', 'KNN']

    # Modelo 1: Regresión Lineal
    modelo_lr = LinearRegression()
    modelo_lr.fit(X_train, y_train)
    y_pred_lr = modelo_lr.predict(X_test)
    evaluar_modelo("LinearRegression", modelo_lr, X_test, y_test, y_pred_lr)
    modelos.append(modelo_lr)


    # Modelo 2: Árbol de Decisión
    modelo_dt = DecisionTreeRegressor(random_state=42)
    modelo_dt.fit(X_train, y_train)
    y_pred_dt = modelo_dt.predict(X_test)
    evaluar_modelo("DecisionTree", modelo_dt, X_test, y_test, y_pred_dt)
    modelos.append(modelo_dt)

    # Modelo 3: Random Forest
    modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo_rf.fit(X_train, y_train)
    y_pred_rf = modelo_rf.predict(X_test) #predecir
    evaluar_modelo("RandomForest", modelo_rf, X_test, y_test, y_pred_rf)
    modelos.append(modelo_rf)


    # Modelo 4: SVR
    modelo_svr = SVR(kernel='linear')
    modelo_svr.fit(X_train, y_train)
    y_pred_svr = modelo_svr.predict(X_test) #predecir
    evaluar_modelo("SVR", modelo_svr, X_test, y_test, y_pred_svr)
    modelos.append(modelo_svr)


    # Modelo 5: Gradient Boosting
    modelo_gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
    modelo_gb.fit(X_train, y_train)
    y_pred_gb = modelo_gb.predict(X_test) #predecir
    evaluar_modelo("GradientBoosting", modelo_gb, X_test, y_test, y_pred_gb)
    modelos.append(modelo_gb)

    # Modelo 6: Redes neuronales
    modelo_mlp = MLPRegressor(hidden_layer_sizes=(50,50), max_iter=1000, random_state=42)
    modelo_mlp.fit(X_train, y_train)
    y_pred_mlp = modelo_mlp.predict(X_test) #predecir
    evaluar_modelo("MLPRegressor", modelo_mlp, X_test, y_test, y_pred_mlp)
    modelos.append(modelo_mlp)

    # Modelo 7: KNN
    modelo_knn = KNeighborsRegressor(n_neighbors=5)
    modelo_knn.fit(X_train, y_train)
    y_pred_knn = modelo_knn.predict(X_test) #predecir
    evaluar_modelo("KNN", modelo_knn, X_test, y_test, y_pred_knn)
    modelos.append(modelo_knn)

    return modelos, nombre_modelo

def evaluar_modelo(nombre, modelo, X_test, y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Modelo: {nombre}")
    print(f"Mean Squared Error (MSE): {mse:.3f}")
    print(f"R2 Score: {r2:.3f}")
    print("-" * 40)

if __name__ == "__main__":
    X, y = load_data()
    
    modelos, nombre_modelo = trained_model(X, y)

    for modelo, nombre in zip(modelos, nombre_modelo):
        modelo_path = f'../models/{nombre}_trained_model.pkl'
        joblib.dump(modelo, modelo_path)
        print(f'Modelo {nombre} guardado en: {modelo_path}')