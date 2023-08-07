import numpy as np
import pandas as pd
import tensorflow as tf
import tkinter as tk
from tkinter import ttk

data = pd.read_csv('./data/results.csv', encoding='ISO-8859-1')

def get_prediction():
    home = home_var.get()
    away = away_var.get()
    test_hg = int(home_goals_entry.get())
    test_ag = int(away_goals_entry.get())

    preResult = pd.concat([data[data['HomeTeam'] == home], data[data['AwayTeam'] == home]]).sort_index()
    result = pd.concat([preResult[preResult['AwayTeam'] == away]]).sort_index()

    new_result = result[result["Season"] >= "2000"]
    new_result.loc[(result.FTR == 'H'), 'FTR'] = 0
    new_result.loc[(result.FTR == 'A'), 'FTR'] = 2
    new_result.loc[(result.FTR == 'D'), 'FTR'] = 1
    x_data = new_result.iloc[:, 7:9]
    y_data = new_result.iloc[:, 6]
    y_oneHot = tf.keras.utils.to_categorical(y_data, 3)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=3, input_dim=x_data.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=0.1), metrics=['accuracy'])

    test_data = np.array([[test_hg, test_ag]])
    prediction = model.predict(test_data)
    if np.argmax(prediction) == 0:
        result_label.config(text="Result: {} - {} (Home Win)".format(test_hg, test_ag))
    elif np.argmax(prediction) == 1:
        result_label.config(text="Result: {} - {} (Draw)".format(test_hg, test_ag))
    else:
        result_label.config(text="Result: {} - {} (Away Win)".format(test_hg, test_ag))

root = tk.Tk()
root.title("EPL Winning Team Predictor")
root.geometry("300x300")

home_label = ttk.Label(root, text="Home Team:")
home_label.pack()
home_var = tk.StringVar()
home_entry = ttk.Entry(root, textvariable=home_var)
home_entry.pack()

away_label = ttk.Label(root, text="Away Team:")
away_label.pack()
away_var = tk.StringVar()
away_entry = ttk.Entry(root, textvariable=away_var)
away_entry.pack()

home_goals_label = ttk.Label(root, text="Home Goals:")
home_goals_label.pack()
home_goals_entry = ttk.Entry(root)
home_goals_entry.pack()

away_goals_label = ttk.Label(root, text="Away Goals:")
away_goals_label.pack()
away_goals_entry = ttk.Entry(root)
away_goals_entry.pack()

predict_button = ttk.Button(root, text="Predict", command=get_prediction)
predict_button.pack()

result_label = ttk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()