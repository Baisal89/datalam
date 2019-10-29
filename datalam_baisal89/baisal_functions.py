#import train test split form sklearn
from sklearn.model_selection import train_test_split


#defining function find_nulls
def find_nulls(df):
    return df.isnull().sum()

#defining function baisal89_test_split and return it
def baisal89_test_split(df):
    X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, train_size=0.80, test_size=0.20,
    stratify=y_train, random_state=42)

    return X_train, X_val, y_train, y_val
