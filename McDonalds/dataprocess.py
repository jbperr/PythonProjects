import os, os.path
import json
import collections
import csv
from tqdm import tqdm
import pandas as pd

path_to_json = "/LocInfo/"
gravy = 162
gravynum = 0

num = 0

mcd_list = []


for file_name in tqdm(
    [file for file in os.listdir(path_to_json) if file.endswith(".json")]
):
    with open(path_to_json + file_name) as json_file:
        data = json.load(json_file)

    header = data["response"]["restaurant"]

    breakfast_menu = header["availableMenuProducts"]["1"]
    # lunch_menu = header["availableMenuProducts"]["2"]
    # dinner_menu = header["availableMenuProducts"]["3"]
    address = header["address"]["addressLine1"]
    town = header["address"]["cityTown"]
    state = header["address"]["stateProvince"]
    zip_code = header["address"]["postalZip"]
    store_id = header["nationalStoreNumber"]
    store_latitude = header["location"]["latitude"]
    store_longitude = header["location"]["longitude"]
    phone_number = header["phoneNumber"]
    # store_open_date = header["generalStatus"]["startDate"]
    bisc_gravy = 1 if 162 in breakfast_menu else 0

    jsonlist = [
        store_id,
        address,
        town,
        state,
        zip_code[:5],
        store_latitude,
        store_longitude,
        phone_number,
        bisc_gravy,
    ]

    mcd_list.append(jsonlist)


# print(mcd_list)


df = pd.DataFrame(
    mcd_list,
    columns=[
        "store_id",
        "address",
        "town",
        "state",
        "zip_code",
        "store_latitude",
        "store_longitude",
        "phone_number",
        "bisc_gravy",
    ],
)

print(df["bisc_gravy"].describe())
# df.to_csv("PROCESSED_McDATA.csv")
