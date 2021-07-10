from binance.client import Client


def get_status_in_val(cl: Client, coin: str):
    '''
    This function outputs the balance on your Balance account in the currency you need.
    :param cl: object client.
    :param coin: the name of the cryptocurrency.
    :return: the amount of remaining funds in your account.
    '''
    return round(get_account_balance_in_coin(cl.get_account(), 'ETH') * get_ex_coin(cl, coin), 2)


def get_account_balance_in_coin(account: dict, coin: str):
    '''
    This function outputs the balance on your Finance account in the cryptocurrency you need.
    :param account: balances.
    :param coin: the name of the cryptocurrency.
    :return: the amount of cryptocurrency on your account, if there are any problems, it returns 0.0 .
    '''
    for asset in account["balances"]:
        if asset["asset"] == coin:
            return float(asset['free'])
    return 0.0


def get_ex_coin(cl: Client, coin: str) -> float:
    '''
    This function displays the exchange rate of the cryptocurrency you need.
    :param cl: object client.
    :param coin: the name of the currencies whose exchange rate you need.
    :return: exchange rate
    '''
    return float(cl.get_symbol_ticker(symbol=coin)["price"])
