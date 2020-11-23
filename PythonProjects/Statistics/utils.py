import csv
import os
import re
from typing import List
import numpy as np
from utilities import CustomError, color_print
from utilities.utils import handle_user_input
from matplotlib import pyplot as plt


def get_csv_data(path: str) -> (List[str], List[List[str]]):
    """

    :param path: path to a csv file
    :return: labels for read data along with a list of each registered instance
    """
    assert os.path.isfile(path), "argv is not a path to a valid file"
    fd = open(path)
    try:
        csv_fd = csv.reader(fd)
    except Exception as e:
        raise CustomError("file not a csv file")
    data = []
    for i in csv_fd:
        data.append(i)
    for i in range(len(data)):
        if data[i][-1] == "":
            data[i] = data[i][:-1]
    assert len(data) > 1, "fisierul csv nu are destule date (1 linie de etichete pe coloane si o linie de date)"
    return data[0], data[1:]


def get_eligible_labels(labels: List[str], param: List[str]) -> List[str]:
    """

    :param labels: labels for csv data
    :param param: first row of data
    :return: filtered labels which point only to numeric data
    """
    return list(filter(lambda x: param[labels.index(x)].strip().isdigit(), labels))


def plot_data(labels: List[str], data: List[List[str]]):
    """

    :param labels: column names: first line in csv file
    :param data: all data in csv file, each row being a list of data
    :return: nothing
    """
    choosable_labels = get_eligible_labels(labels, data[0])
    color_print("Alege o coloana pentru a realiza statistici peste ea")
    color_print(f"Coloane disponibile: {', '.join(choosable_labels)}")
    pattern = re.compile(f"({'|'.join(choosable_labels)})")
    chosen_label = handle_user_input(pattern)
    target_data = np.array([int(i[labels.index(chosen_label)]) for i in data])
    age_data = np.array([int(i[labels.index("varsta")]) for i in data])
    iq_data = np.array([int(i[labels.index("IQ")]) for i in data])
    color_print(f"Minimul: {target_data.min()}", color='green')
    color_print(f"Maximul: {target_data.max()}", color='green')
    color_print(f"Media: {target_data.mean()}", color='green')
    color_print(f"Mediana: {np.median(target_data)}", color='green')
    color_print(f"Deviatia standard: {target_data.std()}", color='green')
    color_print(f"Cvartila Q1: {np.quantile(target_data, .25)}", color='green')
    color_print(f"Cvartila Q2: {np.quantile(target_data, .50)}", color='green')
    color_print(f"Cvartila Q3: {np.quantile(target_data, .75)}", color='green')
    color_print(f"Covarianta: {np.cov(target_data)}", color='green')
    color_print(f"Coeficientul de corelatie intre varsta si IQ: \n{np.corrcoef(age_data, iq_data)}", color='green')
    plt.scatter(age_data, iq_data, c='r', label='data')
    plt.plot(age_data, iq_data, label='$Varsta / IQ$')
    plt.xlabel('varsta')
    plt.ylabel('iq')
    plt.title('relatie varsta - iq')
    plt.legend()
    plt.show()
