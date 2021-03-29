from math import floor

import matplotlib.gridspec as gridspec #lgtm [py/unused-import]
import matplotlib.pyplot as plt

ATPdata = {

    "Amikacin" : {
                    "Details" : ["Akhova and Tkachenko (2014)", "(nmol/mg dw)", "E. coli EH40"],
                    "Time (mins)" : [0, 30, 60, 90, 120, 150, 180],
                    "ATP" : {"Untreated" : [4.1, 3.5, 3.5, 1.75, 1.5, 2, 2.4],
                             "25 ug/mL" : [4.4, 4.9, 4.8, 4.6, 1.5, 2.5, 2.5]}},

    "Ampicillin and clavulanic acid" : {
                                        "Details" : ["Cornel et al., 1982", "(units)", "E. coli (TEM-1)"],
                                        "Time (hours)" : [0, 1, 2, 3, 4],
                                        "ATP" : {"Untreated" : [0.52, 0.86, 1.14, 1.77, 2.75],
                                                "0.1 mg/mL" : [0.52, 0.38, 0.56, 0.47, 0.38],
                                                "10 mg/mL" : [0.52, 0.28, 0.14, 0.11, 0.04]}},

    "Carbenicillin and clavulanic acid" : {
                                           "Details" : ["Cornel et al., 1982", "(units)", "E. coli (TEM-1)"],
                                           "Time (hours)" : [0, 1, 2, 3, 4],
                                           "ATP" : {"Untreated" : [1.19, 2.64, 4.69, 10, 10],
                                                    "0.1 mg/mL" : [1.19, 1.53, 1.94, 2.65, 3.18],
                                                    "10 mg/mL" : [1.19, 1.08, 0.73, 0.45, 0.32]}
                                            },

    "Cefotaxime" : {
                    "Details" : ["Akhova and Tkachenko (2014)", "(nmol / mg dw)", "E. coli EH40"],
                    "Time (mins)" : [0, 30, 60, 90, 120, 150, 180],
                    "ATP" : {"Untreated" : [2.1, 2.7, 2.7, 2.1, 1.6, 1.5, 1.1],
                             "1.2 ug/mL" : [1.6, 4, 2.5, 2.5, 2.2, 1.5, 2]}
                             },

    "Clindamycin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [12700000, 70000000, 215000000],
                             "2 ug/mL" : [12300000, 68000000, 190000000],
                             "8 ug/mL" : [13500000, 68500000, 198000000]},
                    "CFU/mL" : {"Untreated" : [46000000, 255000000, 778000000],
                                "2 ug/mL" : [44900000, 247000000, 715000000],
                                "8 ug/mL" : [49100000, 249000000, 715000000]}},

    "Doxycycline" : {
                    "Details" : ["Hojer and Nilsson (1978)", r"($x10^{-14}$ M)", "Enterobacter cloacae"],
                    "Time (hours)" : [0, 1, 2, 3, 4],
                    "ATP" : {"Untreated" : [32000000, 100000000, 180000000, 250000000, 350000000],
                            "0.1 ug/mL" : [32000000, 87000000, 109700000, 152000000, 250000000],
                            "1.0 ug/mL" : [32000000, 50700000, 105000000, 105000000, 111000000],
                            "5.0 ug/mL" : [32000000, 19000000, 30500000, 35000000, 44000000]},
                    "CFU/mL" : {"Untreated" : [170000000, 270000000, 470000000, 740000000, 830000000],
                                "0.1 ug/mL" : [170000000, 240000000, 380000000, 420000000, 470000000],
                                "1.0 ug/mL" : [170000000, 103000000, 110000000, 140000000, 370000000],
                                "5.0 ug/mL" : [170000000, 86000000, 27000000, 26000000, 46000000]}
                    },

    "Erythromycin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [12500000, 44500000, 148000000],
                             "2 ug/mL" : [14800000, 42000000, 124000000],
                             "8 ug/mL" : [15700000, 39600000, 106000000]},
                    "CFU/mL" : {"Untreated" : [45300000, 162000000, 538000000],
                                "2 ug/mL" : [53800000, 153000000, 449000000],
                                "8 ug/mL" : [56900000, 144000000, 384000000]}},

    "Gentamicin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Unknown Uropathogen"],
                    "Time (hours)" : [0, 1, 2, 3],
                    "ATP" : {"Untreated" : [7.1, 7.7, 8.2, 8.7],
                             "0.25 xMIC" : [7.1, 7.4, 7.5, 7.5],
                             "MIC" : [7.1, 6.8, 6.7, 6.7],
                             "4 xMIC" : [7.1, 6.7, 6.7, 6.7]},
                    "CFU/mL" : {"Untreated" : [59, 63, 70, 77],
                                "0.25 xMIC" : [59, 60, 59, 58],
                                "MIC" : [59, 35, 29, 27],
                                "4 xMIC" : [59, 20, 20, 20]}},

    "Levofloxacin" : {
                    "Details" : ["Matsui et al., 2019", "(amol)", "E. coli"],
                    "Time (hours)" : [2, 4, 6],
                    "ATP" : {"Untreated" : [6321, 337947, 775523],
                             "1 ug/mL" : [614, 1282, 1508],
                             "2 ug/mL" : [263, 153, 256],
                             "4 ug/mL" : [176, 48, 53]}},
    
    "Nalidixic acid" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli ATCC 25922"],
                    "Time (hours)" : [0, 2, 4, 6, 24],
                    "ATP" : {"Untreated" : [6.7, 8.1, 9, 8.9, 9.1],
                             "12.5 ug/mL" : [6.7, 7.1, 7.4, 7.4, 6.9]},
                    "CFU/mL" : {"Untreated" : [6.4, 7, 8, 9.2, 9.6],
                                "12.5 ug/mL" : [6.4, 5.6, 5, 4, 0]}},

    "Nitrofurantoin" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Staphylococcus aureus"],
                    "Time (hours)" : [0, 2, 4, 6],
                    "ATP" : {"Untreated" : [55, 63, 68, 77],
                             "50 ug/mL" : [55, 64, 63, 62.7]}},
   
    "Penicillin G" : {
                     "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli ATCC 25922"],
                     "Time (hours)" : [0, 1, 2, 3, 6, 24],
                     "ATP" : {"Untreated" : [7300000, 24100000, 128000000, 595000000, 1010000000, 1670000000],
                              "128 ug/mL" : [8400000, 17900000, 3320000, 2450000, 880000, 416000]},
                     "CFU/mL" : {"Untreated" : [26500000, 87600000, 464000000, 2160000000, 3650000000, 6050000000],
                                 "128 ug/mL" : [30500000, 74900000, 12100000, 8890000, 3200000, 1510000]}},

    "Sulfasoxazole" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "E. coli"],
                    "Time (hours)" : [0, 2, 4, 6],
                    "ATP" : {"Untreated" : [1550000, 42000000, 680000000, 1130000000],
                             "1 mg/mL" : [1540000, 39100000, 386000000, 705000000],
                             "16 mg/mL" : [1570000, 39000000, 368000000, 635000000]},
                    "CFU/mL" : {"Untreated" : [5610000, 152000000, 2460000000, 4070000000],
                                "1 mg/mL": [5560000, 142000000, 1400000000, 2550000000],
                                "16 mg/mL" : [5660000, 141000000, 1330000000, 2300000000]}},
   
    "Tetracycline" : {
                    "Details" : ["Vellend et al., 1977", "(fg/mL)", "Unknown Uropathogen"],
                    "Time (hours)" : [0, 1, 2],
                    "ATP" : {"Untreated" : [74.6, 82, 86.7],
                             "0.25 xMIC" : [74.6, 75.6, 78],
                             "MIC" : [74.6, 72.8, 74.4],
                             "4 xMIC" : [74.6, 70.8, 70]},
                    "CFU/mL" : {"Untreated" : [62.4, 67.1, 74.3],
                                "0.25 xMIC" : [62.4, 62.8, 60.5],
                                "MIC" : [62.4, 54.8, 53.3],
                                "4 xMIC" : [62.4, 51.4, 44]}}                
    }

