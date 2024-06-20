
def Concat_Compare():
    workstation_df = pd.read_excel(workstation_file, sheet_name="Master 2")
    workstation_df.insert(11, "Concat", "")
  
    workstation_df['Concat'] = workstation_df.iloc[:, :8].apply(lambda row: ''.join(row.astype(str)), axis=1)

    if is_first_working_day(current_date) == False:
        workstation_df.insert(12, "Compare", "")
        workstation_final_df = pd.read_excel(workstation_final, sheet_name="Master 2")
        for index, row in workstation_df.iterrows():
            concat_value = row["Concat"]
            try:
                compare_value = workstation_final_df.loc[workstation_final_df["Concat"] == concat_value, "Concat"].values[0]
                workstation_df.at[index, "Compare"] = compare_value
            except IndexError:
                workstation_df.at[index, "Compare"] = ""

        new_df = workstation_df[workstation_df['Compare'] == '']
        new_df['Compare'] = "New"
        workstation_df = workstation_df[workstation_df['Compare'] != '']

        with pd.ExcelWriter(workstation_file, mode='a', if_sheet_exists='replace') as writer:
            workstation_df.to_excel(writer, sheet_name="Master 2", index=False)
            new_df.to_excel(writer, sheet_name="New", index=False)
        print("Concat And Compare Column Is Created")

    else:
        with pd.ExcelWriter(workstation_file, mode='a', if_sheet_exists='replace') as writer:
            workstation_df.to_excel(writer, sheet_name="Master 2", index=False)
        print("Compare Column Is Created")


update the code in following excel logic:
5.	Add 2 columns before Vul. Since column and name them as “Concat” and ”Compare” respectively
a)	In “Concat” column, apply =CONCATENATE(A2,B2,C2,D2,E2,F2,G2,H2) and drag for the remaining ones.  
b)	In “Compare” column, apply =VLOOKUP(previous baseline version (concate column), current concate column, 1, false)(copy paste as values). Select #N/A by applying filter, rename all #N/A to New and copy all to new sheet ‘New’ and  delete from Master 2.

