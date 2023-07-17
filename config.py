# Настройки RabbitMQ
rabbit = 'http://dev.int.nl-dev.ru:30673/#/'
stock_balance_queue = rabbit + 'queues/%2F/invoice-1c-to-stock-balance'
user_rabbit = 'developer'
password_rabbit = '345-asd'

# Настройки базы данных
database = "lottery"
user_database = "lottery"
password_database = "lottery"
host = "postgres1.dev.int.nl-dev.ru"
port = "5432"

# Запросы в БД
number_ticket = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        7 unit,
        count(*) ticket_in_box,
        min(p.number) ticket_in_box_first,
        max(p.number) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.draw_id as text) draw_id,
        cast(p.product_id as text) product_id
    from number_handler.number_ticket_paper p
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
    and p.box_number is not null
    group by p.box_number, p.draw_id, p.product_id
    order by random()
    limit 1;
"""

number_coupon = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        6 unit,
        count(*) ticket_in_box,
        min(coalesce(s.number, p.number)) ticket_in_box_first,
        max(coalesce(s.number, p.number)) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.product_id as text) product_id
    from number_handler.number_coupon p
    left join ticket_set_handler.ticket_set s on s.id = p.ticket_set_id
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
        and p.box_number is not null
    group by p.box_number, product_id
    order by random()
    limit 1;
"""

bingo_ticket = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        7 unit,
        count(*) ticket_in_box,
        min(coalesce(s.number, p.number)) ticket_in_box_first,
        max(coalesce(s.number, p.number)) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.draw_id as text) draw_id,
        cast(p.product_id as text) product_id
    from bingo_handler.bingo_ticket_paper p
    left join ticket_set_handler.ticket_set s on s.id = p.ticket_set_id
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
        and p.box_number not like '3%'
        and p.box_number is not null
    group by p.box_number, draw_id, product_id
    order by random()
    limit 1;
"""

bingo_coupon = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        6 unit,
        count(*) ticket_in_box,
        min(coalesce(s.number, p.number)) ticket_in_box_first,
        max(coalesce(s.number, p.number)) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.product_id as text) product_id
    from bingo_handler.bingo_coupon p
    left join ticket_set_handler.ticket_set s on s.id = p.ticket_set_id
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
        and p.box_number  like '102%'
        and p.box_number is not null
    group by p.box_number, product_id
    order by random()
    limit 1;
"""

instant_ticket = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        7 unit,
        count(*) ticket_in_box,
        min(p.number) ticket_in_box_first,
        max(p.number) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.product_id as text) product_id
    from instant_handler.instant_ticket p
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
    and p.box_number is not null
    group by p.box_number, p.product_id
    order by random()
    limit 1;
"""

ticket_set_number = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        7 unit,
        count(*) ticket_in_box,
        min(coalesce(s.number, p.number)) ticket_in_box_first,
        max(coalesce(s.number, p.number)) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.draw_id as text) draw_id,
        cast(p.product_id as text) product_id
    from bingo_handler.bingo_ticket_paper p
    left join ticket_set_handler.ticket_set s on s.id = p.ticket_set_id
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
        and p.box_number like '310001%'
        and p.box_number is not null
    group by p.box_number, draw_id, product_id
    order by random()
    limit 1;
"""

ticket_set_coupon = """
    select
        gen_random_uuid() packaging_id,
        gen_random_uuid() external_id,
        cast(p.box_number as text) box,
        7 unit,
        count(*) ticket_in_box,
        min(coalesce(s.number, p.number)) ticket_in_box_first,
        max(coalesce(s.number, p.number)) ticket_in_box_last,
        min(p.pack_number) pack_number_first,
        max(p.pack_number) pack_number_last,
        cast(p.product_id as text) product_id
    from bingo_handler.bingo_coupon p
    left join ticket_set_handler.ticket_set s on s.id = p.ticket_set_id
    where not exists (
        select 1
        from stock_balance.packaging b
        where b.box = p.box_number
    )
        and p.box_number like '310002%'
        and p.box_number is not null
    group by p.box_number, product_id
    order by random()
    limit 1;
"""

XML = """
<Message xmlns="http://www.t1-consulting.ru" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <Body>
    <classData44 xmlns="http://www.t1-consulting.ru" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <invoiceId>15e40c82-ddf0-11ed-b04a-005056b9da48</invoiceId>
        <invoiceNumber>50УТ-000063</invoiceNumber>
        <updateId/>
        <updateVersion/>
        <invoiceDate>2023-04-20T00:00:00</invoiceDate>
        <invoiceVersion>AAAAAAAD9ZI=</invoiceVersion>
        <partnerName>ПОЧТА РОССИИ АО</partnerName>
        <partnerId>e9ad273c-147b-11ec-ac9b-141877510b08</partnerId>
        <recipient>6c7458be-45cb-464a-83b9-51ba4ab43814</recipient>
        <invoiceAcceptanceStatus/>
        <invoiceRejectedComment/>
        <invoiceRejectedManager/>
        <tickets>
            <row>
                <productId>eb69ee0b-2847-4a86-91c6-19d9a2d6112b</productId>
                <productName>Name Lottery</productName>
                <drawId>9c4aa071-0d37-4bc3-9e90-c7a3d6893bbf</drawId>
                <logisticType>coupon</logisticType>
                <drawNumber/>
                <series>010</series>
                <numberOrder/>
                <quant>1</quant>
                <lostQuant>0</lostQuant>
                <packaging>
                    <row>
                        <id>d0496b96-d53f-11ed-b044-005056b9da48</id>
                        <box>206302701000067</box>
                        <unit>7</unit>
                        <ticketInBox>2400</ticketInBox>
                    </row>
                </packaging>
            </row>
        </tickets>
    </classData44></Body>
    <ClassId>44</ClassId>
    <CreationTime>2023-05-16T12:47:22</CreationTime>
    <Id>6eb2d189-bf0e-47b8-a89e-774fa897490d</Id>
    <Receiver/>
    <Source>UT</Source>
    <Type>DTP</Type>
</Message>
"""
