#! python3

from read_h5 import *
from create_sqlite_2table import *






def put_file_in_bdd(fichier_h5,x, curseur):
    name = str(fichier_h5)
    fichier = read_h5(fichier_h5)
    if x == 1:
        convert_h5force_dataframe(fichier)
        code_confog_maquette(fichier)
    ##on remplit essaie

    #on cherche quel essaie correspond aux données
        date = ("09/19",)
        curseur.execute("SELECT id_essaie FROM essaie WHERE date = ?",date)
        id = curseur.fetchone()[0]

#on remplit avec les donnéees du fichier
        for ligne in range(fichier.shape[0]):
            donnees_h5 = [i for i in fichier.iloc[ligne,:]]
            donnees_h5.append(id)
            donnees_h5.append(str(fichier.index[ligne]))
            curseur.execute('''INSERT INTO données_force (NROT, NLOT,NPT, TI, BETA, PI0, M0C, RE0C, CXC, CYC, CZC, CLAAC, CMAAC, CNAAC, ALPHAC, CONF, essaie_id,id_date) VALUES (?,?,?, ?, ?, ?,?,?,?, ?, ?, ?, ?,?,?,?, ?,?)''',donnees_h5)


    #####DEBUGUE
    # for essaie in curseur.execute("SELECT * FROM essaie"):
    #     print("essaie :", essaie)
    #     print("\n")
    #
    #
    #


    # print(fichier.iloc[154,:])
    # dt = str(fichier.index[154])
    # curseur.execute("SELECT * FROM données WHERE id_date = ?", (dt, ))
    # print(curseur.fetchone())


    else:
        convert_h5pressure_dataframe(fichier)

        date = ("09/19",)
        curseur.execute("SELECT id_essaie FROM essaie WHERE date = ?",date)
        id = curseur.fetchone()[0]
        for ligne in range(fichier.shape[0]):
            donnees_h5 = [i for i in fichier.iloc[ligne,:]]
            donnees_h5.append(id)
            if name[-12].isdigit():
                donnees_h5.append(int(name[-12:-8]))
            else:
                donnees_h5.append(int(name[-11:-8]))
            #donnees_h5.append(str(fichier.index[ligne]))
            curseur.execute('''INSERT INTO données_pressure (NPT,KP_PS3101, KP_PS3102, KP_PS3103, KP_PS3104, KP_PS3105, KP_PS3106, KP_PS3107, KP_PS3201, KP_PS3202, KP_PS3203, KP_PS3204, KP_PS3205, KP_PS3206, KP_PS3207, KP_PS3208, KP_PS3209, KP_PS3210, KP_PS3211, KP_PS3212, KP_PS3213, KP_PS3214, KP_PS3301, KP_PS3302, KP_PS3303, KP_PS3304, KP_PS3305, KP_PS3306, KP_PS3307, KP_PS3308, KP_PS3309, KP_PS3401, KP_PS3402, KP_PS3403, KP_PS3404, KP_PS3405, KP_PS3406, KP_PS3407, KP_PS3408, KP_PS3409, KP_PS3410, KP_PS3411, KP_PS3412, KP_PS3421, KP_PS3422, KP_PS3423, KP_PS3424, KP_PS3425, KP_PS3426, KP_PS3427, KP_PS3428, KP_PS3501, KP_PS3502, KP_PS3503, KP_PS3504, KP_PS3505, KP_PS3506, KP_PS3510, KP_PS3511, KP_PS3512, KP_PS3513, KP_PS3514, KP_PS3515, KP_PS1101, KP_PS1102, KP_PS1103, KP_PS1104, KP_PS1105, KP_PS1106, KP_PS1107, KP_PS1108, KP_PS1109, KP_PS1110, KP_PS1111, KP_PS1112, KP_PS1113, KP_PS1114, KP_PS1115, KP_PS1116, KP_PS1117, KP_PS1118, KP_PS1119, KP_PS1120, KP_PS1121, KP_PS1122, KP_PS1123, KP_PS1124, KP_PS1125, KP_PS1126, KP_PS1127, KP_PS1128, KP_PS1129, KP_PS1130, KP_PS1201, KP_PS1202, KP_PS1203, KP_PS1204, KP_PS1205, KP_PS1206, KP_PS1207, KP_PS1208, KP_PS1209, KP_PS1210, KP_PS1211, KP_PS1212, KP_PS1213, KP_PS1214, KP_PS1215, KP_PS1216, KP_PS1217, KP_PS1218, KP_PS1219, KP_PS1220, KP_PS1221, KP_PS1222, KP_PS1223, KP_PS1224, KP_PS1225, KP_PS1226, KP_PS1227, KP_PS1228, KP_PS1229, KP_PS1230, KP_PS1301, KP_PS1302, KP_PS1303, KP_PS1304, KP_PS1305, KP_PS1306, KP_PS1307, KP_PS1308, KP_PS1309, KP_PS1310, KP_PS1311, KP_PS1312, KP_PS1313, KP_PS1314, KP_PS1315, KP_PS1316, KP_PS1317, KP_PS1318, KP_PS1319, KP_PS1320, KP_PS1321, KP_PS1322, KP_PS1323, KP_PS1324, KP_PS1325, KP_PS1326, KP_PS1327, KP_PS1328, KP_PS1329, KP_PS1330, KP_PS1401, KP_PS1402, KP_PS1403, KP_PS1404, KP_PS1405, KP_PS1406, KP_PS1407, KP_PS1408, KP_PS1409, KP_PS1410, KP_PS1411, KP_PS1412, KP_PS1413, KP_PS1414, KP_PS1415, KP_PS1416, KP_PS1417, KP_PS1418, KP_PS1419, KP_PS1420, KP_PS1421, KP_PS1422, KP_PS1423, KP_PS1424, KP_PS1425, KP_PS1426, KP_PS1427, KP_PS1428, KP_PS1429, KP_PS1430, KP_PS1501, KP_PS1502, KP_PS1503, KP_PS1504, KP_PS1505, KP_PS1506, KP_PS1507, KP_PS1508, KP_PS1509, KP_PS1510, KP_PS1511, KP_PS1512, KP_PS1513, KP_PS1514, KP_PS1515, KP_PS1516, KP_PS1517, KP_PS1518, KP_PS1519, KP_PS1520, KP_PS1521, KP_PS1522, KP_PS1523, KP_PS1524, KP_PS1525, KP_PS1526, KP_PS1527, KP_PS1528, KP_PS1529, KP_PS1530, KP_PS2101, KP_PS2102, KP_PS2103, KP_PS2104, KP_PS2105, KP_PS2106, KP_PS2107, KP_PS2108, KP_PS2109, KP_PS2110, KP_PS2111, KP_PS2112, KP_PS2113, KP_PS2114, KP_PS2115, KP_PS2116, KP_PS2117, KP_PS2118, KP_PS2119, KP_PS2120, KP_PS2121, KP_PS2122, KP_PS2123, KP_PS2124, KP_PS2125, KP_PS2126, KP_PS2127, KP_PS2128, KP_PS2129, KP_PS2130, KP_PS2212, KP_PS2213, KP_PS2214, KP_PS2215, KP_PS2216, KP_PS2217, KP_PS2218, KP_PS2219, KP_PS2220, KP_PS2221, KP_PS2301, KP_PS2302, KP_PS2303, KP_PS2304, KP_PS2305, KP_PS2306, KP_PS2307, KP_PS2308, KP_PS2309, KP_PS2310, KP_PS2311, KP_PS2312, KP_PS2313, KP_PS2314, KP_PS2315, KP_PS2316, KP_PS2317, KP_PS2318, KP_PS2319, KP_PS2320, KP_PS2321, KP_PS2322, KP_PS2323, KP_PS2324, KP_PS2325, KP_PS2326, KP_PS2327, KP_PS2328, KP_PS2329, KP_PS2330, KP_PS2401, KP_PS2402, KP_PS2403, KP_PS2404, KP_PS2405, KP_PS2406, KP_PS2407, KP_PS2408, KP_PS2409, KP_PS2410, KP_PS2411, KP_PS2412, KP_PS2413, KP_PS2414, KP_PS2415, KP_PS2416, KP_PS2417, KP_PS2418, KP_PS2419, KP_PS2420, KP_PS2421, KP_PS2422, KP_PS2423, KP_PS2424, KP_PS2425, KP_PS2426, KP_PS2427, KP_PS2428, KP_PS2429, KP_PS2430, KP_PS2501, KP_PS2502, KP_PS2503, KP_PS2504, KP_PS2505, KP_PS2506, KP_PS2507, KP_PS2508, KP_PS2509, KP_PS2510, KP_PS2511, KP_PS2512, KP_PS2513, KP_PS2514, KP_PS2515, KP_PS2516, KP_PS2517, KP_PS2518, KP_PS2519, KP_PS2520, KP_PS2521, KP_PS2522, KP_PS2523, KP_PS2524, KP_PS2525, KP_PS2526, KP_PS2527, KP_PS2528, KP_PS2529, KP_PS2530, KP_PS4101, KP_PS4102, KP_PS4103, KP_PS4104, KP_PS4105, KP_PS4106, KP_PS4107, KP_PS4108, KP_PS4109, KP_PS4110, KP_PS4111, KP_PS4112, KP_PS4113, KP_PS4114, KP_PS4115, KP_PS4116, KP_PS4117, KP_PS4118, KP_PS4119, KP_PS4120, KP_PS4121, KP_PS4122, KP_PS4123, KP_PS4124, KP_PS4125, KP_PS4126, KP_PS4127, KP_PS5101, KP_PS5102, KP_PS5103, KP_PS5104, KP_PS5105, KP_PS5106, KP_PS5107, KP_PS5108, KP_PS5109, KP_PS5110, KP_PS5111, KP_PS5112, KP_PS5113, KP_PS5114, KP_PS5115, KP_PS5116, KP_PS5117, KP_PS5118, KP_PS5119, KP_PS5120, KP_PS5121, KP_PS5122, KP_PS5123, KP_PS5124, KP_PS5125, KP_PS5126, KP_PS5127, KP_PS5201, KP_PS5202, KP_PS5203, KP_PS5204, KP_PS5205, KP_PS5206, KP_PS5207, KP_PS5208, KP_PS5209, KP_PS5210, KP_PS5211, KP_PS5212, KP_PS5213, KP_PS5214, KP_PS5215, KP_PS5216, KP_PS5217, KP_PS5218, KP_PS5219, KP_PS5220, KP_PS5221, KP_PS5222, KP_PS5223, KP_PS5224, KP_PS5225, KP_PS5226, KP_PS5227, KP_PS5501, KP_PS5502, KP_PS5503, KP_PS5504, KP_PS5505, KP_PS5506, KP_PS5507, KP_PS5508, KP_PS5509, KP_PS5510, KP_PS5511, KP_PS5512, KP_PS5513, KP_PS5514, KP_PS5515, KP_PS5516, KP_PS5517, KP_PS5518, KP_PS5519, KP_PS5520, KP_PS5521, KP_PS5522, KP_PS5523, KP_PS5524, KP_PS5525, KP_PS5526, KP_PS5527, essaie_id, NLOT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?)''',donnees_h5)
