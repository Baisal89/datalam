from sklearn.model_selection import train_test_split



def find_nulls(df):
    return df.isnull().sum()


def baisal89_test_split(df):
    X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, train_size=0.80, test_size=0.20,
    stratify=y_train, random_state=42)

    return X_train, X_val, y_train, y_val