Antibiotic_ATP_CFU = []
Antibiotic_ATP = []

def TidyData():

    """Changes units into sensible scientific notation instead of values given in thousands"""

    for antibiotic in ATPdata.keys():
        DataPool = []

        for conc in ATPdata[antibiotic]["ATP"]:
            for value in ATPdata[antibiotic]["ATP"][conc]:
                DataPool.append(value)

        if all(value > 1000 for value in DataPool):
            Decimals = 1
            while not all(value / (10 ** Decimals) < 10 for value in DataPool):
                Decimals += 1    

            for conc in ATPdata[antibiotic]["ATP"]:
                for n, value in enumerate(ATPdata[antibiotic]["ATP"][conc]):
                    ATPdata[antibiotic]["ATP"][conc][n-1] = value / (10**Decimals)
                    ATPdata[antibiotic]["CFU/mL"][conc][n-1] = ATPdata[antibiotic]["CFU/mL"][conc][n-1] / (10**Decimals)

            if antibiotic == "Doxycycline":
                ATPdata[antibiotic]["Details"][1].replace("14", str(14 + Decimals))
            else:
                ATPdata[antibiotic]["Details"][1] = r"($x10^{-" + str(Decimals) + "}$ " + ATPdata[antibiotic]["Details"][1][1:]


