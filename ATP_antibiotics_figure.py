import matplotlib.pyplot as plt

ATPdata = {

    "Amikacin" : {
                    "Details" : ["Akhova and Tkachenko (2014)", "(nmol/mg dw)", "Escherichia coli EH40"],
                    "Time (min)" : [0, 30, 60, 90, 120, 150, 180],
                    "ATP" : {"Untreated" : [4.1, 3.5, 3.5, 1.75, 1.5, 2, 2.4],
                             "25ug/mL" : [4.4, 4.9, 4.8, 4.6, 1.5, 2.5, 2.5]}},

    "Ampicillin and clavulanic acid" : {
                                        "Details" : ["Cornel et al., 1982", "(units)", "Escherichia coli (TEM-1)"],
                                        "Time (hours)" : [0, 1, 2, 3, 4],
                                        "ATP" : {"Untreated" : [0.52, 0.86, 1.14, 1.77, 2.75],
                                                "0.1mg/mL" : [0.52, 0.38, 0.56, 0.47, 0.38],
                                                "10mg/mL" : [0.52, 0.28, 0.14, 0.11, 0.04]}},

    "Carbenicillin and clavulanic acid" : {
                                           "Details" : ["Cornel et al., 1982", "(units)", "Escherichia coli (TEM-1)"],
                                           "Time (hours)" : [0, 1, 2, 3, 4],
                                           "ATP" : {"Untreated" : [1.19, 2.64, 4.69, 10, 10],
                                                    "0.1mg/mL" : [1.19, 1.53, 1.94, 2.65, 3.18],
                                                    "10mg/mL" : [1.19, 1.08, 0.73, 0.45, 0.32]}
                                            },

    "Cefotaxime" : {
                    "Details" : ["Akhova and Tkachenko (2014)", "(nmol / mg dw)", "Escherichia coli EH40"],
                    "Time (min)" : [0, 30, 60, 90, 120, 150, 180],
                    "ATP" : {"Untreated" : [2.1, 2.7, 2.7, 2.1, 1.6, 1.5, 1.1],
                             "1.2ug/mL" : [1.6, 4, 2.5, 2.5, 2.2, 1.5, 2]}
                             },

    "Clindamycin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Escherichia coli (UPEC)"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [12700000, 70000000, 215000000],
                             "2ug/mL" : [12300000, 68000000, 190000000],
                             "8ug/mL" : [13500000, 68500000, 198000000]},
                    "CFU/mL" : {"Untreated" : [46000000, 255000000, 778000000],
                                "2ug/mL" : [44900000, 247000000, 715000000],
                                "8ug/mL" : [49100000, 249000000, 715000000]}},

    "Doxycycline" : {
                    "Details" : ["Hojer and Nilsson (1978)", "(M)", "Enterobacter cloacae"],
                    "Time (hours)" : [0, 1, 2, 3, 4],
                    "ATP" : {"Untreated" : [0.00000032, 0.000001, 0.0000018, 0.0000025, 0.0000035],
                            "0.1ug/mL" : [0.00000032, 0.00000087, 0.000001097, 0.00000152, 0.0000025],
                            "1.0ug/mL" : [0.00000032, 0.000000507, 0.00000105, 0.00000105, 0.00000111],
                            "5.0ug/mL" : [0.00000032, 0.00000019, 0.000000305, 0.00000035, 0.00000044]},
                    "CFU/mL" : {"Untreated" : [170000000, 270000000, 470000000, 740000000, 830000000],
                                "0.1ug/mL" : [170000000, 240000000, 380000000, 420000000, 470000000],
                                "1.0ug/mL" : [170000000, 103000000, 110000000, 140000000, 370000000],
                                "5.0ug/mL" : [170000000, 86000000, 27000000, 26000000, 46000000]}
                    },

    "Erythromycin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli (UPEC)"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [12500000, 44500000, 148000000],
                             "2ug/mL" : [14800000, 42000000, 124000000],
                             "8ug/mL" : [15700000, 39600000, 106000000]},
                    "CFU/mL" : {"Untreated" : [45300000, 162000000, 538000000],
                                "2ug/mL" : [53800000, 153000000, 449000000],
                                "8ug/mL" : [56900000, 144000000, 384000000]}},

    "Gentamicin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Unknown Uropathogen"],
                    "Time (hours)" : [0, 1, 2, 3],
                    "ATP" : {"Untreated" : [7.1, 7.7, 8.2, 8.7],
                             "0.25xMIC" : [7.1, 7.4, 7.5, 7.5],
                             "MIC" : [7.1, 6.8, 6.7, 6.7],
                             "4xMIC" : [7.1, 6.7, 6.7, 6.7]},
                    "CFU/mL" : {"Untreated" : [59, 63, 70, 77],
                                "0.25xMIC" : [59, 60, 59, 58],
                                "MIC" : [59, 35, 29, 27],
                                "4xMIC" : [59, 20, 20, 20]}},

    "Levofloxacin" : {
                    "Details" : ["Matsui et al., 2019", "(amol)", "Escherichia coli"],
                    "Time (hours)" : [2, 4, 6],
                    "ATP" : {"Untreated" : [6321, 337947, 775523],
                             "1ug/mL" : [614, 1282, 1508],
                             "2ug/mL" : [263, 153, 256],
                             "4ug/mL" : [176, 48, 53]}},
    
    "Nalidixic acid" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Escherichia coli ATCC 25922"],
                    "Time (hours)" : [0, 2, 4, 6, 24],
                    "ATP" : {"Untreated" : [6.7, 8.1, 9, 8.9, 9.1],
                             "12.5ug/mL" : [6.7, 7.1, 7.4, 7.4, 6.9]},
                    "CFU/mL" : {"Untreated" : [6.4, 7, 8, 9.2, 9.6],
                                "12.5ug/mL" : [6.4, 5.6, 5, 4, 0]}},

    "Nitrofurantoin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Staphylococcus aureus"],
                    "Time (hours)" : [0, 2, 4, 6],
                    "ATP" : {"Untreated" : [55, 63, 68, 77],
                             "50ug/mL" : [55, 64, 63, 62.7]}},
   
    "Penicillin G" : {
                     "Details" : ["Vellend et al., 1977", "(fg/mL)", "Escherichia coli ATCC 25922"],
                     "Time (hours)" : [0, 1, 2, 3, 6, 24],
                     "ATP" : {"Untreated" : [7300000, 24100000, 128000000, 595000000, 1010000000, 1670000000],
                              "128ug/mL" : [8400000, 17900000, 3320000, 2450000, 880000, 416000]},
                     "CFU/mL" : {"Untreated" : [26500000, 87600000, 464000000, 2160000000, 3650000000, 6050000000],
                                 "128ug/mL" : [30500000, 74900000, 12100000, 8890000, 3200000, 1510000]}},

    "Sulfasoxazole" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Escherichia coli (UPEC)"],
                    "Time (hours)" : [0, 2, 4, 6],
                    "ATP" : {"Untreated" : [1550000, 42000000, 680000000, 1130000000],
                             "1mg/mL" : [1540000, 39100000, 386000000, 705000000],
                             "16mg/mL" : [1570000, 39000000, 368000000, 635000000]},
                    "CFU/mL" : {"Untreated" : [5610000, 152000000, 2460000000, 4070000000],
                                "1mg/mL": [5560000, 142000000, 1400000000, 2550000000],
                                "16mg/mL" : [5660000, 141000000, 1330000000, 2300000000]}},
   
    "Tetracycline" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Unknown Uropathogen"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [74.6, 82, 86.7],
                             "0.25xMIC" : [74.6, 75.6, 78],
                             "MIC" : [74.6, 72.8, 74.4],
                             "4xMIC" : [74.6, 70.8, 70]},
                    "CFU/mL" : {"Untreated" : [62.4, 67.1, 74.3],
                                "0.25xMIC" : [62.4, 62.8, 60.5],
                                "MIC" : [62.4, 54.8, 53.3],
                                "4xMIC" : [62.4, 51.4, 44]}}                
    }

