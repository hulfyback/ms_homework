# Trading Simulation

This simple project is for simulating buying and selling quotes. You can create quotes with price and quantity, and these quotes can be added to different named order books.

You are able to add a single quote to an order book, or list of quotes and you can read quotes from a CSV file, as well, to make the process faster.

There is a function to merge different order books into a combined book to simplify trading.

In sample_datas folder, there are 3 different lists of quotes in CSV files. 

Here is a sample to see, how many different ways you can add quotes to order books, and then, merge them into a single combined book. Just copy the code snippet below and paste it into the main module:
```python
    # create quots one by one
    q1 = quote.Quote(100, 0.1)
    q2 = quote.Quote(200, 0.2)
    q3 = quote.Quote(300, 0.3)

    # create an order book named LSE
    ob_lse = order_book.OrderBook('LSE')

    # add a single quote to LSE
    ob_lse.add_quote(q1)

    # add multiple quotes to LSE
    ob_lse.add_quotes([q2, q3])

    # create an other order book named TRQS
    ob_trqs = order_book.OrderBook('TRQS')

    # read quotes from csv into order book
    ob_trqs.read_quotes_from_csv('sample_datas/trqs.csv')
    
    # create a new merged book named MB
    mb = merged_book.MergedBook('MB')

    # add order books to merged book
    mb.add_orderbook(ob_lse)
    mb.add_orderbook(ob_trqs)

    # add order book to merged book from a csv file
    mb.read_orderbook_from_csv('BATS', 'sample_datas/bats.csv')

    # simulate trading (quantity, price)
    mb.simulateBuy(100, 0.1)
    mb.simulateBuy(250, 0.25)
    mb.simulateBuy(250, 0.25)
    mb.simulateBuy(250, 0.25)

    # print formatted merged book to console
    print(mb)
```


    