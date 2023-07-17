import psycopg2
import config
import xml.dom.minidom


con = psycopg2.connect(
    database=config.database,
    user=config.user_database,
    password=config.password_database,
    host=config.host,
    port=config.port
)
print("Database opened successfully")

cur = con.cursor()

# cur.execute(config.number_ticket)
# cur.execute(config.number_coupon)
# cur.execute(config.bingo_ticket)
# cur.execute(config.bingo_coupon)
# cur.execute(config.instant_ticket)
# cur.execute(config.ticket_set_number)
# cur.execute(config.ticket_set_coupon)


def mapping(select_number):
    cur.execute(select_number)
    print(cur.fetchone())


# mapping(config.ticket_set_number)



cur.close()