AntibioticData = {
                  "Bactericidal" : ["Amikacin", "Ampicillin and clavulanic acid", "Carbenicillin and clavulanic acid", 
                                    "Cefotaxime", "Gentamicin", "Levofloxacin", "Nalidixic acid", "Nitrofurantoin", "Penicillin G"],
                  "Bacteriostatic" : ["Doxycycline", "Erythromycin", "Sulfasoxazole", "Tetracycline"],
                  "Class" : {
                             "Aminoglycosides" : ["Amikacin", "Gentamicin"],
                             "Amphenicols" : ["Chloramphenicol"],
                             "Beta-lactams" : ["Ampicillin and clavulanic acid", "Carbenicillin and clavulanic acid", "Penicillin G"],
                             "Cephalosporin" : ["Cefotaxime"],
                             "Fluoroquinolones" : ["Levofloxacin"],
                             "Macrolides" : ["Erythromycin"],
                             "Nitrofurans" : ["Nitrofurantoin"],
                             "Quinolones" : ["Nalidixic acid"],
                             "Sulfonamides" : ["Sulfasoxazole"],
                             "Tetracyclines" : ["Doxycycline", "Tetracycline"]},
                  "Mode of Action" : {
                             "Cell Wall Synthesis" : ["Beta-lactams", "Cephalosporins"],
                             "Folate Synthesis" : ["Sulfonamides"],
                             "DNA Gyrase" : ["Fluoroquinolones", "Quinolones"],
                             "Protein Synthesis" : ["Aminoglycosides", "Amphenicols", "Macrolides", "Nitrofurans", "Tetracyclines"]
                   }}


