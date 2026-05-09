# Seminar 3 Python - Prelucrări statistice și agregări în pandas

# Exemplu 1: Conversia coloanei date din șir de caractere în dată calendaristică
import dateutil
import pandas as pd

# Citim datele din csv
df = pd.read_csv('phone_data.csv')
# Afișăm tipurile de date inițiale @todo

# Convertim coloana 'date' folosind parser-ul din dateutil
df['date'] = df['date'].apply(dateutil.parser.parse, dayfirst=True)
# Afișăm tipurile de date după conversie @todo

# Exemplu 2: Prelucrări statistice simple
df = pd.read_csv('phone_data.csv')
# Numărăm înregistrările din coloana 'item' @todo
print('Numar inregistrari')

# Găsim durata maximă din coloana 'duration' @todo
print('Durata maxima a unei convorbiri/transfer date')

# Suma durateleor pentru apeluri din coloana 'duration'@todo

print('Numarul total de secunde la apeluri')

# Numărăm apelurile din fiecare lună @todo

print('Numarul de apeluri in fiecare luna')

# Aflăm numărul de rețele unice din 'network' @todo
print('Numar de retele - elimina duplicatele')

# Exemplu 3: Statistici descriptive cu describe()
df = pd.read_csv('phone_data.csv')
# Obținem statistici descriptive pentru 'network_type' și 'duration' @todo
print('Statistici descriptive')


# Exemplu 4: Posibilități de grupare
df = pd.read_csv('phone_data.csv')

# Afișăm cheile grupurilor pentru 'item'
print(df.groupby(['item']).groups.keys())

# Numărăm apelurile din grupul 'call'
print(len(df.groupby(['item']).groups['call']))

# Afișăm cheile grupurilor pentru 'month'

# Numărăm înregistrările pentru luna '2014-11' @todo

print(len(df.groupby(['month']).groups['2014-11']))

# Exemplu 5: Utilizarea funcțiilor de agregare cu GroupBy
df = pd.read_csv('phone_data.csv')

# Afișăm prima înregistrare pentru fiecare valoare din 'item'
print('Prima inregistrare din coloana item pe valori distincte')
print(df.groupby('item').first())

# Suma duratelor pentru fiecare lună @todo
print('Durata insumata pentru fiecare luna')

# Suma duratelor pentru apeluri în funcție de rețea
print('Durata insumata pe convorbiri (calls), pentru fiecare retea')

print(df[df['item'] == 'call'].groupby('network')['duration'].sum())

# Exemplu 6: Grupări complexe
df = pd.read_csv('phone_data.csv')

# Numărăm apelurile, sms-urile, transferul de date pentru fiecare lună
print('Numarul de apeluri, sms, transfer date pentru fiecare luna')
print(df.groupby(['month', 'item'])['date'].count())

# Exemplu 7: Gruparea și agregarea datelor
df = pd.read_csv('phone_data.csv')

# Grupează după 'month' și 'item' și calculează statistici pentru fiecare grup
print(df.groupby(['month', 'item']).agg({'duration': sum,  # suma duratelor
                                         'network_type': "count",  # numărul de tipuri de rețele
                                         'date': 'first'}))  # prima apariție (dată) pentru fiecare grup

# Salvăm rezultatul agregării într-un nou fișier csv
df1 = df.groupby(['month', 'item']).agg({'duration': sum,
                                         'network_type': "count",
                                         'date': 'first'})
df1.to_csv('agregare.csv')

# Exemplu 8: Aplicarea mai multor funcții unei singure coloane din grup
df = pd.read_csv('phone_data.csv')
# Grupează după 'month' și 'item'. Calculează statistici pentru fiecare grup
print(df.groupby(['month', 'item']).agg({'duration': [min, max, sum],  # min, max și sum pentru 'duration'
                                         'network_type': "count",  # numărul de 'network_type'
                                         'date': [min, 'first',
                                                  'nunique']}))  # min, prima apariție și numărul de date unice

# Prelucrarea seturilor de date cu merge / join dataframes
# Utilizăm fișierele .csv cu o coloană comună pentru a demonstra merge/join

# Exemplu 9: Inner merge sau inner join
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

# Inner join între 'user_usage' și 'user_device' pe coloana 'use_id'
result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplele 10, 11, 12, 13, 14 și 15 urmează aceeași structură, modificând doar parametrul 'how' al metodei merge
# pentru a ilustra diferite tipuri de join: 'left', 'right', 'outer', inclusiv cu indicator.

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())


df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='right')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())


df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='outer')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())


df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='outer',
                  indicator=True)
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')
df3 = pd.read_csv('supported_devices.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')

df3.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result,
                  df3[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')
print(result.head())
print(result.shape)


# Reprezentare grafică cu pachetul matplotlib

# Exemplu 16: Reprezentare grafică cu bare cu matplotlib.pyplot
import matplotlib.pyplot as plt

# Setăm opțiunea pentru afișarea unui număr maxim de coloane
pd.set_option("display.max_columns", 10)
df = pd.read_csv('clienti_leasing20.csv')
# Afișăm coloana 'AGE'
print(df['AGE'])

# Reprezentăm grafic coloana 'AGE' sub formă de bare
df['AGE'].plot(kind='bar')
plt.xlabel('ID_CLIENT')
plt.ylabel('AGE')
plt.show()

# Exemplul 17: Histogramă cu matplotlib.pyplot
# Reprezentăm grafic coloana 'AGE' sub formă de histogramă
print(df['AGE'])
df['AGE'].plot(kind='hist')
plt.xlabel('AGE')
plt.show()

# Exemplul 18: Grafic cu gruparea și sortarea datelor
# Filtrăm datele pentru sexul masculin și grupăm după 'JOB' sumând 'VENIT_PER_YEAR'
plot_data = df[df['SEX'] == 'm']
plot_data = plot_data.groupby('JOB')['VENIT_PER_YEAR'].sum()
# Sortăm și reprezentăm grafic rezultatele
plot_data.sort_values().plot(kind='bar')
plt.show()
