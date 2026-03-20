def predict_income_drop(weather, avg_income):
    if weather == "rain":
        return avg_income * 0.7
    return avg_income