def GetReferences():
        References = []
        [References.append(ATPdata[antibiotic]["Details"][0]) for antibiotic in ATPdata.keys() if ATPdata[antibiotic]["Details"][0] not in References]
        print(References)

def GetSpecies():
        Species = []
        [Species.append(ATPdata[antibiotic]["Details"][2:][0]) for antibiotic in ATPdata.keys()]
        print(Species)

def GetAntibiotics():
        print([[value, antibiotic] for value, antibiotic in enumerate(ATPdata.keys())])

def CreateAxes(rows, cols):
        for row in range(0, rows, 2):
                for col in range(cols):
                        for i in range(2):       
                                yield row+i, col

def Time(antibiotic): #because units of time for each antibiotic data is different, this function returns the time with units
        for key in ATPdata[antibiotic].keys():
                if key.startswith("Time"):
                        return key 

def DisplayAllATPdata():

        axes = CreateAxes(4, 4)

        fig, axs = plt.subplots(nrows=4, ncols=4, constrained_layout=True)

        for antibiotic in ATPdata.keys():
                NewAx = next(axes)
                [axs[NewAx].plot(ATPdata[antibiotic][Time(antibiotic)], ATPdata[antibiotic]["ATP"][item]) for item in ATPdata[antibiotic]["ATP"].keys()]
                #formatting
                axs[NewAx].set_title(antibiotic, fontsize=10)
                axs[NewAx].set_xlabel(Time(antibiotic), fontsize=8)
                axs[NewAx].set_ylabel("ATP " + ATPdata[antibiotic]["Details"][1], fontsize=8, rotation=90)
                axs[NewAx].legend([label for label in ATPdata[antibiotic]["ATP"].keys()], fontsize=7, title="Concentration", title_fontsize=8)

def DisplayAll():
        rows, cols = 6, 5
        axes = CreateAxes(rows, cols)
        fig, axs = plt.subplots(nrows=rows, ncols=cols, constrained_layout=True)
        for antibiotic in ATPdata.keys():
                NewAx = next(axes)
                [axs[NewAx].plot(ATPdata[antibiotic][Time(antibiotic)], ATPdata[antibiotic]["ATP"][item]) for item in ATPdata[antibiotic]["ATP"].keys()]
                
                #formatting
                axs[NewAx].set_title(antibiotic, fontsize=10)
                axs[NewAx].set_xlabel(Time(antibiotic), fontsize=8)
                axs[NewAx].set_ylabel("ATP " + ATPdata[antibiotic]["Details"][1], fontsize=8, rotation=90)
                axs[NewAx].legend([label for label in ATPdata[antibiotic]["ATP"].keys()], fontsize=7, title="Abx conc.", title_fontsize=8)


                if "CFU/mL" in ATPdata[antibiotic]:
                        NewAx = next(axes)
                        [axs[NewAx].plot(ATPdata[antibiotic][Time(antibiotic)], ATPdata[antibiotic]["CFU/mL"][item]) for item in ATPdata[antibiotic]["CFU/mL"].keys()]
                        axs[NewAx].set_xlabel(Time(antibiotic), fontsize=8)
                        axs[NewAx].set_ylabel("CFU/mL", fontsize=8, rotation=90)

                else:
                        NewAx = next(axes)
                        axs[NewAx].text(0.5, 0.5, "No Data", ha="center", va="center")

DisplayAllATPdata()
plt.show()
