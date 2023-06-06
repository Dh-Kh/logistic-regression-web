import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
dataframe = pd.read_csv("CreditScore.csv")
dataframe.loc[dataframe["Age"] > 50, "Age"] = 0
dataframe.loc[dataframe["Age"] < 50, "Age"] = 1
dataframe.loc[dataframe["Gender"] != "Male", "Gender"] = 0
dataframe.loc[dataframe["Gender"] == "Male", "Gender"] = 1
dataframe.loc[dataframe["Income"] < 60000, "Income"] = 0
dataframe.loc[dataframe["Income"] > 60000, "Income"] = 1
dataframe.loc[dataframe["Education"] == "High School Diploma", "Education"] = 0
dataframe.loc[dataframe["Education"] != "High School Diploma", "Education"] = 1
dataframe.loc[dataframe["Number of Children"] >= 3, "Number of Children"] = 0
dataframe.loc[dataframe["Number of Children"] < 3, "Number of Children"] = 1
dataframe.loc[dataframe["Home Ownership"] == "Rented", "Home Ownership"] = 0
dataframe.loc[dataframe["Home Ownership"] == "Owned", "Home Ownership"] = 1
dataframe.loc[dataframe["Credit Score"] == "Low", "Credit Score"] = 0
dataframe.loc[dataframe["Credit Score"] == "Average", "Credit Score"] = 0
dataframe.loc[dataframe["Credit Score"] == "High", "Credit Score"] = 1
dataframe["Credit Score"] = pd.to_numeric(dataframe["Credit Score"])
droped_data = ["Marital Status"]
dataframe = dataframe.drop(droped_data, axis=1)
x = dataframe.drop("Credit Score", axis=1)
y = dataframe["Credit Score"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=0)
machine = LogisticRegression(random_state=0)
machine.fit(xtrain, ytrain)

def make_user_prediction(user_input: list):
    try:
        user_input = [user_input]
        input_result = pd.DataFrame(user_input, columns=xtrain.columns)
        prediction = machine.predict(input_result)
        return prediction
    except ValueError:
        pass