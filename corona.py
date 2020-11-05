import pandas as pd

Landkreis = 'Heidenheim'

#Method which returns a pandas dataframe
def GetCsvData(link):
    dataframe = pd.read_csv(link)
    return dataframe

def FilterLK(dataframe, landkreis):
    filtered_dataframe = dataframe[dataframe['GEN'] == landkreis]
    return filtered_dataframe

def GetValue(dataframe, ColumnName):
    value = dataframe[ColumnName].to_string(index = False)
    return value

if __name__ =="__main__":
    #RKI Link with current Corona data 
    CsvLink = 'https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv'
    df = GetCsvData(CsvLink)
    #Remove all NaN
    df.dropna()
    df = FilterLK(df, Landkreis)
    bundesland = GetValue(df, 'BL')
    einwohnerzahlLk = GetValue(df, 'EWZ')
    einwohnerzahlBl = GetValue(df, "EWZ_BL")
    siebenTageInzidenzLk = GetValue(df, "cases7_per_100k")
    cases_per_100k = GetValue(df, 'cases_per_100k')
    anzahlTodesfaelle = GetValue(df, 'deaths')
    todesrate = GetValue(df, 'death_rate')
    letztesUpdate = GetValue(df, 'last_update')

    print('Bundesland: ' + bundesland)
    print('Einwohnerzahl: '+ einwohnerzahlBl)
    print('Landkreis: ' + Landkreis)
    print('Einwohnerzahl: ' + einwohnerzahlLk)
    print('Sieben Tage Inzidenz: ' + siebenTageInzidenzLk)
    print('Fälle pro 100k: ' + cases_per_100k)
    print('Todesfälle: ' + anzahlTodesfaelle)
    print('Todesrate: ' + todesrate + '%')
    print('Daten wurden zuletzt am ' + letztesUpdate + 'aktualisiert')