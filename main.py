import errors
import merged_book
import order_book
import quote

if __name__ == '__main__':
    mb = merged_book.MergedBook('MB')
    
    mb.read_orderbook_from_csv('LSE', 'sample_datas/lse.csv')
    mb.read_orderbook_from_csv('TRQS', 'sample_datas/trqs.csv')
    mb.read_orderbook_from_csv('BATS', 'sample_datas/bats.csv')

    mb.simulateBuy(100, 0.1)
    mb.simulateBuy(250, 0.25)
    mb.simulateBuy(250, 0.25)
    mb.simulateBuy(250, 0.25)

    print(mb)