def SortAntibioticNames(): #filter antibiotics into lists of either those with both ATP and CFU data and just those with ATP data
    for antibiotic in ATPdata.keys():
        if "ATP" and "CFU/mL" in ATPdata[antibiotic]:
            Antibiotic_ATP_CFU.append(antibiotic)
        elif "ATP" in ATPdata[antibiotic]:
            Antibiotic_ATP.append(antibiotic)
        else:
            print("Error: {antibiotic} not allocated a list" % antibiotic)

    Antibiotic_ATP_CFU.sort(), Antibiotic_ATP.sort()


def Get_ATP_per_CFU_data():
    for antibiotic in Antibiotic_ATP_CFU:
        ATP_per_CFU = {}
        for conc in ATPdata[antibiotic]["ATP"].keys():
            ATP_per_CFU[conc] = []
            for ATP_data, CFU_data in zip(ATPdata[antibiotic]["ATP"][conc], ATPdata[antibiotic]["CFU/mL"][conc]):
                ATP_per_CFU[conc].append(round(ATP_data / CFU_data, 3) if CFU_data != 0 else 0)
        ATPdata[antibiotic].update({"ATP_per_CFU" : ATP_per_CFU})


def Time(antibiotic): #because units of time for each antibiotic data is different, this function returns the time with units
    for key in ATPdata[antibiotic].keys():
            if key.startswith("Time"):
                    return key 


def DefineHeading(antibiotic): return antibiotic + " against " + ATPdata[antibiotic]["Details"][2]


def Plot_ATP_CFU_Data():
    fig1 = plt.figure(constrained_layout=True)

    widths = [2, 2]
    height = [1, 2, 1, 2, 1, 2]

    gs = fig1.add_gridspec(ncols=2, nrows=6, width_ratios = widths, height_ratios = height)
    
    counter = 0 #keeps track of which antibiotic 

    for col in range(2):
        for row in range(6):

            ax = fig1.add_subplot(gs[row, col])
    
            abx = Antibiotic_ATP_CFU[floor(counter / 2)]
            time_unit = Time(abx)
            
            if counter == 0 or counter % 2 == 0: #count determines which data its plotting
                #Plotting ATP per CFU/mL data which is above its respective ATP plot
                ax.set_title(DefineHeading(abx))
                ax.get_xaxis().set_visible(False)
                ax.text(0, 1, "ATP per CFU/mL", horizontalalignment = "left", verticalalignment = "bottom", transform = ax.transAxes, fontsize='small')

                for conc in ATPdata[abx]["ATP"].keys():
                    ax.plot(ATPdata[abx][time_unit], ATPdata[abx]['ATP_per_CFU'][conc], 'o-')

            else:
                #plotting ATP data under ATP per CFU/mL data
                ax.set_xlabel(time_unit, fontsize=10)
                ax.set_ylabel('ATP ' + ATPdata[abx]['Details'][1], fontsize=10, rotation=90)
                
                for conc in ATPdata[abx]["ATP"].keys():
                    ax.plot(ATPdata[abx][time_unit], ATPdata[abx]['ATP'][conc], 'o-')
            
                ax.legend([label for label in ATPdata[abx]["ATP"].keys()], bbox_to_anchor=(1, 0), loc='lower left', fontsize='small')
            
            counter += 1
           

def Plot_ATP_data(): #plots ATP data singularly which do not have CFU data
    _, ax = plt.subplots(nrows=3, ncols=2, constrained_layout=True)
    counter = 0

    for axi in ax:
        for axis in axi:
                
            abx = Antibiotic_ATP[counter]
            time_unit = Time(abx)

            axis.set_title(DefineHeading(abx))

            axis.set_xlabel(time_unit, fontsize=10)
            axis.set_ylabel('ATP ' + ATPdata[abx]['Details'][1], fontsize=10, rotation=90)

            for conc in ATPdata[abx]["ATP"].keys(): #for each concentration of antibiotic...
                axis.plot(ATPdata[abx][time_unit], ATPdata[abx]['ATP'][conc], 'o-')

            axis.legend([label for label in ATPdata[abx]["ATP"].keys()], bbox_to_anchor=(1, 0), loc='lower left', fontsize='small')

            counter += 1
            

if __name__ == "__main__":
    TidyData()
    SortAntibioticNames()
    Get_ATP_per_CFU_data()
    Plot_ATP_CFU_Data(), Plot_ATP_data()
    plt.show()
