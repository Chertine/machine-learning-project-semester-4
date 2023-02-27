import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, f1_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
root = tk.Tk()
root.geometry("1200x800")
canvas1 = tk.Canvas(root, width=1200, height=800)
canvas1.pack()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
fig1, ax1 = plt.subplots(figsize=(4, 4))
w = FigureCanvasTkAgg(fig1, root).get_tk_widget()
fig2, ax2 = plt.subplots(figsize=(4, 4))
e = FigureCanvasTkAgg(fig2, root).get_tk_widget()

def start():
    age = entry1.get()
    salary = entry2.get()
    array = np.array([[age, salary]])
    df = pd.DataFrame(data=array, index=[400], columns=['Age', 'EstimatedSalary'])
    Datframe = pd.read_csv('Social_Network_Ads.csv')
    StdScaler = StandardScaler()
    X = Datframe.drop(['Purchased'], axis='columns')
    X = pd.concat([X, df], axis=0)
    X = pd.DataFrame(StdScaler.fit_transform(X), columns=X.columns)
    entered_value = X.iloc[400, :].to_frame().transpose()
    X = X.drop([400], axis='rows')
    Y = pd.DataFrame(Datframe['Purchased'])
    test_rat = float(entry3.get())
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_rat)
    Random_Forest_Model = RandomForestClassifier()
    Random_Forest_Model.fit(np.array(X_train), np.ravel(Y_train))
    Y_pred = Random_Forest_Model.predict(np.array(X_test))
    value_prediction = Random_Forest_Model.predict(np.array(entered_value))
    canvas1.delete("all")
    label1 = tk.Label(root, text="accuracy score: {} %".format(round(accuracy_score(Y_test, Y_pred) * 100, 2)))
    canvas1.create_window(200, 50, window=label1)
    label2 = tk.Label(root, text="precision score: {} %".format(round(precision_score(Y_test, Y_pred, average='binary') * 100, 2)))
    canvas1.create_window(400, 50, window=label2)
    label3 = tk.Label(root, text="f1- score: {} %".format(round(f1_score(Y_test, Y_pred, average='binary') * 100, 2)))
    canvas1.create_window(600, 50, window=label3)
    label4 = tk.Label(root, text="recall score: {} %".format(round(recall_score(Y_test, Y_pred, average='binary') * 100, 2)))
    canvas1.create_window(800, 50, window=label4)
    if(value_prediction == 1):
        label5 = tk.Label(root, text="Entered Value Prediction: 1 (Purchased)")
    else:
        label5 = tk.Label(root, text="Entered Value Prediction: 0 (Not Purchased)")
    canvas1.create_window(600, 100, window=label5)
    X_train = X_train[['Age', 'EstimatedSalary']].to_numpy()
    Y_train = Y_train[['Purchased']].to_numpy()

    X_test = X_test[['Age', 'EstimatedSalary']].to_numpy()
    Y_test = Y_test[['Purchased']].to_numpy()


    plot_decision_regions(X_train, Y_train.ravel(), clf=Random_Forest_Model, ax=ax1)
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Estimated Salary")
    plt.tight_layout()
    w.place(x=50, y=200)
    label5 = tk.Label(root, text="Training Dataset")
    canvas1.create_window(300, 170, window=label5)


    plot_decision_regions(X_test, Y_test.ravel(), clf=Random_Forest_Model, ax=ax2)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Estimated Salary")
    plt.tight_layout()
    e.place(x=650, y=200)
    label6 = tk.Label(root, text="Testing Dataset")
    canvas1.create_window(900, 170, window=label6)

    button2 = tk.Button(text='< Previous', command=init_main)
    canvas1.create_window(600, 600, window=button2)



def init_main():
    canvas1.delete('all')
    try:
        w.place_forget()
        e.place_forget()
    except NameError as a:
        print("rip")
    insert_Age = tk.Label(root, text="Insert Age:")
    canvas1.create_window(500, 300, window=insert_Age)
    canvas1.create_window(650, 300, window=entry1)
    insert_Salary = tk.Label(root, text="Insert Salary:")
    canvas1.create_window(500, 350, window=insert_Salary)
    canvas1.create_window(650, 350, window=entry2)
    insert_Ratio = tk.Label(root, text="Insert Testing ratio:")
    canvas1.create_window(500, 400, window=insert_Ratio)

    canvas1.create_window(650, 400, window=entry3)
    button1 = tk.Button(text='Start Training', command=start)
    canvas1.create_window(600, 600, window=button1)




init_main()
root.mainloop()