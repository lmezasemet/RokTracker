import pandas as pd


#take as input an xlsx file and return a dictionary with the following structure:
# total_power = sum of all the power in the file
#total killpoints = sum of all the killpoints in the file
#total deads = sum of all the deads in the file
#total t4 kills = sum of all the t4 kills in the file
#total t5 kills = sum of all the t5 kills in the file
#total ressources gathered = sum of all the ressources gathered in the file


def analyse_top_scanfile(file, top):
    file_info = pd.read_excel(io=file, usecols=["Power", "T4 Kills", "T5 Kills", "Total Kills", "Deads", "Killpoints", "Rss Gathered"])
    file_info = file_info.head(top)  # Select the top rows based on the 'top' parameter
    total_power = sum(file_info["Power"])
    total_killpoints = sum(file_info["Killpoints"])
    total_deads = sum(file_info["Deads"])
    total_t4_kills = sum(file_info["T4 Kills"])
    total_t5_kills = sum(file_info["T5 Kills"])
    sum_total_kills = sum(file_info["Total Kills"])
    total_ressources_gathered = sum(file_info["Rss Gathered"])
    date = file_info["date"]
    return {
        "total_power": f"{total_power:,}",
        "total_killpoints": f"{total_killpoints:,}",
        "total_deads": f"{total_deads:,}",
        "total_t4_kills": f"{total_t4_kills:,}",
        "total_t5_kills": f"{total_t5_kills:,}",
        "sum_total_kills": f"{sum_total_kills:,}",
        "total_ressources_gathered": f"{total_ressources_gathered:,}",
        "date": date
    }


result = analyse_top_scanfile("DKP_scan/3165_top900.xlsx", top=300) #Change the file name and the top value

def count_people_by_power(file, top):
    file_info = pd.read_excel(io=file, usecols=["Power"], nrows=top)
    above_100m = len(file_info[file_info["Power"] > 100000000])
    above_80m = len(file_info[file_info["Power"] > 80000000])
    above_60m = len(file_info[file_info["Power"] > 60000000])
    return above_100m, above_80m, above_60m

above_100m, above_80m, above_60m = count_people_by_power("DKP_scan/3165_top900.xlsx", top=300) #Change the file name and the top value

result["people_above_100m"] = str(above_100m)
result["people_above_80m"] = str(above_80m)
result["people_above_60m"] = str(above_60m)

#save the result in a new file
new_file = pd.DataFrame()
new_file["Key"] = result.keys()
new_file["Value"] = result.values()
new_file.to_excel("DKP_scan/3165_top300_analysis.xlsx", index=False)
print(result)