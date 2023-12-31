from main import *

#Load Test Dataset
df_predict = pd.read_csv(r"E:\Machine Learning\milestone 2\milestone 2\milestone2\milestone2\games-classification-dataset.csv")

def prediction(model_name, data):
    #Load Model
    pickled_model = pickle.load(open(model_name, 'rb'))
    
    #Pre-Process Data 
    X_Test = data.drop(columns='Rate', axis=1, inplace=False)
    Y_Test = pd.DataFrame(data['Rate'])
    cols, X_test, y_test = pre(X_Test, Y_Test)
    
    #Select the features that was only in the training model
    colummns = X_test.columns    
    for i in selected_columns:
      if i not in colummns:
        X_test[i] = 0
    X_test = X_test[selected_columns]  
    
    #Predict using the pickle model
    pickle_test = pickled_model.predict(X_test)
    
    #Replace values to match the test data to measure Accuracy
    mapping = {'Low': 0, 'Intermediate': 1, 'High': 2}
    for value in ['Low', 'Intermediate', 'High']:
        if value in y_test:
            y_test['Rate'] = y_test['Rate'].replace({value: mapping[value]})
   
    #Measuring Accuracy
    print('Accuracy of Decision Tree picke Test: {:.2f}%'.format(accuracy_score(y_test, pickle_test) * 100))
    print('Mean Square Error of Decision Tree pickle Test: ' , metrics.mean_squared_error(Y_Test,pickle_test))

#Call function to return the predicted data using a model
prediction('Decision Tree.pkl', df_predict)


   

