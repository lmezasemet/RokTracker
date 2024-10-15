# Load the previously modified data
import os
import pandas as pd


# Load the previously modified data using os.path.join
# location C:\Users\louis\Documents\GitHub\RokTracker\DKP_scan\KVK6
merged_file_path = os.path.join('C:\\', 'Users', 'louis', 'Documents', 'GitHub', 'RokTracker', 'DKP_scan', 'KVK6', 'DKP-kvk6-after-z5-with-power-mm.xlsx')
merged_data = pd.read_excel(merged_file_path)

# Define power ranges and corresponding KP and Deads requirements
def assign_requirements(power):
    if pd.isna(power):
        return 0, 0
    if power < 40e6:
        return 140000000, 400000
    elif power < 50e6:
        return 185000000, 500000
    elif power < 60e6:
        return 225000000, 600000
    elif power < 70e6:
        return 290000000, 775000
    elif power < 80e6:
        return 370000000, 1000000
    elif power < 90e6:
        return 450000000, 1250000
    elif power < 100e6:
        return 540000000, 1650000
    elif power < 112.5e6:
        return 680000000, 2125000
    elif power < 125e6:
        return 680000000, 2375000
    elif power < 137.5e6:
        return 760000000, 3000000
    elif power < 150e6:
        return 760000000, 3500000
    else:  # power is 150 or more
        print(f'Power is {power} or more')
        return 825000000, 4000000

# Apply the function to assign KP and Deads based on power-mm
merged_data[['KP req', 'Deads req']] = merged_data['power-mm'].apply(
    lambda x: pd.Series(assign_requirements(x))
)



#based on the requirements we just assigned, we can now calculate the difference between the actual KP and Deads and the requirements
#calculate the percentage of KP and Deads met using the "KP gained" and "Deads" columns
merged_data['KP %'] = (merged_data['KP Gained'] / merged_data['KP req'])* 100
merged_data['Deads %'] = (merged_data['Deads'] / merged_data['Deads req']) * 100








# Save the updated data
updated_file_path = os.path.join('C:\\', 'Users', 'louis', 'Documents', 'GitHub', 'RokTracker', 'DKP_scan', 'KVK6', 'DKP-kvk6-after-z5-with-power-mm-and-requirements.xlsx')
merged_data.to_excel(updated_file_path, index=False)
print(f'Updated data saved to {updated_file_path}')

