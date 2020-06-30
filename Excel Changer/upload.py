import psycopg2
# ---------------------
# Connect to PostgreSQL
# ---------------------
t_host = "192.168.16.150"
t_port = "5432"
t_dbname = "michi_bkp_2"
t_name_user = "michi"
data_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_name_user, password=t_password)

cur = connect.cursor()

transaction = 'C:/Users/erikr/github/Roshka/Excel Changer/data/30-06-2020_15-28-33.csv'
with open(transaction, 'r') as file:

        cur.copy_from(f,'transaction_check', sep=',')
conn.commit()        

#Aca va el sql command para sacar una de las tablas
cur.execute('')
